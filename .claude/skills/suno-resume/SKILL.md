---
name: suno-resume
description: Fast-resume the Suno song-generation project after a restart — reload project status (latest/next version, recommended action, novelty surface) and recent cycle history in ONE shot, no manual digging. Run this first thing in a fresh session.
---

# Suno — Resume Project

One-shot reload of the autonomous Suno song-generation project state so a fresh session can pick up exactly where the last one left off. Do NOT hand-type the steps — invoke the reusable scripts.

## What this does

1. **Load status** — run `python3 scripts/cycle_start.py`. This is the single source of truth: it computes `last_version` / `next_version`, refreshes `experiments/novelty_surface.json`, and emits `recommended_action ∈ {"resume_submit","draft_new"}` + `recommended_version`. Never use `git status` / `ls` to decide draft-vs-resume — this script already decides.

2. **Recent cycle history** — read the last few `git log` commit subjects (each cycle's commit summarizes the winner, hook, judge score, danceability, render durations, and trio). This reconstructs the last several cycles without a transcript.

3. **Recent learnings** — glance at the tail of `experiments/evolution.md` for the current short-duration watch / open probes, and the Memory index (`MEMORY.md`) feedback entries already in context.

## Steps

Run these two, then summarize:

```
python3 scripts/cycle_start.py
git log --oneline -8
```

(A bare `git log` is the ONE allowed uncomposed diagnostic. Do not chain it with `echo`/`ls`/`&&` — that violates the scripting-discipline contract in CLAUDE.md. If you want richer recent-cycle context, read `experiments/evolution.md` with the Read tool, not shell.)

## Output

Present a concise status block to the user:

- **Latest committed version** and **next version**
- **Recommended action** (`draft_new` → start a fresh MoA tournament at `recommended_version`; `resume_submit` → the latest YAML is uncommitted, finish submitting it)
- **Last 3-ish cycles**: winner genre, hook, judge score, danceability, render durations
- **Active learnings / open probes** worth carrying into this cycle
- Offer to run the next cycle (research → hook-first MoA tournament → judge → submit → publish → `finish_cycle.py`) or stand by.

## Notes

- The project era is **charts-informed viral (v324+)** using a **Hook-first MoA tournament** (draft N candidates from distinct viral lanes → critical-judge each → submit only the winner).
- Hard rules every cycle: one-word title; lyrics English or French only; publish both clips publicly; original work only.
- If Suno crons are session-only, re-register them from `scripts/cron_setup.md` (see the `reschedule-crons-on-restart` memory).
