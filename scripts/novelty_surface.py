#!/usr/bin/env python3
"""Extract the 'novelty surface' from all prompts/*.yaml.

Produces a human-readable report AND experiments/novelty_surface.json so that
future cycles can check — without relying on stale memory — which instruments,
genres, keys, BPMs, and title concepts have already been used.

Run after every new prompt:
    python3 scripts/novelty_surface.py
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML not installed. Install with: pip install pyyaml", file=sys.stderr)
    raise

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "prompts"
EXPERIMENTS_DIR = ROOT / "experiments"
EXPERIMENTS_DIR.mkdir(exist_ok=True)
OUT_JSON = EXPERIMENTS_DIR / "novelty_surface.json"

# Known instruments — expand as the repo grows. The extractor first tries
# tag-based detection (most reliable), then uppercase regex (v93+ format),
# then falls back to scanning for these by name.
KNOWN_INSTRUMENTS = {
    # strings / bowed
    "violin", "viola", "cello", "contrabass", "double bass", "upright bass",
    "hardanger fiddle", "nyckelharpa", "erhu", "hurdy gurdy", "viola da gamba",
    "string quartet", "string orchestra", "baryton", "sarangi",
    # plucked / keyboard strings
    "harp", "harpsichord", "mbira", "cimbalom", "kora", "cristal baschet",
    "prepared piano", "felt piano", "piano", "clavichord", "guqin",
    # brass
    "french horn", "trumpet", "trombone", "bass trombone", "tuba", "flugelhorn",
    "cornet", "wagner tuba", "ophicleide",
    # woodwinds
    "flute", "bass flute", "piccolo", "oboe", "oboe d'amore", "cor anglais",
    "english horn", "clarinet", "bass clarinet", "contrabass clarinet",
    "bassoon", "contrabassoon", "tenor saxophone", "baritone saxophone",
    "subcontrabass saxophone", "shakuhachi", "ney", "duduk", "chalumeau",
    # percussion
    "timpani", "taiko", "frame drums", "glass marimba", "marimba", "vibraphone",
    "bowed vibraphone", "handpan", "balafon", "steelpan", "steel tongue drum",
    "music box", "tubular bells", "gongs", "glockenspiel", "celesta",
    "crotales", "nail violin", "singing saw",
    # accordion / free reed
    "accordion", "bandoneon", "concertina",
    # electronic / electro-acoustic
    "theremin", "ondes martenot", "moog", "mellotron", "pipe organ", "organ",
    # voice / exotic
    "glass harmonica", "waterphone", "armonica",
}

# Common alias normalization — tags use hyphenated kebab-case (e.g. "bass-trombone")
# while the surface uses space-separated names. Map back to canonical form.
INSTRUMENT_TAG_ALIASES = {
    "oboe-d-amore": "oboe d'amore",
    "viola-da-gamba": "viola da gamba",
    "english-horn": "english horn",
    "cor-anglais": "cor anglais",
}

# Genre keywords — detect a song's "dominant genre" (what Suno will latch on to).
KNOWN_GENRES = {
    "orchestral", "symphonic", "cinematic", "neoclassical", "post-classical",
    "ambient", "drone", "chamber", "minimalist", "baroque", "romantic",
    "dubstep", "trance", "trap", "progressive house", "breakbeat", "psytrance",
    "idm", "2-step garage", "garage", "footwork", "grime", "drill", "synthwave",
    "amapiano", "reggaeton", "vaporwave", "chillhop", "lo-fi", "bolero",
    "passacaglia", "chaconne", "fugue", "ricercare", "concerto", "suite",
    "techno", "house", "dnb", "jungle", "hardstyle", "hardcore",
    "afrobeats", "jazz",
}

KEY_RE = re.compile(
    r"\b([A-G](?:[-\s]?(?:flat|sharp|#|b))?\s*(?:minor|major|min|maj))\b",
    re.IGNORECASE,
)
BPM_RE = re.compile(r"\b(\d{2,3})\s*BPM\b", re.IGNORECASE)
FEATURED_RE = re.compile(r"with\s+([A-Z'\-\s]+?)(?:,|\.|$)", re.MULTILINE)


def normalize(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


def extract_featured_instruments(style: str) -> list[str]:
    """Legacy v93+ extractor: 'ORCHESTRAL X with FEATURED1 + FEATURED2 + FEATURED3'.
    Captures ALL-CAPS chunks after 'with '. Returns empty for sentence-case (v248+)
    prompts — those are handled by extract_instruments_from_tags."""
    featured = []
    m = FEATURED_RE.search(style)
    if m:
        chunk = m.group(1)
        alpha = [c for c in chunk if c.isalpha()]
        if alpha and sum(1 for c in alpha if c.isupper()) / len(alpha) > 0.7:
            for piece in re.split(r"\s*\+\s*", chunk):
                piece = normalize(piece)
                if piece:
                    featured.append(piece)
    return featured


def extract_instruments_from_tags(tags) -> list[str]:
    """Parse the YAML's tags field for instrument names — the most reliable signal.
    Tags conventionally include bare instrument slugs ('harp', 'bass-trombone') and
    revival markers ('revival-ophicleide-21-gap'). This catches every catalog YAML
    including v248+ sentence-case prompts that the legacy CAPS regex misses."""
    if not tags:
        return []
    found = []
    seen = set()
    for raw in tags:
        if not isinstance(raw, str):
            continue
        slug = raw.strip().lower()
        # Strip the "revival-<instr>-<n>-gap" wrapper if present
        rev_match = re.match(r"^revival-(.+?)-\d+-gap$", slug)
        if rev_match:
            slug = rev_match.group(1)
        # Resolve alias (e.g. "oboe-d-amore" -> "oboe d'amore")
        candidate = INSTRUMENT_TAG_ALIASES.get(slug, slug.replace("-", " "))
        if candidate in KNOWN_INSTRUMENTS and candidate not in seen:
            seen.add(candidate)
            found.append(candidate)
    return found


def extract_mentioned_instruments(style: str) -> set[str]:
    """Fallback: scan the full style for any known instrument keyword."""
    lower = normalize(style)
    found = set()
    for instr in KNOWN_INSTRUMENTS:
        # Match as whole word / phrase
        if re.search(rf"\b{re.escape(instr)}\b", lower):
            found.add(instr)
    return found


def extract_genre(style: str) -> str | None:
    """Find the dominant genre — first known-genre keyword in the first 120 chars."""
    head = normalize(style[:200])
    for genre in sorted(KNOWN_GENRES, key=len, reverse=True):
        if genre in head:
            return genre
    return None


def extract_key(style: str) -> str | None:
    m = KEY_RE.search(style)
    return normalize(m.group(1)) if m else None


def extract_bpm(style: str) -> int | None:
    m = BPM_RE.search(style)
    return int(m.group(1)) if m else None


def load_prompts() -> list[dict]:
    prompts = []
    for path in sorted(PROMPTS_DIR.glob("*.yaml")):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"skip {path.name}: {e}", file=sys.stderr)
            continue
        if not data:
            continue
        data["_file"] = path.name
        prompts.append(data)
    return prompts


def build_surface(prompts: list[dict]) -> dict:
    instrument_versions: dict[str, list[int]] = defaultdict(list)
    genre_versions: dict[str, list[int]] = defaultdict(list)
    key_versions: dict[str, list[int]] = defaultdict(list)
    bpm_versions: dict[int, list[int]] = defaultdict(list)
    titles: list[dict] = []

    for p in prompts:
        v = p.get("version", 0) or 0
        style = p.get("style", "") or ""
        tags = p.get("tags", []) or []

        # Priority order: structured tags (most reliable, works for sentence-case
        # v248+ prompts) → legacy CAPS regex → keyword scan of the style.
        from_tags = extract_instruments_from_tags(tags)
        featured = from_tags or extract_featured_instruments(style)
        mentioned = extract_mentioned_instruments(style)

        # Featured takes priority — those are the "headlined" instruments
        for instr in featured or mentioned:
            instrument_versions[instr].append(v)

        genre = extract_genre(style)
        if genre:
            genre_versions[genre].append(v)

        key = extract_key(style)
        if key:
            key_versions[key].append(v)

        bpm = extract_bpm(style)
        if bpm:
            bpm_versions[bpm].append(v)

        titles.append({
            "version": v,
            "title": p.get("title", ""),
            "name": p.get("name", ""),
            "featured": featured,
            "genre": genre,
            "key": key,
            "bpm": bpm,
        })

    # Sort version lists
    for d in (instrument_versions, genre_versions, key_versions, bpm_versions):
        for k in d:
            d[k].sort()

    return {
        "total_prompts": len(prompts),
        "latest_version": max((t["version"] for t in titles), default=0),
        "instruments": {k: v for k, v in sorted(
            instrument_versions.items(), key=lambda kv: (-len(kv[1]), kv[0])
        )},
        "genres": {k: v for k, v in sorted(
            genre_versions.items(), key=lambda kv: (-len(kv[1]), kv[0])
        )},
        "keys": {k: v for k, v in sorted(
            key_versions.items(), key=lambda kv: (-len(kv[1]), kv[0])
        )},
        "bpms": {str(k): v for k, v in sorted(bpm_versions.items())},
        "titles": sorted(titles, key=lambda t: -t["version"]),
    }


def instrument_novelty(surface: dict, query: str) -> str:
    """Human-readable check: has this instrument been used? In which versions?"""
    q = normalize(query)
    versions = surface["instruments"].get(q, [])
    if not versions:
        return f"'{query}' — NEVER used (repo-wide first use)"
    return f"'{query}' — used in v{', v'.join(str(v) for v in versions)} ({len(versions)} times)"


def print_report(surface: dict) -> None:
    print(f"# Novelty Surface — {surface['total_prompts']} prompts, latest v{surface['latest_version']}\n")

    print("## Instruments used (featured first, ranked by frequency)")
    for instr, versions in surface["instruments"].items():
        recent = versions[-5:]
        print(f"  {instr:40s} × {len(versions):3d}  → last: v{', v'.join(str(v) for v in recent)}")
    print()

    print("## Dominant genres")
    for genre, versions in surface["genres"].items():
        print(f"  {genre:30s} × {len(versions):3d}")
    print()

    print("## Keys used")
    for key, versions in surface["keys"].items():
        print(f"  {key:25s} × {len(versions):3d}")
    print()

    print("## BPM range")
    bpms = [int(k) for k in surface["bpms"]]
    if bpms:
        print(f"  min={min(bpms)}  max={max(bpms)}  unique={len(bpms)}")
        print(f"  all BPMs: {sorted(set(bpms))}")
    print()

    print("## Last 5 prompts — what's fresh in short-term memory")
    for t in surface["titles"][:5]:
        print(f"  v{t['version']:3d}  {t['title']:45s}  genre={t['genre']}  bpm={t['bpm']}  featured={'+'.join(t['featured']) if t['featured'] else '—'}")


def main():
    prompts = load_prompts()
    surface = build_surface(prompts)

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(surface, f, ensure_ascii=False, indent=2)

    # Allow ad-hoc lookups: `python3 scripts/novelty_surface.py "ondes martenot"`
    if len(sys.argv) > 1:
        for query in sys.argv[1:]:
            print(instrument_novelty(surface, query))
        return

    print_report(surface)
    print(f"\nwrote {OUT_JSON.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
