#!/usr/bin/env python3
"""Bootstrap one Suno cycle — reusable, parametrized.

Replaces the hand-typed inline bash that was used to compute the next version
number (`ls prompts/ | grep -oE 'v[0-9]+' | sort -V | tail -1`) and to refresh
the novelty surface. Those are deterministic, recurring cycle steps and must
live in a script per CLAUDE.md "Scripting discipline" — never as one-off bash.

Does the deterministic pre-draft work and emits a compact JSON summary:
  1. compute the next version number from prompts/*-v<N>.yaml
  2. (optional) refresh experiments/novelty_surface.json via novelty_surface.py

Examples
--------
  python3 scripts/cycle_start.py                # next version + refresh novelty
  python3 scripts/cycle_start.py --no-novelty   # just compute the next version
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "prompts"
NOVELTY_SCRIPT = ROOT / "scripts" / "novelty_surface.py"

VERSION_RE = re.compile(r"-v(\d+)\.yaml$")


def scan_versions() -> list[int]:
    return sorted(
        int(m.group(1))
        for p in PROMPTS_DIR.glob("*-v*.yaml")
        if (m := VERSION_RE.search(p.name))
    )


def main() -> None:
    ap = argparse.ArgumentParser(description="Bootstrap one Suno cycle.")
    ap.add_argument(
        "--no-novelty",
        action="store_true",
        help="skip refreshing experiments/novelty_surface.json",
    )
    args = ap.parse_args()

    versions = scan_versions()
    last = versions[-1] if versions else 0
    summary = {
        "last_version": last,
        "next_version": last + 1,
        "prompt_count": len(versions),
        "novelty_refreshed": None,
    }

    if not args.no_novelty:
        result = subprocess.run(
            [sys.executable, str(NOVELTY_SCRIPT)],
            capture_output=True,
            text=True,
        )
        summary["novelty_refreshed"] = result.returncode == 0
        if result.returncode != 0:
            sys.stderr.write(result.stderr)

    print(json.dumps(summary))


if __name__ == "__main__":
    main()
