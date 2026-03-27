# AGG Brake Lite

Minimal local risk warning tool for AI checkout and payment automation.

## What It Does

`agg_brake_lite` is a tiny Python package for one narrow job:

- warn when an AI-driven checkout or payment amount exceeds a configured limit
- write a local JSONL risk log
- export an anonymous version of that log

This first version is intentionally small:

- local only
- observe-first
- one rule only: `amount > max_amount`

## Scope

Use this package to test whether AI-driven money-adjacent actions need a local brake.

This package does **not**:

- call payment providers
- hold secrets
- block network requests directly
- implement a general rule engine
- provide production guarantees

## Quick Start

```python
from agg_brake_lite import (
    check_payment,
    export_anonymous_logs,
    export_anonymous_logs_to_file,
)

is_safe, message, event = check_payment(
    amount=120,
    max_amount=100,
    currency="USD",
    metadata={"cart_id": "demo-cart-001"},
)
print(is_safe)
print(message)
print(event)

print(export_anonymous_logs())
print(export_anonymous_logs_to_file())
```

## Install

From this repository:

```bash
pip install -e .
```

Repository:

- [https://github.com/tumingjiang7-gif/agg-brake-lite.git](https://github.com/tumingjiang7-gif/agg-brake-lite.git)

## Core API

### `check_payment(amount, max_amount, currency="USD", metadata=None, log_file="agg_brake_log.jsonl")`

Returns:

- `is_safe`: `bool`
- `message`: `str`
- `event`: `dict`

Behavior:

- if `amount <= max_amount`, returns a safe result
- if `amount > max_amount`, returns a warning result
- every call appends a JSONL event locally
- automatically generates a `trace_id`
- computes `context_hash` when optional `metadata` is provided

### `export_anonymous_logs(log_file="agg_brake_log.jsonl")`

Returns a JSON string with anonymous events. It strips:

- `amount`
- `currency`
- `max_amount`

and keeps only:

- `trace_id`
- `event_time`
- `rule_id`
- `is_safe`
- `violation`
- `context_hash`

### `export_anonymous_logs_to_file(output_file="agg_brake_anonymous_export.json")`

Writes the anonymous export to a local file and returns the output path.

## Example

See:

- [examples/basic_usage.py](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/examples/basic_usage.py)
- [examples/templates/langchain_example.py](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/examples/templates/langchain_example.py)
- [examples/templates/crewai_example.py](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/examples/templates/crewai_example.py)
- [examples/templates/autogpt_example.py](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/examples/templates/autogpt_example.py)
- [FAQ.md](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/FAQ.md)
- [FEEDBACK_TEMPLATE.md](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/FEEDBACK_TEMPLATE.md)
- [RELEASE_NOTES_v0.1.0.md](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/RELEASE_NOTES_v0.1.0.md)
- [SUPPORT_POLICY.md](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/SUPPORT_POLICY.md)
- [POST_TEMPLATES.md](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/POST_TEMPLATES.md)
- [PAYMENT_INSTRUCTIONS_CN.md](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/PAYMENT_INSTRUCTIONS_CN.md)
- [DELIVERY_WORKFLOW_CN.md](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/DELIVERY_WORKFLOW_CN.md)
- [VALIDATION_PLAYBOOK.md](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/VALIDATION_PLAYBOOK.md)
- [VALIDATION_SCORECARD_TEMPLATE.md](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/VALIDATION_SCORECARD_TEMPLATE.md)
- [scripts/release_check.ps1](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/scripts/release_check.ps1)
- [scripts/release_check.sh](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/scripts/release_check.sh)
- [scripts/export_pilot_bundle.py](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/scripts/export_pilot_bundle.py)

## Founder Pilot

Current founder pilot defaults:

- price: `19.9 CNY`
- payment: `WeChat`
- note: `AGG Brake + your email`
- contact: `642635193@qq.com`

Keep the first offer simple:

- one-time founder pilot purchase
- current observe-first package
- bug fixes for the first release window
- no promise of full future product access

## Pilot Feedback

If someone really installs this package, ask for structured feedback instead of open-ended chat.

Use:

- [FEEDBACK_TEMPLATE.md](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/FEEDBACK_TEMPLATE.md)

## Manual Delivery

If you need to hand a founder pilot bundle to someone, export one zip:

```bash
python scripts/export_pilot_bundle.py
```

That bundle includes the README, FAQ, support policy, feedback template, examples, and source files needed for a lightweight pilot handoff.

For the current China-first flow, see:

- [PAYMENT_INSTRUCTIONS_CN.md](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/PAYMENT_INSTRUCTIONS_CN.md)
- [DELIVERY_WORKFLOW_CN.md](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/DELIVERY_WORKFLOW_CN.md)

## Disclaimer

This package is for early testing and evaluation.

- No warranty is provided.
- Production use is at the user's own risk.
- The package defaults to fail-open behavior for local logging errors.
