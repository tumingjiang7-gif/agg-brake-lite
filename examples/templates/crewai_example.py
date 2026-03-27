"""Minimal copy-paste sketch for calling AGG Brake Lite inside a CrewAI task."""

from agg_brake_lite import check_payment


def review_checkout(amount: float, currency: str = "USD") -> str:
    is_safe, message, event = check_payment(
        amount=amount,
        max_amount=100,
        currency=currency,
        metadata={"framework": "crewai", "task": "review_checkout"},
    )

    if not is_safe:
        return f"Risk observed. Escalate to a human before paying. {message} trace_id={event['trace_id']}"

    return f"Observed safe checkout. trace_id={event['trace_id']}"
