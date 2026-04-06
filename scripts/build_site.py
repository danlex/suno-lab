#!/usr/bin/env python3
"""Generate docs/songs.json and docs/index.html from prompts/*.yaml."""

import json
import os
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML not installed. Install with: pip install pyyaml")
    raise

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "prompts"
DOCS_DIR = ROOT / "docs"
DOCS_DIR.mkdir(exist_ok=True)


def load_prompts():
    songs = []
    for path in sorted(PROMPTS_DIR.glob("*.yaml")):
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(f"skip {path.name}: {e}")
                continue
        if not data:
            continue
        data["_file"] = path.name
        data["_slug"] = path.stem
        songs.append(data)

    def version_key(s):
        return s.get("version", 0) or 0

    songs.sort(key=version_key, reverse=True)
    return songs


def main():
    songs = load_prompts()
    # Write JSON data file
    out_json = DOCS_DIR / "songs.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(songs, f, ensure_ascii=False, indent=2)
    print(f"wrote {out_json} ({len(songs)} songs)")

    # Write index.html
    html = INDEX_HTML_TEMPLATE
    out_html = DOCS_DIR / "index.html"
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {out_html}")


INDEX_HTML_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Suno Music Prompt Laboratory</title>
<style>
  :root {
    --bg: #0a0a0f;
    --panel: #15151e;
    --panel-hover: #1d1d2a;
    --text: #e8e8f0;
    --muted: #7a7a90;
    --accent: #ff6a3d;
    --accent-2: #ffb347;
    --border: #26263a;
    --tag: #2a2a40;
    --tag-text: #c5c5e0;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", Segoe UI, Roboto, sans-serif; }
  body { max-width: 1100px; margin: 0 auto; padding: 48px 24px 96px; }
  header { margin-bottom: 48px; }
  h1 { font-size: 2.4rem; margin: 0 0 8px; background: linear-gradient(90deg, var(--accent), var(--accent-2)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; letter-spacing: -0.02em; }
  .subtitle { color: var(--muted); font-size: 1rem; margin: 0; }
  .meta-bar { display: flex; gap: 24px; margin-top: 20px; flex-wrap: wrap; color: var(--muted); font-size: 0.9rem; }
  .meta-bar strong { color: var(--text); }
  input[type="search"] { width: 100%; padding: 14px 18px; background: var(--panel); border: 1px solid var(--border); border-radius: 12px; color: var(--text); font-size: 1rem; margin: 28px 0 36px; outline: none; transition: border-color 0.2s; }
  input[type="search"]:focus { border-color: var(--accent); }
  input[type="search"]::placeholder { color: var(--muted); }
  .songs { display: flex; flex-direction: column; gap: 16px; }
  .song { background: var(--panel); border: 1px solid var(--border); border-radius: 14px; padding: 24px 28px; transition: background 0.15s, border-color 0.15s; }
  .song:hover { background: var(--panel-hover); border-color: #3a3a5a; }
  .song-head { display: flex; align-items: baseline; gap: 14px; flex-wrap: wrap; margin-bottom: 10px; }
  .version { display: inline-block; padding: 2px 10px; background: var(--accent); color: #0a0a0f; font-weight: 700; font-size: 0.75rem; border-radius: 999px; letter-spacing: 0.03em; }
  .title { font-size: 1.35rem; font-weight: 600; margin: 0; color: var(--text); }
  .name-slug { color: var(--muted); font-size: 0.8rem; font-family: "SF Mono", Menlo, monospace; margin-left: auto; }
  .tags { display: flex; flex-wrap: wrap; gap: 6px; margin: 10px 0 14px; }
  .tag { padding: 3px 10px; background: var(--tag); color: var(--tag-text); font-size: 0.72rem; border-radius: 999px; font-family: "SF Mono", Menlo, monospace; }
  .style-block { color: #c0c0d4; font-size: 0.92rem; line-height: 1.55; margin: 8px 0; white-space: pre-wrap; }
  .section-label { color: var(--muted); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 14px; margin-bottom: 4px; }
  .notes { color: #9a9ab0; font-size: 0.85rem; line-height: 1.5; font-style: italic; }
  .instrumental-badge { display: inline-block; padding: 1px 8px; background: #1a3a2a; color: #7fd9a0; font-size: 0.7rem; border-radius: 999px; margin-left: 6px; }
  details summary { cursor: pointer; color: var(--accent-2); font-size: 0.82rem; margin-top: 6px; user-select: none; }
  details summary:hover { color: var(--accent); }
  details[open] summary { margin-bottom: 6px; }
  footer { margin-top: 64px; text-align: center; color: var(--muted); font-size: 0.85rem; border-top: 1px solid var(--border); padding-top: 24px; }
  footer a { color: var(--accent-2); text-decoration: none; }
  .hidden { display: none; }
  @media (max-width: 640px) {
    body { padding: 32px 16px 72px; }
    h1 { font-size: 1.8rem; }
    .song { padding: 18px 20px; }
    .name-slug { display: none; }
  }
</style>
</head>
<body>
<header>
  <h1>Suno Music Prompt Laboratory</h1>
  <p class="subtitle">Iterative prompt engineering for Suno v5.5 — cinematic, orchestral, experimental.</p>
  <div class="meta-bar">
    <div>Total experiments: <strong id="count">—</strong></div>
    <div>Latest version: <strong id="latest">—</strong></div>
    <div>Model: <strong>Suno v5.5</strong></div>
  </div>
</header>

<input id="search" type="search" placeholder="Search by title, tag, key, style, instrument…" autofocus>

<main class="songs" id="songs"></main>

<footer>
  Generated from <code>prompts/*.yaml</code> via <code>scripts/build_site.py</code>. All prompts handcrafted.
</footer>

<script>
const songsEl = document.getElementById('songs');
const searchEl = document.getElementById('search');
const countEl = document.getElementById('count');
const latestEl = document.getElementById('latest');
let ALL = [];

function escapeHtml(s) {
  if (s == null) return '';
  return String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

function renderSong(s) {
  const tags = (s.tags || []).map(t => `<span class="tag">${escapeHtml(t)}</span>`).join('');
  const instrumental = s.instrumental ? '<span class="instrumental-badge">instrumental</span>' : '';
  const exclude = s.exclude_styles ? `<div class="section-label">Exclude</div><div class="notes">${escapeHtml(s.exclude_styles)}</div>` : '';
  const notes = s.notes ? `<details><summary>Notes</summary><div class="notes">${escapeHtml(s.notes)}</div></details>` : '';
  return `
    <article class="song" data-search="${escapeHtml((s.title||'') + ' ' + (s.name||'') + ' ' + (s.style||'') + ' ' + (s.tags||[]).join(' ') + ' ' + (s.notes||''))}">
      <div class="song-head">
        <span class="version">v${escapeHtml(s.version)}</span>
        <h2 class="title">${escapeHtml(s.title || s.name || '(untitled)')}${instrumental}</h2>
        <span class="name-slug">${escapeHtml(s._file || '')}</span>
      </div>
      <div class="tags">${tags}</div>
      <div class="section-label">Style</div>
      <div class="style-block">${escapeHtml(s.style || '')}</div>
      ${exclude}
      ${notes}
    </article>
  `;
}

function render(list) {
  songsEl.innerHTML = list.map(renderSong).join('');
}

async function load() {
  const r = await fetch('songs.json');
  ALL = await r.json();
  countEl.textContent = ALL.length;
  const maxV = ALL.reduce((m, s) => Math.max(m, s.version || 0), 0);
  latestEl.textContent = 'v' + maxV;
  render(ALL);
}

searchEl.addEventListener('input', () => {
  const q = searchEl.value.toLowerCase().trim();
  if (!q) { render(ALL); return; }
  const terms = q.split(/\s+/);
  const filtered = ALL.filter(s => {
    const hay = ((s.title||'') + ' ' + (s.name||'') + ' ' + (s.style||'') + ' ' + (s.tags||[]).join(' ') + ' ' + (s.notes||'')).toLowerCase();
    return terms.every(t => hay.includes(t));
  });
  render(filtered);
});

load();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    main()
