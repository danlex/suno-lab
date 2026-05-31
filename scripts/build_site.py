#!/usr/bin/env python3
"""Generate docs/songs.json and docs/index.html from prompts/*.yaml.

The site is a static showcase of the entire catalog. The HTML template is a
single self-contained file (no external deps) that hydrates from songs.json
and suno_urls.json on load and supports:
  - Stats dashboard (technique count, instrument diversity, BPM/key distribution)
  - Search across titles, tags, style, notes
  - Filter chips for techniques, instruments, and keys
  - Sort by version (newest / oldest)
  - Pagination
  - Embedded Suno players per song
"""

import json
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

    songs.sort(key=lambda s: s.get("version", 0) or 0, reverse=True)
    return songs


def slim_song(s):
    """Strip heavy fields for the web JSON — keep only what the UI needs."""
    notes = s.get("notes", "") or ""
    if len(notes) > 200:
        notes = notes[:200] + "..."
    return {
        "v": s.get("version"),
        "n": s.get("name", ""),
        "t": s.get("title", ""),
        "s": s.get("style", ""),
        "g": s.get("tags", []),
        "i": 1 if s.get("instrumental") else 0,
        "o": notes,
        "f": s.get("_file", ""),
    }


def main():
    songs = load_prompts()
    slim = [slim_song(s) for s in songs]
    out_json = DOCS_DIR / "songs.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(slim, f, ensure_ascii=False, separators=(",", ":"))
    print(f"wrote {out_json} ({len(songs)} songs)")

    out_html = DOCS_DIR / "index.html"
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(INDEX_HTML_TEMPLATE)
    print(f"wrote {out_html}")

    out_analytics = DOCS_DIR / "analytics.html"
    with open(out_analytics, "w", encoding="utf-8") as f:
        f.write(ANALYTICS_HTML_TEMPLATE)
    print(f"wrote {out_analytics}")


INDEX_HTML_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Suno Music Prompt Laboratory — 240+ Cinematic Orchestral Experiments</title>
<meta name="description" content="Searchable archive of 240+ iterative Suno AI prompts for cinematic, orchestral, and experimental music. Explores 50+ architectural forms and genre fusions with engineering notes and structured metadata.">
<meta name="keywords" content="Suno AI, prompt engineering, cinematic music, orchestral music, AI music generation, film score, neoclassical, chaconne, fugue, cantus firmus, klangfarbenmelodie, ritornello, threnody, Suno v5.5">
<meta name="author" content="Alexandru DAN">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#ff6a3d">
<link rel="canonical" href="https://suno.alexandrudan.com/">
<link rel="alternate" type="application/json" href="https://suno.alexandrudan.com/songs.json" title="Songs JSON">
<meta property="og:title" content="Suno Music Prompt Laboratory — 240+ Cinematic Orchestral Experiments">
<meta property="og:description" content="240+ Suno AI prompts exploring 50+ architectural forms of cinematic orchestral music. Embedded players, engineering notes, reproducible prompts.">
<meta property="og:url" content="https://suno.alexandrudan.com/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Suno Music Prompt Laboratory">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Suno Music Prompt Laboratory">
<meta name="twitter:description" content="240+ iterative Suno AI prompt experiments.">
<meta name="twitter:creator" content="@danlex77">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Suno Music Prompt Laboratory",
  "url": "https://suno.alexandrudan.com/",
  "description": "Searchable archive of iterative Suno AI prompts for cinematic, orchestral, and experimental music generation.",
  "inLanguage": "en",
  "author": {"@type": "Person", "name": "Alexandru DAN", "url": "https://alexandrudan.com"}
}
</script>
<style>
  :root {
    --bg: #0a0a0f;
    --bg-soft: #0e0e16;
    --panel: #15151e;
    --panel-hover: #1d1d2a;
    --panel-soft: #11111a;
    --text: #e8e8f0;
    --muted: #7a7a90;
    --muted-2: #56566a;
    --accent: #ff6a3d;
    --accent-2: #ffb347;
    --accent-3: #7aa2ff;
    --border: #26263a;
    --border-soft: #1c1c2a;
    --tag: #2a2a40;
    --tag-text: #c5c5e0;
    --tag-active: #ff6a3d;
    --tag-active-text: #0a0a0f;
    --good: #7fd9a0;
    --warn: #ffb347;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", Segoe UI, Roboto, sans-serif; -webkit-font-smoothing: antialiased; }
  body { max-width: 1200px; margin: 0 auto; padding: 48px 24px 96px; }

  /* Header */
  header { margin-bottom: 36px; }
  h1 { font-size: 2.6rem; margin: 0 0 6px; background: linear-gradient(90deg, var(--accent), var(--accent-2)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; letter-spacing: -0.025em; }
  .subtitle { color: var(--muted); font-size: 1.02rem; margin: 0 0 18px; max-width: 720px; line-height: 1.5; }
  .meta-bar { display: flex; gap: 22px; color: var(--muted); font-size: 0.88rem; flex-wrap: wrap; }
  .meta-bar strong { color: var(--text); font-variant-numeric: tabular-nums; }

  /* Stats dashboard */
  .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; margin: 28px 0 28px; }
  .stat-card { background: var(--panel-soft); border: 1px solid var(--border-soft); border-radius: 12px; padding: 16px 18px; }
  .stat-label { color: var(--muted); font-size: 0.72rem; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 8px; }
  .stat-value { color: var(--text); font-size: 1.85rem; font-weight: 700; letter-spacing: -0.02em; font-variant-numeric: tabular-nums; line-height: 1; }
  .stat-sub { color: var(--muted-2); font-size: 0.78rem; margin-top: 6px; }
  .stat-bar { display: flex; height: 8px; margin-top: 10px; gap: 1px; border-radius: 4px; overflow: hidden; background: var(--bg-soft); }
  .stat-bar > span { flex: 1; opacity: 0.85; transition: opacity 0.15s; }
  .stat-bar > span:hover { opacity: 1; }

  /* Controls */
  .controls { background: var(--panel-soft); border: 1px solid var(--border-soft); border-radius: 14px; padding: 18px 20px; margin: 0 0 28px; }
  .control-row { display: flex; gap: 12px; align-items: center; margin-bottom: 14px; flex-wrap: wrap; }
  .control-row:last-child { margin-bottom: 0; }
  input[type="search"] { flex: 1; min-width: 220px; padding: 12px 16px; background: var(--bg-soft); border: 1px solid var(--border); border-radius: 10px; color: var(--text); font-size: 0.95rem; outline: none; transition: border-color 0.15s; }
  input[type="search"]:focus { border-color: var(--accent); }
  input[type="search"]::placeholder { color: var(--muted-2); }
  select { padding: 10px 14px; background: var(--bg-soft); border: 1px solid var(--border); border-radius: 10px; color: var(--text); font-size: 0.9rem; outline: none; cursor: pointer; }
  select:focus { border-color: var(--accent); }
  .control-label { color: var(--muted); font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.06em; margin-right: 4px; }

  .chips { display: flex; flex-wrap: wrap; gap: 6px; }
  .chip { padding: 4px 11px; background: var(--tag); color: var(--tag-text); font-size: 0.74rem; border-radius: 999px; cursor: pointer; border: 1px solid transparent; transition: background 0.12s, border-color 0.12s, color 0.12s; user-select: none; font-family: "SF Mono", Menlo, monospace; }
  .chip:hover { border-color: var(--accent); }
  .chip.active { background: var(--tag-active); color: var(--tag-active-text); font-weight: 600; }
  .chip-count { opacity: 0.6; font-size: 0.68rem; margin-left: 2px; }
  .chip.active .chip-count { opacity: 0.85; }

  .filter-section { margin-top: 10px; }
  .filter-section-label { color: var(--muted); font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 6px; }
  .clear-btn { padding: 5px 12px; background: transparent; color: var(--muted); border: 1px solid var(--border); border-radius: 999px; cursor: pointer; font-size: 0.74rem; transition: color 0.12s, border-color 0.12s; }
  .clear-btn:hover { color: var(--accent); border-color: var(--accent); }

  /* Result count */
  .result-info { color: var(--muted); font-size: 0.85rem; margin: 0 0 18px; }
  .result-info strong { color: var(--text); }

  /* Songs */
  .songs { display: flex; flex-direction: column; gap: 14px; }
  .song { background: var(--panel); border: 1px solid var(--border); border-radius: 14px; padding: 22px 26px; transition: background 0.15s, border-color 0.15s; }
  .song:hover { background: var(--panel-hover); border-color: #3a3a5a; }
  .song-head { display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap; margin-bottom: 8px; }
  .version { display: inline-block; padding: 3px 10px; background: var(--accent); color: #0a0a0f; font-weight: 700; font-size: 0.74rem; border-radius: 999px; letter-spacing: 0.03em; font-variant-numeric: tabular-nums; }
  .title { font-size: 1.32rem; font-weight: 600; margin: 0; color: var(--text); letter-spacing: -0.01em; }
  .name-slug { color: var(--muted); font-size: 0.78rem; font-family: "SF Mono", Menlo, monospace; margin-left: auto; }

  .song-meta { display: flex; gap: 14px; flex-wrap: wrap; color: var(--muted); font-size: 0.78rem; margin: 6px 0 12px; font-family: "SF Mono", Menlo, monospace; }
  .song-meta span { display: inline-flex; align-items: center; gap: 4px; }
  .song-meta .technique-label { color: var(--accent-2); }
  .song-meta .key-label { color: var(--accent-3); }

  .tags { display: flex; flex-wrap: wrap; gap: 5px; margin: 8px 0 12px; }
  .tag { padding: 3px 10px; background: var(--tag); color: var(--tag-text); font-size: 0.7rem; border-radius: 999px; font-family: "SF Mono", Menlo, monospace; }
  .tag-revival { background: #2a3a2a; color: #b0e0c5; }
  .tag-new { background: #3a2a2a; color: #ffb347; }

  .section-label { color: var(--muted); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 14px; margin-bottom: 4px; }
  .style-block { color: #c0c0d4; font-size: 0.92rem; line-height: 1.55; margin: 8px 0; white-space: pre-wrap; }
  .notes { color: #9a9ab0; font-size: 0.85rem; line-height: 1.5; font-style: italic; }
  .instrumental-badge { display: inline-block; padding: 1px 8px; background: #1a3a2a; color: #7fd9a0; font-size: 0.7rem; border-radius: 999px; margin-left: 6px; }
  .style-preview { color: #c0c0d4; font-size: 0.88rem; line-height: 1.5; cursor: pointer; }
  .style-preview:hover { color: var(--accent-2); }
  details summary { cursor: pointer; color: var(--accent-2); font-size: 0.82rem; margin-top: 6px; user-select: none; }
  details summary:hover { color: var(--accent); }
  details[open] summary { margin-bottom: 6px; }

  /* Pagination */
  .pagination { display: flex; align-items: center; justify-content: center; gap: 6px; margin: 36px 0 0; flex-wrap: wrap; }
  .pagination button { background: var(--panel); border: 1px solid var(--border); color: var(--text); padding: 7px 13px; border-radius: 8px; cursor: pointer; font-size: 0.85rem; transition: background 0.15s, border-color 0.15s; font-variant-numeric: tabular-nums; }
  .pagination button:hover:not(:disabled) { background: var(--panel-hover); border-color: var(--accent); }
  .pagination button.active { background: var(--accent); color: #0a0a0f; font-weight: 700; border-color: var(--accent); }
  .pagination button:disabled { opacity: 0.3; cursor: default; }
  .page-info { color: var(--muted); font-size: 0.8rem; margin: 0 6px; }

  footer { margin-top: 64px; text-align: center; color: var(--muted); font-size: 0.84rem; border-top: 1px solid var(--border); padding-top: 24px; }
  footer a { color: var(--accent-2); text-decoration: none; }
  footer a:hover { color: var(--accent); }

  .hidden { display: none; }

  @media (max-width: 720px) {
    body { padding: 32px 14px 72px; }
    h1 { font-size: 1.95rem; }
    .stat-card { padding: 12px 14px; }
    .stat-value { font-size: 1.5rem; }
    .song { padding: 16px 18px; }
    .name-slug { display: none; }
    .pagination button { padding: 6px 10px; font-size: 0.8rem; }
  }
</style>
</head>
<body>

<header>
  <h1>Suno Music Prompt Laboratory</h1>
  <p class="subtitle">Iterative prompt engineering for Suno v5.5 — cinematic, orchestral, experimental. Every prompt is a single hour-long cycle: research → drafted → judged ≥90 → submitted → published. Filter, search, sort.</p>
  <div class="meta-bar">
    <div>Total experiments: <strong id="count">—</strong></div>
    <div>Latest version: <strong id="latest">—</strong></div>
    <div>Model: <strong>Suno v5.5</strong></div>
    <div><a href="analytics.html" style="color: var(--accent-2); text-decoration: none;">→ Analytics</a></div>
  </div>
</header>

<section class="stats" id="stats"></section>

<section class="controls">
  <div class="control-row">
    <input id="search" type="search" placeholder="Search by title, tag, technique, instrument, key, style…" autofocus>
    <span class="control-label">Sort</span>
    <select id="sort">
      <option value="newest">Newest first</option>
      <option value="oldest">Oldest first</option>
    </select>
    <button class="clear-btn" id="clearAll">Clear filters</button>
  </div>
  <div class="filter-section">
    <div class="filter-section-label">Technique</div>
    <div class="chips" id="techChips"></div>
  </div>
  <div class="filter-section">
    <div class="filter-section-label">Featured instrument</div>
    <div class="chips" id="instChips"></div>
  </div>
  <div class="filter-section">
    <div class="filter-section-label">Key</div>
    <div class="chips" id="keyChips"></div>
  </div>
</section>

<p class="result-info"><strong id="resultCount">0</strong> songs match — page <strong id="pageNum">1</strong> of <strong id="pageTotal">1</strong></p>

<main class="songs" id="songs"></main>
<nav class="pagination" id="pagination"></nav>

<footer>
  Built by <a href="https://alexandrudan.com">alexandrudan.com</a> &middot; <a href="https://tvl.tech">tvl.tech</a> &middot; <a href="https://github.com/danlex/suno-lab">github.com/danlex/suno-lab</a>
</footer>

<script>
const songsEl = document.getElementById('songs');
const searchEl = document.getElementById('search');
const sortEl = document.getElementById('sort');
const countEl = document.getElementById('count');
const latestEl = document.getElementById('latest');
const statsEl = document.getElementById('stats');
const techChipsEl = document.getElementById('techChips');
const instChipsEl = document.getElementById('instChips');
const keyChipsEl = document.getElementById('keyChips');
const paginationEl = document.getElementById('pagination');
const resultCountEl = document.getElementById('resultCount');
const pageNumEl = document.getElementById('pageNum');
const pageTotalEl = document.getElementById('pageTotal');
const clearAllEl = document.getElementById('clearAll');
const PER_PAGE = 20;

let ALL = [];
let SUNO_URLS = {};
let SEARCH_INDEX = [];
let currentPage = 1;
let currentList = [];
let activeFilters = { tech: null, inst: null, key: null };

// Known instrument vocabulary — used to extract instruments from tag arrays.
const INSTRUMENT_VOCAB = new Set([
  'harp','tubular-bells','viola-da-gamba','cor-anglais','hurdy-gurdy','handpan',
  'bass-flute','celesta','glockenspiel','contrabass-clarinet','ondes-martenot','music-box',
  'prepared-piano','upright-bass','subcontrabass-saxophone','ophicleide','baryton','clavichord',
  'cristal-baschet','tenor-saxophone','french-horn','nyckelharpa','bass-trombone','cimbalom',
  'duduk','cornet','singing-saw','steel-tongue-drum','contrabassoon','felt-piano',
  'oboe-d-amore','mellotron','flugelhorn','tuba','harpsichord','vibraphone','viola',
  'bass-clarinet','marimba','glass-marimba','bowed-vibraphone','double-bass','waterphone',
  'theremin','chalumeau','crotales','trumpet','trombone','piccolo','clarinet','oboe',
  'bandoneon','shakuhachi','erhu','frame-drums','taiko','balafon','kora','guqin','sarangi',
  'nail-violin','singing-saw','steelpan','mbira','bowed-vibraphone','glass-harmonica',
]);

const KEY_RE = /^([a-g])(-flat|-sharp)?-(minor|major)$/;

function escapeHtml(s) {
  if (s == null) return '';
  return String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

function prettyKey(k) {
  const m = k.match(KEY_RE);
  if (!m) return k;
  const note = m[1].toUpperCase();
  const acc = m[2] === '-flat' ? '♭' : m[2] === '-sharp' ? '♯' : '';
  return `${note}${acc} ${m[3]}`;
}

// Pretty-print a slug (kebab-case → Title Case).
function prettySlug(s) {
  return s.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
}

function parseTags(g) {
  const tags = (g || []).map(t => String(t).toLowerCase());
  let technique = null, bpm = null, key = null;
  const instruments = [];
  const isNew = tags.includes('new-technique') || tags.includes('research-driven');
  const isInstrumental = true;

  for (const t of tags) {
    // technique: tag containing "technique-new" or starting with "orchestral-"
    if (!technique && (t.endsWith('-technique-new') || t.startsWith('orchestral-'))) {
      technique = t.replace(/^orchestral-/, '').replace(/-technique-new$/, '');
    }
    // BPM: "157bpm"
    if (!bpm) {
      const m = t.match(/^(\d{2,3})bpm$/);
      if (m) bpm = parseInt(m[1]);
    }
    // key: "f-sharp-minor", "g-major"
    if (!key && KEY_RE.test(t)) key = t;
    // instruments
    if (INSTRUMENT_VOCAB.has(t)) instruments.push(t);
  }
  return { technique, bpm, key, instruments };
}

function buildIndex() {
  SEARCH_INDEX = ALL.map(s => {
    const parsed = parseTags(s.g);
    return {
      s,
      parsed,
      hay: ((s.t||'') + ' ' + (s.n||'') + ' ' + (s.s||'') + ' ' + (s.g||[]).join(' ') + ' ' + (s.o||'')).toLowerCase()
    };
  });
}

function computeStats() {
  const techCounts = new Map();
  const instCounts = new Map();
  const keyCounts = new Map();
  const bpmBuckets = new Map(); // bucket → count
  let withBPM = 0;
  let instrumentalCount = 0;

  for (const e of SEARCH_INDEX) {
    if (e.parsed.technique) techCounts.set(e.parsed.technique, (techCounts.get(e.parsed.technique)||0)+1);
    for (const inst of e.parsed.instruments) {
      instCounts.set(inst, (instCounts.get(inst)||0)+1);
    }
    if (e.parsed.key) keyCounts.set(e.parsed.key, (keyCounts.get(e.parsed.key)||0)+1);
    if (e.parsed.bpm) {
      withBPM++;
      // bucket: 60-79, 80-99, 100-119, 120-139, 140-159, 160+
      const b = Math.floor((e.parsed.bpm - 60) / 20);
      const label = (b < 0) ? '<60' : (b >= 5) ? '160+' : `${60 + b*20}–${79 + b*20}`;
      bpmBuckets.set(label, (bpmBuckets.get(label)||0)+1);
    }
    if (e.s.i) instrumentalCount++;
  }

  return { techCounts, instCounts, keyCounts, bpmBuckets, withBPM, instrumentalCount };
}

function renderStats() {
  const { techCounts, instCounts, keyCounts, bpmBuckets, instrumentalCount } = computeStats();
  const totalSongs = ALL.length;
  const uniqueTech = techCounts.size;
  const uniqueInst = instCounts.size;
  const uniqueKey = keyCounts.size;

  // Top technique
  const topTech = [...techCounts.entries()].sort((a,b) => b[1] - a[1])[0];
  // Top instrument
  const topInst = [...instCounts.entries()].sort((a,b) => b[1] - a[1])[0];

  // BPM distribution bar (ordered buckets)
  const order = ['<60','60–79','80–99','100–119','120–139','140–159','160+'];
  const max = Math.max(...[...bpmBuckets.values()], 1);
  const barColors = ['#56566a','#7aa2ff','#7fd9a0','#ffd166','#ffb347','#ff6a3d','#cf4566'];
  const barHtml = order.map((label, i) => {
    const v = bpmBuckets.get(label) || 0;
    const h = Math.max(2, Math.round(v / max * 100));
    return `<span title="${label} BPM: ${v} songs" style="background: ${barColors[i]}; flex: ${v || 0.1}"></span>`;
  }).join('');

  statsEl.innerHTML = `
    <div class="stat-card">
      <div class="stat-label">Songs in catalog</div>
      <div class="stat-value">${totalSongs}</div>
      <div class="stat-sub">${instrumentalCount} instrumental · ${totalSongs - instrumentalCount} vocal</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Unique techniques</div>
      <div class="stat-value">${uniqueTech}</div>
      <div class="stat-sub">${topTech ? `Most used: <strong>${escapeHtml(prettySlug(topTech[0]))}</strong> (${topTech[1]}×)` : ''}</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Unique instruments</div>
      <div class="stat-value">${uniqueInst}</div>
      <div class="stat-sub">${topInst ? `Most featured: <strong>${escapeHtml(prettySlug(topInst[0]))}</strong> (${topInst[1]}×)` : ''}</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Unique keys</div>
      <div class="stat-value">${uniqueKey}</div>
      <div class="stat-sub">across 24 possible major/minor pairs</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">BPM distribution</div>
      <div class="stat-value" style="font-size: 1.05rem; font-weight: 500; line-height: 1.3;">60–180+</div>
      <div class="stat-bar">${barHtml}</div>
      <div class="stat-sub">Hover bars for counts</div>
    </div>
  `;
}

function renderChips() {
  const { techCounts, instCounts, keyCounts } = computeStats();
  // Top 16 techniques by count
  const topTech = [...techCounts.entries()].sort((a,b) => b[1] - a[1]).slice(0, 16);
  techChipsEl.innerHTML = topTech.map(([t, c]) =>
    `<span class="chip ${activeFilters.tech === t ? 'active' : ''}" data-filter="tech" data-value="${escapeHtml(t)}">${escapeHtml(prettySlug(t))} <span class="chip-count">${c}</span></span>`
  ).join('');

  // Top 20 instruments by count
  const topInst = [...instCounts.entries()].sort((a,b) => b[1] - a[1]).slice(0, 20);
  instChipsEl.innerHTML = topInst.map(([t, c]) =>
    `<span class="chip ${activeFilters.inst === t ? 'active' : ''}" data-filter="inst" data-value="${escapeHtml(t)}">${escapeHtml(prettySlug(t))} <span class="chip-count">${c}</span></span>`
  ).join('');

  // Keys: all, sorted by count desc
  const topKeys = [...keyCounts.entries()].sort((a,b) => b[1] - a[1]).slice(0, 20);
  keyChipsEl.innerHTML = topKeys.map(([t, c]) =>
    `<span class="chip ${activeFilters.key === t ? 'active' : ''}" data-filter="key" data-value="${escapeHtml(t)}">${escapeHtml(prettyKey(t))} <span class="chip-count">${c}</span></span>`
  ).join('');

  // Wire chip clicks
  document.querySelectorAll('.chip').forEach(el => {
    el.addEventListener('click', () => {
      const f = el.dataset.filter, v = el.dataset.value;
      activeFilters[f] = activeFilters[f] === v ? null : v;
      renderChips();
      applyFilters();
    });
  });
}

function applyFilters() {
  const q = searchEl.value.toLowerCase().trim();
  const terms = q ? q.split(/\s+/) : [];
  const sort = sortEl.value;

  let filtered = SEARCH_INDEX.filter(e => {
    if (terms.length && !terms.every(t => e.hay.includes(t))) return false;
    if (activeFilters.tech && e.parsed.technique !== activeFilters.tech) return false;
    if (activeFilters.inst && !e.parsed.instruments.includes(activeFilters.inst)) return false;
    if (activeFilters.key && e.parsed.key !== activeFilters.key) return false;
    return true;
  }).map(e => e.s);

  if (sort === 'oldest') filtered = filtered.slice().reverse();
  // newest is default order (already sorted desc by build_site)

  currentList = filtered;
  currentPage = 1;
  renderPage();
}

function renderSong(s) {
  const tags = (s.g || []).map(t => {
    let cls = 'tag';
    if (t.startsWith('revival-')) cls += ' tag-revival';
    if (t.startsWith('new-') || t === 'research-driven') cls += ' tag-new';
    return `<span class="${cls}">${escapeHtml(t)}</span>`;
  }).join('');
  const parsed = parseTags(s.g);
  const metaParts = [];
  if (parsed.technique) metaParts.push(`<span class="technique-label">${escapeHtml(prettySlug(parsed.technique))}</span>`);
  if (parsed.key) metaParts.push(`<span class="key-label">${escapeHtml(prettyKey(parsed.key))}</span>`);
  if (parsed.bpm) metaParts.push(`<span>${parsed.bpm} BPM</span>`);
  if (parsed.instruments.length) metaParts.push(`<span>${parsed.instruments.map(prettySlug).join(' · ')}</span>`);
  const metaHtml = metaParts.length ? `<div class="song-meta">${metaParts.join('')}</div>` : '';

  const instrumental = s.i ? '<span class="instrumental-badge">instrumental</span>' : '';
  const notes = s.o ? `<details><summary>Notes</summary><div class="notes">${escapeHtml(s.o)}</div></details>` : '';
  const title = s.t || s.n || '';
  const ids = (SUNO_URLS[title] || []).slice(0, 1);
  const players = ids.map(id =>
    `<iframe src="https://suno.com/embed/${id}" width="100%" height="120" frameborder="0" allow="autoplay" loading="lazy" style="border-radius:10px;margin-top:8px;"></iframe>`
  ).join('');
  const playerSection = players ? `<div class="section-label">Listen</div>${players}` : '';
  const styleText = escapeHtml(s.s || '');
  const stylePreview = styleText.length > 200 ? styleText.slice(0, 200) + '…' : styleText;
  const styleSection = styleText.length > 200
    ? `<details><summary class="style-preview">${stylePreview}</summary><div class="style-block">${styleText}</div></details>`
    : `<div class="style-block">${styleText}</div>`;

  return `
    <article class="song">
      <div class="song-head">
        <span class="version">v${escapeHtml(s.v)}</span>
        <h2 class="title">${escapeHtml(title || '(untitled)')}${instrumental}</h2>
        <span class="name-slug">${escapeHtml(s.f || '')}</span>
      </div>
      ${metaHtml}
      ${playerSection}
      <div class="tags">${tags}</div>
      <div class="section-label">Style</div>
      ${styleSection}
      ${notes}
    </article>
  `;
}

function totalPages() { return Math.max(1, Math.ceil(currentList.length / PER_PAGE)); }

function renderPage() {
  const start = (currentPage - 1) * PER_PAGE;
  const page = currentList.slice(start, start + PER_PAGE);
  songsEl.innerHTML = page.map(renderSong).join('');
  resultCountEl.textContent = currentList.length;
  pageNumEl.textContent = currentPage;
  pageTotalEl.textContent = totalPages();
  renderPagination();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function renderPagination() {
  const tp = totalPages();
  if (tp <= 1) { paginationEl.innerHTML = ''; return; }
  let html = '';
  html += `<button ${currentPage === 1 ? 'disabled' : ''} onclick="goPage(${currentPage - 1})">Prev</button>`;
  for (let i = 1; i <= tp; i++) {
    if (tp <= 9 || i === 1 || i === tp || Math.abs(i - currentPage) <= 1) {
      html += `<button class="${i === currentPage ? 'active' : ''}" onclick="goPage(${i})">${i}</button>`;
    } else if (i === 2 && currentPage > 4) {
      html += `<span class="page-info">…</span>`;
    } else if (i === tp - 1 && currentPage < tp - 3) {
      html += `<span class="page-info">…</span>`;
    }
  }
  html += `<button ${currentPage === tp ? 'disabled' : ''} onclick="goPage(${currentPage + 1})">Next</button>`;
  paginationEl.innerHTML = html;
}

function goPage(p) {
  currentPage = Math.max(1, Math.min(p, totalPages()));
  renderPage();
}

async function load() {
  const [r, u] = await Promise.all([
    fetch('songs.json'),
    fetch('suno_urls.json').catch(() => ({ ok: false }))
  ]);
  ALL = await r.json();
  if (u.ok) SUNO_URLS = await u.json();
  countEl.textContent = ALL.length;
  const maxV = ALL.reduce((m, s) => Math.max(m, s.v || 0), 0);
  latestEl.textContent = 'v' + maxV;
  buildIndex();
  renderStats();
  renderChips();
  applyFilters();
}

let searchTimer;
searchEl.addEventListener('input', () => {
  clearTimeout(searchTimer);
  searchTimer = setTimeout(applyFilters, 180);
});
sortEl.addEventListener('change', applyFilters);
clearAllEl.addEventListener('click', () => {
  activeFilters = { tech: null, inst: null, key: null };
  searchEl.value = '';
  renderChips();
  applyFilters();
});

load();
</script>
</body>
</html>
"""


ANALYTICS_HTML_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Catalog Analytics · Suno Music Prompt Laboratory</title>
<meta name="description" content="Catalog intelligence for the Suno Music Prompt Laboratory: technique family distribution, version timeline, instrument lineage, BPM and key trends across 240+ iterative experiments.">
<meta name="theme-color" content="#ff6a3d">
<link rel="canonical" href="https://suno.alexandrudan.com/analytics.html">
<style>
  :root {
    --bg: #0a0a0f;
    --bg-soft: #0e0e16;
    --panel: #15151e;
    --panel-soft: #11111a;
    --text: #e8e8f0;
    --muted: #7a7a90;
    --muted-2: #56566a;
    --accent: #ff6a3d;
    --accent-2: #ffb347;
    --border: #26263a;
    --border-soft: #1c1c2a;
    /* Technique family palette */
    --fam-formal: #6c8cff;
    --fam-narrative: #ff8a55;
    --fam-harmonic: #57d49a;
    --fam-rhythmic: #ffd166;
    --fam-textural: #c084fc;
    --fam-other: #7a7a90;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", Segoe UI, Roboto, sans-serif; -webkit-font-smoothing: antialiased; }
  body { max-width: 1200px; margin: 0 auto; padding: 48px 24px 96px; }
  header { margin-bottom: 36px; }
  .brand { display: flex; align-items: baseline; gap: 14px; flex-wrap: wrap; }
  .brand-mark { color: var(--muted); font-size: 0.85rem; text-decoration: none; }
  .brand-mark:hover { color: var(--accent); }
  h1 { font-size: 2.2rem; margin: 4px 0 6px; background: linear-gradient(90deg, var(--accent), var(--accent-2)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; letter-spacing: -0.02em; }
  .subtitle { color: var(--muted); margin: 0 0 16px; font-size: 0.98rem; }

  section { background: var(--panel-soft); border: 1px solid var(--border-soft); border-radius: 14px; padding: 22px 24px; margin-bottom: 22px; }
  h2 { font-size: 1.15rem; margin: 0 0 4px; color: var(--text); letter-spacing: -0.01em; }
  .section-sub { color: var(--muted); font-size: 0.85rem; margin: 0 0 18px; max-width: 680px; line-height: 1.5; }

  /* Stat cards */
  .stat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 12px; }
  .stat { background: var(--bg-soft); border: 1px solid var(--border-soft); border-radius: 10px; padding: 14px 16px; }
  .stat-label { color: var(--muted); font-size: 0.7rem; letter-spacing: 0.07em; text-transform: uppercase; margin-bottom: 6px; }
  .stat-value { color: var(--text); font-size: 1.7rem; font-weight: 700; letter-spacing: -0.02em; font-variant-numeric: tabular-nums; line-height: 1; }
  .stat-sub { color: var(--muted-2); font-size: 0.78rem; margin-top: 4px; }

  /* Timeline */
  .timeline-wrap { background: var(--bg-soft); border: 1px solid var(--border-soft); border-radius: 10px; padding: 16px; overflow-x: auto; }
  .timeline-svg { width: 100%; height: 70px; display: block; }
  .timeline-axis { color: var(--muted); font-size: 0.7rem; font-family: "SF Mono", Menlo, monospace; }

  /* Family legend */
  .legend { display: flex; gap: 14px; flex-wrap: wrap; margin-top: 12px; }
  .legend-item { display: inline-flex; align-items: center; gap: 6px; font-size: 0.78rem; color: var(--muted); }
  .legend-swatch { width: 11px; height: 11px; border-radius: 3px; display: inline-block; }

  /* Family distribution bars */
  .fam-bar-row { display: grid; grid-template-columns: 180px 1fr 60px; gap: 12px; align-items: center; margin: 6px 0; }
  .fam-bar-label { color: var(--text); font-size: 0.86rem; font-weight: 500; }
  .fam-bar-track { background: var(--bg-soft); height: 22px; border-radius: 5px; overflow: hidden; }
  .fam-bar-fill { height: 100%; border-radius: 5px 0 0 5px; }
  .fam-bar-count { color: var(--muted); font-size: 0.82rem; font-variant-numeric: tabular-nums; text-align: right; }

  /* Instrument table */
  .inst-table { width: 100%; border-collapse: collapse; font-size: 0.86rem; }
  .inst-table th { text-align: left; color: var(--muted); font-weight: 500; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.06em; padding: 6px 10px; border-bottom: 1px solid var(--border-soft); }
  .inst-table td { padding: 7px 10px; border-bottom: 1px solid var(--border-soft); color: var(--text); }
  .inst-table tr:last-child td { border-bottom: none; }
  .inst-table .num { font-variant-numeric: tabular-nums; color: var(--muted); }
  .gap-deep { color: var(--accent-2); font-weight: 600; }
  .gap-very-deep { color: var(--accent); font-weight: 700; }
  .inst-name { font-family: "SF Mono", Menlo, monospace; font-size: 0.82rem; }
  .inst-family { color: var(--muted); font-size: 0.74rem; font-family: "SF Mono", Menlo, monospace; }

  /* BPM scatter */
  .scatter-wrap { background: var(--bg-soft); border: 1px solid var(--border-soft); border-radius: 10px; padding: 12px; }
  .scatter-svg { width: 100%; height: 320px; display: block; }
  .scatter-grid { stroke: var(--border-soft); stroke-width: 1; }
  .scatter-axis-label { fill: var(--muted); font-size: 11px; font-family: "SF Mono", Menlo, monospace; }
  .scatter-dot { fill: var(--accent); opacity: 0.7; }

  /* Key heatmap */
  .keys-grid { display: grid; grid-template-columns: repeat(12, 1fr); gap: 4px; max-width: 720px; }
  .key-cell { background: var(--bg-soft); border: 1px solid var(--border-soft); padding: 8px 6px; border-radius: 6px; text-align: center; font-size: 0.78rem; color: var(--text); font-family: "SF Mono", Menlo, monospace; cursor: default; transition: background 0.15s; }
  .key-cell.count-0 { opacity: 0.3; }
  .key-cell .count { display: block; color: var(--muted); font-size: 0.7rem; margin-top: 2px; }
  .key-row-label { color: var(--muted); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.07em; margin: 14px 0 6px; }

  footer { margin-top: 48px; text-align: center; color: var(--muted); font-size: 0.84rem; border-top: 1px solid var(--border); padding-top: 22px; }
  footer a { color: var(--accent-2); text-decoration: none; }
  footer a:hover { color: var(--accent); }

  @media (max-width: 720px) {
    body { padding: 32px 14px 72px; }
    h1 { font-size: 1.7rem; }
    .fam-bar-row { grid-template-columns: 130px 1fr 48px; gap: 8px; }
    .keys-grid { grid-template-columns: repeat(6, 1fr); }
  }
</style>
</head>
<body>

<header>
  <div class="brand">
    <a href="index.html" class="brand-mark">← Catalog</a>
  </div>
  <h1>Catalog Analytics</h1>
  <p class="subtitle">Cross-version intelligence on the Suno Music Prompt Laboratory — technique families, instrument lineage, tempo and key trends across all <span id="totalVersions">—</span> versions.</p>
</header>

<section>
  <h2>Snapshot</h2>
  <p class="section-sub">High-level rollups across the whole catalog.</p>
  <div class="stat-grid" id="snapshotStats"></div>
</section>

<section>
  <h2>Version timeline</h2>
  <p class="section-sub">One bar per version, colored by technique family. Hover for the title.</p>
  <div class="timeline-wrap">
    <svg id="timeline" class="timeline-svg" preserveAspectRatio="none"></svg>
  </div>
  <div class="legend" id="famLegend"></div>
</section>

<section>
  <h2>Technique families</h2>
  <p class="section-sub">How techniques cluster across the catalog — formal architecture, narrative/dramatic, harmonic device, rhythmic/temporal, textural/sound-design, other.</p>
  <div id="famBars"></div>
</section>

<section>
  <h2>Instrument lineage</h2>
  <p class="section-sub">Top instruments by total appearances, with gap (versions since last use) and family. Deep-gap instruments are revival candidates — highlighted in orange.</p>
  <div style="overflow-x: auto;">
    <table class="inst-table">
      <thead>
        <tr><th>Instrument</th><th>Family</th><th>Uses</th><th>Last version</th><th>Gap</th></tr>
      </thead>
      <tbody id="instTable"></tbody>
    </table>
  </div>
</section>

<section>
  <h2>BPM over time</h2>
  <p class="section-sub">Each dot is one version (x-axis) at its BPM (y-axis). Bands of clustering reveal tempo eras.</p>
  <div class="scatter-wrap">
    <svg id="bpmScatter" class="scatter-svg"></svg>
  </div>
</section>

<section>
  <h2>Key distribution</h2>
  <p class="section-sub">Each cell is one key. Brighter = more uses. Click-target labels show the count.</p>
  <div class="key-row-label">Major keys</div>
  <div class="keys-grid" id="majorKeys"></div>
  <div class="key-row-label">Minor keys</div>
  <div class="keys-grid" id="minorKeys"></div>
</section>

<footer>
  Built by <a href="https://alexandrudan.com">alexandrudan.com</a> &middot; <a href="index.html">Browse the catalog</a> &middot; <a href="https://github.com/danlex/suno-lab">github.com/danlex/suno-lab</a>
</footer>

<script>
const FAMILY_RULES = [
  { fam: 'formal', label: 'Formal architecture', color: 'var(--fam-formal)', match: ['cantus', 'passacaglia', 'chaconne', 'ritornello', 'hymn', 'cabaletta', 'scherzo', 'double-variation', 'lament-bass', 'hocket', 'fugue', 'canon', 'rondo', 'sonata', 'arch', 'concerto', 'theme-and-variations', 'french-overture', 'ricercare', 'passamezzo'] },
  { fam: 'narrative', label: 'Narrative / dramatic', color: 'var(--fam-narrative)', match: ['threnody', 'apotheosis', 'climax', 'metamorphosis', 'thematic-meta', 'siciliano'] },
  { fam: 'harmonic', label: 'Harmonic device', color: 'var(--fam-harmonic)', match: ['quartal', 'klangfarben', 'spectral', 'twelve-tone'] },
  { fam: 'rhythmic', label: 'Rhythmic / temporal', color: 'var(--fam-rhythmic)', match: ['metric', 'alap', 'velocity', 'perpetuum', 'tarantella', 'isorhythm', 'stile-concitato', 'asymmetric-metric', 'col-legno'] },
  { fam: 'textural', label: 'Textural / sound-design', color: 'var(--fam-textural)', match: ['granular', 'musique-concrete', 'additive', 'micropolyphony', 'minimalism', 'dissolution', 'aleatoric', 'stochastic'] },
];

const FAMILY_INFO = { formal: { color: 'var(--fam-formal)', label: 'Formal architecture' }, narrative: { color: 'var(--fam-narrative)', label: 'Narrative / dramatic' }, harmonic: { color: 'var(--fam-harmonic)', label: 'Harmonic device' }, rhythmic: { color: 'var(--fam-rhythmic)', label: 'Rhythmic / temporal' }, textural: { color: 'var(--fam-textural)', label: 'Textural / sound-design' }, other: { color: 'var(--fam-other)', label: 'Other' } };

const INSTRUMENT_VOCAB = {
  'harp': 'plucked_strings', 'tubular-bells': 'mallet_perc', 'viola-da-gamba': 'bowed_strings',
  'cor-anglais': 'woodwinds', 'hurdy-gurdy': 'bowed_strings', 'handpan': 'metallic_idiophones',
  'bass-flute': 'woodwinds', 'celesta': 'keyboards', 'glockenspiel': 'mallet_perc',
  'contrabass-clarinet': 'woodwinds', 'ondes-martenot': 'early_electronic', 'music-box': 'keyboards',
  'prepared-piano': 'keyboards', 'upright-bass': 'plucked_strings', 'subcontrabass-saxophone': 'woodwinds',
  'ophicleide': 'brass', 'baryton': 'bowed_strings', 'clavichord': 'keyboards',
  'cristal-baschet': 'bowed_strings', 'tenor-saxophone': 'woodwinds', 'french-horn': 'brass',
  'nyckelharpa': 'bowed_strings', 'bass-trombone': 'brass', 'cimbalom': 'metallic_idiophones',
  'duduk': 'woodwinds', 'cornet': 'brass', 'singing-saw': 'metallic_idiophones',
  'steel-tongue-drum': 'metallic_idiophones', 'contrabassoon': 'woodwinds', 'felt-piano': 'keyboards',
  'oboe-d-amore': 'woodwinds', 'mellotron': 'keyboards', 'flugelhorn': 'brass', 'tuba': 'brass',
  'harpsichord': 'keyboards', 'vibraphone': 'mallet_perc', 'viola': 'bowed_strings',
  'bass-clarinet': 'woodwinds', 'marimba': 'mallet_perc', 'glass-marimba': 'mallet_perc',
  'bowed-vibraphone': 'mallet_perc', 'double-bass': 'bowed_strings', 'waterphone': 'metallic_idiophones',
  'theremin': 'early_electronic', 'chalumeau': 'woodwinds', 'crotales': 'mallet_perc',
  'trumpet': 'brass', 'trombone': 'brass', 'piccolo': 'woodwinds', 'clarinet': 'woodwinds',
  'oboe': 'woodwinds', 'bandoneon': 'free_reed', 'shakuhachi': 'woodwinds', 'erhu': 'bowed_strings',
  'frame-drums': 'percussion', 'taiko': 'percussion', 'balafon': 'mallet_perc', 'kora': 'plucked_strings',
  'guqin': 'plucked_strings', 'sarangi': 'bowed_strings', 'nail-violin': 'metallic_idiophones',
  'steelpan': 'mallet_perc', 'mbira': 'metallic_idiophones', 'glass-harmonica': 'bowed_strings',
};

const KEY_RE = /^([a-g])(-flat|-sharp)?-(minor|major)$/;
const MAJOR_KEYS = ['c-major','c-sharp-major','d-flat-major','d-major','d-sharp-major','e-flat-major','e-major','f-major','f-sharp-major','g-flat-major','g-major','g-sharp-major','a-flat-major','a-major','a-sharp-major','b-flat-major','b-major'];
const MINOR_KEYS = ['c-minor','c-sharp-minor','d-flat-minor','d-minor','d-sharp-minor','e-flat-minor','e-minor','f-minor','f-sharp-minor','g-minor','g-sharp-minor','a-flat-minor','a-minor','a-sharp-minor','b-flat-minor','b-minor'];

function prettyKey(k) {
  const m = k.match(KEY_RE);
  if (!m) return k;
  const acc = m[2] === '-flat' ? '♭' : m[2] === '-sharp' ? '♯' : '';
  return `${m[1].toUpperCase()}${acc}${m[3] === 'minor' ? 'm' : ''}`;
}

function prettySlug(s) {
  return s.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
}

function classifyTechnique(t) {
  if (!t) return 'other';
  const s = t.toLowerCase();
  for (const r of FAMILY_RULES) {
    if (r.match.some(m => s.includes(m))) return r.fam;
  }
  return 'other';
}

function parseTags(g) {
  const tags = (g || []).map(t => String(t).toLowerCase());
  let technique = null, bpm = null, key = null;
  const instruments = [];
  for (const t of tags) {
    if (!technique && (t.endsWith('-technique-new') || t.startsWith('orchestral-'))) {
      technique = t.replace(/^orchestral-/, '').replace(/-technique-new$/, '');
    }
    if (!bpm) {
      const m = t.match(/^(\d{2,3})bpm$/);
      if (m) bpm = parseInt(m[1]);
    }
    if (!key && KEY_RE.test(t)) key = t;
    if (INSTRUMENT_VOCAB[t]) instruments.push(t);
  }
  return { technique, bpm, key, instruments };
}

async function load() {
  const songs = await fetch('songs.json').then(r => r.json());
  songs.sort((a, b) => (a.v || 0) - (b.v || 0));  // ascending for timeline
  const versions = songs.map(s => {
    const parsed = parseTags(s.g);
    return { ...s, parsed, family: classifyTechnique(parsed.technique) };
  });
  document.getElementById('totalVersions').textContent = versions.length;
  renderSnapshot(versions);
  renderTimeline(versions);
  renderFamilyBars(versions);
  renderInstruments(versions);
  renderBPMScatter(versions);
  renderKeyHeatmap(versions);
}

function renderSnapshot(versions) {
  const minV = versions[0].v, maxV = versions[versions.length - 1].v;
  const techniques = new Set(versions.map(v => v.parsed.technique).filter(Boolean));
  const instruments = new Set();
  versions.forEach(v => v.parsed.instruments.forEach(i => instruments.add(i)));
  const bpms = versions.map(v => v.parsed.bpm).filter(x => x != null);
  const meanBpm = bpms.length ? Math.round(bpms.reduce((a,b) => a+b, 0) / bpms.length) : '—';
  const keys = new Set(versions.map(v => v.parsed.key).filter(Boolean));
  const famCounts = {};
  versions.forEach(v => { famCounts[v.family] = (famCounts[v.family] || 0) + 1; });
  const topFam = Object.entries(famCounts).sort((a,b) => b[1] - a[1])[0];

  document.getElementById('snapshotStats').innerHTML = `
    <div class="stat"><div class="stat-label">Versions</div><div class="stat-value">${versions.length}</div><div class="stat-sub">v${minV} → v${maxV}</div></div>
    <div class="stat"><div class="stat-label">Unique techniques</div><div class="stat-value">${techniques.size}</div><div class="stat-sub">Top family: <strong style="color: ${FAMILY_INFO[topFam[0]].color}">${FAMILY_INFO[topFam[0]].label}</strong> (${topFam[1]})</div></div>
    <div class="stat"><div class="stat-label">Unique instruments</div><div class="stat-value">${instruments.size}</div><div class="stat-sub">tracked across catalog</div></div>
    <div class="stat"><div class="stat-label">Mean BPM</div><div class="stat-value">${meanBpm}</div><div class="stat-sub">${bpms.length} versions with BPM tag</div></div>
    <div class="stat"><div class="stat-label">Keys explored</div><div class="stat-value">${keys.size}<span style="color: var(--muted); font-size: 1rem; font-weight: 400;">/24</span></div><div class="stat-sub">of all major+minor pairs</div></div>
  `;
}

function renderTimeline(versions) {
  const svg = document.getElementById('timeline');
  const w = svg.clientWidth || 1100;
  const h = 70;
  svg.setAttribute('viewBox', `0 0 ${w} ${h}`);
  const n = versions.length;
  const barW = Math.max(1.5, w / n - 0.5);
  let html = '';
  versions.forEach((v, i) => {
    const x = i / n * w;
    const fill = FAMILY_INFO[v.family].color;
    const title = `v${v.v} · ${v.t || ''} · ${v.parsed.technique ? prettySlug(v.parsed.technique) : 'unclassified'}`;
    html += `<rect x="${x.toFixed(2)}" y="14" width="${barW.toFixed(2)}" height="42" fill="${fill}" opacity="0.85"><title>${title}</title></rect>`;
  });
  // axis labels
  html += `<text x="0" y="68" class="timeline-axis">v${versions[0].v}</text>`;
  html += `<text x="${w-1}" y="68" class="timeline-axis" text-anchor="end">v${versions[n-1].v}</text>`;
  svg.innerHTML = html;

  // Legend
  const legend = document.getElementById('famLegend');
  legend.innerHTML = Object.entries(FAMILY_INFO).map(([k, v]) =>
    `<span class="legend-item"><span class="legend-swatch" style="background:${v.color}"></span>${v.label}</span>`
  ).join('');
}

function renderFamilyBars(versions) {
  const counts = {};
  versions.forEach(v => { counts[v.family] = (counts[v.family] || 0) + 1; });
  const total = versions.length;
  const order = ['formal', 'narrative', 'harmonic', 'rhythmic', 'textural', 'other'];
  const max = Math.max(...Object.values(counts));
  const html = order.map(fam => {
    const c = counts[fam] || 0;
    const pct = max ? (c / max * 100).toFixed(1) : 0;
    const pctOfTotal = (c / total * 100).toFixed(0);
    return `
      <div class="fam-bar-row">
        <div class="fam-bar-label">${FAMILY_INFO[fam].label}</div>
        <div class="fam-bar-track"><div class="fam-bar-fill" style="width: ${pct}%; background: ${FAMILY_INFO[fam].color};"></div></div>
        <div class="fam-bar-count">${c} <span style="color: var(--muted-2)">(${pctOfTotal}%)</span></div>
      </div>
    `;
  }).join('');
  document.getElementById('famBars').innerHTML = html;
}

function renderInstruments(versions) {
  const maxV = Math.max(...versions.map(v => v.v));
  const usage = new Map();  // name -> {count, lastV}
  versions.forEach(v => {
    v.parsed.instruments.forEach(inst => {
      const prev = usage.get(inst) || { count: 0, lastV: 0 };
      usage.set(inst, { count: prev.count + 1, lastV: Math.max(prev.lastV, v.v) });
    });
  });
  const rows = [...usage.entries()].map(([name, info]) => ({
    name, family: INSTRUMENT_VOCAB[name] || 'other',
    count: info.count, lastV: info.lastV, gap: maxV - info.lastV
  })).sort((a, b) => b.count - a.count || b.gap - a.gap);

  // Show top 30
  const html = rows.slice(0, 30).map(r => {
    let gapClass = '';
    if (r.gap >= 25) gapClass = 'gap-very-deep';
    else if (r.gap >= 15) gapClass = 'gap-deep';
    return `<tr>
      <td><span class="inst-name">${prettySlug(r.name)}</span></td>
      <td><span class="inst-family">${r.family}</span></td>
      <td class="num">${r.count}</td>
      <td class="num">v${r.lastV}</td>
      <td class="num ${gapClass}">${r.gap}</td>
    </tr>`;
  }).join('');
  document.getElementById('instTable').innerHTML = html;
}

function renderBPMScatter(versions) {
  const svg = document.getElementById('bpmScatter');
  const W = svg.clientWidth || 1100;
  const H = 320;
  const padL = 50, padR = 16, padT = 14, padB = 36;
  svg.setAttribute('viewBox', `0 0 ${W} ${H}`);

  const data = versions.map(v => ({ x: v.v, y: v.parsed.bpm })).filter(d => d.y != null);
  if (!data.length) { svg.innerHTML = ''; return; }
  const xMin = Math.min(...data.map(d => d.x));
  const xMax = Math.max(...data.map(d => d.x));
  const yMin = Math.min(60, Math.min(...data.map(d => d.y)));
  const yMax = Math.max(200, Math.max(...data.map(d => d.y)));
  const sx = x => padL + (x - xMin) / (xMax - xMin || 1) * (W - padL - padR);
  const sy = y => padT + (1 - (y - yMin) / (yMax - yMin || 1)) * (H - padT - padB);

  let html = '';
  // grid lines (horizontal: every 20 BPM)
  for (let y = 60; y <= 200; y += 20) {
    const py = sy(y);
    html += `<line class="scatter-grid" x1="${padL}" y1="${py}" x2="${W - padR}" y2="${py}"/>`;
    html += `<text class="scatter-axis-label" x="${padL - 6}" y="${py + 4}" text-anchor="end">${y}</text>`;
  }
  // x axis
  html += `<line class="scatter-grid" x1="${padL}" y1="${H - padB}" x2="${W - padR}" y2="${H - padB}"/>`;
  // x ticks every ~25 versions
  const step = Math.max(20, Math.round((xMax - xMin) / 8));
  for (let v = Math.ceil(xMin / step) * step; v <= xMax; v += step) {
    const px = sx(v);
    html += `<text class="scatter-axis-label" x="${px}" y="${H - padB + 18}" text-anchor="middle">v${v}</text>`;
  }
  // dots
  data.forEach(d => {
    html += `<circle class="scatter-dot" cx="${sx(d.x).toFixed(1)}" cy="${sy(d.y).toFixed(1)}" r="3"><title>v${d.x}: ${d.y} BPM</title></circle>`;
  });
  // y axis label
  html += `<text class="scatter-axis-label" x="${padL - 38}" y="${H/2}" text-anchor="middle" transform="rotate(-90 ${padL - 38} ${H/2})">BPM</text>`;
  svg.innerHTML = html;
}

function renderKeyHeatmap(versions) {
  const counts = new Map();
  versions.forEach(v => { if (v.parsed.key) counts.set(v.parsed.key, (counts.get(v.parsed.key) || 0) + 1); });
  const max = Math.max(...counts.values(), 1);
  const renderRow = (keys, target) => {
    const html = keys.map(k => {
      const c = counts.get(k) || 0;
      const alpha = c / max;
      const bg = c > 0 ? `rgba(255, 106, 61, ${0.15 + 0.65 * alpha})` : 'var(--bg-soft)';
      const cls = c === 0 ? 'count-0' : '';
      return `<div class="key-cell ${cls}" style="background: ${bg};">${prettyKey(k)}<span class="count">${c}</span></div>`;
    }).join('');
    document.getElementById(target).innerHTML = html;
  };
  renderRow(MAJOR_KEYS, 'majorKeys');
  renderRow(MINOR_KEYS, 'minorKeys');
}

load();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    main()
