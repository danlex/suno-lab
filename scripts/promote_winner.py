#!/usr/bin/env python3
"""Promote the winning MoA-tournament candidate into prompts/ as the cycle's version YAML.

The 10x best-of-N tournament drafts candidates into the scratchpad (NOT prompts/), so
prompts/ never gets polluted with losers. After the orchestrator picks a winner by
judge score + danceability, this script copies the winning scratchpad YAML to
prompts/<slug>-v<N>.yaml and (optionally) cleans up any stray candidate files that
landed in prompts/ for this version.

Reusable, parametrized — replaces the one-off `cp`/`rm` that the contract forbids for
recurring cycle steps.

Usage:
  python3 scripts/promote_winner.py --version 355 --slug pulse \
      --winner /path/to/scratchpad/cand-a-v355.yaml \
      [--cleanup-stray]

  --version N           the cycle version number (int)
  --slug SLUG           one-word slug for the winning title (lowercase); the file
                        becomes prompts/<slug>-v<N>.yaml
  --winner PATH         absolute path to the winning candidate YAML (usually in scratchpad)
  --cleanup-stray       delete any OTHER prompts/*-v<N>.yaml files (stray losers that a
                        drafter mistakenly wrote to prompts/), keeping only the promoted winner

Prints a JSON summary. Idempotent: re-running with the same args overwrites the winner file.
"""
import argparse
import glob
import json
import os
import re
import shutil
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPTS_DIR = os.path.join(REPO, "prompts")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", type=int, required=True)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--winner", required=True, help="absolute path to winning candidate YAML")
    ap.add_argument("--cleanup-stray", action="store_true",
                    help="delete other prompts/*-v<N>.yaml files (stray losers)")
    args = ap.parse_args()

    slug = args.slug.strip().lower()
    if not re.fullmatch(r"[a-z0-9]+", slug):
        print(json.dumps({"error": f"slug must be one lowercase word (got {args.slug!r})"}))
        sys.exit(1)

    if not os.path.isfile(args.winner):
        print(json.dumps({"error": f"winner file not found: {args.winner}"}))
        sys.exit(1)

    dest = os.path.join(PROMPTS_DIR, f"{slug}-v{args.version}.yaml")

    deleted = []
    if args.cleanup_stray:
        # Sweep both stray canonical losers (*-v<N>.yaml) and tournament
        # candidate files that a drafter mistakenly wrote to prompts/ instead
        # of scratchpad (*-cand<N>.yaml). Never delete the promoted winner.
        patterns = [
            os.path.join(PROMPTS_DIR, f"*-v{args.version}.yaml"),
            os.path.join(PROMPTS_DIR, f"*-cand{args.version}.yaml"),
        ]
        for pattern in patterns:
            for path in glob.glob(pattern):
                if os.path.abspath(path) != os.path.abspath(dest):
                    os.remove(path)
                    deleted.append(os.path.basename(path))

    # Winner may already be the destination (re-run after a prior promote);
    # copying a file onto itself raises SameFileError, so skip in that case.
    if os.path.abspath(args.winner) != os.path.abspath(dest):
        shutil.copyfile(args.winner, dest)

    print(json.dumps({
        "promoted": os.path.relpath(dest, REPO),
        "from": args.winner,
        "deleted_stray": deleted,
        "version": args.version,
        "slug": slug,
    }))


if __name__ == "__main__":
    main()
