# Cron failure log

## 2026-06-01 — v265 failed at submit

Reason: Chrome MCP extension is connected to a localhost:8765 tab only. The suno.com/create tab is in a separate Chrome window outside the MCP tab group, so the extension cannot navigate or fill it. Submitter (`suno-submitter`) reported `browser_disconnected` after find/read_page attempts confirmed no controllable suno.com tab.
State: Draft YAML at `prompts/fervo-v265.yaml` (Funk carioca / baile funk / tamborzão 150 BPM, G minor, shouty assertive female Portuguese MC — sixth orthogonal viral-arm voice). Style 945, lyrics 915, exclude 405, blocklist clean — all fields pre-validated via `scripts/yaml_field_check.py`. **Committed at user request (2026-06-01)** to clear the dirty working tree — this means the BACKLOG GUARD's `latest_yaml_uncommitted` check will NOT auto-trigger a retry. v265 is NOT submitted to Suno; clip UUIDs are NOT in `docs/suno_urls.json`; the site catalog still shows only through v264.
Action taken: Aborted submission per constraint #4 — no retry. No log of partial form fill (the submitter never reached the form).
Next cycle should: Because v265 is committed but NOT submitted, the runbook's auto-resume logic will skip it. The next cron will draft v266 fresh unless this entry is acted on. To recover v265: open suno.com/create in a Chrome window the MCP extension actually controls, confirm `list_connected_browsers` returns a tab with `suno.com/create` URL, then manually invoke `/suno prompts/fervo-v265.yaml` followed by `python3 scripts/finish_cycle.py --version 265 --clips <UUID1> <UUID2> --technique "funk carioca / baile funk / tamborzão viral cycle - shouty female Portuguese MC" --key "G minor" --bpm 150 --trio "tamborzão 808 kick + tambor/surdo + baile siren"`.

Retry attempt 1 (2026-06-01, next cron fire): same disconnect state. MCP tab group contains `localhost:8765` and `tiktok.com/tiktokstudio/upload` — no suno.com tab present. YAML still unchanged on disk. Exited per constraint 4; did NOT draft v266 since v265 recovery remains pending.

Retry attempt 2 (2026-06-01, next cron fire): same disconnect state — identical tab list (localhost:8765 + tiktok.com/tiktokstudio/upload). YAML unchanged. Exited per constraint 4; still not drafting v266.

Retry attempt 3 (2026-06-01, next cron fire): same disconnect state — same two tabs (localhost:8765 + tiktok.com/tiktokstudio/upload). YAML unchanged. Exited per constraint 4. v266 still not drafted.

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
