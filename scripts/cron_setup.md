# Cron setup — recreate after session restart

Session-only crons die when Claude exits. After starting a fresh session in this repo, ask Claude to re-register these (it can use `CronCreate`).

## 1. Hourly Suno cycle (every hour at :17)

**Schedule:** `17 * * * *`

**Prompt:**

```
Run the autonomous Suno cycle. Working directory: /Users/adan/work/claude/code/suno

Read and follow scripts/hourly_cycle_prompt.md exactly — it contains the full steps (research → refresh novelty_surface → draft v### → judge ≥90 → /suno submit → build_site → commit → push), the safety floors (no blocklist words, failure log format, no destructive retries), and the 3-min arc templates.

Hard constraints for every new prompt:
1. **Song duration: 2:30 to 3:30 (target ~3:00).** Include "total duration around 3:00" (or "2:30 to 3:30 film cue" / "three-minute miniature") in the first 200 chars of the style field. All timestamps must fit within 0:00–3:30. Use the 3-min arc template in scripts/hourly_cycle_prompt.md. This supersedes the earlier 1–2 min cap (see memory feedback_song_duration_one_minute.md).
2. Auto-submit is authorized per feedback_cron_auto_submit_override.md — do not pause to ask the user, they are not in session.
3. Judge score must be ≥90 before submission. If judge stalls below 90 after 5 iterations, log to experiments/cron_failures.md and exit without submitting.
4. If the Chrome MCP extension is disconnected or suno.com is unreachable, log to experiments/cron_failures.md with step="submit" and exit — do not retry. The next cron fire will try again.
5. Commit + push are mandatory. If push fails, log and exit.
6. Before drafting, always run `python3 scripts/novelty_surface.py` and consult experiments/novelty_surface.json to verify novelty claims.

Next version number: read `ls prompts/ | grep -oE 'v[0-9]+' | sort -V | tail -1` and add 1. Do not hardcode a version — always compute from the filesystem.
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
