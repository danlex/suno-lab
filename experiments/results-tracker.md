# Cycle log

Per-cycle record of what was tried, why, and what we learned. Append new entries at the top. Always update `experiments/evolution.md` when a cycle adds a durable technique or learning.

---

## 2026-04-12 — v113 cycle (first 1–2 minute duration test)

**Submitted:** v113 "The Question That Keeps Being Asked" — NEOCLASSICAL FUGUE FILM SCORE with clavichord + hurdy gurdy + viola da gamba. First fugue form in the repo. Three never-used Baroque instruments as a historically-coherent trio.

**What was tried:**
- First application of the new 1–2 minute song duration constraint. Prompt included "total duration 1:00 to 2:00" in the first 200 chars + compressed arc template (0:00/0:20/0:45/1:00/1:25 silence/1:30 return/1:50 end).
- First Baroque fugue form: three voices imitative entry (clavichord subject → hurdy gurdy answer a fifth up → viola da gamba subject in deepest voice), stretto at 1:00, silence at 1:25.

**Why:**
- User direction: songs should be 1–2 minutes, never longer.
- Evolution.md "next-cycle priorities" called for trying an architectural form not yet explored. Fugue was the top choice.
- Novelty surface confirmed all three instruments were repo first-uses.

**What we learned — MAJOR:**
- **Duration hint WORKS.** Suno produced versions of **1:08** and **0:44** — both under the 2:00 cap. The 1:08 is within the 1–2 minute target zone; the 0:44 actually undershot the 1:00 floor. This confirms Suno honors "total duration 1:00 to 2:00" language in the style field — the timestamps + duration phrase are load-bearing, not decorative.
- **0:44 undershoot is a new failure mode to address.** The prompt said "1:00 to 2:00" but Suno produced a sub-minute song for one of the two versions. Likely causes: (a) the silence+end instruction at 1:25-1:50 got truncated, (b) Suno's length model averaged across "1:00" and "2:00" and picked a shorter target. Candidate fix for next cycle: change "total duration 1:00 to 2:00" to "total duration 1:30 to 2:00" or add "do not shorten below 1:00".
- **Fugue as a form: unknown until we listen.** Did Suno actually produce three imitative voices, or did it collapse them into homophony? Verify by listening.

**Submission incident — the form-hijack bug:**
- After I clicked Create successfully for v113, a Suno detail panel for an unrelated song ("The Purpose of Life") opened and replaced the form fields with the detail-song's values. This did NOT affect my v113 submission (it had already gone through), but it masked the success — when I inspected the form afterwards I saw old data and thought v113 had failed.
- **Harness fix needed:** the `/suno` skill should (1) verify submission by polling the workspace for the new title rather than inspecting form state, and (2) detect and close any detail panel before/after submitting. Add to `.claude/skills/suno/SKILL.md` next cycle.

**Harness additions this cycle:**
- scripts/hourly_cycle_prompt.md — self-contained cycle instructions for the CronCreate hourly schedule
- feedback_song_duration_one_minute.md memory — 1–2 minute duration constraint
- feedback_cron_auto_submit_override.md memory — auto-submit authorized in cron context
- CronCreate job 5a227a9e — every 2 hours at :13, session-only (durable flag silently ignored in this runtime)

**Open for next cycle:**
- Listen to both v113 versions and verify (a) is it actually a fugue with 3 imitative voices, (b) what was the 0:44 version's final shape
- Fix duration undershoot by adjusting language
- Fix form-hijack bug in /suno skill
- v114 via cron at next :13 fire

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
