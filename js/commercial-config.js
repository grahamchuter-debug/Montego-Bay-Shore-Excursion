/**
 * Public commercial status for Montego Bay Shore Excursion (Phase 14D).
 * INTERNAL supply refs must never be rendered on customer pages.
 *
 * Gate values:
 * - PRODUCTION_READY_LOCKED — journey visible; live Pay & request disabled
 * - BOOKING_ENABLED — checkout allowed against the configured Worker
 *
 * Phase 14E: public config points at PROD Worker — two Montego Bay RTB products live.
 */
window.MGB_COMMERCIAL = {
  bookingsApiUrl: "https://montego-bay-bookings-prod.dark-violet-8d91.workers.dev",
  email: "hello@montegobayshoreexcursion.com",
  siteName: "Montego Bay Shore Excursions",
  defaultPublicBookingStatus: "BOOKING_ENABLED",
  cancellation:
    "Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable. If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  paymentNotConfirmation:
    "Secure your booking request with payment today. We'll confirm your excursion separately, and if we're unable to confirm it, you'll receive a full refund.",
  unableToConfirm:
    "If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  meetingInstructions:
    "Meeting instructions will be provided with your confirmed excursion details.",
  overTenGuidance:
    "For groups larger than 10, email hello@montegobayshoreexcursion.com before requesting.",
  products: {
    "highlights-and-beach-break": {
      productId: "highlights-and-beach-break",
      slug: "highlights-and-beach-break",
      name: "Highlights & Beach Break — Doctor's Cave",
      shortTitle: "Highlights & Beach Break",
      productPath: "/doctors-cave-beach-montego-bay/",
      bookingPath: "/book/highlights-and-beach-break/",
      receivedPath: "/book/highlights-and-beach-break/received/",
      adultUsd: 95,
      childUsd: 65,
      infantUsd: 0,
      guestModel: "adult_child_infant",
      durationLabel: "5 hours",
      maxGuests: 10,
      publicBookingStatus: "BOOKING_ENABLED",
      displayPrice: "Adults (12+) $95 · Children (3–11) $65 · Infants (0–2) free",
    },
    "rose-hall-great-house-and-highlights": {
      productId: "rose-hall-great-house-and-highlights",
      slug: "rose-hall-great-house-and-highlights",
      name: "Rose Hall Great House & Highlights",
      shortTitle: "Rose Hall & Highlights",
      productPath: "/rose-hall-great-house-montego-bay/",
      bookingPath: "/book/rose-hall-great-house-and-highlights/",
      receivedPath: "/book/rose-hall-great-house-and-highlights/received/",
      adultUsd: 125,
      childUsd: 80,
      infantUsd: 0,
      guestModel: "adult_child_infant",
      durationLabel: "Allow around 5–6 hours",
      maxGuests: 10,
      publicBookingStatus: "BOOKING_ENABLED",
      displayPrice: "Adults (12+) $125 · Children (3–11) $80 · Infants (0–2) free",
    },
  },
};
