#!/usr/bin/env python3
"""Commit and push a specific set of files — reusable, parametrized.

For NON-CYCLE commits (infrastructure / script / doc edits) so the orchestrator
never types `git add A B && git commit -m "..." && git push` inline. Cycle
commits (a new prompt YAML + URLs + evolution + docs/) go through
scripts/finish_cycle.py — this script is for everything else.

Examples
--------
  python3 scripts/commit_files.py \
      --files scripts/cycle_start.py CLAUDE.md \
      --message "Extend cycle_start.py + tighten contract"

  python3 scripts/commit_files.py --files README.md --message "fix typo" --no-push
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(cmd: list[str]) -> None:
    sys.stdout.write(f"  $ {' '.join(cmd)}\n")
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if result.stdout:
        sys.stdout.write(result.stdout)
    if result.returncode != 0:
        if result.stderr:
            sys.stderr.write(result.stderr)
        sys.exit(result.returncode)


def main() -> None:
    ap = argparse.ArgumentParser(description="Stage, commit, and push specific files.")
    ap.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to stage and commit. Pass each file as a separate arg; "
        "never use globs like '*' to avoid accidentally staging extra files.",
    )
    ap.add_argument(
        "--message",
        required=True,
        help="Commit message (the Co-Authored-By trailer is added automatically).",
    )
    ap.add_argument(
        "--no-push",
        action="store_true",
        help="Skip the final `git push origin`. Useful for staged-only commits.",
    )
    args = ap.parse_args()

    run(["git", "add", "--", *args.files])
    msg = (
        f"{args.message}\n\n"
        "Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
    )
    run(["git", "commit", "-m", msg])
    if not args.no_push:
        run(["git", "push"])
    sys.stdout.write("done.\n")


if __name__ == "__main__":
    main()
