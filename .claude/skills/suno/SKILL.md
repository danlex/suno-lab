---
name: suno
description: Post a prompt to Suno AI via browser automation at suno.com/create in Custom mode
---

# Suno — Post Prompt to Browser

Submit a song prompt to Suno via Chrome browser automation.

## Arguments

`/suno <path-to-yaml-prompt-file>`

If no file is given, read the most recently modified YAML file in `prompts/`.

## YAML Prompt Format

```yaml
name: "song-name"
version: 1
style: "genre, mood, instruments..."       # Max 1000 chars
title: "Song Title"                         # Optional field below More Options in Suno UI
lyrics: |
  [Intro]
  ...
  [End]
instrumental: false
vocal_gender: female                        # Optional: "female" or "male"
exclude_styles: "Arabic, rock, electronic"  # Optional: styles to exclude
notes: "What changed in this version"
tags: [genre, experiment-name]
```

## Process

1. **Read the prompt YAML file.** Fields: `style`, `title`, `lyrics`, `instrumental`, `vocal_gender`, `exclude_styles`.

2. **Run the Judge.** Evaluate the prompt against `/judge` criteria (9 dimensions, score 0-100). If score < 90, iterate on weak criteria (up to 5 rounds) before proceeding. Only submit prompts scoring >= 90.

3. **Check style character count.** The style field has a **1000 character limit**. If the style text exceeds 1000 chars:
   - Preserve the first ~200 chars (genre anchor — most important for Suno)
   - Preserve the last ~150 chars (negative prompts, key, BPM — critical)
   - Trim from the middle, removing less essential descriptive phrases
   - Report the final character count

3. **Load browser tools** via ToolSearch (`select:mcp__claude-in-chrome__tabs_context_mcp`, etc.).

4. **Get browser state.** Call `tabs_context_mcp` (use `createIfEmpty: true` if needed).

5. **Navigate to `https://suno.com/create`.** Create a new tab or reuse one already on suno.com. **Wait 3-5 seconds** for the page to load — use `screenshot` or `read_page` to confirm the UI is ready before interacting. If you see "Something went wrong", refresh the page and wait again.

6. **Ensure Advanced mode is active** (look for the "Advanced" tab at the top, click if needed). Note: Suno calls Custom mode "Advanced" in the UI.

7. **Fill fields in this order:**
   - **Lyrics**: Click the lyrics textarea, enter the `lyrics` value. Preserve all metatags (`[Verse]`, `[Chorus]`, `[Silence]`, etc.) and line breaks exactly as written.
   - **Style**: Click the styles textarea, select all (Cmd+A), then type the `style` value to replace any existing text. After entering, Suno shows clickable tag suggestions below — do **NOT** click these as they may override the custom style.

8. **Set More Options** (click "More Options" to expand):
   - **Exclude Styles**: If `exclude_styles` is set in YAML, enter it in the "Exclude styles" field. This provides double reinforcement of negative prompts.
   - **Vocal Gender**: If `vocal_gender` is set in YAML, or if the style mentions soprano/female/woman, click "Female". If it mentions male/baritone/tenor, click "Male".

9. **Fill Title** (scroll down below More Options):
   - **Title**: Find the "Song Title (Optional)" field. Enter the `title` value from YAML if provided.

10. **Click the Create button.** This generates 2 song versions.

11. **Report back** that the prompt was submitted with the song title.

## Error Handling

- **"Something went wrong"**: Refresh the page (`navigate` to suno.com/create again), wait 3-5 seconds, retry from step 6.
- **Login required**: Inform the user and stop. Do not attempt to log in.
- **Page not loading**: Wait up to 10 seconds. If still not loaded, inform the user to check their browser.
- **Browser extension disconnected**: Open claude.ai yourself by running `open -a "Google Chrome" https://claude.ai` via Bash. Wait 5 seconds, then retry. Never ask the user to do this.

## Important

- Do NOT generate or modify prompt content. The user provides all prompt content.
- Preserve all metatags and formatting exactly as written.
- Each generation costs credits — always confirm with the user before clicking Create if there's any ambiguity.
- Style must be under 1000 characters. Check BEFORE entering into the browser.
