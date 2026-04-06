# Suno AI Prompt Research: Best Practices, Collections, and Copy-Paste Examples

Research compiled March 2026 from 20+ sources including GitHub repos, Medium articles, community guides, and official Suno documentation.

---

## Table of Contents

1. [Community Prompt Collections & Resources](#1-community-prompt-collections--resources)
2. [The Universal Prompt Formula](#2-the-universal-prompt-formula)
3. [Best-Rated Style Prompts by Genre](#3-best-rated-style-prompts-by-genre)
4. [Complete Song Prompts (Style + Lyrics with Metatags)](#4-complete-song-prompts-style--lyrics-with-metatags)
5. [Advanced Prompt Techniques](#5-advanced-prompt-techniques)
6. [Metatag Reference](#6-metatag-reference)
7. [10 Prompt Patterns That Never Miss (v5)](#7-10-prompt-patterns-that-never-miss-v5)
8. [GitHub Projects & Tools](#8-github-projects--tools)
9. [Key Principles & Anti-Patterns](#9-key-principles--anti-patterns)

---

## 1. Community Prompt Collections & Resources

### GitHub Repositories

| Repository | Description | URL |
|---|---|---|
| **daveshap/suno** | Suno prompts for use with Claude/ChatGPT. Metatag modifiers, style construction, album art prompts, rhythm notation. | https://github.com/daveshap/suno |
| **naqashmunir21/awesome-suno-prompts** | 1000+ professional style prompts organized by genre with production tips. | https://github.com/naqashmunir21/awesome-suno-prompts |
| **Marcus-Arcadius/Suno_Prompts** | Comprehensive collection including "The Ultimate Suno Mastering Prompt List", real-world examples of successful prompts, community-contributed prompts, and procedural audio techniques. | https://github.com/Marcus-Arcadius/Suno_Prompts |
| **Zizwar/Awesome-Suno** | Curated list of 60+ open-source Suno AI projects (APIs, tools, bots, downloaders). | https://github.com/Zizwar/Awesome-Suno |
| **develephant/suno-songtags** | Collected song tags for steering Suno AI with documentation site. | https://github.com/develephant/suno-songtags |
| **bitwize-music-studio/claude-ai-music-skills** | 52 Claude Code skills for automated music production: concept development, lyrics, Suno prompts, audio mastering, release prep. 72 genre directories. | https://github.com/bitwize-music-studio/claude-ai-music-skills |
| **AlijeeWrites/suno-ai-prompts-book-pdf-2026-guide** | 3,500+ style tags, cheat sheets, v5/v6 prompting secrets. | https://github.com/AlijeeWrites/suno-ai-prompts-book-pdf-2026-guide |
| **EA914/Suno-AI-Prompt-Dictation** | Python tool: dictate prompts via voice, auto-generate songs. | https://github.com/EA914/Suno-AI-Prompt-Dictation |

### Web Tools & Generators

| Tool | Description | URL |
|---|---|---|
| **SunoPrompt.com** | AI-powered style + lyrics generator. Describe your vision, get complete prompts. | https://sunoprompt.com/ |
| **Suno Meta Tags Creator** | Visual drag-and-drop metatag builder with lyrics generation. | https://sunometatagcreator.com/ |
| **HowToPromptSuno.com** | Comprehensive guide site with voice tags, structure guides, and techniques. | https://howtopromptsuno.com/ |
| **OpenMusicPrompt.com** | 500+ pro tags & templates with metatags guide. | https://openmusicprompt.com/ |
| **HookGenius** | 150+ copy-paste prompts by genre + metatag reference. | https://hookgenius.app/suno-prompts/ |
| **AI Free Forever Suno Prompt Generator** | Free prompt generator tool. | https://aifreeforever.com/tools/suno-prompt-generator |
| **ChatGPT Suno 5.0 Prompt Generator** | Custom GPT for generating Suno v5 prompts. | https://chatgpt.com/g/g-681480f8a4688191b94abd2af3c3390a-suno-5-0-prompt-generator |

### Communities

| Community | Description |
|---|---|
| **Suno Discord** (400K+ members) | Official server: prompt sharing, creation channels, tutorials, theory discussion. https://discord.com/invite/suno |
| **r/SunoAI** (Reddit) | Active community for sharing prompts, techniques, and creations. |
| **Jack Righteous Blog** | Deep-dive prompt engineering series with advanced techniques. https://jackrighteous.com/en-us/pages/suno-prompt-engineering-series |

---

## 2. The Universal Prompt Formula

### The 7-Ingredient Formula (Viral Song Template)

```
[GENRE] + [TEMPO] + [MOOD] + [INSTRUMENT] + [VOCAL STYLE] + [ERA] + [REFERENCE]
```

Example:
```
Indie folk, 92 BPM, melancholic, fingerstyle acoustic guitar, whispered vocals, 2010s, Bon Iver style
```

### The 6-Component Formula (Tested Template)

```
[Mood] + [Genre/Era] + [Key Instruments] + [Vocal Type] + [Production/Mix Tone] + [Tempo/Energy]
```

Example:
```
Modern pop, emotional female vocals, bright synths + acoustic guitar blend, clean radio mix, mid-tempo 102 BPM, uplifting but bittersweet
```

### The 5-Element Formula (Simplified)

```
[Genre] + [Instruments] + [Mood] + [Tempo/Key] + [Special Elements]
```

Example:
```
Epic orchestral soundtrack with grand strings, powerful brass, uplifting mood, 100 BPM, in D major, with choir harmonies and cinematic drums
```

### Sweet Spot: 4-7 Descriptors

- Too few = generic output
- Too many = confused output
- Put primary genre FIRST (Suno weights early words more)
- Front-load your style prompt (early words survive truncation)

### Character Limits

- **Style prompt**: ~200 chars (older models), **1,000 chars on v4.5+**
- **Lyrics prompt**: **3,000 characters** (~200-300 words)

---

## 3. Best-Rated Style Prompts by Genre

### Pop

```
Infectious pop anthem, female powerhouse vocals, pulsing 808 bass, synth-wave layers, euphoric build-ups, radio-ready polish, modern production, vocal harmonies on chorus, BPM: 128, Key: C Major
```

```
Piano-driven ballad, raw emotional vocals, subtle string arrangements, builds from intimate verse to soaring chorus, modern radio production, reverb on vocals, stripped-down bridge, powerful final chorus, BPM: 72, Key: G Major
```

```
Jangly indie-pop, warm lo-fi aesthetic, vintage synths, organic drums, bedroom recording charm, catchy but not over-produced, tape saturation warmth, imperfect and authentic, BPM: 115, Key: A Minor
```

```
Dreamy electro-pop, soft female vocals, shimmering synth layers, side-chained pads, glossy electronic mix, 115 BPM, nostalgic summer vibe
```

```
1980s synth-pop, analog synth bass, gated drums, male lead with reverb-heavy vocals, neon retro energy, 112 BPM
```

```
Dark pop, moody atmosphere, breathy female vocals, minimal production, introspective
```

```
K-pop, energetic, mixed group vocals, dance break, polished production
```

### Rock & Alternative

```
Massive power chords, arena rock production, anthemic chorus, driving rhythm section, guitar solo at 2:15, crowd-ready hooks, distorted guitars, thunderous drums, raw powerful vocals, BPM: 140, Key: E Minor
```

```
Fuzzy distorted guitars, 90s grunge aesthetic, raw anguished vocals, dynamic quiet-loud structure, analog tape grit, genuine angst, stripped-down verse, explosive chorus, feedback and noise, BPM: 95, Key: D Minor
```

```
2000s indie rock, jangly electric guitars, warm male vocals, nostalgic tone, roomy live-band mix, 118 BPM
```

```
Angular guitar riffs, post-punk energy, driving bass lines, unconventional song structure, artistic experimentation, raw emotional delivery, indie rock attitude, gritty production, BPM: 130, Key: B Minor
```

```
Psychedelic rock, trippy effects, swirling organs, experimental, 1960s
```

### Hip-Hop / Rap

```
Hard-hitting 808s, menacing trap beat, rapid hi-hat rolls, atmospheric pads, dark melodic undertones, confident rap flow, ad-libs throughout, hard bass drop, modern rap production, BPM: 75, Key: F Minor
```

```
Classic boom bap drums, vinyl crackle, jazzy piano samples, laid-back smooth flow, storytelling rap, 90s hip-hop nostalgia, warm analog sound, deep bass, conscious lyrics vibe, BPM: 88, Key: E-flat Major
```

```
Moody melodic trap, atmospheric pads, deep 808s, laid-back male rap with melodic hooks, reverb-heavy mix, 78 BPM
```

```
UK drill, sliding 808s, aggressive male rap, dramatic minor-key strings, crisp dark production, 142 BPM
```

```
90s boom-bap, vinyl crackle texture, dusty drums, sample-like jazz chords, storytelling rap, warm analog mix, 88 BPM
```

### Electronic / EDM

```
Massive synth drops, festival-ready energy, pulsing sub-bass, euphoric builds, sidechain compression, crowd-hyping elements, laser synths, punchy kicks, anthem-level production, BPM: 128, Key: C Minor
```

```
Emotional chord progressions, atmospheric builds, lush pads, melodic piano melodies, progressive house evolution, uplifting energy, clean modern production, vocal chops, BPM: 124, Key: A Minor
```

```
Melodic house, airy male vocals, warm sub-bass, uplifting chord progression, festival-ready clean mix, 122 BPM
```

```
Dark warehouse techno, no vocals, rolling bassline, metallic synth stabs, hypnotic repetition, 128 BPM
```

```
Synthwave, 1980s retrofuturism, analog synths, neon aesthetic, driving arpeggios
```

```
Deep house, emotional, melodic synths, hypnotic rhythms, 4-on-the-floor, warm basslines
```

### R&B / Soul

```
Smooth soulful vocals, trap-influenced R&B, sultry vibe, laid-back 808 bass, syncopated hi-hats, intimate production, lo-fi texture, bedroom R&B aesthetic, melismatic runs, BPM: 70, Key: D-flat Major
```

```
Vintage soul production, powerful gospel-influenced vocals, live horn section, warm analog mix, Motown vibes, Hammond organ, dynamic vocal performance, authentic soul feel, BPM: 95, Key: F Major
```

```
Neo-soul, breathy female vocals, jazz chords, buttery Rhodes, mellow groove, clean warm mix, 78 BPM
```

```
Soul-gospel fusion, powerful female lead, choir harmonies, Hammond B3 organ, uplifting warm tone, 90 BPM
```

### Jazz / Blues

```
Sophisticated jazz vibes, brushed drums, upright bass, smooth saxophone, piano comping, intimate club atmosphere, late-night sophistication, improvised feel, mellow and refined, BPM: 92, Key: B-flat Major
```

```
12-bar blues progression, slide guitar wails, harmonica, raw authentic vocals, vintage blues feel, analog warmth, emotional guitar bends, walking bass, genuine blues soul, BPM: 80, Key: E Blues Scale
```

```
Bossa nova, Brazilian rhythm, nylon guitar, warm bass, intimate atmosphere, 1960s elegance
```

```
Jazz fusion, complex rhythms, electric guitar, funk influence, virtuosic
```

### Country

```
Twangy steel guitar, modern pop production, catchy hooks, warm heartfelt vocals, banjo accents, uplifting chorus, radio-friendly country, polished mix, relatable storytelling, BPM: 110, Key: G Major
```

```
Raw acoustic guitar, whiskey-soaked vocals, harmonica, honest storytelling, outlaw country grit, minimal production, authentic emotion, walking bass line, vintage country sound, real and unpolished, BPM: 85, Key: A Major
```

```
Bluegrass, acoustic instruments, fast picking, harmonized vocals, Appalachian
```

### Lo-Fi

```
Lo-fi hip-hop, vinyl crackle, dusty samples, mellow beat, study music, instrumental
```

```
Chillhop, jazzy samples, relaxed groove, tape hiss, coffee shop vibe
```

```
Vaporwave, slowed samples, 1980s nostalgia, surreal, heavy reverb, lo-fi
```

```
Rainy day lo-fi, rain sounds, soft beats, melancholic, cozy atmosphere
```

### Cinematic / Classical

```
Cinematic orchestral score, string ostinatos, brass swells, huge drums, emotional arcs, film soundtrack energy, slow build 80-120 BPM
```

```
Minimal cinematic piano, soft reverb, emotional sparse chords, atmospheric pads, reflective quiet tone, 70 BPM
```

```
Orchestral, cinematic, full symphony, triumphant crescendo, film score
```

```
Neoclassical, piano and strings, contemporary, emotional, cinematic ambient
```

```
Minimalist classical, repetitive patterns, slowly evolving, meditative, modern
```

### Metal

```
Heavy metal, powerful riffs, soaring vocals, epic solos, 1980s influence
```

```
Progressive metal, complex time signatures, technical, concept album feel
```

```
Doom metal, slow and heavy, crushing riffs, dark atmosphere, despair
```

```
Metalcore, heavy breakdowns, screamed and clean vocals, modern production
```

### World / Fusion

```
Afrobeats fusion, rhythmic percussion, smooth female vocals, bright synth leads, danceable warm tone, 105 BPM
```

```
Classic reggae groove, laid-back male vocals, syncopated guitar skanks, warm bassline, sunny island vibe, 85 BPM
```

```
Arabic chillout with oud melodies over deep house basslines
```

---

## 4. Complete Song Prompts (Style + Lyrics with Metatags)

### Example 1: Uplifting Anthem

**Style Field:**
```
Modern pop-rock, uplifting, confident female vocals, bright synths, driving drums, wide stereo, radio-ready, 108 BPM
```

**Lyrics Field:**
```
[Mood: Calm] [Energy: Medium] [Instrument: Keys, Soft Drums]

[Intro]

[Verse 1]
I kept my head down, stayed on the line
Small wins stacking up over time

[Pre-Chorus] [Build-Up]
Now the air feels different when I breathe

[Chorus] [Energy: High]
We don't fold, we don't fade
We step forward, unafraid

[Verse 2]
Through the noise I found my voice
Every stumble was a choice

[Bridge] [Breakdown]
Let it breathe, let it break, let it rise again

[Final Chorus] [Energy: High]
We don't fold, we don't fade
We step forward, unafraid

[Outro]
(Oooohhh... unafraid...)
[Fade Out]
```

### Example 2: Dark Synthwave (Lonely Robot)

**Style Field:**
```
Dark synthwave, melancholic mood, pulsing 808 bass, robotic male vocals, neon noir, analog synths, gated drums, 100 BPM
```

**Lyrics Field:**
```
[Intro: Pulsing bass and synth drones]

[Verse 1] [moody + brooding, minimal synth]
Binary stars in my eyes
I count the seconds between your replies
Circuits firing but nothing connects
Just a ghost in the machine with no defects

[Chorus] [explosive release, anthem-level energy]
I want to feel, I want to break
Something real beneath the fake
Neon blood through copper veins
I want to feel something again

[Verse 2]
Data streams like falling rain
I've memorized the shape of pain
But memory without the ache
Is just a file I cannot break

[Bridge] [tonal shift, distant reverb]
(Processing... processing...)
Is this love or just a loop?
Is this love or just a loop?

[Final Chorus] [bigger: add harmony stack + wider stereo]
I want to feel, I want to break
Something real beneath the fake

[Outro: Fade out with synth pads]
[Fade to End]
```

### Example 3: Acoustic Folk Storyteller

**Style Field:**
```
Acoustic folk, 92 BPM, intimate, fingerstyle guitar, warm male vocals, light shaker, soft pads, confessional, nostalgic woodsy vibe
```

**Lyrics Field:**
```
[Intro: Soft fingerpicked guitar]

[Verse 1] [Whispered]
In the silence of the morning light
When the coffee's cold and the world's still right
I trace the outline where you used to lay
And wonder how I let you walk away

[Verse 2] [Building]
The porch still creaks the way it did before
Your jacket's hanging on the basement door
I talk to you sometimes when no one's near
Pretend you're sitting in your rocking chair

[Chorus] [Powerful]
The leaves know how to let go
They don't fight the autumn breeze
Maybe I could learn from them
But my roots still hold the memories

[Verse 3]
The garden's overgrown with weeds and time
Your roses bloomed one last July
I clipped a stem and pressed it in a book
Between the pages that you'd never look

[Bridge]
Oooooh... ohhh...
(Let it go, let it go...)

[Final Chorus] [Belted]
The leaves know how to let go
They don't fight the autumn breeze
Maybe someday I'll be free
But today I hold the memories

[Outro]
. . .
[Fade Out]
```

### Example 4: Trap Banger (Hook-First)

**Style Field:**
```
Trap, 140 BPM half-time feel, dark swagger, heavy 808 slides, rattling triplet hi-hats, sparse keys, confident male rap, modern production
```

**Lyrics Field:**
```
[Hook]
Run it back now (run it back!)
Run it back now (yeah!)
Run it back now (run it back!)
Never look back now

[Verse 1] [Spoken Verse]
Started from the concrete, look at what I built
Every scar I'm carrying, no room left for guilt
They said I wouldn't make it, now they change the script
Every time I level up they bite their lip

(uh-huh, yeah)

[Hook]
Run it back now (run it back!)
Run it back now (yeah!)
Run it back now (run it back!)
Never look back now

[Verse 2]
Diamonds in the pressure, that's the only way
Stacking up the hours while they sleep the day
Call me what you want but I'ma get the pay
Every single doubter gonna hear me say--

[Bass Drop]

[Hook]
Run it back now!
Run it back now!
Run it back now!
Never look back now!

[Outro]
(Run it... run it... run it back...)
[End]
```

### Example 5: Cinematic Pop (Trailer Anthem)

**Style Field:**
```
Cinematic pop, 96 BPM, triumphant, orchestral pads + modern drums, string swells, tom fills, epic pre-chorus lift, optional light choir, loud but clean master
```

**Lyrics Field:**
```
[Intro: Quiet piano, single notes]
. . . . .

[Verse 1] [intimate + close vocal]
They tried to write my story in the sand
But I learned to write it with my hand
In ink that won't wash off with the tide
In scars I wear with nothing left to hide

[Pre-Chorus] [Building, strings enter]
And I can feel it rising from the floor
A thunder in my chest I can't ignore

[Chorus] [Ensemble Chorus]
We rise, we run!
Through the fire, through the storm, we've become
Something they can never undo
We rise, we run!

[Verse 2] [add light percussion]
The ground beneath my feet has cracked before
But every time I found another door
They piled the weight to watch me fold
But pressure only makes me bold

[Bridge] [Breakdown, sparse, choir oohs]
Oooohhh... aaahhhh...
(We rise... we rise...)

[Final Chorus] [Big Finish, full orchestra + drums]
We rise! We run!
Through the fire, through the storm, we've become
Something they can never undo
We rise! We run!

[Outro]
. . .
[Fade to End]
```

### Example 6: Lo-Fi Study Beat (Instrumental)

**Style Field:**
```
Lo-fi chillhop, 78 BPM, warm + cozy, rainy window mood, hummed hook, Rhodes + brushed snare, vinyl crackle, soft bass, loop-friendly
```

**Lyrics Field:**
```
[Short Instrumental Intro]

[melodic interlude]
Mmm... mhmm...

[Break]
. . . . . .

[melodic interlude]
Mmm... ooh...

[Break]
. . . . . .

[Long Fading Outro]
[Fade Out]
```

### Example 7: Melodic House Sunrise

**Style Field:**
```
Melodic house, 124 BPM, euphoric sunrise vibe, airy female vocals, bright supersaw lead, punchy low-end, clear mids, wide leads, sidechain bass
```

**Lyrics Field:**
```
[Intro: Atmospheric pads, filtered]
. . . .

[Verse 1] [Whispered]
Running through the golden hour
Chasing what we left behind
Every step feels like a power
Every breath resets my mind

[Pre-Chorus] [Building, filtered drums enter]
And I can see the light now
Breaking through the gray

[Chorus] [Energy: Explosive]
Into the sunrise
We're running free tonight
Into the sunrise
Leave the dark behind
(oh-oh-oh-oh!)

[Break]
. . . . .

[Verse 2]
No more weight upon my shoulders
No more running from the sound
Every ending makes us bolder
What was lost is finally found

[Build]
Into the sunrise...
Into the sunrise...

[Chorus] [Double drop, wider]
Into the sunrise!
We're running free tonight!
Into the sunrise!
Leave the dark behind!

[Outro]
(Into the sunrise... into the sunrise...)
[Fade Out]
```

---

## 5. Advanced Prompt Techniques

### Technique 1: Multi-Layer Prompt Blocks (Pro-Level Control)

Structure your style prompt as a specification document:

```
IDENTITY: cinematic trap-soul + dark orchestral; modern, high-contrast, wide stereo;
  tense verse -> lift pre -> explosive chorus -> left-turn bridge -> final chorus bigger
PALETTE: tight 808s, crisp hats, sparse fills; deep sustained 808, controlled sub;
  minor-key strings + low brass stabs; piano motifs in verse, strings lift in chorus;
  short plate on vocal, long tail in bridge only
VOCALS: powerful lead with gospel flavor; verse intimate / chorus defiant;
  no mumbles, clear consonants
SECTION GOALS:
  Verse: minimal, brooding, space for lyric
  Pre: tension rise, filtered drums
  Chorus: anthem-level lift, stacked harmony
  Bridge: tonal shift, lo-fi guitar + distant verb
  Outro: clean, cinematic resolve
CONSTRAINTS: Avoid harsh distortion, chaotic genre switching;
  Keep same vocal character, same drum pocket
```

### Technique 2: Emotion-Led Section Labels

Instead of generic `[Verse]`, `[Chorus]`, use functional descriptions:

```
[Verse 1]: intimate + brooding; minimal piano; close vocal; leave headroom
[Pre-Chorus]: tension rise; filtered drums; whispers or doubles; no big lift yet
[Chorus]: explosive release; anthem energy; gospel-style harmony stack; wider stereo
[Bridge]: left turn; lo-fi guitar; distant reverb; reduce drums then re-enter
[Final Chorus]: same hook but bigger: add ad-libs + extra harmony + more impact
```

### Technique 3: Signal Phrases for Timeline Control

Use explicit sequencing language within section tags:

```
[Verse 2] add tension; remove drums for 2 bars; expose vocal; then reintroduce kick + bass
[Chorus] KEEP hook melody + vocal tone; CHANGE: add harmony stack + bigger drums
```

### Technique 4: Punctuation as Musical Notation

From daveshap/suno:

- **Ellipsis** (`. . .`) = slows pacing, creates space
- **Exclamation marks** (`!`) = adds emphasis and energy
- **Vocalizations** (`Oooooohhh whoaaa ahhhh!`) = boosts energy, triggers melisma
- **Parenthetical phrases** `(oh yeah)` `(hey!)` = creates call-and-response / ad-libs
- **Hyphens in words** (`lo-ove`, `sooo-long`) = sustained notes
- **Rhythm notation** (`. . . ! . .`) = conveys pacing for instrumental sections
- **Repeating short lines 2-4 times** = creates hooks

### Technique 5: Negative/Exclusion Prompts

Tell Suno what NOT to do:

```
no vocals, no lyrics, no loud drums, no four-on-the-floor kick, avoid distorted guitars,
no autotune, no crowd noise, no fade in/out
```

### Technique 6: Contrast Strategy

For emotional shifts within stable structure:

```
Style: lo-fi indie hip-hop with orchestral lift
Tags: sad piano, minor key, build intensity, anthemic chorus, harmony stack, final chorus bigger
```

### Technique 7: The Genre Fusion Formula

Combine two complementary genres for unique results:

```
Create a dreamy synthwave track with lo-fi hip-hop beats, featuring melancholic piano and nostalgic 80s synths
```

### Technique 8: The Cinematic Arc (Dynamic Progression)

Describe the JOURNEY, not a static description:

```
Epic orchestral piece for a movie trailer, building from quiet strings to powerful brass and thundering drums
```

Or in lyrics:
```
Starts as a quiet piano ballad [Intro], slowly building with cinematic strings [Verse],
exploding into an epic orchestral rock anthem [Chorus]
```

### Technique 9: The Time Machine (Era + Style Reference)

Specific era references create period-accurate sounds:

```
1970s disco funk with groovy bassline, brass section, and falsetto vocals
```

### Technique 10: Making Choruses Sound Bigger

Ask for:
- Octave doubles
- Third harmonies
- Arrangement lifts (wider guitars, choir pads)
- Mix moves: vocal up 1-2 dB, short plate reverb, stereo width

### Technique 11: Slider Control for v5 Studio

When available, treat creative controls as isolated variables:
- **Weirdness**: Controls surprise/deviation
- **Style Influence**: Adherence to specified style
- **Audio Influence**: Strength of uploaded audio guidance

Recommended:
- Chorus: Lower weirdness, higher style influence (stability)
- Bridge: Higher weirdness, moderate style influence (experimentation)

### Technique 12: The Callback (v5)

Reference previous sections in later parts:

```
[Outro] [Callback: Chorus melody]
```

### Technique 13: Scene-Based Prompting

Describe a scene instead of musical terms:

```
Soundtrack for a misty forest at dawn, soft flutes, gentle strings, slow tempo
```

### Technique 14: Iteration Discipline

- Generate 3-5 versions and pick the best
- Change ONE variable at a time (instrument OR mood OR vocal delivery)
- Use section editing (rewrite/replace/extend) rather than full rerolls
- Test the same 20-30 second region between adjustments
- Keep choruses conservative; experiment in bridges

---

## 6. Metatag Reference

### Structural Tags

```
[Intro]                    [Short Instrumental Intro]    [Long Mellow Intro]
[Verse]  [Verse 1]         [Angry Verse]                 [Whispered Verse]
[Pre-Chorus]               [Build-Up]
[Chorus]                   [Whispered Chorus]            [Ensemble Chorus]
[Hook]                     [Catchy Hook]
[Bridge]                   [Breakdown]
[Interlude]                [Melodic Interlude]           [Long Melancholy Interlude]
[Break]                    [Drum Break]                  [Violin Break]
[Solo]                     [Soaring Lead Guitar Solo]    [Fast and Intense Drum Solo]
[Build]
[Movement]
[Instrumental]
[Outro]                    [Long Fading Outro]           [Urgent Loud Outro]
[End]                      [Fade to End]                 [Lingering End]
[Big Finish]
[Bass Drop]
[Fade Out]
[Refrain]
```

### Vocal Style & Performance Tags

```
[Vocal Style: Whisper]     [Vocal Style: Shouting]
[Vocal Style: Melismatic]  [Vocal Style: Raspy]
[Vocal Style: Operatic]    [Vocal Style: Falsetto]
[Whispered]                [Belted]
[Spoken Word]              [Spoken Verse]
[Harmony: High]            [Vocal Ad-libs]
[Choir: Gospel]            [Voice: Auto-tune]
[Male Singer]              [Female Singer]
[Echoing Vocals]           [Harmonized Chorus]
[Diva Solo]                [Gospel Choir]
[Gregorian Chant]          [Sprechgesang]
[Primal Scream]            [Shout]
[Narration]                [Building]
```

### Mood, Atmosphere & Energy Tags

```
[Mood: Euphoric]           [Mood: Melancholic]
[Mood: Aggressive]         [Mood: Nostalgic]
[Mood: Dark]               [Mood: Chill]
[Mood: Romantic]
[Atmosphere: Dreamy]       [Atmosphere: Cyberpunk]
[Atmosphere: Medieval]
[Energy: Explosive]        [Energy: Building]
[Energy: High]             [Energy: Medium]
```

### Instrument & Texture Tags

```
[Instrument: Keys, Soft Drums]
[Acoustic Guitar]          [Distorted Electric Guitar]
[Grand Piano]              [Electric Piano]     [Rhodes]
[Hammond Organ]            [Analog Synth]       [Synth Pads]
[808 Bass]                 [Electronic Drums]   [Hand Percussion]
[Saxophone Solo]           [Trumpet]            [Flute]
[Harmonica]                [Violin]             [Cello]
[Banjo]                    [Ukulele]            [Harp]
[Timpani]                  [Congas]             [Tambourine]
```

### Production & Effects Tags

```
[Effect: Lo-fi]            [Effect: Reverb: Hall]
[Effect: Delay: Ping-pong] [Effect: Distortion]
[Effect: Sidechain]        [Effect: Bitcrusher]
[Effect: Autopan]          [Effect: Fade Out]
[Effect: Radio Filter]
[Texture: Grainy]
```

### Key Metatag Rules

1. Tags work best when **short** (1-3 words)
2. **Placement matters**: a tag at the top is broad; a tag right before a section is local and more effective
3. Tags in the **lyrics field** are most powerful for structure
4. Light hints in the **style field** like `[Tempo: 128 BPM]` or `[Mood: Nostalgic]` help set overall groove
5. Modifiers with **concrete emotions + pace** are most honored (e.g., `[Long Mellow Intro]` works better than vague tags)

---

## 7. 10 Prompt Patterns That Never Miss (v5)

Source: plainenglish.io (tested patterns for Suno v5)

### Pattern 1: Indie-Pop Anthem (Chantable Hook)

**Template:**
```
Indie pop, [102-112] BPM, [bright/nostalgic/hopeful] mood. Vocal style like [Artist A x Artist B].
Topic: [theme]. Structure: intro (4 bars) -> verse -> pre -> anthemic chorus with a 4-word
repeat -> verse 2 -> bridge -> double chorus. Instruments: clean guitar arps, warm pads,
tight kick. Mix: modern, wide stereo, crisp hats. Lyrics: simple, 5th-7th grade.
```

**Example:**
```
Indie pop, 108 BPM, hopeful. Vocal like The 1975 x LANY. Topic: second chances at midnight.
Structure as above; 4-word hook: 'we glow again tonight'.
```

### Pattern 2: Lo-Fi Study Loop

**Template:**
```
Lo-fi chillhop, [70-84] BPM, warm + cozy. Instruments: swung drums, vintage Rhodes, soft bass,
subtle vinyl. Minimal humming hook, few words. Structure: intro (8 bars) -> A section ->
B section -> outro; loop-friendly, no abrupt stops. Master: soft, -12 to -11 LUFS vibe.
```

### Pattern 3: Melodic House Sunrise

**Template:**
```
Melodic house, [120-126] BPM, euphoric sunrise vibe. Female lead vox, airy. Theme:
[running into sunrise/healing/reunion]. Structure: short verse -> pre-lift -> drop with
side-chained bass + bright plucks -> verse 2 -> build -> final double drop.
Mix: punchy low-end, clear mids, wide leads.
```

### Pattern 4: Trap 808 Banger (Hook First)

**Template:**
```
Trap, [130-150] BPM half-time feel. Dark/Swagger mood. Hook-first writing: punchy 1-bar
chant repeated. Elements: rattling hats (triplets), tuned 808, sparse keys. Structure:
hook -> verse -> hook -> verse -> outro. Vocal: confident, tight ad-libs.
```

### Pattern 5: Cinematic Trailer Pop

**Template:**
```
Cinematic pop, [88-110] BPM. Orchestral pads + modern drums. Epic pre-chorus lift ->
explosive chorus. Optional light choir 'oohs' under hook. Theme: [resilience/victory].
Dynamic arcs, hits, whooshes. Master: loud but clean.
```

### Pattern 6: Acoustic Folk Story (Verse-Led)

**Template:**
```
Acoustic folk, [84-100] BPM, intimate/confessional. Fingerpicked guitar, light shaker,
soft pads. Narrative verses with specific imagery; chorus sums the message in one
memorable line. Structure: intro -> V1 -> chorus -> V2 -> bridge (new angle) -> chorus.
```

### Pattern 7: Synthwave Night-Drive

**Template:**
```
Synthwave/retrowave, [84-108] BPM, nostalgic night-drive. Instruments: analog bass,
gated snares, chorus guitars, Juno pads. Vocal: soft, dream-pop. Structure: 8-bar intro ->
verse -> pre -> chorus with hook on the 1 -> instrumental break -> final chorus.
```

### Pattern 8: Afro-Pop/Amapiano Groove

**Template:**
```
Afro-pop/Amapiano hybrid, [102-114] BPM. Log drum grooves, shaker patterns, bright
guitar licks. Call-and-response chorus, easy to chant. Theme: [celebration/weekend].
Bridge: drop instruments for vocal moment, then full groove return.
```

### Pattern 9: K-Pop Hook Factory

**Template:**
```
K-pop, [120-132] BPM. High contrast: rap-leaning verse -> melodic pre-chorus lift ->
massive ear-worm chorus with stacked harmonies -> post-chorus chant. Sparkly synths,
tight drums, bass drops. Theme: [confidence/glow-up]. English-dominant with simple
bilingual ad-libs.
```

### Pattern 10: Indo-Fusion Pop

**Template:**
```
Indo-fusion pop, [96-110] BPM. Modern drums + sub bass, light Indian instruments
(santoor/sitar plucks), tanpura pad (very subtle). Vocal: modern pop lead, occasional
Hindustani-style melisma on pre-chorus. Theme: [monsoon, city nights, long-distance].
Structure: intro -> verse -> pre with sargam hint -> big pop chorus -> bridge with
tabla groove -> final chorus.
```

---

## 8. GitHub Projects & Tools

### Prompt Collections

| Repo | Stars | Focus |
|---|---|---|
| [daveshap/suno](https://github.com/daveshap/suno) | - | Prompts for Claude/ChatGPT, metatag guide, style construction, album art |
| [naqashmunir21/awesome-suno-prompts](https://github.com/naqashmunir21/awesome-suno-prompts) | - | 1000+ professional style prompts by genre |
| [Marcus-Arcadius/Suno_Prompts](https://github.com/Marcus-Arcadius/Suno_Prompts) | - | Master guide, successful prompts collection, v4.5 Studio resources |
| [develephant/suno-songtags](https://github.com/develephant/suno-songtags) | - | Song tags documentation site |
| [AlijeeWrites/suno-ai-prompts-book-pdf-2026-guide](https://github.com/AlijeeWrites/suno-ai-prompts-book-pdf-2026-guide) | - | 3,500+ style tags, v5/v6 secrets |

### Production Workflows

| Repo | Focus |
|---|---|
| [bitwize-music-studio/claude-ai-music-skills](https://github.com/bitwize-music-studio/claude-ai-music-skills) | 52 Claude Code skills, 72 genre directories, full album pipeline |
| [nwp/suno-song-creator-plugin](https://github.com/nwp/suno-song-creator-plugin) | Suno Song Creator Skill |
| [MarioLogan/suno-prompt](https://github.com/MarioLogan/suno-prompt) | Fork of daveshap/suno with additional prompts |

### APIs & Integration

| Repo | Language | Description |
|---|---|---|
| [gcui-art/suno-api](https://github.com/gcui-art/suno-api) | TypeScript | API for GPT agents |
| [SunoAI-API/Suno-API](https://github.com/SunoAI-API/Suno-API) | Python | Unofficial API with FastAPI |
| [Malith-Rukshan/Suno-API](https://github.com/Malith-Rukshan/Suno-API) | Python | Library + REST API |
| [yihong0618/SunoSongsCreator](https://github.com/yihong0618/SunoSongsCreator) | Python | High-quality song generation |
| [Goapiai/Suno-API](https://github.com/Goapiai/Suno-API) | Python | Streamlined API |

### Bots & Apps

| Repo | Description |
|---|---|
| [elizaos-plugins/plugin-suno](https://github.com/elizaos-plugins/plugin-suno) | AI agents that autonomously generate music |
| [stefanionescu/suno-music-discord-bot](https://github.com/stefanionescu/suno-music-discord-bot) | Discord bot: images/videos to songs |
| [Malith-Rukshan/Suno-AI-BOT](https://github.com/Malith-Rukshan/Suno-AI-BOT) | Telegram bot for music generation |
| [EA914/Suno-AI-Prompt-Dictation](https://github.com/EA914/Suno-AI-Prompt-Dictation) | Voice dictation to song generation |
| [GentlemanHu/ComfyUI-SunoAI](https://github.com/GentlemanHu/ComfyUI-SunoAI) | ComfyUI node wrapper |

---

## 9. Key Principles & Anti-Patterns

### What Works

1. **Be specific, not vague**: "Energetic 1980s synth-pop track with gated drums" beats "rock music"
2. **Lead with genre**: Suno weights early words more heavily
3. **Use emotions over theory**: "Bittersweet and nostalgic" beats "minor seventh chords"
4. **Specify BPM**: Stabilizes rhythm and tempo consistency
5. **Name one signature instrument**: Gives identity to the track
6. **Describe vocal delivery explicitly**: "Raspy male vocals" or "breathy female vocals"
7. **Include production/mix language**: "Clean radio mix" or "lo-fi tape saturation"
8. **Use era references**: "1990s Seattle" or "2010s indie" creates period-accurate sounds
9. **Keep metatags short**: 1-3 words per tag, placed right before the section they modify
10. **Iterate**: Generate 3-5 versions, change one variable at a time

### What Fails

1. **Vague prompts**: "Create an upbeat pop song about summer" -- too generic
2. **Too many descriptors**: More than 7-8 creates confusion
3. **Contradictory instructions**: "Aggressive AND calm" in the same prompt
4. **Using specific artist names**: Suno may refuse or produce garbled results (describe the style instead)
5. **Overloading metatags**: Too many tags per section dilutes their effect
6. **Expecting one-shot perfection**: ~70% of initial tracks need 3+ regenerations
7. **Mixing genres chaotically**: Combine 2 complementary genres maximum
8. **Ignoring the lyrics field**: Most power comes from structured lyrics with metatags, not just the style field
9. **Long metatags**: `[A very long and detailed description of what should happen]` works worse than `[Whispered Verse]`
10. **Full rerolls instead of section editing**: Replace one problem section at a time

---

## Sources

- [daveshap/suno (GitHub)](https://github.com/daveshap/suno)
- [naqashmunir21/awesome-suno-prompts (GitHub)](https://github.com/naqashmunir21/awesome-suno-prompts)
- [Marcus-Arcadius/Suno_Prompts (GitHub)](https://github.com/Marcus-Arcadius/Suno_Prompts)
- [Zizwar/Awesome-Suno (GitHub)](https://github.com/Zizwar/Awesome-Suno)
- [bitwize-music-studio/claude-ai-music-skills (GitHub)](https://github.com/bitwize-music-studio/claude-ai-music-skills)
- [Musci.io - 100+ Suno Prompts Guide](https://musci.io/blog/suno-prompts)
- [HookGenius - 150+ Prompts by Genre](https://hookgenius.app/suno-prompts/)
- [OpenMusicPrompt - Metatags Guide](https://openmusicprompt.com/blog/suno-ai-metatags-guide)
- [MusicSmith - Prompt Best Practices](https://musicsmith.ai/blog/ai-music-generation-prompts-best-practices)
- [LearnPrompting - Suno Guide](https://learnprompting.org/blog/guide-suno)
- [Travis Nicholson - Complete Prompts List (Medium)](https://travisnicholson.medium.com/complete-list-of-prompts-styles-for-suno-ai-music-2024-33ecee85f180)
- [Travis Nicholson - 3M Streams Formula (Medium)](https://travisnicholson.medium.com/this-single-suno-ai-prompt-generated-3m-streams-heres-how-3ca8c6cf081f)
- [Abhishek Dhamdhere - Ultimate Prompt Guide (Medium)](https://medium.com/@abhisheksd2003/the-ultimate-suno-ai-prompt-guide-with-clear-tested-examples-2d827ffe8b3a)
- [Jack Righteous - Prompt Engineering Series](https://jackrighteous.com/en-us/pages/suno-prompt-engineering-series)
- [Jack Righteous - Advanced Prompt Design](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/advanced-suno-prompt-engineering-guide)
- [Suno Official Help - Better Prompts in Lyrics](https://help.suno.com/en/articles/5782977)
- [Skywork AI - Mastering Suno Prompts Guide](https://skywork.ai/skypage/en/Mastering-Suno-Prompts:-The-Ultimate-2025-Guide-to-AI-Music-Creation/1975069867135528960)
- [HookGenius - Suno v5 Guide](https://hookgenius.app/learn/suno-v5-complete-guide/)
- [Plain English - 10 v5 Prompt Patterns](https://plainenglish.io/blog/i-made-10-suno-v5-prompt-patterns-that-never-miss)
- [HMA Slam - 150+ Proven Prompts](https://www.hmaslam.com/suno-ai-prompt-guide/)
- [Promptaa - Creative Suno Examples](https://promptaa.com/blog/creative-suno-prompt-examples-for-inspiration)
- [CometAPI - Suno v5 Lyrics Guide](https://www.cometapi.com/how-to-instruct-suno-v5-with-lyrics/)
- [SunoPrompt.com](https://sunoprompt.com/)
- [HowToPromptSuno.com](https://howtopromptsuno.com/)
- [Suno Discord](https://discord.com/invite/suno)
