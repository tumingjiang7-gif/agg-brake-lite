from __future__ import annotations

import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.export_pilot_bundle import export_pilot_bundle


class ExportPilotBundleTests(unittest.TestCase):
    def test_export_pilot_bundle_writes_expected_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "pilot_bundle.zip"
            written = export_pilot_bundle(output_path=output_path)

            self.assertEqual(written, output_path)
            self.assertTrue(output_path.exists())

            with zipfile.ZipFile(output_path, "r") as archive:
                names = set(archive.namelist())

            self.assertIn("README.md", names)
            self.assertIn("FAQ.md", names)
            self.assertIn("SUPPORT_POLICY.md", names)
            self.assertIn("PAYMENT_INSTRUCTIONS_CN.md", names)
            self.assertIn("DELIVERY_WORKFLOW_CN.md", names)
            self.assertIn("FEEDBACK_TEMPLATE.md", names)
            self.assertIn("examples/basic_usage.py", names)
            self.assertIn("src/agg_brake_lite/core.py", names)


if __name__ == "__main__":
    unittest.main()
