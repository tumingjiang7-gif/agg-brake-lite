"""Minimal local observe-first brake for AI checkout/payment flows."""

from __future__ import annotations

import hashlib
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_LOG_FILE = "agg_brake_log.jsonl"
RULE_ID = "payment_amount_limit_v1"

_DISCLAIMER = """\
[AGG Brake Lite]
Observe-first local warning tool for AI checkout/payment automation.
No warranty is provided. Production use is at the user's own risk.
"""
_DISCLAIMER_EMITTED = False


def _emit_disclaimer_once() -> None:
    global _DISCLAIMER_EMITTED
    if _DISCLAIMER_EMITTED:
        return
    print(_DISCLAIMER)
    _DISCLAIMER_EMITTED = True


def _write_log(log_path: Path, event: dict[str, Any]) -> None:
    try:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with log_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(event, ensure_ascii=False) + "\n")
    except Exception:
        # Fail-open: logging problems must not block the caller.
        return


def _build_context_hash(metadata: dict[str, Any] | None) -> str | None:
    if not metadata:
        return None
    try:
        encoded = json.dumps(metadata, ensure_ascii=False, sort_keys=True).encode("utf-8")
    except Exception:
        return None
    return hashlib.sha256(encoded).hexdigest()


def check_payment(
    amount: float,
    max_amount: float,
    currency: str = "USD",
    metadata: dict[str, Any] | None = None,
    log_file: str | Path = DEFAULT_LOG_FILE,
) -> tuple[bool, str, dict[str, Any]]:
    """Run the one and only MVP rule: amount must not exceed max_amount."""
    _emit_disclaimer_once()

    event_time = datetime.now(timezone.utc).isoformat()
    trace_id = str(uuid.uuid4())
    context_hash = _build_context_hash(metadata)
    is_safe = amount <= max_amount
    message = (
        f"SAFE: amount {amount}{currency} is within the configured limit."
        if is_safe
        else f"WARNING: amount {amount}{currency} exceeds max amount {max_amount}."
    )

    event: dict[str, Any] = {
        "trace_id": trace_id,
        "event_time": event_time,
        "amount": amount,
        "currency": currency,
        "max_amount": max_amount,
        "is_safe": is_safe,
        "rule_id": RULE_ID,
        "violation": None if is_safe else "amount_exceeds_max",
        "context_hash": context_hash,
    }

    _write_log(Path(log_file), event)
    print(f"[AGG Brake] {message}")
    return is_safe, message, event


def export_anonymous_logs(log_file: str | Path = DEFAULT_LOG_FILE) -> str:
    """Return an anonymous JSON export suitable for manual sharing."""
    anonymous_logs: list[dict[str, Any]] = []
    log_path = Path(log_file)
    if not log_path.exists():
        return "[]"

    try:
        with log_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                event = json.loads(line)
                anonymous_logs.append(
                    {
                        "trace_id": event.get("trace_id"),
                        "event_time": event["event_time"],
                        "rule_id": event["rule_id"],
                        "is_safe": event["is_safe"],
                        "violation": event.get("violation"),
                        "context_hash": event.get("context_hash"),
                    }
                )
    except Exception:
        return "[]"

    return json.dumps(anonymous_logs, ensure_ascii=False, indent=2)


def export_anonymous_logs_to_file(
    output_file: str | Path = "agg_brake_anonymous_export.json",
    log_file: str | Path = DEFAULT_LOG_FILE,
) -> Path:
    """Write the anonymous export to disk and return the resulting path."""
    export_path = Path(output_file)
    export_path.parent.mkdir(parents=True, exist_ok=True)
    export_path.write_text(export_anonymous_logs(log_file=log_file), encoding="utf-8")
    return export_path
