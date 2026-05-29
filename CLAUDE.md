# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> ## ⚠ TOP-PRIORITY CONTRACT — READ FIRST
> **No vanilla / one-off bash or `python3 -c` for ANY recurring cycle step. The user does not approve it.**
> If a step is deterministic and recurs, it belongs in a committed reusable script under `scripts/` (write one if missing). This includes labelled diagnostic compounds (`echo "—status—"; git status …`, `ls | grep | sort`, chained `&&` shell pipelines for inspection, `python3 -c "import json; …"`). The full rule is below under "Scripting discipline (contract — non-negotiable)" — every cycle step MUST satisfy it.

## Project Overview

This is a **Suno AI music generation prompt engineering workspace**. The goal is to craft, iterate on, and execute Suno prompts via browser automation (Claude-in-Chrome) against `suno.com/create`.

Suno generates complete songs (vocals + instruments + lyrics) from text prompts in under 60 seconds. Current model is **v5.5** (March 2026).

## Suno Prompt Anatomy

We use **Custom Mode** exclusively at `suno.com/create`. Fields:

| Field | Limit | Purpose |
|-------|-------|---------|
| **Style** | 1,000 chars | Genre, mood, tempo, instruments, vocal style |
| **Lyrics** | 1,000 chars | Exact lyrics with structural metatags |
| **Title** | 100 chars | Song name |
| **Instrumental** | toggle | Remove vocals |

**Style prompt approach:** v5.5 prefers conversational flowing descriptions over comma-separated tags. Write sentences, not lists: "Sublime neoclassical orchestral vocalise with monumental cinematic grandeur..." not "neoclassical, orchestral, sublime, cinematic." Aim for 850-950 chars to leave room for negative prompts and key/BPM at the end.

### Metatags (embedded in lyrics)

Structural: `[Intro]`, `[Verse]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Post-Chorus]`, `[Bridge]`, `[Hook]`, `[Interlude]`, `[Break]`, `[Outro]`, `[End]`, `[Fade Out]`, `[Big Finish]`, `[Short Instrumental Intro]`

Performance: `[Whispered]`, `[Spoken Word]`, `[Belted]`, `[Male singer]`, `[Harmonized chorus]`

Instrument/FX: `[Acoustic guitar]`, `[Synth pads]`, `[Jazz saxophone solo]`, `[Silence]`, `[Applause]`

Ad-libs use parentheses inline: `(oh yeah)`, `(hey!)`

### Prompt Best Practices
- Front-load style with genre and mood (survives truncation)
- Write descriptions, not commands: "Upbeat pop track with..." not "Create an upbeat..."
- No artist names — use genre/era descriptors instead
- Use negative prompts: "no autotune", "no heavy bass"
- Keep lyrics 8-12 lines per generation to avoid timing errors
- Use `[End]` as standalone section to signal endings
- BPM and timestamps work: "120 BPM", "lyrics begin at 0:15"
- Expect 8-15 iterations to nail a prompt — small changes matter
- v5.5 prefers conversational style descriptions over comma-separated tags
- **Silence before climax** is the #1 frisson trigger — build to 80%, drop to near-silence, then deliver climax that exceeds expectations (use `[Silence]` metatag)
- **Key modulation** at climax: half-step up (e.g., D Major → Eb Major) after silence = goosebump multiplier
- **Glass harmonica** creates spatial disorientation (1-4 kHz, brain can't locate sound) — more ethereal than crystal bowls
- **Three-layer instrument control**: genre anchor + specify instruments + negative prompts (+ Exclude styles field)
- Avoid words that trigger wrong genres: "Dune"/"desert" triggers Arabic, "epic"/"massive" triggers rock/drums
- Always verify style is under 1000 chars BEFORE submitting — count characters, don't estimate

## Browser Automation

Songs are generated via Chrome automation at `suno.com/create`. The UI flow:

1. Navigate to `suno.com/create`
2. Select **Advanced** tab (top-left) — this is Custom mode
3. Fill **Lyrics** and **Style** fields
4. Expand **More Options** → set Exclude styles, Vocal Gender
5. Fill **Song Title (Optional)** field (below More Options)
6. Click **Create** → generates 2 versions
7. Listen, then optionally Extend/Edit/Crop/Replace

Key URLs:
- Create: `suno.com/create`
- Song: `suno.com/song/{UUID}`

## Skill: `/suno`

Run `/suno` (or `/suno prompts/some-file.yaml`) to submit a prompt to Suno via Chrome browser automation. The skill reads the YAML file, navigates to `suno.com/create`, fills Custom mode fields, and clicks Create.

All prompt content comes from the user — the skill never generates or modifies prompts on its own.

## Project Structure

```
.claude/skills/suno/  # /suno skill for browser automation
prompts/              # Saved prompt experiments (YAML files)
experiments/          # Logs and notes from generation sessions
scripts/              # Helper scripts for prompt generation
```

## Autonomous Hourly Cycle

The project runs an autonomous hourly generation cycle. Each cycle:

1. **Research** — WebSearch for one rotating topic (new instruments, genre fusions, frisson techniques, film scoring trends)
2. **Create** — Write a new YAML prompt that evolves from recent versions with one meaningful change
3. **Submit** — Use `/suno` or browser automation to submit to Suno at `suno.com/create`
4. **Save** — Rebuild website (`python3 scripts/build_site.py`), commit, and push to git

### After each cycle, always:
Run the reusable close-out script — do **not** hand-type the steps:
- `python3 scripts/finish_cycle.py --version <N> --clips <uuid1> <uuid2> [--technique ... --key ... --bpm ... --trio ...]`
  - It registers clip UUIDs in `docs/suno_urls.json`, appends the `evolution.md` row, rebuilds the site (`build_site.py`), stages only the cycle's files (never `git add -A`), commits, and pushes.

### Scripting discipline (contract — non-negotiable)
- **No vanilla / one-off script execution. The user does not approve it — full stop.** Do not run ad-hoc inline `bash` (incl. `ls | grep | sort`, `echo` labels, heredocs, chained `&&` pipelines for inspection) or `python3 -c "..."` snippets to perform ANY deterministic, recurring cycle step. This explicitly includes: **computing the next version number**, refreshing the novelty surface, registering URLs, building the site, logging, committing/pushing, inspecting prompt/JSON/YAML state, AND **deciding draft-vs-resume** (whether the latest YAML is uncommitted).
- Every deterministic, repeatable step MUST live in a **reusable, parametrized script** under `scripts/` and be invoked as `python3 scripts/<name>.py …`. Current entrypoints:
  - `scripts/cycle_start.py` — computes the latest/next version from `prompts/`, refreshes `experiments/novelty_surface.json`, AND emits `recommended_action ∈ {"resume_submit","draft_new"}` + `recommended_version` so the orchestrator never needs `git status`/`ls` to decide. Use this instead of any shell composition.
  - `scripts/novelty_surface.py` — regenerates the novelty surface.
  - `scripts/finish_cycle.py` — full save+publish close-out (URLs, evolution row, build, stage, commit, push).
  - `scripts/build_site.py` — rebuilds `docs/`.
- If a needed deterministic step has **no script yet, WRITE one** (parametrized, reusable, committed via the next `finish_cycle.py`) and run that — never improvise a one-off, even "just this once."
- The ONLY acceptable raw `bash` is a **single, uncomposed, throwaway** diagnostic that no script could sensibly own (e.g. `ps aux | grep …` while debugging a stuck process, a bare `git status` to confirm the working tree). Composing it with `echo` labels, chaining via `&&` with other inspections, or wrapping it in a shell prologue is the violation.

#### BANNED — explicit examples (these are vanilla cycle work; do not run them)
- `ls prompts/ | grep -oE 'v[0-9]+' | sort -V | tail -1`
- `echo "=== next version ==="; python3 scripts/cycle_start.py; echo "=== untracked ==="; git status --short prompts/`
- `python3 -c "import json; d=json.load(open('docs/suno_urls.json')); print(len(d))"`
- `python3 scripts/cycle_start.py && git status --short prompts/`
- `cat prompts/*-v230.yaml | grep -E '^(style|title|instrumental):'`
- any compound shell that *both* runs a script AND adds an `echo`/`git status`/`ls` for context

#### ALLOWED — these are the only safe shell patterns
- `python3 scripts/cycle_start.py` (the script alone)
- `python3 scripts/finish_cycle.py --version N --clips A B …`
- a bare `git status` or `ps aux | grep <pid>` (single, uncomposed, debugging-only)
- `kill <pid>` (single, uncomposed, debugging a stuck process)

#### When in doubt
Default to writing a new script and running that. The user has repeated this rule multiple times; the failure mode is *always* "I added one little `echo`/`git status` to get context" — that "one little thing" is the violation. If a piece of state is worth observing routinely, it goes in a script.

### Current era: Synthesis (v93+)
Combining electronic genres (dubstep, trance, trap, prog house, breakbeat, psytrance) with full orchestra + unusual instruments (waterphone, glass harmonica, taiko, prepared piano, handpan, contrabass clarinet, cimbalom, pipe organ). Always instrumental. Key frisson triggers: silence-before-climax, half-step modulation, Shepard tones.

## Prompt File Format

Prompts are stored as YAML in `prompts/`:

```yaml
name: "song-name"
version: 1
style: "genre, mood, instruments..."         # Max 1000 chars — aim for 850-950
title: "Song Title"
lyrics: |
  [Intro]
  ...
  [Verse 1]
  ...
  [Chorus]
  ...
  [End]
instrumental: false
vocal_gender: female                          # Optional: "female" or "male"
exclude_styles: "Arabic, rock, electronic"    # Optional: reinforces negative prompts
notes: "What we're testing with this prompt"
tags: [genre, experiment-name]
```
