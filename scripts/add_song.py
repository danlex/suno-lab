#!/usr/bin/env python3
"""Add (or update) a song entry in docs/suno_urls.json.

Reusable, parametrized entrypoint for manually registering a song's clip UUIDs
(e.g. a hand-made track outside the autonomous version cycle) into the site's
URL map. Idempotent: re-running with the same title merges/dedupes UUIDs.

Usage:
    python3 scripts/add_song.py --title "I am the blackhole" \
        --clips d104c2e7-9169-43d6-8c66-de3a7f389d47

Accepts either raw UUIDs or full suno.com/song/<uuid> URLs (query string ok).
"""
import argparse
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URLS_PATH = os.path.join(REPO, "docs", "suno_urls.json")
UUID_RE = re.compile(
    r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.I
)


def extract_uuid(token: str) -> str:
    m = UUID_RE.search(token)
    if not m:
        sys.exit(f"error: no UUID found in {token!r}")
    return m.group(0).lower()


def main() -> None:
    ap = argparse.ArgumentParser(description="Add/update a song in docs/suno_urls.json")
    ap.add_argument("--title", required=True, help="Song title (JSON key)")
    ap.add_argument(
        "--clips",
        required=True,
        nargs="+",
        help="One or more clip UUIDs or suno.com/song/<uuid> URLs",
    )
    args = ap.parse_args()

    with open(URLS_PATH) as f:
        data = json.load(f)

    new_uuids = [extract_uuid(c) for c in args.clips]
    existing = data.get(args.title, [])
    merged = list(existing)
    for u in new_uuids:
        if u not in merged:
            merged.append(u)
    data[args.title] = merged

    with open(URLS_PATH, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(json.dumps({
        "title": args.title,
        "uuids": merged,
        "total_songs": len(data),
        "path": os.path.relpath(URLS_PATH, REPO),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
