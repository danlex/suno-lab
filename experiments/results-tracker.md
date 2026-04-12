# Cycle log

Per-cycle record of what was tried, why, and what we learned. Append new entries at the top. Always update `experiments/evolution.md` when a cycle adds a durable technique or learning.

---

## 2026-04-12 — v120 + v121 cycle (maximum pattern-breaking batch)

**Submitted:** v120 "Every Voice Chasing the Last" — ORCHESTRAL CANON with bass flute + steelpan (DUO). v121 "Beginning at the End" — ORCHESTRAL DISSOLUTION with harpsichord + bass trombone + glass marimba.

**Patterns broken in v120:**
- First MAJOR KEY in synthesis era (G major, every v93-v119 was minor)
- First DUO instead of trio (evolution.md priority #8)
- First CANON/ROUND form (new architectural form)
- First JOYFUL emotion (all prior were melancholic/dark)
- 152 BPM (fastest in synthesis era)
- NO silence-before-climax (breaking the "always use" default)
- "processional" instead of "film score for X scene"

**Patterns broken in v121:**
- First INVERTED ARC (starts at fortississimo, decays to nothing)
- First half-step DOWN modulation (Db major → C major, all prior went UP)
- First "no crescendo, no build-up" negative prompts
- 46 BPM (near-bottom of range)
- "underscore" instead of "film score"

**What we learned:**
- **v120 clips: 0:54 and 0:56** — both under the 1-minute floor despite "total duration 1:00 to 2:00" language. At 152 BPM, Suno produced very short clips. Reinforces: duration is NOT prompt-controllable, and faster tempo may correlate with shorter output.
- **Double-submission bug recurred.** First Create click appeared to fail (songs didn't show in workspace for ~15 seconds), so I clicked again. Both went through = 4 clips instead of 2. Same as v114. Lesson: ALWAYS wait 20+ seconds before assuming failure. Never re-click Create.
- **v121 clips:** still generating at time of commit.

**Harness lesson:** Add 20-second minimum wait after Create click before checking workspace. The workspace may lag behind the actual generation start.

**Open:**
- Listen to v120 to hear if Suno renders a canon/round in major key
- Listen to v121 to hear if Suno renders a decay arc (starts loud, ends quiet)
- Try sonata form or concerto grosso next
- Still open: try duo vs trio comparison (v120 = first duo)

---

## 2026-04-12 — v119 cycle (first theme-and-variations + triple deep revival)

**Submitted:** v119 "The Same Story Told Three Ways" — ORCHESTRAL THEME AND VARIATIONS with theremin + tubular bells + contrabassoon. First theme-and-variations form in the repo. All three instruments are deep revivals (15-17 version gaps). Clip 1: 1:43. Clip 2: pending.

**What was tried:**
- First theme-and-variations architecture: each instrument states the SAME melody through its own timbre (theremin = eerie/hovering, tubular bells = ceremonial/sacred, contrabassoon = dark/subterranean), then all three combine.
- Triple deep revival trio: theremin (v101, 17-gap), tubular bells (v101, 17-gap), contrabassoon (v103, 15-gap). All from different instrument families (electronic / metallic percussion / double-reed woodwind).
- New BPM (62, never used) and near-virgin key (F# minor, used only once).
- Scene: "witness-testimony" — three witnesses describing the same vanished moment through different filters.

**Why:**
- Evolution.md priority #7: try theme-and-variations or sonata form. Theme-and-variations chosen because the concept naturally maps to three instruments taking turns with the same melody.
- Research: contemporary theremin revival in orchestral film scoring (Loki, Nimona, First Man scores + ACO 2025 tour with Carolina Eyck). Theremin evolving beyond sci-fi cliché into serious orchestral voice.
- All three instruments at 15+ version gaps = maximum combined revival depth.

**What we learned:**
- **Clip 1 duration: 1:43** — within the 1-2 minute target despite duration language being "concluded as dead" in evolution.md. This may be a coincidence (Suno ignores duration language but the arc template timestamps naturally guided a shorter song).
- **Theme-and-variations as form:** unknown until listening whether Suno actually produced three distinct timbral variations of the same melody or collapsed into homophony. Verify by listening.
- **Judge score: 100/100** — first perfect score. All 9 criteria passed cleanly. The deep revival trio + new form + new key/BPM + new scene maximized novelty.

**Harness additions this cycle:**
- Remote triggers created: Suno Generation Cycle (every 2h) + Suno Review & Publish Cycle (daily) via RemoteTrigger API — durable, survive session exit.

**Open:**
- Listen to both clips to verify theme-and-variations form was rendered
- Next form to try: sonata form or concerto grosso
- Priority #8 still open: try a duo instead of trio

---

## 2026-04-12 — v115 cycle (first rondo + lyrics-metatag duration experiment)

**Submitted:** v115 "What Keeps Coming Back" — NEOCLASSICAL RONDO FILM SCORE with cornet + cimbalom + frame drums. First rondo (ABACA) form in the repo. First use of `[End]` metatag in the lyrics field of an instrumental prompt as a duration control experiment.

**What was tried:**
- First iterative-recurrence architecture: rondo ABACA where refrain A returns between episodes B and C. Contrasts v114 arch (ABCBA palindromic).
- Lyrics field filled with ONLY structural metatags: `[Short Instrumental Intro]\n[Refrain]\n[Episode 1]\n[Refrain]\n[Episode 2]\n[Silence]\n[Refrain]\n[End]`. First time we combine instrumental=true with non-empty lyrics (metatags only, no text) as a duration + structure signal.
- Tighter duration language: "total duration 1:40 to 1:55 (ends at 1:55, never longer)" instead of v114's "1:30 to 2:00". Narrower window.
- Trio: CORNET (repo first use) + CIMBALOM (v98, 16-version deep revival) + FRAME DRUMS (v96, 18-version deep revival).

**Why:**
- v113 produced 0:44 (under), v114 produced 2:27 (over the 2:00 cap). Duration language in style field alone is insufficient.
- Research this cycle found Suno's official stance: **duration is NOT prompt-controllable**, only via the Extend feature. But CLAUDE.md notes `[End]` metatag as a structural signal. This cycle tests whether the metatag works as a duration reinforcement.

**What we learned:**
- **Browser extension disconnected mid-cycle.** Applied `feedback_browser_self_fix.md` — opened claude.ai via Bash to reconnect, no user prompt needed. Reconnected cleanly.
- **Suno's placeholder text rotates randomly per page load** — my form-field matcher that looked for "hard kick" / "smooth vocals" failed this time because placeholder was "dissonant harmonies, 85bpm, space synth, dj scratching, slap". Fix: identify style field by position (textarea index 1) or by elimination (not-lyrics, not-other-prompt-fields). Applied in-session.
- **Pending:** does `[End]` metatag + tighter style language actually hold duration? Listen to v115's two clips and measure. If it holds, codify as standard practice for all future prompts.

**Harness additions this cycle:**
- Style-field identification by elimination (not by placeholder matching)
- Explicit "clear lyrics before set" step in submission flow (v114 lesson applied)

**Open:**
- Verify v115 duration constraint works (empirical test pending generation completion)
- Codify /suno skill with: (1) lyrics clear-before-set, (2) style field by elimination, (3) title-poll verification, (4) browser reconnect on disconnect
- Next cycle: theme-and-variations form, or return to electronic fusion after 4 pure-orchestral cycles

---

## 2026-04-12 — v114 cycle (first arch form + duration-language iteration)

**Submitted:** v114 "The First and Last Note Are the Same" — NEOCLASSICAL FILM SCORE with shakuhachi + bass oboe + waterphone. First palindromic ARCH FORM (ABCBA) in the repo. Two repo first-uses (shakuhachi, bass oboe) + one deep revival (waterphone, last in v94 — 20 versions ago).

**What was tried:**
- First symmetric architecture — arch form where the second half mirrors the first in reverse. Contrasts with all prior linear forms (v110 bolero, v111 passacaglia, v112 lone-center, v113 fugue).
- Duration-language iteration: tightened "total duration 1:00 to 2:00" → "1:30 to 2:00" to raise the floor after v113's 0:44 undershoot.
- First use of shakuhachi. Needed new exclude_styles entries ("zen meditation", "new age") to prevent the Japanese flute from triggering wrong aesthetic.

**Why:**
- Research (chaconne vs passacaglia) revealed the distinction is "arbitrary and historically unfounded" per scholarship, so pivoted from chaconne to arch form for cleaner form-novelty signal.
- v113's 0:44 undershoot demanded a duration-language fix this cycle to test whether a higher floor holds.

**What we learned:**
- **Form-hijack bug (continued from v113) was bigger than I thought.** When I first clicked Create for v114, nothing submitted. Investigation revealed (a) the lyrics field had been auto-filled with `[Climax] AAAHH... AAHH...` from a hijack when I interacted with the detail panel, (b) Suno likely refused the submit because instrumental=on + lyrics=non-empty is contradictory state. Fix: clear lyrics field explicitly before every submission, not just trust the initial state. This should go in the `/suno` skill hardening.
- **Post-submit verification fix works.** Instead of inspecting form state after clicking Create (which gets hijacked), polled the workspace for the new title appearing as a song-link. Clean and reliable — confirmed v114 submitted on the second Create click without ambiguity.
- **Pending:** does the "1:30 to 2:00" language actually raise the floor, or does Suno still undershoot? Verify by listening to both v114 versions.

**Harness additions this cycle:**
- Post-submit verification via title-poll (applied in-session; should be codified in `.claude/skills/suno/SKILL.md` next cycle)
- `exclude_styles` pattern for shakuhachi/non-Western flutes: add "zen meditation, new age" to prevent wrong aesthetic triggering
- Lyrics-field clear step before submission (new /suno skill step)

**Open:**
- Listen to v113 + v114 in a batch to verify duration constraint actually works
- Codify the /suno post-submit fix + lyrics-clear step in the skill
- Next cycle should try another unexplored form: theme-and-variations, rondo, or sonata form

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
