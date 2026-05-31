#!/usr/bin/env python3
"""Reusable text utilities used by Suno cycle subagents.

Replaces the ad-hoc `python3 -c "s='...'; print(len(s))"` invocations the
suno-drafter previously ran inline for character counting and trimming. Those
were vanilla `python3 -c` snippets that triggered permission prompts and
violated the CLAUDE.md scripting discipline.

Subcommands
-----------
  count        Count characters in a string (from --text or stdin).
  in-range     Exit code 0 if length is within --min..--max (else 1) plus a JSON report.
  blocklist    Scan a string for any banned substrings (from a comma-list); JSON report.

Examples
--------
  python3 scripts/text_tools.py count --text "some style prose"
  python3 scripts/text_tools.py count < draft.txt
  python3 scripts/text_tools.py in-range --min 850 --max 950 --text "..."
  python3 scripts/text_tools.py blocklist --terms "Dune,desert,epic" --text "..."
"""
import argparse
import json
import sys


def read_text(args) -> str:
    if args.text is not None:
        return args.text
    return sys.stdin.read()


def cmd_count(args) -> int:
    text = read_text(args)
    print(json.dumps({"length": len(text)}))
    return 0


def cmd_in_range(args) -> int:
    text = read_text(args)
    n = len(text)
    in_range = args.min <= n <= args.max
    print(json.dumps({"length": n, "min": args.min, "max": args.max, "in_range": in_range}))
    return 0 if in_range else 1


def cmd_blocklist(args) -> int:
    text = read_text(args)
    haystack = text.lower()
    terms = [t.strip() for t in args.terms.split(",") if t.strip()]
    hits = [t for t in terms if t.lower() in haystack]
    print(json.dumps({"hits": hits, "clean": not hits}))
    return 0 if not hits else 1


def main() -> int:
    ap = argparse.ArgumentParser(description="Reusable text utilities for Suno cycle agents.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_count = sub.add_parser("count", help="Count characters.")
    p_count.add_argument("--text", help="Inline text. If omitted, reads stdin.")
    p_count.set_defaults(func=cmd_count)

    p_range = sub.add_parser("in-range", help="Check whether length is within a range.")
    p_range.add_argument("--text", help="Inline text. If omitted, reads stdin.")
    p_range.add_argument("--min", type=int, required=True)
    p_range.add_argument("--max", type=int, required=True)
    p_range.set_defaults(func=cmd_in_range)

    p_block = sub.add_parser("blocklist", help="Scan for forbidden substrings.")
    p_block.add_argument("--text", help="Inline text. If omitted, reads stdin.")
    p_block.add_argument("--terms", required=True, help="Comma-separated list of banned substrings.")
    p_block.set_defaults(func=cmd_blocklist)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
