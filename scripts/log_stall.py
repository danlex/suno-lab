#!/usr/bin/env python3
"""Reusable stall/abort close-out for the autonomous generation loop.

Prepends a structured entry to experiments/cron_failures.md and (optionally)
removes the stalled scrap prompt YAML so cycle_start.py doesn't mistake it for
an in-progress "resume" draft. Use this instead of ad-hoc `rm`/`echo`/heredoc
bash whenever a cycle stalls below the ship bar and we advance to the next
version.

Usage:
  python3 scripts/log_stall.py --version 389 \
      --note "Afropop->Afro-house, best 78/d8; concept-level ceiling (D2/D6/D1). Advancing to v390." \
      [--scores "draft1 71/d7, redraft 78/d8"] \
      [--remove-draft prompts/countdown389-v389.yaml]

Prints a JSON status line. Does NOT commit (finish_cycle.py owns commits; the
stall entry rides along with the next successful cycle's commit).
"""
import argparse
import datetime
import json
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(REPO, "experiments", "cron_failures.md")
HEADER = "# Cron failure log\n"


def main():
    ap = argparse.ArgumentParser(description="Log a stalled/aborted cycle and optionally remove its scrap draft.")
    ap.add_argument("--version", required=True, help="Version number that stalled, e.g. 389")
    ap.add_argument("--note", required=True, help="Root-cause + decision text (one paragraph).")
    ap.add_argument("--scores", default="", help="Optional per-candidate scores summary line.")
    ap.add_argument("--remove-draft", default="", help="Optional path to the stalled scrap YAML to delete (repo-relative or absolute).")
    ap.add_argument("--date", default="", help="Optional ISO date override (defaults to today).")
    args = ap.parse_args()

    date = args.date or datetime.date.today().isoformat()

    lines = [f"### {date} — v{args.version} STALL/ABORT (autonomous loop). NOT SHIPPED."]
    if args.scores:
        lines.append(f"Scores: {args.scores}")
    lines.append(args.note)
    entry = "\n".join(lines) + "\n\n"

    if os.path.exists(LOG):
        with open(LOG, "r") as f:
            content = f.read()
    else:
        content = HEADER + "\n"

    if content.startswith(HEADER):
        rest = content[len(HEADER):].lstrip("\n")
        new = HEADER + "\n" + entry + rest
    else:
        new = HEADER + "\n" + entry + content

    with open(LOG, "w") as f:
        f.write(new)

    removed = None
    if args.remove_draft:
        p = args.remove_draft
        if not os.path.isabs(p):
            p = os.path.join(REPO, p)
        if os.path.exists(p):
            os.remove(p)
            removed = os.path.relpath(p, REPO)

    print(json.dumps({
        "logged": True,
        "version": args.version,
        "log": os.path.relpath(LOG, REPO),
        "removed_draft": removed,
    }))


if __name__ == "__main__":
    main()
