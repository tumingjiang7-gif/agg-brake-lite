from agg_brake_lite import (
    check_payment,
    export_anonymous_logs,
    export_anonymous_logs_to_file,
)


def main() -> None:
    safe_result = check_payment(
        amount=50.0,
        max_amount=100.0,
        metadata={"cart_id": "cart-safe-001"},
    )
    print(safe_result)

    warning_result = check_payment(
        amount=150.0,
        max_amount=100.0,
        metadata={"cart_id": "cart-risk-001"},
    )
    print(warning_result)

    print(export_anonymous_logs())
    print(export_anonymous_logs_to_file())


if __name__ == "__main__":
    main()
