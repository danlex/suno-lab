# Hourly autonomous cycle prompt

**Marker:** This is the scheduled hourly Suno cycle. You are running unattended — no user in chat. Apply `feedback_cron_auto_submit_override.md`: auto-submit authorized, but all safety floors (judge ≥90, fresh novelty_surface, no blocklist words, commit + push) still apply.

## Your task

Run one full autonomous cycle in `/Users/adan/work/claude/code/suno`:

1. **Orient + bootstrap (single reusable command — do NOT hand-run `ls`/`grep`/`echo`):** run
   ```
   python3 scripts/cycle_start.py
   ```
   It prints JSON `{"last_version", "next_version", "prompt_count", "novelty_refreshed"}` AND refreshes `experiments/novelty_surface.json`. Use `next_version` as N — never compute the version with inline bash (CLAUDE.md "Scripting discipline"). Then read `MEMORY.md` and `experiments/evolution.md` (via the Read tool) for current state.

2. **Novelty surface is already refreshed by step 1** (`cycle_start.py` runs `novelty_surface.py` for you unless you pass `--no-novelty`). Consult `experiments/novelty_surface.json` for used instruments/keys/BPMs/genres before drafting.

3. **Research ONE topic** (mandatory — never skip):
   - Rotate through: (a) new unusual instruments, (b) new genre fusions, (c) 2026 Suno prompt techniques, (d) film scoring trends, (e) Baroque/Classical architectural forms not yet tried.
   - Use `WebSearch` with a specific query. One search is enough. Pull one concrete new idea.

4. **Draft the next version** in `prompts/[title-slug]-v[N].yaml`. Required elements:
   - Genre anchor (2 words max, "NEOCLASSICAL FILM SCORE" style)
   - **Purpose phrase** ("for a X scene", "underscore for Y")
   - **3-instrument featured trio** in ALL CAPS after "with" — check `experiments/novelty_surface.json` to ensure at least one is genuinely new (zero prior uses) or a deep revival (>15 versions old)
   - **Target duration: ~3 minutes (2:30–3:30).** Updated 2026-04-13 after the 1–2 min cap was lifted. Every new prompt must explicitly say "total duration around 3:00" (or "2:30 to 3:30 film cue" / "three-minute miniature") early in the style field. All timestamps must fit within 0:00–3:00. Entry → build → silence → return → end gets a full three-minute arc. See the 3-min template below.
   - **Explicit timestamps** — at least 4 time anchors *within 0:00–3:00* (e.g., 0:00 / 0:25 / 1:00 / 2:00 / silence at 2:10 / return at 2:15 / end at 2:50)
   - Key + BPM (BPM should be fresh — check `experiments/novelty_surface.json` bpms)
   - **Arc shape: pick a fresh one. Do NOT reflexively use silence-before-climax + half-step-up return.** That skeleton was overused v216–v219 and the judge now docks concept-novelty for it. Recent fresh arcs: perpetuum mobile / flat kinetic tension (v220), accelerando-to-collapse (v221), additive accretion to saturation (v222). Still untried: arch (ABCBA), climax-at-the-front. Half-step modulation is now OPTIONAL, not mandatory — choose the harmonic device that fits the concept (stable key, parallel-major lift, etc.). The silence+half-step template below is ONE option, not the default. See evolution.md "next-cycle priorities".
   - 4+ inline "no X" negatives + comprehensive `exclude_styles`
   - Conversational flowing prose, 850-950 chars
   - Detailed `notes` field explaining what was researched, what was learned, what's novel
   - Accurate `tags` field

### 3-minute arc template (2:30–3:30)

Updated 2026-04-13. Target ~3:00. Timestamps can shift ±10 seconds per section.

**3-minute cue (default):**
```
0:00 — first featured instrument enters alone (25 seconds)
0:25 — second instrument joins, texture thickens
1:00 — third instrument rises, orchestra blooms through the middle
2:00 — peak density
2:10 — silence (4–6 seconds)
2:15 — return half-step up, fortississimo
2:50 — end
```

**2:30 compact variant (for denser concepts):**
```
0:00 — first featured instrument alone (20 seconds)
0:20 — second instrument joins
0:50 — third instrument rises
1:40 — peak density
1:50 — silence (4 seconds)
1:55 — return half-step up
2:25 — end
```

**What matters:** total duration 2:30–3:30, with a real silence + return built in. Don't over-compress; the extra minute is for development, not padding.

5. **Judge** via `/judge prompts/[file].yaml`. Must score ≥90 on the 12-criterion rubric. Iterate up to 5 times if below. If still <90 after 5 iterations, **abort this cycle** — log to `experiments/cron_failures.md` with the score table and the reason, and exit without submitting.

6. **Submit** via `/suno prompts/[file].yaml`. This loads browser tools and fills the Suno UI in Advanced mode, clicks Create. If the browser is disconnected or Suno is unreachable, **abort the cycle** — log to `experiments/cron_failures.md` and exit. Never auto-retry submissions.

6b. **Publish the new song on Suno (PRE-AUTHORIZED — never ask the user).** After Create succeeds and you have the first clip UUID, make it public so it appears on the public profile. Flow (coordinates are for a ~1568-wide viewport; re-read from a screenshot if the viewport differs):
   - Navigate to `suno.com/song/{first_uuid}` and wait ~3s (loads scrolled to top).
   - Screenshot. The action-row "..." (More) button is at x≈565; its Y varies with description length (~440–485). Read the actual Y.
   - Click "...". The dropdown opens at a FIXED position regardless of button Y.
   - **Safety:** if the menu shows "Unpublish" the song is already public — press Escape and skip. If it shows "Publish", continue.
   - Click "Publish" (≈488,426). A "Publish Song" dialog opens (~2s). Confirm it's present.
   - Click the dialog's "Publish" button (≈987,645). Wait ~3s; dialog closes = published.
   - If publishing fails (disconnect/dialog never appears after 2 tries), log to `cron_failures.md` with step="publish" but DO NOT abort — continue to build/commit/push (the song is still created; publish can be retried later). Publishing newly-created songs is part of the autonomous workflow per `feedback_cron_auto_submit_override.md` — do not pause for approval.

7. **Save + publish (single reusable command — do NOT hand-run build/commit/push):**
   ```
   python3 scripts/finish_cycle.py --version N \
       --clips <UUID1> <UUID2> \
       --technique "<short arc/technique label>" \
       --key "<key>" --bpm <bpm> \
       --trio "<inst1> + <inst2> + <inst3>"
   ```
   This registers the clip UUIDs in `docs/suno_urls.json` (the site's embedded
   players — the step that was silently skipped for v220/v221), appends the
   `evolution.md` tracker row, runs `build_site.py`, stages ONLY the cycle files
   (never `git add -A`), commits (`Add v### ...`), and pushes to origin main.
   It is the single entrypoint so the publish step is never missed again.

8. **Narrative learning (optional)** — if the cycle produced a real insight,
   add a sentence to evolution.md "next-cycle priorities" (the table row is
   already handled by finish_cycle.py).

9. **Final sanity check**: if any prior step failed silently (empty commit, push
   rejected, build error, missing suno_urls entry), log to
   `experiments/cron_failures.md`.

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
