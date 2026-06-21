---
name: judge
description: Critically evaluate a Suno prompt YAML for genuine musical quality, score 0-100 on a demanding curve, iterate toward the bar
---

# Judge — Critically Evaluate a Suno Prompt

Score a prompt for whether it is genuinely *good music people would replay and share* — not whether it followed the template. Be hard. Most competent prompts deserve a 75, not a 98.

## Arguments

`/judge <path-to-yaml-prompt-file>` — if no file given, read the most recently modified YAML in `prompts/`.

## How scoring works — read this first

Scoring is **two stages**: a compliance **GATE** (pass/fail, earns zero points) and a **QUALITY score** (0–100, demanding curve). A prompt that passes every gate but is musically ordinary is a **75, not a 98**. Format compliance is the price of entry, not a source of points.

### Calibration anchors (apply these honestly — do NOT grade-inflate)

| Band | Meaning | How often it should happen |
|------|---------|----------------------------|
| **93–100** | Genuinely track-of-the-year caliber. A hook you can't shake, a distinct identity vs. all ~358 prior songs, fearless production. | Rare — a few per dozen cycles. |
| **85–92** | Strong, confident, clearly above the catalog average. Ships in a normal era. | Occasional. |
| **75–84** | Competent and on-formula. Hits the proven template, nothing wrong, nothing unforgettable. | **This is the default. Most drafts land here.** |
| **60–74** | A real weakness: generic hook, retread concept, decorative instruments, or a formulaic arc. | Common on first pass. |
| **<60** | Fails a gate, or is derivative/forgettable. | — |

If you find yourself scoring most candidates 95+, you are being too lenient. Re-read this table and push them down to where they belong.

## Stage 1 — Compliance GATE (binary; earns no points)

Every item must pass. Any failure → **cap the score at 60** and fix it before quality scoring can matter. These are necessary, never sufficient.

- Style 850–950 chars (verify via `python3 scripts/text_tools.py`); lyrics <1000 chars
- Title: exactly ONE word, English or French
- Lyrics: English or French only
- Key + BPM both stated, with a half-step (or comparable) modulation at the climax
- ≥3 inline "No X" negatives in style + a populated `exclude_styles`
- Blocklist clean (see list below) — in the `style` and `lyrics` fields
- ≥3 timestamps; a purpose phrase ("underscore for Y"); conversational prose, not a tag list
- Duration levers present: an explicit lyric-free mid-song vamp/break (~30–50s) AND last lyric ≥ ~2:40
- No `[Silence]` metatag (it truncates)

Report the gate as PASS/FAIL with the one-line reason for any failure. Fix gate failures first in iteration.

## Stage 2 — QUALITY score (0–100). These are HARD. Score each on its sub-scale, then sum.

| # | Dimension | Max | What a top score demands (and what caps it low) |
|---|-----------|-----|--------------------------------------------------|
| 1 | **Hook strength & memorability** | 25 | A specific, singable/recognizable hook that earns a replay. Generic chant ("take it to the floor", "I don't stop") caps at **12**. A hook with a real melodic or rhythmic signature you could identify in 3 seconds → 20+. Be honest: most lyric hooks here are filler — score them 10–14. |
| 2 | **Distinctiveness vs. the WHOLE catalog** | 20 | Not "different from the last 3" — different from all ~358. Another competent entry in an already-shipped lane (melodic-techno build-drop, disco-house key-change, dark-techno) caps at **11** no matter how clean. A genuinely fresh genre/structure/identity → 16+. A debut genre or a real structural novelty earns the top. |
| 3 | **Production ambition & cohesion** | 15 | The instrument trio must *do real work* — carry the hook, define the texture, change the section. If the trio is decoration bolted onto a generic groove (named in the style but not structurally load-bearing) cap at **7**. Generic production tokens ("polished studio mix, wide stereo") earn nothing on their own. |
| 4 | **Danceability conviction** | 15 | Honestly: how hard does this move *our* beat-driven/edgy audience? A mid-tempo or warmth-softened groove caps at **9**. Only a genuinely floor-filling, physical groove earns 13+. |
| 5 | **Emotional / narrative payload** | 15 | Do the lyrics + scene land a real feeling, or are they competent filler? Placeholder verses ("every step I take alone") cap at **7**. A genuine, specific emotional arc → 12+. |
| 6 | **Frisson execution & freshness of device** | 10 | The climax must be effective AND not formulaic. The "build → strip to kick → half-step lift → drop" arc is now used by *every* candidate — when you see it, it is FORMULAIC: cap this dimension at **5**. A genuinely different or unusually well-built climax earns 8+. |

**Final score = sum of the six (0–100)**, then apply the gate cap (≤60 if any gate failed).

### Anti-convergence rule (critical)
The tournament has collapsed onto one template: minor-key dance track, three "revival" instruments named in the style, build to ~1:30, strip to a bare element, half-step modulation, drop, late final lyric. **This template is the baseline, not an achievement.** A prompt that only executes the template competently is a **75**. Points above that must be *earned* by a hook, an identity, or a device that breaks the pattern. Reward divergence; penalize convergence.

## Jargon Blocklist (gate item)

**Trigger words (wrong genre):** "Dune"/"desert"/"sand"/"oasis" → Arabic; "epic"/"massive"/"explosion" → rock/drums; "wall of sound"/"metal"/"heavy" → rock; "frisson" → not a prompt term.
**Unverified jargon:** "appoggiatura", "Shepard tone", "melisma", "voix celeste"; any composer/artist name; reference-based descriptions ("Evanescence-like") — describe the sound, not the reference.

## Process

1. Refresh novelty surface: `python3 scripts/novelty_surface.py` if stale.
2. Read the target YAML; read enough prior prompts (not just the last 3 — sample across the catalog) to judge dimension 2 honestly.
3. Run the **gate**. Note failures.
4. Score the **six quality dimensions** against the demanding sub-scales. Apply the calibration table and the anti-convergence rule. Do not inflate.
5. If below the caller's bar (`hard_floor`, default 90): fix gate failures and the lowest-scoring *fixable* dimensions. Note: dimensions 1/2/6 usually CANNOT be fixed by editing the style — a formulaic concept stays formulaic. Say so rather than nudging the number up.
6. Cap at 5 iterations. If still below the bar, **STALLED** — return best honest score. Do NOT inflate to clear the bar.

## Output Format

```
## Judge Report: <title> v<version>
Final score: XX/100 | Iteration: N/5 | Gate: PASS/FAIL | Verdict: PASS | ITERATE | STALLED

Gate: <PASS, or the failing item(s)>

| # | Dimension | Score | Notes (be specific and critical) |
|---|-----------|-------|------|
| 1 | Hook strength & memorability | X/25 | … |
| 2 | Distinctiveness vs. catalog | X/20 | … |
| 3 | Production ambition & cohesion | X/15 | … |
| 4 | Danceability conviction | X/15 | … |
| 5 | Emotional / narrative payload | X/15 | … |
| 6 | Frisson execution & freshness | X/10 | … |

### Where it loses points
- [the honest, specific reasons — name the formula if it's formulaic]

### Verdict: PASS / ITERATE / STALLED
```

Then a JSON footer for the orchestrator:

```
{"status": "pass"|"iterate"|"stalled", "score": <int>, "danceability": <1-10>, "gate": "pass"|"fail", "iterations": <int>, "file_path": "<path>", "title": "<from yaml>", "blocklist_hits": [<strings>], "title_change_suggested": "<string or null>"}
```

## Integration

`/suno` runs `/judge` before submitting. The cron tournament judges every candidate and ships only the highest honest score that clears the bar. With this rubric most candidates land 70–85; clearing a >95 bar should be genuinely rare and meaningful.
