# AGG Brake Lite v0.1.0

## Scope

This release is intentionally narrow.

- local only
- observe-first
- one rule only: `amount > max_amount`

## Included

- `check_payment(...)`
- local JSONL risk logging
- anonymous export
- `trace_id`
- optional `context_hash`
- basic example
- lightweight templates for LangChain, CrewAI, and AutoGPT

## Not Included

- enforce mode
- approval links
- dashboards
- cloud rule distribution
- provider-specific payment integrations

## Intended Use

This version is for early pilot validation.

Its job is to answer:

- does a local AI payment brake solve a real problem?
- will a real user install it and run it?
- will a real user export logs or share integration feedback?
