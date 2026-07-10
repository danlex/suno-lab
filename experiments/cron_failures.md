# Cron failure log

### 2026-07-11 — v389 STALL (autonomous /loop, 2 drafts) — Afropop-dancehall → Afro-house, best 78/d8. NOT SHIPPED.
Concept: "communal joy + edge of longing" — the last songs of a night, hook "Three more songs and then I lose you" (hook-writer 22/25). Draft 1 (Afropop/dancehall one-drop, 108 BPM, A major) STALLED 71/d7 — danceability only 8/15, judge: 108 one-drop too mellow for our beat-driven audience. Re-draft (Afro-house, 123 BPM, A minor, four-on-the-floor) lifted danceability 8→13/15 (fix worked) but still STALLED 78 — honest concept ceiling ~79-81.
Root cause = concept-level, not editable: (D2 14/20) the bittersweet-dancefloor-farewell theme overlaps v367 ("you look like a memory already", UK garage) DNA; (D6 7/10) strip→drop climax is club-standard; (D1 21/25) countdown hook is literary, no melodic fingerprint in text.
LESSON for the loop: (1) accessible-vocal is necessary but NOT sufficient — the lane must be genuinely beat-driven (≥~120 BPM, driving groove); mellow mid-tempo (one-drop/108) caps danceability. (2) Avoid re-treading the "dancefloor goodbye / you're already a memory" emotional register — it's now a catalog near-neighbor (v367, v389). Next cycles need a distinct emotional theme AND a hook with a stronger in-render melodic identity AND a genuinely novel climax device (not strip→drop, not half-step).
Action: logged, advancing loop to v390 with a fresher concept. Did NOT ship the stalled 78. Stray file prompts/countdown389-v389.yaml left uncommitted as scrap.

### 2026-06-30 — v365 ALL-STALL — 5-candidate MoA tournament (afro house/EBM/UK garage/amapiano/dark techno). Best: EBM 80. Root cause: ALL 5 candidates used half-step modulation (Db→D, Eb→E, G#→A) as the climax device → Dim 6 capped at 5/10 on every candidate. Rescue attempt pending with texture-explosion climax on afro house (debut).

Scores: EBM "Coolant" 80/d7, UK Garage "Glass" 76/d7, Amapiano "Bruise" 76/d7, Dark Techno "Fourier" 69/d8, Afro House "Harmattan" (judge hit session limit, estimated ~80).
Process error: novelty picker assigned a single shared key (Db minor → D minor) to all lanes; ALL drafters then used that half-step as the climax → identical frisson penalty ×5. Fix: key/climax diversification must be enforced ACROSS lanes at the orchestrator level, not delegated to drafters.

### 2026-06-22 — v359 NO-SHIP #3 — HOOK-FIRST + DIVERSIFIED + DEBUT-LANES round, best 82. CEILING IS CONCLUSIVE (~82-84); 88 is unreachable by this pipeline.

Ran the fully-optimized round: 5 DEBUT genres (gqom, jersey club, ghettotech, hard house/donk, bmore), each with a pre-validated hook (20-21/25), a DISTINCT key, a DISTINCT trio, and a DISTINCT non-half-step climax (parallel-major lift / octave-transposition / tempo-reveal / density-re-entry / texture-explosion). Fixed two gate bugs (drafters set "no vocals" on vocal-hook tracks).
Results: Clocked (hard house) 82/d8, Plate (ghettotech) 81/d9, Quartz (jersey) 79/d8, Béton (gqom) 79/d8, Caliper (bmore) 75/d8. Best 82. None ≥88 → no-ship.
WHAT THE DIVERSIFICATION FIXED: distinctiveness rose to 17-18 (from the ~14 shipped-lane cap) — the debut-genre + diversify strategy worked exactly as intended.
WHY 88 IS STILL UNREACHABLE (conclusive across ~30 candidates / 3 rounds): three structural ceilings that no prompt edit can break — (1) HOOK caps ~18-20 because a melodic contour written in TEXT isn't guaranteed in Suno's render, and rhythm-hook genres (gqom/ghettotech/bmore) cap even lower; (2) FRISSON caps at 8 because any build-release macro-arc has "structural cousins"; (3) DISTINCTIVENESS maxes ~18 (debut genre) but "female vocal over dance groove" recurs. These are inherent to text-prompt-judged-by-text-rubric. The honest pipeline ceiling is 82-84.
Progression across rounds: chant 76 → hook-first 84 → hook-first+diversified 82. We have plateaued.
DECISION REQUIRED FROM USER (the bar is their lever): (a) lower the bar to ~83 and ship the genuinely-strong leaders (Clocked/Plate are real debut-genre tracks, danceability 8-9) — RECOMMENDED; (b) keep 88 = effectively permanent no-ship; (c) change the judge to score the AUDIO (listen to renders) instead of the text, which is the only way text→88 could ever be validated.
Action: logged + committing. PAUSED the hourly cron (was 2167a984) to stop burning tokens against an unreachable bar until the user sets a reachable one. Did NOT ship below 88.

### 2026-06-22 — v359 NO-SHIP #2 — HOOK-FIRST round, best 84, none reached 88 (but the fix works)

Ran the full hook-first pipeline (suno-hook-writer now registered): 5 hook-writers produced ownable hooks scoring 21-22/25 (vs the chant round's 14-18), then 5 drafters built around them, then 5 critical judges.
Results: speed-garage "Séraphine" 84/d9, DnB "Encore" 84/d9, afro-house "Dusk" 76/d7, melodic-techno "Kelvin" 76/d8, future-bass "Aureole" 76/d8. Best = 84. None ≥88 → no-ship per the bar.
WIN: the hook-first step demonstrably lifted the ceiling 76 → 84. In-render hook dimension rose to 19-21/25 (was 14-18). The approach is validated.
Remaining gap to 88 is concept-level and narrow: (1) distinctiveness caps at 14-17 because the chosen lanes (melodic-techno, speed-garage) have PRIOR catalog entries — only genuinely debut lanes (afro-house, DnB earned 16-17) score higher; (2) hook caps at ~19-20 because a melodic-contour spec in style text is an instruction Suno may not render faithfully — judges discount for that.
PROCESS ERROR (mine): I gave ALL 5 candidates the SAME key (C minor→E-flat major) and the SAME trio palette (harpsichord/xylophone). The judge penalized "Dusk" and "Aureole" for intra-cycle CONVERGENCE (shared harpsichord + shared modulation). Fix: diversify key, trio, AND climax device ACROSS the 5 candidates each cycle — never give them a single shared recipe. Cron prompt (d5b483da) updated accordingly.
Stray cleanup: drafter L4 wrote to prompts/aureole-v359.yaml instead of scratchpad; removed it so cycle_start version detection stays correct.
Action: logged + committing. Did NOT ship below 88.
Open decision for the user: pipeline now tops out ~84 on the critical scale. Either (a) hold 88 and keep improving the harness toward it, (b) set bar to 84 to ship genuinely-strong tracks, or (c) only run debut-genre lanes (which score the distinctiveness needed).

### 2026-06-21 — v359 NO-SHIP — first run on the critical rubric, no candidate reached 88

Reason: no candidate cleared the ≥88 ship bar on the new CRITICAL judge rubric (commit 6b5170e). Ran TWO full rounds = 10 candidates:
- Round 1 (template-ish lanes): afro-house "Groove" 66, trance "Ascend" 68, electro "Verrou" 67, speed-garage "Slam" 63, hard-groove "Squelch" 68.
- Round 2 (engineered to beat round-1 ceilings: ownable hook + non-half-step climax): electro-swing "Slink" 76, neuro-DnB "Snarl" 75, UK-bassline "Notch" 73, future-garage "Drift" 71, funky-house "Groovelock" 67.
Best = 76 (Slink). All STALLED, none ≥88. No prompt promoted; nothing submitted/published. `prompts/` unchanged (latest committed = v358 torque).
Systemic finding: production/distinctiveness/danceability/frisson dimensions score well (11-17, 8-9), but the LYRIC HOOK is the universal ceiling at 14-18/25 — AI-drafted hooks read as competent chants, not 3-second singable identities. This is a concept-level limit no style edit fixes. To clear 88 regularly the harness likely needs a dedicated hook-generation step (or to accept that 88 is genuinely rare and shipping cadence drops).
Harness fix this cycle: the compliance gate previously REQUIRED a half-step modulation at the climax — the exact move the quality rubric penalizes. Fixed SKILL.md + suno-judge so the gate accepts any clearly-defined climax (beat-flip, half-time, genre-flip, hook-transformation, structural break), half-step no longer privileged.
Action taken: logged + committing the gate fix. Did NOT ship below the bar (correct per the >95→88 critical-bar policy).
Next cycle: cron job fcd33d9b (:07) fires normally. Consider a hook-first drafting pass or a separate hook-writer subagent if ≥88 stays unreached.

### 2026-06-21 — v359 cycle aborted — account usage/session limit

Reason: suno-researcher and novelty-picker subagents both returned "You've hit your session limit · resets 2pm (Europe/Luxembourg)" with zero work done. The Agent (subagent) tool is rate-limited, so the drafters, judges, and submitter cannot run either. Not a Suno/browser problem — a Claude account usage cap.
State: `cycle_start.py` reported v359, `recommended_action="draft_new"`. Nothing drafted; `prompts/` unchanged (latest committed = v358 torque). First cycle under the new CRITICAL judge rubric (commit 6b5170e) — not yet exercised.
Action taken: Logged + exiting without submitting. No retry (would re-hit the cap until reset). Did NOT spawn further subagents.
Next cycle should: The hourly cron (job fcd33d9b, :07) will fire again; once the limit resets at ~2pm Europe/Luxembourg, the next fire should proceed normally with the full pipeline and the ≥88 critical bar.



Reason: `list_connected_browsers` still returns `[]`. Fifth consecutive cycle blocked on v327.
State: `prompts/geurim-v327.yaml` still untracked, judge 98/100.
Action taken: Logged + committing.
Next cycle: Same short-circuit until bridge reconnected.

### 2026-06-04 — cron fire, no-op (cycle 4) — v327 bridge still disconnected

Reason: `list_connected_browsers` still returns `[]`. Fourth consecutive cycle blocked on v327.
State: `prompts/geurim-v327.yaml` still untracked, judge 98/100.
Action taken: Logged + committing. No agent spawned.
Next cycle: Same short-circuit until bridge is reconnected.

### 2026-06-04 — cron fire, no-op (3 stacked) — v327 bridge still disconnected

Reason: Three cron prompts stacked up; per BACKLOG GUARD treated as ONE cycle. `list_connected_browsers` still returns `[]`. Third consecutive cycle blocked on v327.
State: `prompts/geurim-v327.yaml` still untracked, judge 98/100.
Action taken: Logged + committing. No submitter agent spawned.
Next cycle: Same short-circuit until bridge is reconnected. User must manually re-pin the Chrome extension.

### 2026-06-04 — cron fire, no-op — v327 bridge still disconnected

Reason: `list_connected_browsers` returns `[]` and `tabs_context_mcp` returns "Browser extension is not connected." Bridge has not been restored since last cycle's v327 submit failure.
State: `prompts/geurim-v327.yaml` still untracked, judge 98/100. Second consecutive cycle blocked.
Action taken: Logged this no-op + committing. No submitter agent spawned (would only burn another timeout chain on a known-failing state). Same pattern as v304 multi-cycle outage.
Next cycle should: Re-check `list_connected_browsers`. If it returns ≥1 entry, proceed with v327 submit retry. If still empty, short-circuit again. User needs to manually re-pin the Claude Code Chrome extension or refresh a logged-in claude.ai tab so the extension re-connects.

### 2026-06-04 — v327 failed at submit (NO clips generated)

- **YAML**: prompts/geurim-v327.yaml (K-pop cinematic solo ballad, VIRAL ARM cycle 4)
- **Title**: Geurim
- **Judge**: 98/100 (passed)
- **Reason**: Chrome MCP extension disconnected at start of submit (before form interaction). Submitter reported "Browser extension not connected after one reconnect attempt via open -a Google Chrome https://claude.ai. tabId 786913761 unreachable." Create was NOT clicked — server-side state unchanged.
- **State**: `prompts/geurim-v327.yaml` exists on disk untracked, judged 98/100. Nothing was submitted.
- **Action taken**: Submitter exited cleanly per safety floor #4.
- **Next cycle should**: Per BACKLOG GUARD, `cycle_start.py` will return `recommended_action: resume_submit` for v327 (latest_yaml_uncommitted: true). Retry submit when bridge is healthy. No duplicate-clip risk since Create was confirmed NOT clicked.

### 2026-06-04 — v324 failed mid-form (NO clips generated)

- **YAML**: prompts/queda-v324.yaml (Latin sad-trap ballad cinematic, VIRAL PIVOT cycle after 8 monumental)
- **Title**: Queda
- **Judge**: 94/100 (passed)
- **Reason**: Chrome MCP extension disconnected mid-form during submit. Submitter had clicked the Lyrics textarea + issued cmd+a but the `type` command failed with "No tab with id: 786913479". tabs_context_mcp returned no MCP tab groups after one reconnect attempt. **Create was NOT clicked** — server-side state unchanged, no clips generated.
- **State**: `prompts/queda-v324.yaml` exists on disk untracked, judge 94/100. v323 stale form state was still partially loaded (style field still had Perstat content; vocal_gender still Female, not yet corrected to Male; More Options panel was expanded with exclude visible). Nothing was submitted.
- **Action taken**: Submitter exited cleanly. No retry within this cycle per safety floor #4.
- **Next cycle should**: Per BACKLOG GUARD, `cycle_start.py` will return `recommended_action: resume_submit` for v324 (latest_yaml_uncommitted: true). Retry submit directly when bridge is healthy. No duplicate-clip risk since Create was confirmed NOT clicked.

### 2026-06-03 — cron fire, no-op — bridge fully disconnected

Reason: `list_connected_browsers` returns `[]` and `tabs_context_mcp` returns "Browser extension is not connected." Chrome extension dropped between v317 (closed successfully) and this cycle. No previous YAML uncommitted (cycle_start.py reports `recommended_action: draft_new` for v318).
State: Nothing on disk. No agent chain spawned (per safety floor #4 "do NOT retry" — fully bridge-down state). v318 draft was NOT created. Catalog stays at 317.
Action taken: Logged this no-op + committing.
Next cycle should: Re-check `list_connected_browsers`. If it returns ≥1 entry, proceed with full v318 draft cycle. If still empty, short-circuit again. User needs to manually re-pin the Claude Code Chrome extension or refresh a logged-in claude.ai tab so the extension re-connects.

### 2026-06-02 — v304 RETRY-6 — fresh /create tab is in wrong Chrome window

- **connectedAt advanced**: 1780405790503 → 1780409642261 (fresh reconnect confirmed)
- **MCP tab group**: 2 tabs — tabId 786913460 (suno.com/song/9739bef9 "Vök", extension cannot access song pages) + tabId 786913340 (localhost:8902 stuck loading). No suno.com/create tab in MCP group.
- **What user did**: Reconnected the extension (connectedAt advanced) and presumably opened a fresh suno.com/create tab — BUT that tab landed in a different Chrome window (one the MCP extension does not control). `open -a Chrome https://suno.com/create` from the submitter also opened a new tab outside the MCP group.
- **Submitter limitation**: The submitter agent does not have `tabs_create_mcp` in its toolset (Bash, Read, tabs_context_mcp, find, read_page, computer, form_input only). Without it, the submitter cannot create a /create tab inside the MCP group; it can only operate on tabs already in the group.
- **State**: `prompts/ukufa-v304.yaml` untracked, judged 97/100. Sixth consecutive failed submit attempt.
- **Action taken**: Submitter exited per pre-flight protocol. Logged here, committing.
- **Critical user-side fix**: The fresh `suno.com/create` tab must be opened **in the same Chrome window where the Claude Code extension is pinned and currently bridging** — usually the same window as the existing MCP group tabs. Close the Vök song tab (tabId 786913460) and the localhost tab (tabId 786913340) from that window first. Then open suno.com/create in that exact same window (not a new window). Confirm the extension badge is active on the new tab before re-triggering.



Reason: `list_connected_browsers` returns Browser 1 with `connectedAt: 1780405790503` — identical to last cycle's retry-5 failure. No fresh reconnect since user has not closed the stuck `suno.com/song/9739bef9` (Vök) tab in the MCP group. v304 has now been blocked across 8 consecutive cron hours.
State: `prompts/ukufa-v304.yaml` still untracked, judged 97/100.
Action taken: Short-circuited — no submitter agent spawned (would repeat the same Vök-tab hang for the 6th time). Logged this no-op and committed.
Next cycle: Same short-circuit until `connectedAt` advances. The advance signal alone is insufficient (retry-4 and retry-5 both had fresh `connectedAt` but the stuck Vök tab persisted in the MCP group, so the submitter still hung). The user-side fix is: close tabId 786913118 (Vök song page) → open fresh suno.com/create tab IN THE SAME Chrome window where the Claude Code extension is pinned → confirm extension badge active on that tab.

### 2026-06-02 — v304 RETRY-5 — bridge connectedAt advanced again, song-page tab stuck loading

- **connectedAt advanced**: 1780403730367 → 1780405790503 (fresh reconnect confirmed for RETRY-5).
- **MCP tab group**: 2 tabs — tabId 786913118 (suno.com/song/9739bef9... "Vök" — a song page, NOT /create) and tabId 786913340 (localhost:8902/interview). No suno.com/create tab in group.
- **Pre-flight sequence**:
  1. cmd+l + typed https://suno.com/create + Enter → page went into loading state, all tool calls timed out at 45s.
  2. Escape key → still timed out.
  3. F5 reload → waited 10s → ONE successful screenshot (Vök song page visible). Brief window.
  4. Clicked inside the page (tried to find sidebar Create link) → page re-entered loading state, all subsequent calls timed out permanently.
- **Root cause**: Same Service Worker / React SPA deferred-navigation loop as RETRY-3/RETRY-4. Tab is a suno.com/song page; after brief restore via F5, any in-page interaction triggers a new navigation event that the content script cannot settle. Extension waits for document_idle indefinitely.
- **State**: prompts/ukufa-v304.yaml unchanged on disk (untracked), no form fields touched, no clips generated. Sixth consecutive failed submit attempt.
- **Action taken**: Logged per pre-flight protocol ("probe timed out → log and exit, do NOT loop"). Clean exit.
- **Critical user-side fix (still outstanding)**: (1) Chrome DevTools → Application → Service Workers → Unregister on any suno.com tab. OR (2) chrome://settings/content/all → suno.com → Delete (clears site data + SW cache). OR (3) Full Chrome restart. After fix, open a fresh suno.com/create tab IN THE SAME WINDOW as the MCP extension, confirm extension badge is active, then re-trigger submission. The Vök song tab (786913118) must be closed or replaced — it is the persistent stuck-tab across all five retries.


### 2026-06-02 — v304 RETRY-4 — bridge connectedAt advanced but probe still failing

- **connectedAt advanced**: 1780395121178 → 1780403730367 (fresh reconnect confirmed).
- **MCP tab group**: 2 tabs — tabId 786913118 (suno.com/song/... — a song page, not /create) and tabId 786913340 (localhost:8902/interview). No suno.com/create tab in group.
- **Pre-flight probe result**: Every `executeScript` call on tabId 786913118 timed out at 45s ("Page still loading"). Attempted: screenshot (×3), read_page (×1), key Escape, cmd+l + URL navigation, wait 10s×2. Tab title stays "Vök by Alexandru Dan | Suno" — page is a song page stuck in loading state.
- **Root cause**: The tab in the MCP group is a suno.com/song page stuck in a loading loop — NOT a create page. `cmd+l` + URL type + Enter attempted to navigate it to suno.com/create, but the navigation did not land (executeScript still failing). `open -a Chrome https://suno.com/create` was issued but the new tab opened outside the MCP group (MCP group did not update).
- **State**: `prompts/ukufa-v304.yaml` unchanged on disk (untracked), no form fields touched, no clips generated. Fifth consecutive failed submit attempt.
- **Action taken**: Logging "bridge connectedAt advanced but probe still failing" per pre-flight protocol. Clean exit. No retry within this cycle.
- **Critical user-side fix needed**: The MCP group needs a working suno.com/create tab that the extension can inject scripts into. Steps: (1) In Chrome, open a new tab manually → navigate to suno.com/create → confirm the Claude Code extension icon shows active badge. (2) That tab must be in the MCP-controlled window/group (the same window where the extension is pinned). (3) Close the stuck suno.com/song tab (786913118) from the MCP group if possible. (4) Then re-trigger this submission.


### 2026-06-02 — cron fire, no-op — v304 bridge still stuck

Reason: `list_connected_browsers` returns Browser 1 with `connectedAt: 1780395121178` — the SAME timestamp logged across the three prior consecutive failed retries (retry-1, retry-2, retry-3). No fresh reconnect; Chrome MCP session has not been touched. Service Worker on suno.com/create is still in the deferred-navigation state diagnosed last cycle (one-screenshot-then-hang pattern).
State: `prompts/ukufa-v304.yaml` still untracked, judged 97/100. Four consecutive submit attempts now blocked on the same Service Worker condition.
Action taken: Logged. No submitter agent spawned (would only burn another full timeout chain on the same broken state). No commits beyond this entry.
Next cycle should: Same short-circuit until `connectedAt` advances (indicating a fresh extension/Chrome session). User needs to manually clear the Service Worker per retry-3 entry: Chrome DevTools → Application → Service Workers → Unregister on the suno.com/create tab, OR clear all suno.com site data via chrome://settings/content/all, OR full Chrome restart. Once `connectedAt` changes, the next cycle can attempt the fresh-tab submit protocol again.

### 2026-06-02 — cron fire, no-op (cycle 5) — bridge still stuck

Reason: `connectedAt: 1780395121178` — fifth consecutive cycle on the identical timestamp. No fresh extension reconnect from the user. Service Worker still in the same hung state.
State: `prompts/ukufa-v304.yaml` still untracked, judged 97/100. v304 has now been blocked for 5 consecutive cron hours on the same Service Worker condition.
Action taken: Logged. No submitter agent spawned. No other commits.
Next cycle: Same short-circuit until `connectedAt` advances.

## 2026-06-01 — v281 failed mid-form (NO clips generated)

Reason: Chrome MCP extension disconnected mid-form during v281 submit, BEFORE Create button was clicked. Submitter explicitly reports `Create NOT clicked` — server-side state unchanged.
State: Draft YAML at `prompts/tma-v281.yaml` (Russian phonk / drift phonk / Russian-language hyperpop 155 BPM, F minor, male shouty distorted Russian-language MC — 22nd orthogonal voice; Russian = 17th language, biggest unfilled major-language gap). Style 965, lyrics 825, exclude 929, blocklist clean. **NOT committed** — BACKLOG GUARD's `latest_yaml_uncommitted: true` will auto-trigger a retry on next cycle.
Action taken: Aborted per constraint #4. No retry this cycle. No log of partial form fill confused with successful generation — submitter was explicit that Create was never clicked.
Next cycle should: `python3 scripts/cycle_start.py` will return `recommended_action: resume_submit` for v281. Retry submit directly via `/suno prompts/tma-v281.yaml`. No need to check suno.com/me first — Create was confirmed NOT clicked, so no duplicate-clip risk exists.

RESOLVED (2026-06-01): Retry succeeded next cycle. v281 submitted as UUID 6cee6922-7128-4061-9aaf-fba7a0ff226f, classifier correctly identified as "Russian phonk, drift phonk, hyperpop" with Similar Songs panel surfacing other Russian phonk tracks. **Notable anomalies on this submit:** (1) only 1 clip generated (second consecutive cycle with this — v280 also generated 1 not 2; possible Suno-side behavior change), (2) audio encoding took 15+ minutes and was still pending when submitter exited (publish step blocked until encoding completes; user can publish manually later), (3) vocal_gender UI defaulted to **neither selected** (new failure mode beyond Male-default and Female-default — see `feedback_vocal_gender_ui_quirk.md` v281 entry). Closed out via `finish_cycle.py --version 281`.

## 2026-06-01 — v271 failed mid-submit (AMBIGUOUS — verify before retry)

Reason: Chrome MCP extension disconnected mid-form AFTER the Create button click. The first 10-second post-Create wait completed (page was generating, typical Suno render behavior). Tab 786912814 then disappeared from the MCP tab group. Submitter reports `browser_disconnected_midform`.
State: Draft YAML at `prompts/boteco-v271.yaml` (Sertanejo universitário / sofrência ballad 88 BPM, G major, male DUO close harmony Brazilian caipira PT — twelfth orthogonal viral-arm voice; first male-duo architecture). Style 888, lyrics 894, exclude 777, blocklist clean — pre-validated via `scripts/yaml_field_check.py`. **NOT committed** — but BACKLOG GUARD's auto-retry MUST NOT FIRE for this entry, because clips may already exist server-side.
Action taken: Aborted per constraint #4. No retry this cycle.
AMBIGUITY: Suno may have generated 2 "Boteco" clips server-side already (Create was clicked and acknowledged). Blind retry would create duplicate clips and double-charge credits.
Next cycle should: BEFORE running cycle_start.py or treating this as a normal resume, the operator (or the next cycle's first action) must navigate to suno.com/me (the user's workspace) and check whether two "Boteco" clips already exist. Two paths:
  (a) If "Boteco" clips exist on suno.com/me: harvest the two UUIDs, manually publish them via the song page More menu, then close out with `python3 scripts/finish_cycle.py --version 271 --clips <UUID1> <UUID2> --technique "sertanejo universitário / sofrência ballad viral cycle - male duo harmony caipira PT" --key "G major" --bpm 88 --trio "violão + sanfona + upright bass"`.
  (b) If NO "Boteco" clips exist: the Create click never landed; safe to retry submit with `/suno prompts/boteco-v271.yaml`.

RESOLVED (2026-06-01): Chrome MCP tab group was missing entirely (root cause of the whole multi-cycle outage — bridge "connected" but no tab group meant no controllable tabs). Recovery: `tabs_context_mcp({createIfEmpty: true})` created a fresh MCP window/tab group; navigated to suno.com/me; verified no "Boteco" clips existed (Path b applied); retried submit. v271 submitted + both clips published: de515cb4-3c20-4bf8-accf-5ae730628e5f (1:46) and 2438525f-4fd4-4282-aff8-34c81a5678ee (1:46). Suno classified as `sertanejo universitário, sofrência, country/sertanejo ballad` — no drift. Closed out via `finish_cycle.py --version 271`.

## 2026-06-01 — v270 failed at submit

Reason: Chrome MCP bridge bound to localhost-only tab when v270 cycle fired — no suno.com tab in the MCP-controlled group. Bridge state at draft start: 2 tabs (localhost:8765 + Tóxico song page). Bridge state at submit check: 1 tab (localhost:8765 only — Tóxico tab was closed mid-cycle).
State: Draft YAML at `prompts/wahala-v270.yaml` (Afrobeats / Nigerian Afro-fusion 105 BPM, F minor, male falsetto-mix Pidgin-Yoruba-English — eleventh orthogonal viral-arm voice; first falsetto register; pivoted from planned Mandopop direction in direct response to user mid-cycle directive "Make it Viral" — AfroBeats is currently #1 global TikTok-viral lane in 2026). Style 920, lyrics 926, exclude 711, blocklist clean — pre-validated via `scripts/yaml_field_check.py`. **NOT committed** — left uncommitted so BACKLOG GUARD auto-retries on next cycle with live bridge.
Action taken: Aborted submission per constraint #4. No retry this cycle.
Next cycle should: `python3 scripts/cycle_start.py` will return `latest_yaml_uncommitted: true` and `recommended_action: resume_submit` — submit `prompts/wahala-v270.yaml` directly. Close-out: `python3 scripts/finish_cycle.py --version 270 --clips <UUID1> <UUID2> --technique "Afrobeats / Nigerian Afro-fusion / falsetto male" --key "F minor" --bpm 105 --trio "Yoruba talking drum + 808 sub + electric piano"`.

RESOLVED (2026-06-01): User reconnected the Chrome bridge ("try now") and triggered a manual retry. v270 submitted + both clips published: 08e1a591-c7de-4832-ab0b-8f11d62d8281 (2:23) and 9e7f5067-f8bd-443b-b955-3291260553d8 (2:02). Suno classified as `Afrobeats, Afropop, Nigerian Afro-fusion` — no drift. Closed out via `finish_cycle.py --version 270`.

## 2026-06-01 — v265 failed at submit

Reason: Chrome MCP extension is connected to a localhost:8765 tab only. The suno.com/create tab is in a separate Chrome window outside the MCP tab group, so the extension cannot navigate or fill it. Submitter (`suno-submitter`) reported `browser_disconnected` after find/read_page attempts confirmed no controllable suno.com tab.
State: Draft YAML at `prompts/fervo-v265.yaml` (Funk carioca / baile funk / tamborzão 150 BPM, G minor, shouty assertive female Portuguese MC — sixth orthogonal viral-arm voice). Style 945, lyrics 915, exclude 405, blocklist clean — all fields pre-validated via `scripts/yaml_field_check.py`. **Committed at user request (2026-06-01)** to clear the dirty working tree — this means the BACKLOG GUARD's `latest_yaml_uncommitted` check will NOT auto-trigger a retry. v265 is NOT submitted to Suno; clip UUIDs are NOT in `docs/suno_urls.json`; the site catalog still shows only through v264.
Action taken: Aborted submission per constraint #4 — no retry. No log of partial form fill (the submitter never reached the form).
Next cycle should: Because v265 is committed but NOT submitted, the runbook's auto-resume logic will skip it. The next cron will draft v266 fresh unless this entry is acted on. To recover v265: open suno.com/create in a Chrome window the MCP extension actually controls, confirm `list_connected_browsers` returns a tab with `suno.com/create` URL, then manually invoke `/suno prompts/fervo-v265.yaml` followed by `python3 scripts/finish_cycle.py --version 265 --clips <UUID1> <UUID2> --technique "funk carioca / baile funk / tamborzão viral cycle - shouty female Portuguese MC" --key "G minor" --bpm 150 --trio "tamborzão 808 kick + tambor/surdo + baile siren"`.

Retry attempt 1 (2026-06-01, next cron fire): same disconnect state. MCP tab group contains `localhost:8765` and `tiktok.com/tiktokstudio/upload` — no suno.com tab present. YAML still unchanged on disk. Exited per constraint 4; did NOT draft v266 since v265 recovery remains pending.

Retry attempt 2 (2026-06-01, next cron fire): same disconnect state — identical tab list (localhost:8765 + tiktok.com/tiktokstudio/upload). YAML unchanged. Exited per constraint 4; still not drafting v266.

Retry attempt 3 (2026-06-01, next cron fire): same disconnect state — same two tabs (localhost:8765 + tiktok.com/tiktokstudio/upload). YAML unchanged. Exited per constraint 4. v266 still not drafted.

Retry attempt 4 (2026-06-01, next cron fire): same disconnect state — same two tabs. YAML unchanged. Exited per constraint 4. v266 still not drafted.

Retry attempt 5 (2026-06-01, next cron fire): same disconnect state — same two tabs. YAML unchanged. Exited per constraint 4. v266 still not drafted.

RESOLVED (2026-06-01): User reconnected the Chrome bridge to a suno.com tab and triggered a manual retry. v265 submitted + both clips published: 3639f9b3-e042-4356-9cfb-c28b3295cab5 (2:07) and 103106a9-1a7d-4f7d-9451-1535b0e0f2a5 (2:00). Suno classified as `funk carioca, baile funk, street rap` — no drift. Closed out via `finish_cycle.py --version 265`.

## 2026-04-13 — v131 failed at submit

Reason: Chrome MCP extension disconnected. `open -a "Google Chrome" https://claude.ai` attempted, extension still not connected on retry.
State: Draft YAML at `prompts/the-shape-probability-takes-v131.yaml` (943 chars, judge ~97/100, orchestral stochastic, prepared piano + contrabass clarinet + tuba, E minor → F minor, 94 BPM). Not committed, not submitted.
Action taken: Aborted submission per constraint #4. No retry.
Next cycle should: Either (a) reuse this draft and submit when extension reconnects, or (b) let user submit manually via `/suno prompts/the-shape-probability-takes-v131.yaml` from an active session.
Resolution: v131 submitted later in same session (after user rejoined and extension reconnected). 2 clips recorded in docs/suno_urls.json.

## 2026-04-13 — v132 failed at submit

Reason: Chrome MCP extension disconnected at draft-complete / pre-submit. One reconnect attempt via `open -a "Google Chrome" https://claude.ai` — still disconnected. No second retry per constraint.
State: Draft YAML at `prompts/the-intervals-your-ear-forgot-v132.yaml` (932 chars, judge ~98/100, orchestral quarter-tone microtonal, cristal baschet + cimbalom + piccolo, C# → D major, 106 BPM). Committed but NOT submitted.
Action taken: Aborted submission per constraint #4. Committed + pushed the draft so next session / cron can pick it up.
Next cycle should: Before drafting v133, check whether v132 has been submitted to Suno; if not, submit v132 first via `/suno prompts/the-intervals-your-ear-forgot-v132.yaml`.
Resolution: v132 submitted on the next cron fire (browser reconnected). Clips 0:28 + 0:13 — microtonal description also shortens durations even with tonal framing. Noted for evolution.md. URLs recorded in suno_urls.json. **Duration finding: quarter-tone/microtonal language shortens Suno output, like v130 atonal.** Tonal key signatures alone don't protect against it.

## 2026-04-13 — v134 failed at submit (form partially filled)

Reason: Chrome MCP extension dropped mid-type on the title field. Lyrics + style + exclude_styles already entered. Title field had old v133 title still showing, triple-click attempted, then disconnect before new title typed.
State: Form partially populated in tab 786902650. Draft YAML at `prompts/the-line-you-only-hear-together-v134.yaml` committed.
Action taken: Aborted per constraint #4. No retry.
Next cycle should: Check if the Suno tab still has the v134 form. If yes, finish title + Create. If workspace rebuilt, resubmit fresh via `/suno prompts/the-line-you-only-hear-together-v134.yaml`.

## 2026-04-15 v143 submit — browser disconnect
step: submit
yaml: prompts/where-the-chase-keeps-answering-v143.yaml
judge_score: 99
reason: Chrome MCP extension not connected at submission time (after successful publish cycle + v142 submit in same session). Draft + judge pass is preserved; next cron fire picks it up or resubmits.

## 2026-04-15 v144 submit — browser disconnect (same session)
step: submit
yaml: prompts/before-the-gears-agree-v144.yaml
judge_score: 99
reason: Chrome MCP still not connected on this hourly fire. v143 also pending. Two drafts queued.

## 2026-04-17 v146 submit — browser still disconnected
step: submit
yaml: prompts/everything-the-climb-was-for-v146.yaml
judge_score: ~98 (self-assessed, all 12 criteria pass)
reason: Chrome MCP extension still not connected. v143, v144, v145, v146 all queued. User has been asked to re-enable extension.
backlog: v143 (caccia), v144 (phase-process), v145 (romantic piano), v146 (triumphant symphony)

## 2026-04-18 v175 submit — Create button not responding
step: submit
yaml: prompts/built-from-broken-machines-v175.yaml
reason: Create button clicked multiple times but workspace shows no generating songs. Possible credit exhaustion or Suno rate limit after 27 songs in this session. YAML saved, next session can retry.

## 2026-04-19 17:30 — v192 failed at submit

Reason: Chrome MCP extension disconnected during submission attempt
State: v192 YAML drafted at prompts/the-dance-that-stopped-mid-phrase-v192.yaml, not submitted to Suno
Action taken: Logged failure, will commit draft and push. Next cycle should reconnect and submit.
Next cycle should: Open claude.ai to reconnect extension, then submit v192 before drafting v193

## 2026-04-20 10:00 — v194 failed at submit

Reason: Chrome MCP extension disconnected during submission attempt
State: v194 YAML drafted at prompts/the-sound-that-iron-remembers-v194.yaml, not submitted
Action taken: Logged failure, committing draft and pushing. Next cycle should reconnect and submit.
Next cycle should: Open claude.ai to reconnect, then submit v194 before drafting v195

## 2026-05-19 v212 submit — Suno service outage
step: submit
yaml: prompts/where-the-candle-learns-its-name-v212.yaml
judge_score: 96/100 (passed)
reason: Suno returned "Song generation is temporarily unavailable. Please try again shortly." on every Create attempt. ~8 retries over ~15 minutes. Browser extension stays connected throughout; form is correctly filled (style 947/1000, title "Where the Candle Learns Its Name", lyrics/exclude intact). Server-side outage, not a form or browser issue.
state: Form loaded and ready in tab 786909863 at https://suno.com/create. YAML committed.
next_cycle: Reload suno.com/create, re-fill form from YAML, retry Create when service recovers.

## 2026-05-26 — v223 failed at submit

Reason: Chrome MCP extension disconnected — could not reach suno.com/create after one connection retry.
State: `prompts/what-one-reed-remembers-v223.yaml` exists on disk (untracked), judged 96/100 by the suno-judge subagent, awaiting submission. Concept: CLIMAX-AT-THE-FRONT arc with chalumeau (catalog debut) + tuba + theremin, stable B minor, 139 BPM, "What One Reed Remembers". Title is fresh, all gating passed; only the submit step is blocked.
Action taken: Aborted the cycle per runbook ("Never auto-retry submissions"). Nothing committed. No `docs/suno_urls.json` or `evolution.md` change. The YAML is preserved untracked so the work isn't lost — submission can be retried by re-running the suno-submitter agent against the same path once the Chrome extension is reconnected.
Next cycle should: if v223 is still on disk untracked when the next cron fires (`17 * * * *`), retry the submit step on it (skip the research/draft/judge stages — they're already done). Only draft a fresh v224 if v223 was committed or removed in the meantime.

### 2026-05-26 — v223 retry-attempt — still disconnected

Reason: Explicit retry run against this same YAML. `open -a "Google Chrome" https://claude.ai` issued; tabs_context_mcp called again — still returns "Browser extension is not connected." One reconnect attempt exhausted per runbook; no second retry within this run.
State: `prompts/what-one-reed-remembers-v223.yaml` still untracked on disk, unchanged. Form never opened.
Action taken: Logged retry failure. YAML preserved untracked. No commits.
Next cycle should: Reconnect Chrome extension manually, then re-run submitter against `prompts/what-one-reed-remembers-v223.yaml`.


## 2026-05-26 — v223 submission retry failed

- **Prompt**: prompts/what-one-reed-remembers-v223.yaml
- **Title**: What One Reed Remembers
- **Reason**: browser_disconnected — extension not connected after one retry attempt (open claude.ai → re-check)
- **Context**: User had manually reconnected extension prior to request, but extension was still reporting disconnected at submission time
- **Action**: No further auto-retry per instructions. User is actively monitoring.

### 2026-05-26 — cron fire, no-op — bridge still down

Reason: `list_connected_browsers` returned `[]` at the top of the cycle — Chrome extension not bridged to this Claude session. Short-circuited before research/draft/judge to avoid spending an agent chain on a submit that cannot land. Per [[reconnect_chrome.sh]] flow run last hour, the helper did not re-establish a bridge.
State: `prompts/what-one-reed-remembers-v223.yaml` still on disk, untracked, judged 96/100. Three consecutive submit attempts across two cron hours have all failed at the bridge check.
Action taken: Logged. No agents spawned. No commits beyond this log.
Next cycle should: Same short-circuit. Only run the full pipeline (or the v223 retry) when `list_connected_browsers` returns at least one entry. User must reconnect the extension manually (extension icon in Chrome toolbar / chrome://extensions toggle / signed-in claude.ai session).

## 2026-05-26 — v223 submission attempt failed

- **YAML**: prompts/what-one-reed-remembers-v223.yaml
- **Reason**: browser_disconnected — `tabs_context_mcp` returned "No MCP tab groups found" on both attempts (before and after `open -a "Google Chrome" https://claude.ai`)
- **Context**: user reported bridge was restored (deviceId 62ca1d8e-68b7-4185-8507-d91a6f58a81c), but MCP tab group was never established; extension may need manual re-pin or page reload in Chrome
- **Action taken**: clean exit per protocol, no form was touched
- **Next step**: user should open Chrome, navigate to a tab, confirm the Claude Code extension icon is active, then retry submission

### 2026-05-27 — "continue" retry on v223, bridge still down

Reason: User-driven retry. `list_connected_browsers` returned `[]`. Issued `open -a "Google Chrome" https://claude.ai` and re-checked — still `[]`. Per runbook cap (one reconnect attempt per cycle), short-circuited.
State: `prompts/what-one-reed-remembers-v223.yaml` still untracked on disk, judge 96/100, four consecutive submit attempts now blocked at the bridge check.
Action taken: Logged. No agents spawned. No commits beyond this entry.
Next cycle should: Same short-circuit until `list_connected_browsers` returns at least one entry. User needs to manually re-pin the extension (Chrome toolbar icon, chrome://extensions toggle, or refresh a logged-in claude.ai tab) — the helper-open has not been sufficient across these four attempts.

## 2026-06-02 — v304 failed at submit (partial-disconnect state)

- **YAML**: prompts/ukufa-v304.yaml
- **Title**: Ukufa
- **Judge**: 97/100 (passed)
- **Concept**: Zulu isicathamiya × cinematic orchestral ballad, ABSOLUTE family-first Bantu (34th language, 45th orthogonal voice), uhadi (catalog debut) + bass flute + string orchestra, A minor → Bb minor at climax, 74 BPM
- **Reason**: Chrome MCP bridge in partial-disconnect state — `list_connected_browsers` returned Browser 1 (deviceId 62ca1d8e-68b7-4185-8507-d91a6f58a81c), `tabs_context_mcp` returned a tab at suno.com/create, but every `executeScript` injection into the Suno tab timed out after 45s. Submitter tried Escape, `open -a Chrome https://suno.com/create`, and `open -a Chrome https://claude.ai` reconnect — none cleared the block. Tab visible, scripts unreachable.
- **State**: `prompts/ukufa-v304.yaml` exists on disk untracked, judged 97/100, no form fields touched. No clip UUIDs created. No commit run (finish_cycle.py never invoked).
- **Action taken**: Submitter returned failed status; clean exit per safety floor "do NOT retry." No further submit attempts within this cycle.
- **Next cycle should**: Per BACKLOG GUARD, treat `prompts/ukufa-v304.yaml` as the resume target. If `list_connected_browsers` returns ≥1 entry AND `executeScript` works on the suno.com/create tab, retry the submit step against this YAML (skip research/draft/judge — already done). If executeScript still times out, log a retry-failure entry and exit without drafting v305.
- **User-side fix that may help**: refresh or re-pin the Claude Code Chrome extension icon (chrome://extensions toggle, or close + reopen the suno.com/create tab so the extension re-injects). The `list_connected_browsers` check is necessary but not sufficient — the bridge can report connected while still being unable to inject scripts.

### 2026-06-02 — v304 retry-attempt 2 (this cycle) — partial-disconnect persists

- **Reason**: Second consecutive executeScript timeout. `tabs_context_mcp` returned tab 786913118 (suno.com/create) in the MCP group, bridge deviceId 62ca1d8e-68b7-4185-8507-d91a6f58a81c confirmed connected. Three consecutive `read_page`/screenshot probes each timed out at 45s ("Page still loading — executeScript waited 45000ms for document_idle"). Tab title still shows "Suno | AI Music" — page is rendering to the user but extension cannot inject scripts.
- **State**: `prompts/ukufa-v304.yaml` unchanged on disk (untracked), no form fields touched, no clips generated.
- **Action taken**: Logged second consecutive partial-disconnect per pre-flight protocol ("do NOT loop on it"). Clean exit.
- **Root cause hypothesis**: suno.com/create tab may have a Service Worker or navigation state that blocks content-script injection even when the bridge device is "connected." Closing and reopening the suno.com/create tab (not just refreshing) may allow fresh content-script injection.
- **User-side fix**: Close the suno.com/create tab entirely in Chrome, open a new one to https://suno.com/create, confirm the Claude Code extension icon is active in that new tab, then re-trigger submission.

### 2026-06-02 — v304 retry-attempt 3 (RETRY-3, fresh-tab protocol) — hard-reload transient then stuck

- **Protocol applied**: RETRY-3 brief instructed fresh-tab protocol (close stale tab, reuse via hard reload since tabs_close_mcp/tabs_create_mcp not available in tool set).
- **Sequence**:
  1. `tabs_context_mcp` → tab 786913118 (suno.com/create) present, same stale tab from prior cycles.
  2. Screenshot probe → timed out 45s (stale tab confirmed stuck).
  3. `cmd+shift+r` (hard reload) → waited 10s → screenshot succeeded once (form visible, Advanced tab selected, Lyrics empty, Styles placeholder, Create button visible). Pre-flight PASSED momentarily.
  4. Attempted `read_page` (interactive) to get form refs → timed out 45s.
  5. Waited 10s → `read_page` again → timed out 45s.
  6. Screenshot → timed out 45s. Tab re-entered loading loop.
  7. Escape key → waited 15s → screenshot → timed out 45s. Permanent.
- **Root cause refined**: Hard reload clears the stuck state long enough for one screenshot, but any subsequent tool call (read_page, type, key) triggers a new navigation event in the React SPA that the content script cannot settle. The extension waits for `document_idle` but the SPA's Service Worker keeps deferring it indefinitely after any interaction.
- **State**: `prompts/ukufa-v304.yaml` unchanged on disk (untracked), no form fields touched, no clips generated.
- **Action taken**: Logged third consecutive partial-disconnect. Clean exit per protocol.
- **Critical user-side fix needed**: The `cmd+shift+r` approach cannot work — it reloads into the same Service Worker context. The ONLY fix that will work is: (1) Open Chrome DevTools on the suno.com/create tab → Application → Service Workers → "Unregister" the SW, OR (2) Close the tab entirely, clear site data for suno.com (chrome://settings/content/all → suno.com → Delete), then open a fresh suno.com/create tab. After that, confirm the Claude Code extension icon is active (badge visible) in the new tab before re-triggering.
- **Alternative**: If Chrome is restarted entirely between cron cycles, the Service Worker cache is cleared automatically and fresh injection should work.
