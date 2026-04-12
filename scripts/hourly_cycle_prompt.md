# Hourly autonomous cycle prompt

**Marker:** This is the scheduled hourly Suno cycle. You are running unattended — no user in chat. Apply `feedback_cron_auto_submit_override.md`: auto-submit authorized, but all safety floors (judge ≥90, fresh novelty_surface, no blocklist words, commit + push) still apply.

## Your task

Run one full autonomous cycle in `/Users/adan/work/claude/code/suno`:

1. **Orient** — read `MEMORY.md`, `experiments/evolution.md`, and `git log --oneline -5` to know the current state. Identify the latest version number from `ls prompts/ | grep -oE 'v[0-9]+' | sort -V | tail -1`. Next version = latest + 1.

2. **Refresh the novelty surface** — run `python3 scripts/novelty_surface.py`. This regenerates `experiments/novelty_surface.json` with the current used-instruments/keys/BPMs/genres from every prompt YAML.

3. **Research ONE topic** (mandatory — never skip):
   - Rotate through: (a) new unusual instruments, (b) new genre fusions, (c) 2026 Suno prompt techniques, (d) film scoring trends, (e) Baroque/Classical architectural forms not yet tried.
   - Use `WebSearch` with a specific query. One search is enough. Pull one concrete new idea.

4. **Draft the next version** in `prompts/[title-slug]-v[N].yaml`. Required elements:
   - Genre anchor (2 words max, "NEOCLASSICAL FILM SCORE" style)
   - **Purpose phrase** ("for a X scene", "underscore for Y")
   - **3-instrument featured trio** in ALL CAPS after "with" — check `experiments/novelty_surface.json` to ensure at least one is genuinely new (zero prior uses) or a deep revival (>15 versions old)
   - **Target duration: 1–2 minutes, not longer.** Every new prompt must explicitly say "total duration 1:00 to 2:00" (or "60–120 seconds" / "one-to-two-minute film cue") early in the style field. All timestamps must fit under 2:00. The whole arc (entry → build → silence → return → end) compresses into ≤2 minutes, with 0:60 being the floor target. See the short-form arc template below.
   - **Explicit timestamps** — at least 3 time anchors *within 0:00–2:00* (e.g., 0:00 / 0:20 / 0:45 / silence at 1:10 / return at 1:15 / end at 1:50)
   - Key with half-step modulation (e.g., "D minor to Eb minor")
   - BPM
   - Silence-before-climax + return, compressed — silence is 2–4 beats, not 6–8
   - 4+ inline "no X" negatives + comprehensive `exclude_styles`
   - Conversational flowing prose, 850-950 chars
   - Detailed `notes` field explaining what was researched, what was learned, what's novel
   - Accurate `tags` field

### Short-form arc template (1–2 minutes)

Choose whichever fits the concept better — tight 1-minute miniature or longer 2-minute cue — but **never exceed 2:00**.

**1-minute miniature:**
```
0:00 — first featured instrument enters alone (12 seconds)
0:12 — second instrument joins, texture thickens
0:28 — third instrument rises, orchestra blooms
0:42 — peak density
0:45 — silence (2–3 seconds)
0:48 — return half-step up, fortississimo
0:58 — end
```

**2-minute cue:**
```
0:00 — first featured instrument enters alone (20 seconds)
0:20 — second instrument joins
0:45 — third instrument rises, orchestra blooms through the middle
1:20 — peak density
1:25 — silence (3–5 seconds)
1:30 — return half-step up, fortississimo
1:50 — end
```

Each timestamp is a hint, you can shift ±5 seconds per section. **What matters is total duration 1:00–2:00, never longer.**

5. **Judge** via `/judge prompts/[file].yaml`. Must score ≥90 on the 12-criterion rubric. Iterate up to 5 times if below. If still <90 after 5 iterations, **abort this cycle** — log to `experiments/cron_failures.md` with the score table and the reason, and exit without submitting.

6. **Submit** via `/suno prompts/[file].yaml`. This loads browser tools and fills the Suno UI in Advanced mode, clicks Create. If the browser is disconnected or Suno is unreachable, **abort the cycle** — log to `experiments/cron_failures.md` and exit. Never auto-retry submissions.

7. **Rebuild site**: `python3 scripts/build_site.py`

8. **Update evolution.md + results-tracker.md** — append a new cycle-log entry with what was tried, why, what was learned. Move any newly-applied technique from "next-cycle priorities" to "cycle technique register".

9. **Commit + push**: add the new prompt YAML + docs/songs.json + experiments/*.md + experiments/novelty_surface.json. Commit message format: `Add v### [genre] with [instruments]`. Push to origin main.

10. **Final sanity check**: if any prior step failed silently (empty commit, push rejected, build script error), log to `experiments/cron_failures.md`.

## Failure log format

Append to `experiments/cron_failures.md` (create if missing):

```
## YYYY-MM-DD HH:MM — v### failed at [step]

Reason: [concise description]
State: [what was left behind — draft file path, partial commits, etc.]
Action taken: [skipped submission / aborted cycle / etc.]
Next cycle should: [cleanup instructions]
```

## What NOT to do

- Don't skip research — every cycle must actually call WebSearch
- Don't use trigger words from the blocklist ("Dune", "epic", "massive", artist names, "frisson")
- Don't submit below judge ≥90
- Don't repeat the same featured-instrument trio as the last 5 versions
- Don't use pipe organ as a featured instrument (×50 overexposed) — demote to backdrop if needed
- Don't `git add -A` or `git add .` — always add specific files
- Don't skip `commit + push` — nothing is finished until it's pushed
- Don't generate the prompt from memory alone — always refresh novelty_surface and read at least 3 recent prompts first
