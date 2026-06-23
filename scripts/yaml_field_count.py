#!/usr/bin/env python3
"""Report character counts for one or more fields of a prompt YAML.

Reusable cycle helper: verifies that the `style` and `lyrics` fields of a
prompt file are within Suno's limits (each < 1000 chars) without resorting to
ad-hoc `python3 -c` one-liners (banned by the project scripting contract).

Usage:
    python3 scripts/yaml_field_count.py prompts/flicker-v362.yaml
    python3 scripts/yaml_field_count.py prompts/flicker-v362.yaml --fields style lyrics title
    python3 scripts/yaml_field_count.py prompts/flicker-v362.yaml --limit 1000

Exit code is non-zero if any checked field meets or exceeds --limit, so the
script doubles as a pre-submit gate.
"""
import argparse
import json
import sys

import yaml


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path", help="Path to the prompt YAML file")
    ap.add_argument(
        "--fields",
        nargs="+",
        default=["style", "lyrics"],
        help="Field names to count (default: style lyrics)",
    )
    ap.add_argument(
        "--limit",
        type=int,
        default=1000,
        help="Hard limit; field must be strictly under this (default: 1000)",
    )
    args = ap.parse_args()

    with open(args.path, "r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)

    results = {}
    over = []
    for field in args.fields:
        value = data.get(field)
        if value is None:
            results[field] = None
            continue
        n = len(str(value))
        results[field] = n
        if n >= args.limit:
            over.append(field)

    print(json.dumps({
        "path": args.path,
        "limit": args.limit,
        "counts": results,
        "over_limit": over,
        "ok": not over,
    }))
    return 1 if over else 0


if __name__ == "__main__":
    sys.exit(main())
