#!/usr/bin/env python3

"""Basic credential-pattern checks for tracked project files."""

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PATTERNS = {
    "AWS access key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "Private key header": re.compile(
        r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"
    ),
}

SKIP_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".pdf",
    ".zip", ".pyc", ".ico",
}


def tracked_files():
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        capture_output=True,
        check=True,
    )

    for name in result.stdout.split(b"\0"):
        if name:
            yield ROOT / name.decode("utf-8", errors="surrogateescape")


def main():
    findings = []

    for path in tracked_files():
        if not path.is_file() or path.suffix.lower() in SKIP_SUFFIXES:
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeError:
            continue

        for label, pattern in PATTERNS.items():
            if pattern.search(content):
                findings.append(f"{path.relative_to(ROOT)}: {label}")

    if findings:
        print("[FAIL] Potential credentials detected")

        for finding in findings:
            print(f"  - {finding}")

        return 1

    print("[PASS] Basic credential-pattern checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
