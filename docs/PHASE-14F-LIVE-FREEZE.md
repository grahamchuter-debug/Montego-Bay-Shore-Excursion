# Phase 14F — Montego Bay LIVE freeze / close-out (INTERNAL)

**Status:** COMPLETE — live state frozen.  
**Repo:** Montego-Bay-Shore-Excursion  
**Freeze HEAD (pre-docs):** `8409b7913938f58ff8accab10bceb3a5599d77fb`  
**Public:** https://montegobayshoreexcursion.com · Montego Bay Shore Excursions · `hello@montegobayshoreexcursion.com`

This file is internal. Do not publish.

---

## Live products

### CAMBHIGH — Highlights & Beach Break — Doctor's Cave

| Field | Value |
|---|---|
| Route | `/book/highlights-and-beach-break/` |
| Adult / Child / Infant | $95 / $65 / FREE |
| Ages | Adult 12+ · Child 3–11 · Infant 0–2 |
| Max online | 10 |
| Duration | 5 hours |
| Fulfilment | SEG_MANUAL |
| Cancellation | Free outside 14 days · non-refundable from day 14 |
| Unable to confirm | Full refund |

### CAMBROSE — Rose Hall Great House & Highlights

| Field | Value |
|---|---|
| Route | `/book/rose-hall-great-house-and-highlights/` |
| Adult / Child / Infant | $125 / $80 / FREE |
| Ages | Adult 12+ · Child 3–11 · Infant 0–2 |
| Max online | 10 |
| Duration | Allow around 5–6 hours. |
| Fulfilment | SEG_MANUAL |
| Cancellation | Free outside 14 days · non-refundable from day 14 |
| Unable to confirm | Full refund |

### Deferred

**CAMBPVTDRGUIDEFUL** — Private Driver and Guided Full Day.  
Reason: true group-size / banded pricing needs later engine work or a separately approved simplified model. **Do not activate.**

---

## Production gates (exact)

| Gate | Value |
|---|---|
| `LIVE_PAYMENTS_CODE_ENABLED` | `true` |
| `PAYMENTS_MODE` | `live` |
| `BOOKINGS_ENABLED` | `true` |
| `EMAIL_SENDING_ENABLED` | `true` |
| `LIVE_PAYMENTS_UNLOCK` | `MONTEGO_BAY_LIVE_UNLOCK` |

Public `bookingsApiUrl` → PROD Worker · `defaultPublicBookingStatus` = `BOOKING_ENABLED`.

---

## Infrastructure (isolated)

| Surface | Name / id |
|---|---|
| PROD Worker | `montego-bay-bookings-prod` |
| PROD D1 | `montego-bay-bookings-prod` (`151a937b-1d1c-4ecd-8a12-4c91eb3a76f7`) |
| TEST Worker | `montego-bay-bookings-test` |
| TEST D1 | `montego-bay-bookings-test` (`9bd1fbdd-3757-41e8-afc7-72fedc614c08`) |
| Reference prefix | **W2MGB** |

No shared Worker/D1 with Belize, St Lucia, or other destinations.

Ops runbook: `docs/MONTEGO-BAY-OPS-RUNBOOK.md`.

---

## Controlled LIVE proof (accepted)

| Field | Value |
|---|---|
| Reference | **W2MGB-7R3WFMSK** |
| Product | CAMBHIGH |
| Party | 1 adult |
| Amount | $95 USD (9500¢) |
| Final state | **confirmed / paid** |
| Refund | **NOT PERFORMED** |
| Reason | Graham retained the live payment for normal supplier costs (intentional / approved) |

Refund behaviour was already proven in Phase **14D2** Stripe TEST. This LIVE proof is **complete** without a LIVE refund.

---

## First real customer / traffic trigger

**MONTEGO BAY IS FROZEN FOR ROUTINE DEVELOPMENT.**

Do not polish further just because optimisation is possible.

Trigger a fine-tooth-comb commercial/operational review when **either**:

- **A.** the site begins receiving meaningful Google traffic; **or**
- **B.** the first genuine customer booking arrives.

Review scope at trigger:

- exact supplier/net economics and gross margin  
- Stripe/card costs  
- local/direct supplier opportunity  
- product quality and fulfilment experience  
- customer questions/friction and conversion funnel  
- pricing and cancellation wording  
- product expansion  
- image rights/provenance  
- Private Driver opportunity  
- whether direct supplier contracting is worthwhile  

**Until one of those triggers: leave Montego Bay alone.**

---

## Future live-proof policy (Caribbean World 2.0 clones)

Do **not** automatically create/refund a real live card charge for every new destination that reuses this booking architecture.

**Default proof model:**

1. Full automated/unit validation  
2. Real Stripe TEST checkout  
3. TEST webhook persistence  
4. Explicit TEST confirm  
5. TEST refund  
6. Production secrets/gates verified  
7. Production LIVE Checkout readiness verified safely  
8. No real card charge unless payment architecture materially changed, new engine behaviour exists, a genuine defect requires proof, or Graham explicitly requests another live proof  

Otherwise: **first genuine customer booking = live money proof.**

Do not retroactively rewrite earlier phase reports.

---

## Image debt

Seven active images: provenance status **REVIEW**.  
Not fixed in 14F — deferred to first meaningful-traffic / first-booking review.

---

## Schedules / CT-2

**UNTOUCHED.** No authority schedule import. Do not add under freeze.

---

## Out of scope under freeze

Prices · new products · Private Driver activation · booking/Stripe/D1/email architecture changes · public redesign · other destinations · schedules · CT-2 · artificial payments/refunds.
