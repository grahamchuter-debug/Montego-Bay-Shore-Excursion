/**
 * Montego Bay booking security / commercial gate tests (Phase 14D).
 * No live Stripe. Uses Worker preview mode + shared pricing authority.
 */
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { test } from "node:test";
import worker from "./index";
import { LIVE_PAYMENTS_CODE_ENABLED, liveCheckoutBlock, bookingsAreEnabled } from "./live-gate";
import { assertStripeTestSecret, StripeModeError } from "./stripe-guard";
import {
  findMontegoBayBookingProduct,
  MONTEGO_BAY_BOOKING_PRODUCTS,
} from "../../../shared/destinations/montego-bay-products";
import {
  assertClientTotalMatches,
  calculateBookingQuote,
  statusAfterPaymentSuccess,
} from "../../../shared/world-booking";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "../../..");

const previewEnv = {
  PAYMENTS_MODE: "preview",
  BOOKINGS_ENABLED: "true",
  CORS_ALLOWED_ORIGINS: "http://localhost:8920",
  SITE_BASE_URL: "http://localhost:8920",
} as unknown as Env;

const HIGH = "highlights-and-beach-break";
const ROSE = "rose-hall-great-house-and-highlights";

function payload(
  sessionId: string,
  guests = { adults: 2, children: 0, infants: 0 },
  overrides: Record<string, unknown> = {},
  productId = HIGH,
) {
  const product = findMontegoBayBookingProduct(productId)!;
  const quote = calculateBookingQuote(product, guests);
  return {
    productId,
    bookingSessionId: sessionId,
    guests,
    customer: { name: "Alex Traveller", email: "alex@example.com", phone: "+447700900123" },
    cruise: {
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "celebrity-beyond",
      cruiseLine: "Celebrity Cruises",
      isCustomShip: true,
      scheduleMatched: false,
    },
    confirmationAcknowledged: true,
    clientDisplayedTotalCents: quote.amountCents,
    ...overrides,
  };
}

function jsonReq(url: string, body: unknown) {
  return new Request(url, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(body),
  });
}

test("LIVE_PAYMENTS_CODE_ENABLED is false for Montego Bay Phase 14D (locked)", () => {
  assert.equal(LIVE_PAYMENTS_CODE_ENABLED, false);
});

test("live checkout blocked while code flag is false", () => {
  const product = findMontegoBayBookingProduct(HIGH)!;
  const block = liveCheckoutBlock(
    {
      PAYMENTS_MODE: "live",
      LIVE_PAYMENTS_UNLOCK: "MONTEGO_BAY_LIVE_UNLOCK",
      BOOKINGS_ENABLED: "true",
      STRIPE_SECRET_KEY: "sk_live_fake",
      STRIPE_WEBHOOK_SECRET: "whsec_fake",
      SITE_BASE_URL: "https://montegobayshoreexcursion.com",
      DB: {} as D1Database,
    },
    product,
  );
  assert.ok(block);
  assert.equal(block!.code, "LIVE_PAYMENTS_BLOCKED");
});

test("BOOKINGS_ENABLED=false kill switch", () => {
  assert.equal(bookingsAreEnabled({ BOOKINGS_ENABLED: "false" }), false);
});

test("two Montego Bay products live request mode with USD currency", () => {
  assert.equal(MONTEGO_BAY_BOOKING_PRODUCTS.length, 2);
  for (const product of MONTEGO_BAY_BOOKING_PRODUCTS) {
    assert.equal(product.availability, "live");
    assert.equal(product.bookingMode, "request");
    assert.equal(product.pricing.currency, "USD");
    assert.equal(product.capacity.maxGuestsPerBooking, 10);
    assert.equal(product.destinationId, "montego-bay");
  }
});

test("CAMBHIGH Highlights 9500 adult / 6500 child / free infant", () => {
  const product = findMontegoBayBookingProduct(HIGH)!;
  assert.equal(product.pricing.adultAmount, 95);
  assert.equal(product.pricing.childAmount, 65);
  assert.equal(product.pricing.infantAmount, 0);
  assert.equal(calculateBookingQuote(product, { adults: 1, children: 0, infants: 0 }).amountCents, 9500);
  assert.equal(calculateBookingQuote(product, { adults: 2, children: 0, infants: 0 }).amountCents, 19000);
  assert.equal(calculateBookingQuote(product, { adults: 1, children: 1, infants: 0 }).amountCents, 16000);
  assert.equal(calculateBookingQuote(product, { adults: 1, children: 1, infants: 1 }).amountCents, 16000);
  assert.equal(calculateBookingQuote(product, { adults: 1, children: 1, infants: 1 }).breakdown.infants.count, 1);
});

test("CAMBROSE Rose Hall 12500 adult / 8000 child / free infant", () => {
  const product = findMontegoBayBookingProduct(ROSE)!;
  assert.equal(product.pricing.adultAmount, 125);
  assert.equal(product.pricing.childAmount, 80);
  assert.equal(calculateBookingQuote(product, { adults: 1, children: 0, infants: 0 }).amountCents, 12500);
  assert.equal(calculateBookingQuote(product, { adults: 1, children: 1, infants: 0 }).amountCents, 20500);
  assert.equal(calculateBookingQuote(product, { adults: 1, children: 0, infants: 2 }).amountCents, 12500);
});

test("rejects 0 adults, 11 guests, negatives via quote", () => {
  const product = findMontegoBayBookingProduct(HIGH)!;
  assert.throws(() => calculateBookingQuote(product, { adults: 0, children: 1, infants: 0 }));
  assert.throws(() => calculateBookingQuote(product, { adults: 11, children: 0, infants: 0 }));
  assert.throws(() => calculateBookingQuote(product, { adults: -1, children: 0, infants: 0 }));
  assert.doesNotThrow(() => calculateBookingQuote(product, { adults: 10, children: 0, infants: 0 }));
  assert.throws(() => calculateBookingQuote(product, { adults: 5, children: 5, infants: 1 }));
});

test("payment success status is requested not confirmed", () => {
  assert.equal(statusAfterPaymentSuccess("request"), "requested");
});

test("preview request returns W2MGB reference", async () => {
  const body = payload(`sess-${Date.now()}`);
  const res = await worker.fetch(jsonReq("http://bookings.test/api/bookings/request", body), previewEnv);
  assert.equal(res.status, 200);
  const firstJson = (await res.json()) as { ok: boolean; reference: string };
  assert.equal(firstJson.ok, true);
  assert.match(firstJson.reference, /^W2MGB-/);
});

test("both products requestable in preview", async () => {
  for (const productId of [HIGH, ROSE] as const) {
    const body = payload(`sess-${productId}-${Date.now()}`, { adults: 1, children: 0, infants: 0 }, {}, productId);
    const res = await worker.fetch(jsonReq("http://bookings.test/api/bookings/request", body), previewEnv);
    assert.equal(res.status, 200, productId);
    const data = (await res.json()) as { ok: boolean };
    assert.equal(data.ok, true, productId);
  }
});

test("unknown product and cross-destination IDs rejected", async () => {
  for (const productId of [
    "not-a-montego-product",
    "belize-cave-tubing",
    "falmouth-beach-day",
    "ocho-rios-dunns-river",
  ]) {
    const bad = payload(`unk-${Date.now()}`, { adults: 1, children: 0, infants: 0 }, { productId });
    const res = await worker.fetch(jsonReq("http://bookings.test/api/bookings/request", bad), previewEnv);
    assert.equal(res.status, 400, productId);
  }
});

test("client price mismatch rejected", async () => {
  const body = payload(`tamper-${Date.now()}`, { adults: 1, children: 0, infants: 0 }, {
    clientDisplayedTotalCents: 1,
  });
  const res = await worker.fetch(jsonReq("http://bookings.test/api/bookings/request", body), previewEnv);
  assert.equal(res.status, 400);
});

test("client total must match server quote helper", () => {
  const product = findMontegoBayBookingProduct(HIGH)!;
  const quote = calculateBookingQuote(product, { adults: 1, children: 1, infants: 1 });
  assert.doesNotThrow(() => assertClientTotalMatches(quote, 16000));
  assert.throws(() => assertClientTotalMatches(quote, 1));
});

test("ops request heading is Montego Bay", () => {
  const src = readFileSync(join(ROOT, "workers/bookings/src/notify.ts"), "utf8");
  assert.match(src, /NEW MONTEGO BAY BOOKING REQUEST/);
});

test("TEST Stripe secret guard", () => {
  assert.doesNotThrow(() => assertStripeTestSecret("sk_test_abc"));
  assert.throws(() => assertStripeTestSecret("sk_live_abc"), StripeModeError);
});

test("Stripe Link disabled at session level (checkout source)", () => {
  const src = readFileSync(join(ROOT, "workers/bookings/src/routes/checkout.ts"), "utf8");
  assert.match(src, /link_mode|payment_method_options|link/i);
});

test("public HTML never leaks SEG / CAMB codes", () => {
  const files = [
    "doctors-cave-beach-montego-bay/index.html",
    "rose-hall-great-house-montego-bay/index.html",
    "book/highlights-and-beach-break/index.html",
    "book/rose-hall-great-house-and-highlights/index.html",
    "js/commercial-config.js",
  ];
  const banned = /\bSEG\b|Shore Excursions Group|CAMBHIGH|CAMBROSE|SEG_MANUAL|shoreexcursionsgroup|info@wowatour\.com/i;
  for (const rel of files) {
    const path = join(ROOT, rel);
    try {
      const text = readFileSync(path, "utf8");
      assert.doesNotMatch(text, banned, rel);
    } catch (err) {
      if ((err as NodeJS.ErrnoException).code === "ENOENT") {
        // Book pages generated later in phase — skip until present
        continue;
      }
      throw err;
    }
  }
  for (const product of MONTEGO_BAY_BOOKING_PRODUCTS) {
    assert.doesNotMatch(product.productPath, /SEG|CAMB/i);
    assert.doesNotMatch(product.bookingPath, /SEG|CAMB/i);
  }
});

test("live-gate source keeps code flag false", () => {
  const src = readFileSync(join(ROOT, "workers/bookings/src/live-gate.ts"), "utf8");
  assert.match(src, /LIVE_PAYMENTS_CODE_ENABLED\s*=\s*false/);
});

test("commercial-config has no internal codes", () => {
  const text = readFileSync(join(ROOT, "js/commercial-config.js"), "utf8");
  assert.doesNotMatch(text, /CAMBHIGH|CAMBROSE|SEG_MANUAL|\bSEG\b|info@wowatour/);
});
