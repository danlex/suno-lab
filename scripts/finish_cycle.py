#!/usr/bin/env python3
"""Finish (save + publish) one Suno cycle — reusable, parametrized.

Replaces the hand-typed save phase that was run per-cycle (and which silently
skipped the docs/suno_urls.json publish step for v220 and v221). One command
does every deterministic post-submission step:

  1. resolve the prompt YAML for the version  -> title/name
  2. register the clip UUIDs in docs/suno_urls.json (the site's embedded players)
  3. (optional) append a row to the experiments/evolution.md tracker table
  4. rebuild the static site (scripts/build_site.py)
  5. stage ONLY the cycle's files (never `git add -A`)
  6. commit with a templated message
  7. push

Everything after step 2 is opt-out via flags so the same script can also just
backfill missing suno_urls entries for already-committed versions.

Examples
--------
# Full finish for a freshly-submitted version, with an evolution-log row:
  python3 scripts/finish_cycle.py --version 222 \
      --clips 9ca803c6-... ec23e874-... \
      --technique "additive stratum scoring (irreversible accretion)" \
      --key "D# minor (stable)" --bpm 137 \
      --trio "bass clarinet + trumpet + crotales"

# Backfill suno_urls for an older version without touching evolution/commit:
  python3 scripts/finish_cycle.py --version 220 \
      --clips 30aad764-... f8b4b30b-... --no-evo --no-build --no-commit
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "prompts"
DOCS_DIR = ROOT / "docs"
SUNO_URLS = DOCS_DIR / "suno_urls.json"
EVOLUTION = ROOT / "experiments" / "evolution.md"
NOVELTY = ROOT / "experiments" / "novelty_surface.json"
BUILD_SITE = ROOT / "scripts" / "build_site.py"


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def resolve_prompt(version: int) -> Path:
    matches = sorted(PROMPTS_DIR.glob(f"*-v{version}.yaml"))
    if not matches:
        fail(f"no prompt YAML matching *-v{version}.yaml in {PROMPTS_DIR}")
    if len(matches) > 1:
        fail(f"multiple prompts match v{version}: {[m.name for m in matches]}")
    return matches[0]


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def update_suno_urls(title: str, clips: list[str]) -> bool:
    data = {}
    if SUNO_URLS.exists():
        data = json.loads(SUNO_URLS.read_text(encoding="utf-8"))
    if data.get(title) == clips:
        print(f"  suno_urls: '{title}' already up to date")
        return False
    data[title] = clips
    SUNO_URLS.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"  suno_urls: set '{title}' -> {len(clips)} clip(s)")
    return True


def append_evolution_row(version: int, title: str, technique: str,
                         key: str, bpm: str, trio: str) -> bool:
    """Insert a markdown table row after the last numbered data row. Idempotent."""
    text = EVOLUTION.read_text(encoding="utf-8")
    lines = text.splitlines()
    row = f"| {version} | {title} | {technique} | {key} | {bpm} | {trio} |"

    for ln in lines:
        if ln.strip().startswith(f"| {version} |"):
            print(f"  evolution.md: row for v{version} already present, skipping")
            return False

    last_row_idx = None
    for i, ln in enumerate(lines):
        stripped = ln.strip()
        if stripped.startswith("|") and stripped[1:].strip()[:3].rstrip("|").strip().isdigit():
            last_row_idx = i
    if last_row_idx is None:
        fail("could not find an existing numbered table row in evolution.md")

    lines.insert(last_row_idx + 1, row)
    EVOLUTION.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  evolution.md: inserted row for v{version}")
    return True


def run(cmd: list[str]) -> None:
    print(f"  $ {' '.join(cmd)}")
    subprocess.run(cmd, cwd=ROOT, check=True)


def git_stage(paths: list[Path]) -> list[str]:
    existing = [str(p.relative_to(ROOT)) for p in paths if p.exists()]
    if existing:
        run(["git", "add", *existing])
    return existing


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--version", type=int, required=True, help="version number, e.g. 222")
    ap.add_argument("--clips", nargs="+", required=True, help="clip UUID(s) for this song")
    ap.add_argument("--technique", help="evolution.md: short technique label")
    ap.add_argument("--key", help="evolution.md: key column")
    ap.add_argument("--bpm", help="evolution.md: bpm column")
    ap.add_argument("--trio", help="evolution.md: featured-instrument trio")
    ap.add_argument("--message", help="override the git commit message")
    ap.add_argument("--no-evo", action="store_true", help="skip evolution.md row")
    ap.add_argument("--no-build", action="store_true", help="skip build_site.py")
    ap.add_argument("--no-commit", action="store_true", help="stage only, no commit")
    ap.add_argument("--no-push", action="store_true", help="commit but do not push")
    args = ap.parse_args()

    prompt_path = resolve_prompt(args.version)
    data = load_yaml(prompt_path)
    title = data.get("title") or data.get("name")
    if not title:
        fail(f"{prompt_path.name} has no title/name")
    print(f"v{args.version}: {prompt_path.name}  title='{title}'")

    update_suno_urls(title, args.clips)

    want_evo = not args.no_evo and args.technique
    if not args.no_evo and not args.technique:
        print("  evolution.md: skipped (no --technique provided)")
    if want_evo:
        append_evolution_row(args.version, title, args.technique,
                             args.key or "?", args.bpm or "?", args.trio or "?")

    if not args.no_build:
        run([sys.executable, str(BUILD_SITE)])

    staged = git_stage([
        prompt_path, NOVELTY, EVOLUTION,
        DOCS_DIR / "songs.json", DOCS_DIR / "index.html", SUNO_URLS,
    ])
    print(f"  staged: {staged}")

    if args.no_commit:
        print("done (staged only; --no-commit).")
        return

    # Nothing to commit guard
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT)
    if diff.returncode == 0:
        print("done (nothing staged to commit).")
        return

    msg = args.message or (
        f"Add v{args.version} {args.technique or data.get('name','')} "
        f"with {args.trio or ''}".strip()
        + f"\n\nSubmitted to Suno ({len(args.clips)} clips):\n"
        + "\n".join(f"- {c}" for c in args.clips)
        + "\n\nCo-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
    )
    run(["git", "commit", "-m", msg])

    if not args.no_push:
        run(["git", "push"])
    print("done.")


if __name__ == "__main__":
    main()
