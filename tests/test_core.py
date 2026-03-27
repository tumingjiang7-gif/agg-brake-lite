from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from agg_brake_lite import (
    check_payment,
    export_anonymous_logs,
    export_anonymous_logs_to_file,
)


class AggBrakeLiteTests(unittest.TestCase):
    def test_check_payment_allows_safe_amount(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            log_path = Path(tmpdir) / "events.jsonl"
            is_safe, message, event = check_payment(
                amount=50.0,
                max_amount=100.0,
                currency="USD",
                metadata={"cart_id": "safe-001"},
                log_file=log_path,
            )
            self.assertTrue(is_safe)
            self.assertIn("SAFE", message)
            self.assertTrue(event["is_safe"])
            self.assertEqual(event["rule_id"], "payment_amount_limit_v1")
            self.assertIsNotNone(event["trace_id"])
            self.assertIsNotNone(event["context_hash"])
            self.assertTrue(log_path.exists())

    def test_check_payment_warns_when_amount_exceeds_limit(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            log_path = Path(tmpdir) / "events.jsonl"
            is_safe, message, event = check_payment(
                amount=150.0,
                max_amount=100.0,
                currency="USD",
                log_file=log_path,
            )
            self.assertFalse(is_safe)
            self.assertIn("WARNING", message)
            self.assertFalse(event["is_safe"])
            self.assertEqual(event["violation"], "amount_exceeds_max")

    def test_export_anonymous_logs_strips_sensitive_fields(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            log_path = Path(tmpdir) / "events.jsonl"
            check_payment(amount=120.0, max_amount=100.0, log_file=log_path)
            exported = json.loads(export_anonymous_logs(log_file=log_path))
            self.assertEqual(len(exported), 1)
            self.assertIn("trace_id", exported[0])
            self.assertIn("event_time", exported[0])
            self.assertIn("rule_id", exported[0])
            self.assertIn("is_safe", exported[0])
            self.assertIn("violation", exported[0])
            self.assertNotIn("amount", exported[0])
            self.assertNotIn("currency", exported[0])
            self.assertNotIn("max_amount", exported[0])

    def test_export_anonymous_logs_to_file_writes_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            log_path = Path(tmpdir) / "events.jsonl"
            output_path = Path(tmpdir) / "anonymous.json"
            check_payment(amount=120.0, max_amount=100.0, log_file=log_path)
            written = export_anonymous_logs_to_file(output_file=output_path, log_file=log_path)
            self.assertEqual(written, output_path)
            self.assertTrue(output_path.exists())
            exported = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(len(exported), 1)


if __name__ == "__main__":
    unittest.main()
