#!/usr/bin/env python3
"""Review recent Suno cycles to surface patterns the orchestrator should learn from.

Reads docs/clips_meta.json (built by verify_clips.py) and prints, for the last N
versions, the per-cycle fingerprint: structural metadata + playbook moves applied
+ known duration. The output is designed to make patterns visible — which moves
correlate with which durations, which lanes are working, where the playbook
needs another iteration.

Run before drafting a new cycle if you want context:

    python3 scripts/cycle_review.py            # last 10 versions, compact
    python3 scripts/cycle_review.py --n 20     # last 20 versions
    python3 scripts/cycle_review.py --json     # raw JSON for downstream tools

Why a script not a notes file: this is the kind of "look at recent state"
recurring deterministic work that CLAUDE.md scripting discipline mandates be
encapsulated. No vanilla bash / python3 -c / heredocs.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
META = ROOT / "docs" / "clips_meta.json"


def load_meta() -> dict:
    if not META.exists():
        sys.stderr.write(f"missing {META.relative_to(ROOT)} — run verify_clips.py seed first\n")
        sys.exit(1)
    with open(META, "r", encoding="utf-8") as f:
        return json.load(f)


def group_by_version(meta: dict) -> dict[int, list[dict]]:
    grouped: dict[int, list[dict]] = {}
    for entry in meta.values():
        v = entry.get("version")
        if v is None:
            continue
        grouped.setdefault(v, []).append(entry)
    return grouped


def fmt_secs(s) -> str:
    if s is None:
        return "—"
    return f"{int(s)//60}:{int(s)%60:02d}"


def fmt_playbook(p: dict) -> str:
    """Compact 4-char flag string: c=colon-lyrics, b=bar-counts, t=tokens, s=sentence-case."""
    return (
        ("c" if p.get("parametrized_colon_lyrics") else ".")
        + ("b" if p.get("has_bar_counts") else ".")
        + ("t" if p.get("production_tokens") else ".")
        + ("s" if p.get("sentence_case") else ".")
    )


def cmd_default(args) -> int:
    meta = load_meta()
    grouped = group_by_version(meta)
    versions = sorted(grouped.keys(), reverse=True)[: args.n]

    if args.json:
        out = []
        for v in versions:
            clips = grouped[v]
            durations = [c.get("duration_seconds") for c in clips if c.get("duration_seconds") is not None]
            out.append({
                "version": v,
                "title": clips[0].get("title"),
                "technique": clips[0].get("technique"),
                "key": clips[0].get("key"),
                "bpm": clips[0].get("bpm"),
                "style_chars": clips[0].get("style_chars"),
                "playbook": clips[0].get("playbook"),
                "clip_count": len(clips),
                "durations": durations,
                "mean_duration": statistics.mean(durations) if durations else None,
            })
        print(json.dumps(out, indent=2))
        return 0

    header = f"{'v':<5}{'title':<38}{'tech':<28}{'BPM':<6}{'chars':<7}{'flags':<7}{'durations':<18}"
    print(header)
    print("-" * len(header))
    for v in versions:
        clips = grouped[v]
        ex = clips[0]
        durs = [c.get("duration_seconds") for c in clips if c.get("duration_seconds") is not None]
        dur_str = " / ".join(fmt_secs(d) for d in durs) if durs else "(no data)"
        mean_str = (
            f"  μ={fmt_secs(statistics.mean(durs))}"
            if len(durs) >= 2
            else ""
        )
        print(
            f"v{v:<4}"
            f"{(ex.get('title') or '')[:36]:<38}"
            f"{(ex.get('technique') or '')[:26]:<28}"
            f"{ex.get('bpm') or '—':<6}"
            f"{ex.get('style_chars') or '—':<7}"
            f"{fmt_playbook(ex.get('playbook') or {}):<7}"
            f"{dur_str + mean_str:<18}"
        )

    # Summary
    print()
    all_with_dur = [c for c in meta.values() if c.get("duration_seconds") is not None]
    full_length = [c for c in all_with_dur if c.get("duration_seconds", 0) >= 180]
    short = [c for c in all_with_dur if c.get("duration_seconds", 0) < 150]
    print(f"clips with duration data: {len(all_with_dur)} / {len(meta)}")
    if all_with_dur:
        print(
            f"≥3:00 renders: {len(full_length)} ({100*len(full_length)/len(all_with_dur):.0f}%)  •  "
            f"<2:30 renders: {len(short)} ({100*len(short)/len(all_with_dur):.0f}%)"
        )
        # Cross-tab: playbook completeness vs duration
        full_playbook = [
            c for c in all_with_dur
            if all((c.get("playbook") or {}).get(k) for k in (
                "parametrized_colon_lyrics", "has_bar_counts", "production_tokens", "sentence_case"
            ))
        ]
        if full_playbook:
            mean_full = statistics.mean(c["duration_seconds"] for c in full_playbook)
            print(
                f"clips with full playbook (cbts): {len(full_playbook)}  •  "
                f"mean duration: {fmt_secs(mean_full)}"
            )
    print()
    print("flag legend: c=colon-lyrics  b=bar-counts  t=production-tokens  s=sentence-case")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Surface recent-cycle patterns for the orchestrator.")
    ap.add_argument("--n", type=int, default=10, help="Show last N versions (default 10).")
    ap.add_argument("--json", action="store_true", help="Output raw JSON instead of table.")
    ap.set_defaults(func=cmd_default)
    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
