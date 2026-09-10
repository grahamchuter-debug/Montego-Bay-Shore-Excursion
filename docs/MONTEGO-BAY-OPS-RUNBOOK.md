# Montego Bay — Operations Runbook (INTERNAL)

**Audience:** Graham / ops only. Do not publish on the public site.  
**Status:** Live (Phase 14F freeze).  
**Public brand:** Montego Bay Shore Excursions · `hello@montegobayshoreexcursion.com`

---

## Internal product map

| Internal code | Customer-facing name | Book route |
|---|---|---|
| **CAMBHIGH** | Highlights & Beach Break — Doctor's Cave | `/book/highlights-and-beach-break/` |
| **CAMBROSE** | Rose Hall Great House & Highlights | `/book/rose-hall-great-house-and-highlights/` |

**Deferred (do not activate):** CAMBPVTDRGUIDEFUL — Private Driver and Guided Full Day.

Fulfilment mode for both live products: **SEG_MANUAL**. Supplier/source codes stay internal.

---

## Request-to-book lifecycle

1. **Customer pays** via public book journey (Stripe LIVE Checkout).
2. Webhook marks booking **requested / paid**. Payment received is **not** confirmation.
3. **Ops receives** the `ops_request` email (includes internal codes / review link).
4. Graham **checks/secures** the relevant SEG excursion manually.
5. **Only after** successful supplier/SEG confirmation: use explicit operator **CONFIRM** (review token).
6. Customer receives **customer_confirmed** email.
7. Any supplier/SEG voucher or ticket is sent **manually** where required.
8. If **unable to confirm:** customer must receive a **full refund**.
9. **Paid ≠ confirmed.** Never treat payment success as an excursion confirmation before step 5.

---

## Operator actions

- Confirm / decline only via the **single-use review token** from the ops email (or equivalent authenticated operator path).
- Unauthenticated confirm/decline must fail (`OPERATOR_FORBIDDEN`).
- Decline after confirm is blocked (`ALREADY_CONFIRMED`) — use Stripe refund + webhook path if a confirmed booking must be refunded.

---

## Unable to confirm

Full refund to the customer. Booking engine supports refund via operator decline (pre-confirm) or Stripe refund → `charge.refunded` webhook (payment → `refunded`; confirmed status stays confirmed if already confirmed).

---

## References

- Prefix: **W2MGB**
- PROD Worker: `montego-bay-bookings-prod`
- PROD D1: `montego-bay-bookings-prod`
- Freeze / close-out: `docs/PHASE-14F-LIVE-FREEZE.md`
