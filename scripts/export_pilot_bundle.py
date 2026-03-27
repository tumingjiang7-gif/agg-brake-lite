from __future__ import annotations

from pathlib import Path
import shutil
import zipfile


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "dist" / "agg_brake_lite_pilot_bundle.zip"

FILES = [
    ROOT / "README.md",
    ROOT / "FAQ.md",
    ROOT / "SUPPORT_POLICY.md",
    ROOT / "PAYMENT_INSTRUCTIONS_CN.md",
    ROOT / "DELIVERY_WORKFLOW_CN.md",
    ROOT / "FEEDBACK_TEMPLATE.md",
    ROOT / "RELEASE_NOTES_v0.1.0.md",
    ROOT / "LICENSE",
    ROOT / "examples" / "basic_usage.py",
    ROOT / "examples" / "templates" / "langchain_example.py",
    ROOT / "examples" / "templates" / "crewai_example.py",
    ROOT / "examples" / "templates" / "autogpt_example.py",
    ROOT / "src" / "agg_brake_lite" / "__init__.py",
    ROOT / "src" / "agg_brake_lite" / "core.py",
]


def export_pilot_bundle(output_path: Path = DEFAULT_OUTPUT) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in FILES:
            archive.write(path, path.relative_to(ROOT))

    return output_path


if __name__ == "__main__":
    path = export_pilot_bundle()
    print(path)
