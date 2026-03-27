"""Minimal copy-paste sketch for calling AGG Brake Lite before an AutoGPT payment action."""

from agg_brake_lite import check_payment


def guard_payment(amount: float, currency: str = "USD") -> tuple[bool, str]:
    is_safe, message, event = check_payment(
        amount=amount,
        max_amount=100,
        currency=currency,
        metadata={"framework": "autogpt", "action": "guard_payment"},
    )

    if not is_safe:
        return False, f"Observed risky payment. Hold execution. {message} trace_id={event['trace_id']}"

    return True, f"Payment still within the local safety limit. trace_id={event['trace_id']}"
