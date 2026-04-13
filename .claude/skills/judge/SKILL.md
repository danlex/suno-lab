---
name: judge
description: Evaluate a Suno prompt YAML against quality criteria, score 0-100, iterate until perfect (>= 90)
---

# Judge — Evaluate & Perfect a Suno Prompt

Score a prompt against 9 quality criteria. Auto-iterate until score >= 90, then hand off to `/suno`.

## Arguments

`/judge <path-to-yaml-prompt-file>`

If no file given, read the most recently modified YAML in `prompts/`.

## The 12 Criteria (weighted)

| # | Criterion | Weight | Pass (10) | Fail (0) |
|---|-----------|--------|-----------|----------|
| 1 | **Style Length** | 12 | 850-950 chars | >1000 or <500 |
| 2 | **Emotional Clarity** | 12 | Specific scene/feeling with concrete anchor | Generic superlatives ("beautiful", "transcendent") without grounding |
| 3 | **Instrument Count** | 8 | 2-4 named instruments | 6+ instruments (Suno ignores extras) |
| 4 | **Negative Prompts** | 8 | 3+ "No X" exclusions + exclude_styles field | Missing negatives |
| 5 | **Novelty (surface)** | 12 | Against `experiments/novelty_surface.json`: new featured instrument OR never-combined trio OR new key/BPM combo | Repeats a recent (last 5) featured set |
| 6 | **Novelty (concept)** | 8 | Genuinely different title metaphor + arc shape vs last 3 | Near-duplicate with surface rewording |
| 7 | **Key/BPM** | 4 | Both specified + half-step modulation at climax | Neither present |
| 8 | **No Bad Jargon** | 8 | Clean of trigger words and unverified terms | Contains words Suno misinterprets |
| 9 | **Conversational Flow** | 8 | Flowing sentences with verbs and connectors | Comma-separated tag list |
| 10 | **Scene Quality** | 8 | Spatial/temporal/sensory storytelling | Purely technical description |
| 11 | **Timestamps** | 6 | ≥3 explicit time anchors (e.g., "at 0:30", "silence at 2:00") | No time anchors |
| 12 | **Purpose Phrase** | 6 | Use-context phrase ("film score for X scene", "underscore for Y") | Missing |

**Final score:** Weighted average normalized to 0-100. Total weight = 100.

## Jargon Blocklist

**Trigger words (cause wrong genre):**
- "Dune", "desert", "sand", "oasis" → Arabic/Middle Eastern
- "epic", "massive", "explosion" → rock/drums
- "wall of sound", "metal", "heavy" → rock aesthetic
- "frisson" → not a prompt term Suno understands (we use the technique, not the word)

**Unverified jargon (Suno may not understand):**
- "appoggiatura", "Shepard tone", "melisma", "voix celeste"
- Any composer/artist name: "Celibidache", "Barber", "Zimmer", "Villa-Lobos", "Arnalds", "Frahm", "Richter"
- Genre-adjacent artist references ("Evanescence-like", "Interstellar-inspired") — describe the *sound*, not the *reference*

## Novelty Check — two layers

**Layer 1: Surface novelty (criterion #5, weight 12).** Consult `experiments/novelty_surface.json` (regenerate via `python3 scripts/novelty_surface.py` if stale). Check:
- Is at least one featured instrument genuinely new (zero prior uses) or revived from >20 versions ago?
- Is the featured *combination* (pair/trio) new? A trio of individually-used instruments can still be a novel combo.
- Is the key or BPM outside recent usage (last 5 versions)?

Score: 10 if at least two of three hold; 8 if one holds; 5 if none hold but context differs; 0 if duplicates recent.

**Layer 2: Concept novelty (criterion #6, weight 8).** Vs. the last 3 prompts on disk, compare:
1. Title metaphor
2. Opening frame / entry point
3. Arc structure (build-silence-return vs. decay vs. bookend vs. passacaglia-variations vs. bolero-layering vs. ...)
4. Emotional territory

Score: 4/4 different = 10, 3/4 = 8, 2/4 = 5, 1/4 = 2.

## Process

1. **Ensure novelty surface is fresh.** If `experiments/novelty_surface.json` doesn't exist or is older than the newest prompt YAML, run `python3 scripts/novelty_surface.py` first.
2. Read the prompt YAML file being judged.
3. Read the 3 most recent *other* prompt files for concept-novelty comparison.
4. Score all 12 criteria. Output the report table.
5. If score >= 90: **PASS** — output "Ready for /suno submission."
6. If score < 90: Identify criteria scoring < 8. Generate specific fixes targeting ONLY those weak criteria. Apply fixes to the style/lyrics. Re-score. Repeat up to 5 iterations.
7. If still < 90 after 5 iterations: **STALLED** — present best version for human review.

## Output Format

```
## Judge Report: <title> v<version>
Score: XX/100 | Iteration: N/5

| Criterion | Score | Notes |
|-----------|-------|-------|
| Style Length | X/10 | XXX chars |
| Emotional Clarity | X/10 | ... |
| ... | ... | ... |

### Weaknesses
- [specific issues]

### Suggested Fixes
- [specific rewording]

### Verdict: PASS / ITERATE / STALLED
```

## Integration

The `/suno` skill should run `/judge` before submitting. The cron job should run `/judge` after generating each new prompt.
