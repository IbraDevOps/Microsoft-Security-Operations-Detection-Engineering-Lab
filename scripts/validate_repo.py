#!/usr/bin/env python3

"""Validate required project documentation and structure."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "architecture/architecture.md",
    "architecture/threat-model.md",
    "architecture/security-requirements.md",
]

REQUIRED_README_SECTIONS = [
    "Overview",
    "Architecture",
    "Detection",
    "Roadmap",
]

REQUIRED_DETECTIONS = [
    "DET-001",
    "DET-002",
    "DET-003",
    "DET-004",
    "DET-005",
]


def validate_required_files():
    errors = []

    for filename in REQUIRED_FILES:
        path = ROOT / filename

        if not path.is_file():
            errors.append(f"Missing required file: {filename}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"Required file is empty: {filename}")

    return errors


def validate_readme():
    errors = []
    path = ROOT / "README.md"

    if not path.is_file():
        return ["README.md does not exist"]

    content = path.read_text(encoding="utf-8").lower()

    for section in REQUIRED_README_SECTIONS:
        if section.lower() not in content:
            errors.append(f"README missing topic: {section}")

    for detection in REQUIRED_DETECTIONS:
        if detection.lower() not in content:
            errors.append(f"README missing detection: {detection}")

    return errors


def validate_repository():
    errors = []
    errors.extend(validate_required_files())
    errors.extend(validate_readme())

    if errors:
        print("[FAIL] Repository validation failed")

        for error in errors:
            print(f"  - {error}")

        return False

    print("[PASS] Repository structure and documentation validated")
    return True


if __name__ == "__main__":
    raise SystemExit(0 if validate_repository() else 1)
