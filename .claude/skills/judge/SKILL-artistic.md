---
name: judge-artistic
description: Second judge — evaluates the ARTISTIC and MUSICAL quality of a Suno prompt from a film composer's perspective
---

# Artistic Judge — Would a Film Composer Approve?

The first judge (`/judge`) evaluates technical prompt quality. This second judge evaluates ARTISTIC merit — would this prompt produce award-winning music?

## Arguments

`/judge-artistic <path-to-yaml-prompt-file>`

## The 7 Artistic Criteria (weighted)

| # | Criterion | Weight | What a film composer would ask |
|---|-----------|--------|-------------------------------|
| 1 | **Emotional Arc** | 20 | Does it tell a story? Beginning, middle, end? Or static? |
| 2 | **Orchestral Realism** | 15 | Would a real orchestra play this? Are the instrument combinations natural? |
| 3 | **Dynamic Range** | 15 | Is there contrast between quiet and loud? Or monotonously loud/soft? |
| 4 | **Zimmer Test** | 15 | Would this sit alongside Interstellar, Gladiator, Inception? Award-level ambition? |
| 5 | **Uniqueness** | 15 | Has this specific sound been heard before? Or is it a cliche? |
| 6 | **Goosebump Potential** | 10 | Reading this prompt, can you FEEL the music? Does it make you want to hear it? |
| 7 | **Title-Style Coherence** | 10 | Does the title evoke the same feeling as the music described? |

## Scoring

Each criterion 0-10, weighted to 0-100 total. Must score >= 85 to pass.

## Key Questions Per Criterion

### 1. Emotional Arc (20%)
- Is there a clear beginning state and ending state?
- Does something CHANGE during the piece?
- Is the arc surprising or predictable?
- Best: "grief transforms into triumph" / Worst: "it's beautiful and gets more beautiful"

### 2. Orchestral Realism (15%)
- Do these instruments actually play well together?
- Is the described behavior physically possible? (e.g., "hundreds of bows moving as one" = yes)
- Would a conductor recognize this as a real orchestral piece?

### 3. Dynamic Range (15%)
- Is there at least one quiet moment and one loud moment?
- Is there silence or near-silence anywhere?
- Does the piece breathe?

### 4. Zimmer Test (15%)
- Is this ambitious enough for a major film?
- Does it have the scale and emotional weight of award-winning scores?
- Would you put this in the credits of a $200M film?

### 5. Uniqueness (15%)
- Is this a fresh angle or "generic orchestral" filler?
- Does it have a signature element that makes it THIS piece and not any other?
- The "hummable" test: is there a distinctive core idea?

### 6. Goosebump Potential (10%)
- Reading the style description, do you feel something?
- Does it use language that triggers emotional response?
- Would you stop scrolling to listen to this?

### 7. Title-Style Coherence (10%)
- Does the title capture the essence of the music?
- Would you know what to expect from the title alone?
- Is the title poetic but not pretentious?

## Output Format

```
## Artistic Judge: <title>
Score: XX/100

| Criterion | Score | Verdict |
|-----------|-------|---------|
| Emotional Arc | X/10 | ... |
| Orchestral Realism | X/10 | ... |
| Dynamic Range | X/10 | ... |
| Zimmer Test | X/10 | ... |
| Uniqueness | X/10 | ... |
| Goosebump Potential | X/10 | ... |
| Title Coherence | X/10 | ... |

### Artistic Direction
[What a film composer would change]

### Verdict: MASTERPIECE / STRONG / NEEDS WORK / REJECT
```

## Integration

Both judges must pass before `/suno` submission:
- `/judge` (technical) >= 90
- `/judge-artistic` >= 85
- Only submit when BOTH pass
