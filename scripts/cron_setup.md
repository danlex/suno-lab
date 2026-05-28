# Cron setup — recreate after session restart

Session-only crons die when Claude exits. After starting a fresh session in this repo, ask Claude to re-register these (it can use `CronCreate`).

## 1. Suno cycle — every 15 minutes (at :07/:22/:37/:52)

**Schedule:** `7,22,37,52 * * * *` (true 15-min cadence, offset off the :00/:15/:30/:45 marks to dodge congested minute boundaries)

Updated 2026-05-28 from the prior hourly `17 * * * *` per user request ("upload one every 15 minutes"). Note: recurring crons are session-only (the `durable` flag does not persist to disk) and auto-expire after 7 days — re-register at session start and watch the 7-day window.

**Prompt:**

```
Run the autonomous Suno cycle. Working directory: /Users/adan/work/claude/code/suno

Read and follow scripts/hourly_cycle_prompt.md exactly — it contains the full steps (research → refresh novelty_surface → draft v### → judge ≥90 → submit via suno-submitter → scripts/finish_cycle.py to build_site + log + commit + push), the safety floors (no blocklist words, failure log format, no destructive retries), and the 3-min arc templates.

Hard constraints for every new prompt:
1. **Song duration: 2:30 to 3:30 (target ~3:00).** Include a duration cue in the first 200 chars of the style field. All timestamps must fit within 0:00–3:30.
2. Auto-submit is authorized per feedback_cron_auto_submit_override.md — do not pause to ask the user, they are not in session.
3. Judge score must be ≥90 before submission. If judge stalls below 90 after 5 iterations, log to experiments/cron_failures.md and exit without submitting.
4. If the Chrome MCP extension is disconnected (list_connected_browsers returns []) or suno.com is unreachable, log to experiments/cron_failures.md with step="submit" and exit — do not retry. The next cron fire will try again.
5. Close-out is MANDATORY via the reusable script: `python3 scripts/finish_cycle.py --version <N> --clips <uuid1> <uuid2> --technique "..." --key "..." --bpm <bpm> --trio "..."`. No vanilla one-off bash/python for deterministic steps (CLAUDE.md "Scripting discipline"). If push fails, log and exit.
6. Before drafting, always run `python3 scripts/novelty_surface.py` and consult experiments/novelty_surface.json to verify novelty claims.

Next version number: run `python3 scripts/cycle_start.py` (reusable script) and read `next_version` from its JSON output — it also refreshes the novelty surface. Do NOT compute the version with inline `ls`/`grep` bash, and do NOT hardcode it (CLAUDE.md "Scripting discipline").
```

## 2. Secondary Suno cycle (every 2 hours at :13)

**Schedule:** `13 */2 * * *`

**Prompt:** same as above.

Consider removing this one — it overlaps with the hourly on even hours and leads to double submissions.

## 3. Daily review & publish cycle (every day at 2:47 AM)

**Schedule:** `47 2 * * *`

**Prompt text not captured in this session.** If restarting loses it, recreate from `scripts/review_cycle_prompt.md` (or reconstruct from README instructions).

## Why session-only

`CronCreate` with `durable: true` did not actually persist to `.claude/scheduled_tasks.json` in testing (2026-04-13) — the file was never written. All crons behave as session-only regardless of the flag. Until that's fixed upstream, re-registration after restart is manual.
