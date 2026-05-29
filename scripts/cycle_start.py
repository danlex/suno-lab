#!/usr/bin/env python3
"""Bootstrap one Suno cycle — reusable, parametrized.

Replaces the hand-typed inline bash that was used to compute the next version
number (`ls prompts/ | grep -oE 'v[0-9]+' | sort -V | tail -1`), to refresh the
novelty surface, and to inspect whether the previous cycle's YAML is still
uncommitted (`echo ...; git status --short prompts/`). Those are deterministic,
recurring cycle steps and MUST live in a script per CLAUDE.md "Scripting
discipline" — never as one-off shell.

Does the deterministic pre-draft work and emits a compact JSON summary the
orchestrator reads to decide draft-vs-resume:
  1. compute the latest / next version from prompts/*-v<N>.yaml
  2. (optional) refresh experiments/novelty_surface.json via novelty_surface.py
  3. check whether the latest YAML is uncommitted (a prior submit died mid-flight)
  4. emit `recommended_action` ∈ {"resume_submit", "draft_new"} and
     `recommended_version` so the orchestrator never needs `git status` or `ls`
     to make that call.

Examples
--------
  python3 scripts/cycle_start.py                # full bootstrap + novelty refresh
  python3 scripts/cycle_start.py --no-novelty   # skip the novelty regen
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


def scan_versions() -> list[tuple[int, Path]]:
    out: list[tuple[int, Path]] = []
    for p in PROMPTS_DIR.glob("*-v*.yaml"):
        m = VERSION_RE.search(p.name)
        if m:
            out.append((int(m.group(1)), p))
    out.sort(key=lambda t: t[0])
    return out


def is_untracked(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    result = subprocess.run(
        ["git", "status", "--porcelain", "--", str(rel)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    line = result.stdout.strip()
    # `??` = untracked, ` M` = modified-tracked, etc. We only care that it's NOT clean.
    return bool(line)


def main() -> None:
    ap = argparse.ArgumentParser(description="Bootstrap one Suno cycle.")
    ap.add_argument(
        "--no-novelty",
        action="store_true",
        help="skip refreshing experiments/novelty_surface.json",
    )
    args = ap.parse_args()

    versions = scan_versions()
    last_version = versions[-1][0] if versions else 0
    latest_path = versions[-1][1] if versions else None

    latest_uncommitted = bool(latest_path) and is_untracked(latest_path)

    if latest_uncommitted:
        recommended_action = "resume_submit"
        recommended_version = last_version
    else:
        recommended_action = "draft_new"
        recommended_version = last_version + 1

    summary = {
        "last_version": last_version,
        "next_version": last_version + 1,
        "prompt_count": len(versions),
        "latest_yaml_path": (
            str(latest_path.relative_to(ROOT)) if latest_path else None
        ),
        "latest_yaml_uncommitted": latest_uncommitted,
        "latest_committed_version": (
            last_version - 1 if latest_uncommitted else last_version
        ),
        "recommended_action": recommended_action,
        "recommended_version": recommended_version,
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
