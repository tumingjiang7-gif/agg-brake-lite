"""Minimal copy-paste sketch for calling AGG Brake Lite inside a LangChain tool flow."""

from agg_brake_lite import check_payment


def checkout_tool(amount: float, currency: str = "USD") -> str:
    is_safe, message, event = check_payment(
        amount=amount,
        max_amount=100,
        currency=currency,
        metadata={"framework": "langchain", "tool": "checkout_tool"},
    )

    if not is_safe:
        return f"Observed risky checkout. Review before moving money. {message} trace_id={event['trace_id']}"

    return f"Checkout looks safe to continue. trace_id={event['trace_id']}"
