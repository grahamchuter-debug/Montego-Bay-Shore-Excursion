/**
 * Montego Bay destination booking core.
 * Product catalogue: shared/destinations/montego-bay-products.ts
 * Public editorial tours: equity pages via scripts/build-montego-site.py
 * Internal supply mapping: product.supplierReferenceNotes (never public HTML)
 */
import type { DestinationBookingCore } from "../world-booking/types";

export const montegoBayBookingCore = {
  id: "montego-bay",
  siteName: "Montego Bay Shore Excursions",
  siteHostname: "montegobayshoreexcursion.com",
  siteUrl: "https://montegobayshoreexcursion.com",
  bookingEmail: "hello@montegobayshoreexcursion.com",
  originatingSite: "montegobayshoreexcursion.com",
  originatingPort: "Montego Bay, Jamaica",
  bookingRefPrefix: "W2MGB",
  sessionKeyPrefix: "w2-mgb-booking",
  sessionKeyVersion: 1,
  currencyCode: "USD",
  bookableWindow: {
    start: "2026-09-01",
    end: "2028-12-31",
  },
  /** No Montego Bay schedule import — cruise date/ship are customer-entered. */
  schedulePortSlug: "montego-bay",
  customShipSlug: "not-listed",
  contactPath: "/contact",
  termsPath: "/terms",
  privacyPath: "/privacy",
} as const satisfies DestinationBookingCore;
