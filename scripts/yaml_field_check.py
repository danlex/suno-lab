#!/usr/bin/env python3
"""Reusable YAML-field inspector for prompt YAMLs.

Reads a prompts/*.yaml file, extracts a top-level scalar field (style, title,
exclude_styles, lyrics), and runs count / in-range / blocklist over it. Lets
drafter / judge / orchestrator avoid one-off ``python3 -c`` or the trick of
piping a whole YAML file through text_tools.py (which over-counts).

Usage::

    python3 scripts/yaml_field_check.py count       --file prompts/x-vN.yaml --field style
    python3 scripts/yaml_field_check.py in-range    --file prompts/x-vN.yaml --field style --min 600 --max 950
    python3 scripts/yaml_field_check.py blocklist   --file prompts/x-vN.yaml --field style \
                                                    --terms "dune,epic,massive,frisson,capo,da capo"
    python3 scripts/yaml_field_check.py inspect     --file prompts/x-vN.yaml   # all fields + counts

The ``inspect`` subcommand is the routine pre-submit health check: it prints
char counts for style / title / exclude_styles / lyrics in one shot.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    sys.stderr.write("PyYAML required. Install: pip install pyyaml\n")
    sys.exit(2)


CINEMATIC_BLOCKLIST = [
    "dune", "epic", "massive", "frisson", "desert",
    "capo", "da capo", " dc ",
]

FIELD_LIMITS = {
    "style": 1000,
    "title": 100,
    "exclude_styles": 1000,
    "lyrics": 1000,
}


def load_field(path: Path, field: str) -> str:
    data = yaml.safe_load(path.read_text())
    if field not in data:
        sys.stderr.write(f"field '{field}' missing in {path}\n")
        sys.exit(3)
    value = data[field]
    if not isinstance(value, str):
        sys.stderr.write(f"field '{field}' is not a scalar string\n")
        sys.exit(3)
    return value


def cmd_count(args):
    text = load_field(Path(args.file), args.field)
    print(json.dumps({"field": args.field, "chars": len(text)}))


def cmd_in_range(args):
    text = load_field(Path(args.file), args.field)
    n = len(text)
    ok = args.min <= n <= args.max
    print(json.dumps({"field": args.field, "chars": n, "min": args.min, "max": args.max, "in_range": ok}))
    if not ok:
        sys.exit(1)


def cmd_blocklist(args):
    text = load_field(Path(args.file), args.field).lower()
    terms = [t.strip().lower() for t in args.terms.split(",") if t.strip()]
    hits = [t for t in terms if t in text]
    print(json.dumps({"field": args.field, "terms_checked": len(terms), "hits": hits}))
    if hits:
        sys.exit(1)


def cmd_inspect(args):
    path = Path(args.file)
    data = yaml.safe_load(path.read_text())
    out = {"file": str(path)}
    for fld, lim in FIELD_LIMITS.items():
        if fld in data and isinstance(data[fld], str):
            n = len(data[fld])
            out[fld] = {"chars": n, "limit": lim, "ok": n <= lim}
    # Run cinematic blocklist on style only (viral cycles still avoid these triggers).
    if "style" in data and isinstance(data["style"], str):
        s = data["style"].lower()
        hits = [t for t in CINEMATIC_BLOCKLIST if t in s]
        out["style_blocklist_hits"] = hits
    print(json.dumps(out, indent=2))
    if any(not v["ok"] for v in out.values() if isinstance(v, dict)):
        sys.exit(1)
    if out.get("style_blocklist_hits"):
        sys.exit(1)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    pc = sub.add_parser("count")
    pc.add_argument("--file", required=True)
    pc.add_argument("--field", required=True)
    pc.set_defaults(func=cmd_count)

    pr = sub.add_parser("in-range")
    pr.add_argument("--file", required=True)
    pr.add_argument("--field", required=True)
    pr.add_argument("--min", type=int, required=True)
    pr.add_argument("--max", type=int, required=True)
    pr.set_defaults(func=cmd_in_range)

    pb = sub.add_parser("blocklist")
    pb.add_argument("--file", required=True)
    pb.add_argument("--field", required=True)
    pb.add_argument("--terms", required=True)
    pb.set_defaults(func=cmd_blocklist)

    pi = sub.add_parser("inspect")
    pi.add_argument("--file", required=True)
    pi.set_defaults(func=cmd_inspect)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
