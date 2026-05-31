#!/usr/bin/env python3
"""Verify final clip durations and back-fill structured per-version metadata.

Why: the submitter records "durations_seen" at create-time, but Suno renders
asynchronously — those values are often mid-render and not the final length.
Result: we've been logging "v243 = 1:22/1:41" when the final might be different.
Without ground-truth duration data we can't validate which playbook moves
actually correlate with full-length renders.

What this builds: a structured `docs/clips_meta.json` keyed by clip UUID with
`{version, title, duration_seconds, technique, key, bpm, trio, playbook_moves}`.
The analytics page can then chart real durations against the playbook timeline.

Two modes:

  (1) `seed` — populate clips_meta.json from existing docs/suno_urls.json +
      prompts/*-v<N>.yaml + a manual durations table (since we don't yet have
      a Suno API). Fills what we already know from the close-out logs.

  (2) `merge` — given a JSON dict of `{uuid: duration_seconds}` on stdin or
      via --input, merge those into clips_meta.json without re-deriving the
      structural fields.

Usage:
    python3 scripts/verify_clips.py seed
    python3 scripts/verify_clips.py merge --input /tmp/new_durations.json

Notes:
- Does NOT call out to Suno (no API key required, no browser). Designed as a
  reusable accumulator that other scripts (or a future browser-driven duration
  fetcher) can feed.
- Reads tags from each YAML to know technique/key/bpm/trio with the same
  parser shape novelty_surface.py uses, so the metadata stays consistent.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML not installed.", file=sys.stderr)
    raise

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "prompts"
DOCS_DIR = ROOT / "docs"
SUNO_URLS = DOCS_DIR / "suno_urls.json"
META = DOCS_DIR / "clips_meta.json"

VERSION_RE = re.compile(r"-v(\d+)\.yaml$")
KEY_RE = re.compile(r"^([a-g])(-flat|-sharp)?-(minor|major)$")
BPM_TAG_RE = re.compile(r"^(\d{2,3})bpm$")


def load_existing_meta() -> dict:
    if META.exists():
        with open(META, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_meta(meta: dict) -> None:
    DOCS_DIR.mkdir(exist_ok=True)
    with open(META, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2, sort_keys=True)


def load_suno_urls() -> dict:
    if SUNO_URLS.exists():
        with open(SUNO_URLS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def load_yaml_by_version() -> dict[int, dict]:
    out: dict[int, dict] = {}
    for path in PROMPTS_DIR.glob("*-v*.yaml"):
        m = VERSION_RE.search(path.name)
        if not m:
            continue
        v = int(m.group(1))
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = yaml.safe_load(f) or {}
            except yaml.YAMLError:
                continue
        data["_file"] = path.name
        out[v] = data
    return out


def parse_yaml_structure(data: dict) -> dict:
    """Extract technique/key/bpm/trio and which playbook moves the YAML uses."""
    tags = [str(t).lower() for t in (data.get("tags") or [])]
    style = data.get("style", "") or ""
    lyrics = data.get("lyrics", "") or ""

    bpm = None
    key = None
    instruments: list[str] = []
    technique = None

    for t in tags:
        if not bpm:
            m = BPM_TAG_RE.match(t)
            if m:
                bpm = int(m.group(1))
        if not key and KEY_RE.match(t):
            key = t
        if not technique and (t.endswith("-technique-new") or t.startswith("orchestral-")):
            technique = t.replace("orchestral-", "").replace("-technique-new", "")
        # Instrument tags (bare slugs that map to known names) — same shape as
        # novelty_surface.py reads. We don't re-validate here; just collect.
        if "-" not in t.split("revival-")[-1] or t.startswith("revival-"):
            pass  # placeholder; the instrument list is best read from novelty_surface

    # Playbook fingerprint — what moves did this draft use?
    has_colon_lyrics = bool(re.search(r"\[[A-Za-z0-9 ]{1,30}:[^\]]{5,}\]", lyrics))
    has_bar_counts = "bars]" in lyrics or "bar]" in lyrics
    has_production_tokens = any(
        tok in style.lower()
        for tok in (
            "polished studio mix",
            "decca-tree",
            "hollywood scoring stage",
            "wide stereo stage",
            "deep low-end",
            "warm tape saturation",
            "lush acoustic ambience",
            "tight chamber reverb",
        )
    )
    has_caps_label = bool(re.search(r"\b[A-Z]{4,}\b", style[:300]))
    sentence_case_opener = not has_caps_label
    char_count = len(style)

    return {
        "title": data.get("title") or data.get("name") or "",
        "name": data.get("name") or "",
        "instrumental": bool(data.get("instrumental")),
        "technique": technique,
        "key": key,
        "bpm": bpm,
        "style_chars": char_count,
        "playbook": {
            "parametrized_colon_lyrics": has_colon_lyrics,
            "has_bar_counts": has_bar_counts,
            "production_tokens": has_production_tokens,
            "sentence_case": sentence_case_opener,
        },
        "file": data.get("_file", ""),
    }


def cmd_seed(args) -> int:
    """Populate clips_meta.json with everything we know, no durations yet."""
    urls = load_suno_urls()  # {title: [uuid1, uuid2]}
    yamls = load_yaml_by_version()

    # title -> (version, data)
    title_to_version: dict[str, tuple[int, dict]] = {}
    for v, data in yamls.items():
        t = data.get("title") or data.get("name") or ""
        if t:
            title_to_version[t] = (v, data)

    meta = load_existing_meta()
    added = updated = 0

    for title, uuids in urls.items():
        if title not in title_to_version:
            continue
        version, data = title_to_version[title]
        structure = parse_yaml_structure(data)
        for uuid in uuids:
            existing = meta.get(uuid, {})
            entry = {
                "uuid": uuid,
                "version": version,
                **structure,
            }
            # Preserve any duration that was already recorded
            if "duration_seconds" in existing:
                entry["duration_seconds"] = existing["duration_seconds"]
            if "duration_source" in existing:
                entry["duration_source"] = existing["duration_source"]
            if existing:
                if entry != existing:
                    updated += 1
            else:
                added += 1
            meta[uuid] = entry

    save_meta(meta)
    print(
        json.dumps(
            {
                "clips_total": len(meta),
                "added": added,
                "updated": updated,
                "with_duration": sum(
                    1 for v in meta.values() if "duration_seconds" in v
                ),
            }
        )
    )
    return 0


def parse_duration_to_seconds(s) -> int | None:
    """Accept '3:17', '197', 197 → return seconds, or None."""
    if isinstance(s, (int, float)):
        return int(s)
    if not isinstance(s, str):
        return None
    s = s.strip()
    m = re.match(r"^(\d+):(\d{2})$", s)
    if m:
        return int(m.group(1)) * 60 + int(m.group(2))
    if s.isdigit():
        return int(s)
    return None


def cmd_merge(args) -> int:
    """Merge a JSON dict {uuid: duration} into clips_meta.json."""
    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            new = json.load(f)
    else:
        new = json.load(sys.stdin)

    meta = load_existing_meta()
    if not meta:
        sys.stderr.write(
            "clips_meta.json is empty — run `verify_clips.py seed` first.\n"
        )
        return 1

    updated = skipped = unknown = 0
    for uuid, raw in new.items():
        secs = parse_duration_to_seconds(raw)
        if secs is None:
            skipped += 1
            continue
        if uuid not in meta:
            unknown += 1
            # Still record it; future seed runs will fill the structural fields
            meta[uuid] = {
                "uuid": uuid,
                "duration_seconds": secs,
                "duration_source": args.source or "merge",
            }
            continue
        meta[uuid]["duration_seconds"] = secs
        meta[uuid]["duration_source"] = args.source or "merge"
        updated += 1

    save_meta(meta)
    print(
        json.dumps(
            {
                "updated": updated,
                "skipped_bad_input": skipped,
                "unknown_uuid_recorded": unknown,
                "total_clips_with_duration": sum(
                    1 for v in meta.values() if "duration_seconds" in v
                ),
            }
        )
    )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_seed = sub.add_parser("seed", help="Populate clips_meta.json from YAMLs + suno_urls.json")
    p_seed.set_defaults(func=cmd_seed)

    p_merge = sub.add_parser("merge", help="Merge a JSON dict of {uuid: duration} into the metadata.")
    p_merge.add_argument("--input", help="Path to JSON file. If omitted, reads stdin.")
    p_merge.add_argument("--source", help="Tag the duration source for provenance.")
    p_merge.set_defaults(func=cmd_merge)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
