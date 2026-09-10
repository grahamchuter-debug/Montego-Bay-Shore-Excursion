import { montegoBayBookingCore } from "./montego-bay";
import type { AgeBand, BookableProductConfig, ProductCapacity, ProductPricing } from "../world-booking/types";

/**
 * Operational routing: Wow A Tour ops mailbox for Graham’s manual fulfilment.
 * Public customers never see SEG. Graham places corresponding bookings via his
 * established SEG affiliate / white-label account using INTERNAL supply refs only.
 */
const OPERATIONS = {
  id: "wow-a-tour-operations",
  displayName: "Wow A Tour",
  notificationEmail: "info@wowatour.com",
  routingStatus: "production_ready" as const,
};

const REQUEST_SETTLEMENT = "charge_refund" as const;

/** Graham online max — never describe as supplier / vehicle / boat capacity. */
const MGB_CAPACITY: ProductCapacity = {
  minGuests: 1,
  maxGuestsPerBooking: 10,
  maxGuestsPerBookingSource: "approved",
  supplierGroupSize: null,
  maxGuestsPerGuide: null,
};

/** Adult 12+, Child 3–11, Infant 0–2 free (must be recorded). */
const COMBO_AGE_BANDS: readonly AgeBand[] = [
  { id: "adult", label: "Adults (12+)", minAge: 12, maxAge: null, pricingStatus: "priced" },
  { id: "child", label: "Children (3–11)", minAge: 3, maxAge: 11, pricingStatus: "priced" },
  { id: "infant", label: "Infants (0–2)", minAge: 0, maxAge: 2, pricingStatus: "priced" },
];

function adultChildInfantUsd(adultAmount: number, childAmount: number): ProductPricing {
  return {
    model: "adult_child",
    currency: "USD",
    adultAmount,
    childAmount,
    childPricingStatus: "priced",
    infantAmount: 0,
    infantPricingStatus: "priced",
    pricingNeedsConfirmation: false,
  };
}

const SHARED_PENDING = [
  "Customer cancellation APPROVED: free outside 14 days before excursion; from the 14th day non-refundable.",
  "Unable to confirm after payment: full refund to original payment method.",
  "Meeting: Cruise ship pier; exact instructions after confirmation.",
  "Fulfilment: Graham places corresponding booking via established SEG affiliate / white-label route (INTERNAL).",
  "Payment received ≠ excursion confirmed.",
  "Online max 10 guests per booking (Graham online limit — not supplier capacity).",
  "At least one paying adult required.",
  "LIVE_PAYMENTS_CODE_ENABLED true from Phase 14E Graham unlock (request-to-book).",
  "commercial_status=SEG_FULFILMENT_READY · fulfilment_mode=SEG_MANUAL · supplier=UNKNOWN · direct_supplier_status=NOT_CONTACTED · net_cost=UNKNOWN · margin=UNKNOWN",
] as const;

export const MONTEGO_BAY_CANCELLATION_COPY = {
  customerCancellation:
    "Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable. If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  freeWindow: "Free cancellation outside 14 days before your excursion.",
  insideWindow: "From the 14th day before your excursion, bookings are non-refundable.",
  unableToConfirm:
    "If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  paymentNotConfirmation:
    "Secure your booking request with payment today. We'll confirm your excursion separately, and if we're unable to confirm it, you'll receive a full refund.",
  meetingInstructions: "Meeting instructions will be provided with your confirmed excursion details.",
  overTenGuidance: "For groups larger than 10, email hello@montegobayshoreexcursion.com before requesting.",
} as const;

const CAMBHIGH: BookableProductConfig = {
  id: "highlights-and-beach-break",
  destinationId: montegoBayBookingCore.id,
  slug: "highlights-and-beach-break",
  name: "Highlights & Beach Break — Doctor's Cave",
  durationLabel: "5 hours",
  bookingMode: "request",
  availability: "live",
  bookingPath: "/book/highlights-and-beach-break",
  receivedPath: "/book/highlights-and-beach-break/received",
  confirmedPath: "/book/highlights-and-beach-break/received",
  productPath: "/doctors-cave-beach-montego-bay/",
  pricing: adultChildInfantUsd(95, 65),
  ageBands: COMBO_AGE_BANDS,
  capacity: MGB_CAPACITY,
  requiredCustomerFields: ["name", "email", "phone"],
  supplier: OPERATIONS,
  paymentSettlement: REQUEST_SETTLEMENT,
  schedulePortSlug: "montego-bay",
  pendingCommercialRules: [
    ...SHARED_PENDING,
    "Adult USD 95 (12+) · Child USD 65 (3–11) · Infant 0–2 FREE (must record) · require ≥1 adult",
    "Combo: Montego Bay highlights + city/history elements + Doctor's Cave Bathing Beach — NOT a Doctor's Cave-only transfer",
    "Do not invent itinerary stop list beyond verified source facts",
    "Meeting: Cruise ship pier; exact instructions after confirmation",
  ],
  supplierReferenceNotes: [
    "INTERNAL SUPPLY: SEG_MANUAL · CAMBHIGH",
    "INTERNAL CODE: CAMBHIGH",
    "Supplier contact: UNKNOWN · NOT_CONTACTED · net/margin UNKNOWN",
    "Fulfilment: place via established SEG affiliate / white-label route (manual — do not automate).",
    "Selling: Adult USD 95 · Child USD 65 · Infant FREE (0–2 recorded).",
    "Customer cancellation: Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable.",
    "Unable to confirm after payment: full refund to original payment method.",
  ],
};

const CAMBROSE: BookableProductConfig = {
  id: "rose-hall-great-house-and-highlights",
  destinationId: montegoBayBookingCore.id,
  slug: "rose-hall-great-house-and-highlights",
  name: "Rose Hall Great House & Highlights",
  durationLabel: "Allow around 5–6 hours",
  bookingMode: "request",
  availability: "live",
  bookingPath: "/book/rose-hall-great-house-and-highlights",
  receivedPath: "/book/rose-hall-great-house-and-highlights/received",
  confirmedPath: "/book/rose-hall-great-house-and-highlights/received",
  productPath: "/rose-hall-great-house-montego-bay/",
  pricing: adultChildInfantUsd(125, 80),
  ageBands: COMBO_AGE_BANDS,
  capacity: MGB_CAPACITY,
  requiredCustomerFields: ["name", "email", "phone"],
  supplier: OPERATIONS,
  paymentSettlement: REQUEST_SETTLEMENT,
  schedulePortSlug: "montego-bay",
  pendingCommercialRules: [
    ...SHARED_PENDING,
    "Adult USD 125 (12+) · Child USD 80 (3–11) · Infant 0–2 FREE (must record) · require ≥1 adult",
    "Highlights excursion including Rose Hall Great House entrance — NOT merely an entrance ticket",
    "Duration: source conflict 5h vs 6h — customer copy uses 'Allow around 5–6 hours.' Do not assert one exact duration.",
    "Optional beach / incidental source details must not be overstated",
    "Meeting: Cruise ship pier; exact instructions after confirmation",
  ],
  supplierReferenceNotes: [
    "INTERNAL SUPPLY: SEG_MANUAL · CAMBROSE",
    "INTERNAL CODE: CAMBROSE",
    "Supplier contact: UNKNOWN · NOT_CONTACTED · net/margin UNKNOWN",
    "Fulfilment: place via established SEG affiliate / white-label route (manual — do not automate).",
    "Selling: Adult USD 125 · Child USD 80 · Infant FREE (0–2 recorded).",
    "Customer cancellation: Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable.",
    "Unable to confirm after payment: full refund to original payment method.",
  ],
};

export const MONTEGO_BAY_BOOKING_PRODUCTS: readonly BookableProductConfig[] = [CAMBHIGH, CAMBROSE];

export function findMontegoBayBookingProduct(productId: string): BookableProductConfig | undefined {
  return MONTEGO_BAY_BOOKING_PRODUCTS.find((p) => p.id === productId);
}
