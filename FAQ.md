# AGG Brake Lite FAQ

## What is this tool for?

`AGG Brake Lite` is an observe-first local warning tool for AI checkout and payment automation.

It only answers one question:

- "Did this payment amount exceed my local safety limit?"

## What does it do today?

- warns when `amount > max_amount`
- writes a local JSONL log
- exports an anonymous version of that log

## What does it not do?

- it does not call Stripe, PayPal, or other payment providers
- it does not store API keys
- it does not enforce network-level blocking
- it does not provide production guarantees
- it does not try to be a full rule engine

## Is it safe for production?

No production guarantee is provided.

The current version is intentionally small and defaults to fail-open behavior for local logging errors.

## Why is it observe-first?

The first job is to help a developer see whether an AI workflow is trying to spend more than expected.

This reduces fear of false positives and makes first integration lighter.

## What is anonymous export for?

It removes:

- amount
- currency
- max_amount

and keeps only the minimum metadata needed for risk review:

- trace_id
- event_time
- rule_id
- is_safe
- violation
- context_hash

## What counts as useful feedback?

Useful feedback is concrete and real, for example:

- where you integrated the check
- what workflow triggered it
- whether the warning was correct
- what you needed next

Use [FEEDBACK_TEMPLATE.md](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/FEEDBACK_TEMPLATE.md) to keep it short and structured.
