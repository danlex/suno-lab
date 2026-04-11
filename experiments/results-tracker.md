# Cycle log

Per-cycle record of what was tried, why, and what we learned. Append new entries at the top. Always update `experiments/evolution.md` when a cycle adds a durable technique or learning.

---

## 2026-04-12 — v109 (tuned) + v111 cycle

**Submitted:** v109 "Rain on a Window You Remember" (orchestral chillhop + mbira + upright bass), v111 "The Ground That Holds Everything" (orchestral passacaglia + nyckelharpa + hardanger fiddle + ondes martenot).

**What was tried:**
- v109 was committed but never submitted. Ran the judge, scored 88 (style length 994 / only 2 negatives), applied tune-up to 884 chars + 4 negatives, re-scored 94.5, submitted.
- v111 followed v110's break from electronic-fusion into pure orchestral architectural forms. v110 = Bolero (melody constant, orchestration grows). v111 = Passacaglia (bass constant, upper voices transform) — a deliberate inversion. First 3-soloist trio in the repo.

**Why:**
- Memory "uncommon combinations" demands trios, not duos. v111 finally tried three featured instruments.
- Loki/Troll film scores provided the nyckelharpa + hardanger + ondes martenot palette.
- Passacaglia fits the user's "fragile becoming infinite" aesthetic by letting the upper voices transform over an unchanging foundation.

**What we learned:**
- **Memory drift is a real problem.** My v111 notes initially claimed ondes martenot was "never used" — it had been used in v80 and v85. The novelty_surface.py harness was built this cycle to prevent that class of error.
- **Pipe organ and piano are overexposed** (50 and 40 uses). Any v112 "intimate piano + grand organ" concept needs to earn its reuse via novel framing, not assume novelty.
- **v109 demonstrated that tuning for judge criteria works** — 88 → 94.5 from two small fixes (trim + add negatives). The judge is useful even for already-committed prompts.

**Harness additions this cycle:**
- `scripts/novelty_surface.py` — extracts used instruments/genres/keys/BPMs from all YAMLs; writes `experiments/novelty_surface.json`
- Judge skill extended from 9 to 12 criteria (added timestamps, purpose phrase, split novelty into surface + concept layers)
- `experiments/evolution.md` — technique mindmap + instrument novelty map + architectural-form registry + next-cycle priorities
- 3 new feedback memories: new prompt techniques 2026, check novelty_surface before claiming "never used", SOTA hourly ambition

**Open:**
- v112 approved, draft concept is "A Cathedral Built Around One Piano" (felt piano + string orchestra + pipe organ, lone-center-world-grows architecture)
- Need to reconsider pipe organ given overexposure data
- Next cycle should apply timestamps + purpose phrase techniques explicitly

---

## Template for new entries

```
## YYYY-MM-DD — v### cycle

**Submitted:** v### "Title" (genre + featured instruments)

**What was tried:**
- One-line description of the concept and the one meaningful change from prior versions

**Why:**
- Link to memory/research/user direction

**What we learned:**
- Technique insights that should go into evolution.md
- Surprising Suno responses
- Things that didn't work

**Harness additions this cycle:** (if any)

**Open:** (what's deferred to next cycle)
```

---

## Untested assumptions to verify

Things we still don't know if Suno actually honors:
- [ ] Do explicit timestamps ("at 0:30") produce on-time entries? — test in v112+
- [ ] Does "purpose phrase" meaningfully change output? — test in v112+
- [ ] Does "half-step modulation" produce a real key change?
- [ ] Does `[Silence]` metatag produce actual silence?
- [ ] Does BPM specification produce a song at that BPM?
- [ ] Does "fortississimo" change dynamic?
- [ ] Does 3-soloist framing produce three distinct solo voices?

Verification method: submit matched pairs (with/without the technique), listen to both, record which does what.
