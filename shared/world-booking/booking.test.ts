/**
 * Shared booking engine tests — Montego Bay Phase 14D (two RTB products).
 */
import assert from "node:assert/strict";
import { test } from "node:test";
import {
  findMontegoBayBookingProduct,
  MONTEGO_BAY_BOOKING_PRODUCTS,
  MONTEGO_BAY_CANCELLATION_COPY,
} from "../destinations/montego-bay-products";
import { montegoBayBookingCore } from "../destinations/montego-bay";
import {
  assertClientTotalMatches,
  calculateBookingQuote,
  createBookingReference,
  destinationBrandFromCore,
  requestedCustomerEmail,
  statusAfterPaymentSuccess,
  supplierRequestEmail,
  validateCruise,
  validateCustomer,
} from "./index";

const brand = destinationBrandFromCore(montegoBayBookingCore);
const high = findMontegoBayBookingProduct("highlights-and-beach-break");
const rose = findMontegoBayBookingProduct("rose-hall-great-house-and-highlights");
assert.ok(high);
assert.ok(rose);

test("two Montego Bay product IDs present", () => {
  assert.equal(MONTEGO_BAY_BOOKING_PRODUCTS.length, 2);
  assert.deepEqual(
    MONTEGO_BAY_BOOKING_PRODUCTS.map((p) => p.id).sort(),
    ["highlights-and-beach-break", "rose-hall-great-house-and-highlights"].sort(),
  );
});

test("CAMBHIGH adult 95 child 65 infant free; requires adult", () => {
  assert.equal(high!.pricing.adultAmount, 95);
  assert.equal(high!.pricing.childAmount, 65);
  assert.equal(high!.pricing.infantAmount, 0);
  assert.equal(high!.pricing.infantPricingStatus, "priced");
  assert.equal(calculateBookingQuote(high!, { adults: 1, children: 0, infants: 0 }).amountCents, 9500);
  assert.equal(calculateBookingQuote(high!, { adults: 2, children: 0, infants: 0 }).amountCents, 19000);
  assert.equal(calculateBookingQuote(high!, { adults: 1, children: 1, infants: 0 }).amountCents, 16000);
  assert.equal(calculateBookingQuote(high!, { adults: 1, children: 1, infants: 1 }).amountCents, 16000);
  assert.equal(calculateBookingQuote(high!, { adults: 1, children: 1, infants: 1 }).partySize, 3);
  assert.throws(() => calculateBookingQuote(high!, { adults: 0, children: 1, infants: 0 }));
});

test("CAMBROSE adult 125 child 80 infant free; duration wording safe", () => {
  assert.equal(rose!.pricing.adultAmount, 125);
  assert.equal(rose!.pricing.childAmount, 80);
  assert.match(rose!.durationLabel, /5–6|5-6/);
  assert.equal(calculateBookingQuote(rose!, { adults: 1, children: 0, infants: 0 }).amountCents, 12500);
  assert.equal(calculateBookingQuote(rose!, { adults: 1, children: 1, infants: 0 }).amountCents, 20500);
  assert.equal(calculateBookingQuote(rose!, { adults: 1, children: 0, infants: 2 }).amountCents, 12500);
});

test("max 10 guests; 11 rejected; infants count toward max", () => {
  for (const product of [high!, rose!]) {
    assert.equal(product.capacity.maxGuestsPerBooking, 10);
    assert.doesNotThrow(() => calculateBookingQuote(product, { adults: 10, children: 0, infants: 0 }));
    assert.throws(() => calculateBookingQuote(product, { adults: 11, children: 0, infants: 0 }));
    assert.throws(() => calculateBookingQuote(product, { adults: 0, children: 0, infants: 0 }));
    assert.doesNotThrow(() => calculateBookingQuote(product, { adults: 8, children: 1, infants: 1 }));
    assert.throws(() => calculateBookingQuote(product, { adults: 8, children: 1, infants: 2 }));
  }
});

test("client total must match server quote", () => {
  const quote = calculateBookingQuote(high!, { adults: 1, children: 1, infants: 1 });
  assert.doesNotThrow(() => assertClientTotalMatches(quote, 16000));
  assert.throws(() => assertClientTotalMatches(quote, 1));
});

test("payment success status is requested not confirmed", () => {
  assert.equal(statusAfterPaymentSuccess("request"), "requested");
});

test("booking references use Montego Bay W2MGB prefix", () => {
  assert.match(createBookingReference(montegoBayBookingCore), /^W2MGB-/);
  assert.equal(montegoBayBookingCore.bookingRefPrefix, "W2MGB");
});

test("customer and cruise validation", () => {
  assert.equal(
    validateCustomer({ name: "Alex Traveller", email: "alex@example.com", phone: "+447700900123" }),
    null,
  );
  assert.ok(validateCustomer({ name: "A", email: "x", phone: "1" }));
  assert.ok(
    validateCruise({
      date: "2020-01-01",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    }),
  );
  assert.equal(
    validateCruise({
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    }),
    null,
  );
});

test("cancellation copy covers 14-day policy and full refund", () => {
  assert.match(MONTEGO_BAY_CANCELLATION_COPY.customerCancellation, /outside 14 days/i);
  assert.match(MONTEGO_BAY_CANCELLATION_COPY.customerCancellation, /14th day/i);
  assert.match(MONTEGO_BAY_CANCELLATION_COPY.unableToConfirm, /full refund/i);
  assert.match(MONTEGO_BAY_CANCELLATION_COPY.paymentNotConfirmation, /confirm.*separately|separately.*confirm/i);
});

test("customer email never exposes SEG or internal codes", () => {
  const mail = requestedCustomerEmail({
    brand,
    product: high!,
    reference: "W2MGB-TEST0001",
    cruise: {
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    },
    guests: { adults: 1, children: 0, infants: 0 },
    amountLabel: "USD $95.00",
    customerName: "Alex Traveller",
  });
  const blob = JSON.stringify(mail);
  assert.doesNotMatch(blob, /\bSEG\b|CAMBHIGH|Shore Excursions Group|info@wowatour/i);
  assert.match(blob, /request|confirm/i);
});

test("ops email includes internal supply notes for Graham", () => {
  const mail = supplierRequestEmail({
    product: high!,
    reference: "W2MGB-TEST0001",
    cruise: {
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    },
    guests: { adults: 1, children: 1, infants: 1 },
    amountLabel: "USD $160.00",
    customer: {
      name: "Alex Traveller",
      email: "alex@example.com",
      phone: "+447700900123",
    },
    destinationLabel: "Montego Bay Shore Excursions — new booking request",
  });
  const blob = JSON.stringify(mail);
  assert.match(blob, /CAMBHIGH|SEG_MANUAL/i);
});

test("reject foreign destination product lookup", () => {
  assert.equal(findMontegoBayBookingProduct("belize-cave-tubing"), undefined);
  assert.equal(findMontegoBayBookingProduct("private-driver-montego-bay"), undefined);
});
