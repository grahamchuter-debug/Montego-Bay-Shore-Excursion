# Phase 14D — Montego Bay TEST secrets (names only)

Graham adds these manually. Never commit values.

## TEST Worker: `montego-bay-bookings-test`

```bash
cd Montego-Bay-Shore-Excursion
npx wrangler secret put STRIPE_SECRET_KEY --config workers/bookings/wrangler.jsonc
npx wrangler secret put STRIPE_WEBHOOK_SECRET --config workers/bookings/wrangler.jsonc
npx wrangler secret put OPERATOR_TEST_TOKEN --config workers/bookings/wrangler.jsonc
# Optional until email proof:
# npx wrangler secret put RESEND_API_KEY --config workers/bookings/wrangler.jsonc
# npx wrangler secret put TEST_ONLY_EMAIL_OVERRIDE --config workers/bookings/wrangler.jsonc
```

Stripe TEST webhook endpoint:

`https://montego-bay-bookings-test.dark-violet-8d91.workers.dev/api/stripe/webhook`

Events (same estate pattern as Belize/St Lucia):

- `checkout.session.completed`
- `checkout.session.expired`
- `checkout.session.async_payment_failed`
- `charge.refunded`
- `payment_intent.payment_failed` (if used elsewhere)

## PROD Worker: `montego-bay-bookings-prod` (scaffold only — locked)

Do **not** unlock in 14D.

`BOOKINGS_ENABLED=false` · `EMAIL_SENDING_ENABLED=false` · `LIVE_PAYMENTS_CODE_ENABLED=false` in code.

PROD secrets belong in Phase 14E.
