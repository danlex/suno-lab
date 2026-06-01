# Evolution — Technique mindmap & current state

This file is my evolving knowledge of Suno prompt craft. Update it at the end of every cycle with any new learning. Data anchors refresh by running `python3 scripts/novelty_surface.py`.

Last updated: v211 (2026-05-19)

## Mindmap (Mermaid)

```mermaid
mindmap
  root((Suno craft v130))
    Techniques — What works
      Frisson triggers
        Silence before climax
        Half-step modulation at climax
        Three-soloist trio
        Trio contrast with orchestral backdrop
      Architectural forms
        Bolero — melody constant, orchestration grows [v110]
        Passacaglia — bass constant, upper voices transform [v111]
        Lone-center — piano constant, world builds around it [v112]
        Fugue — imitative voices, stretto compression [v113]
        Arch form — palindromic ABCBA [v114]
        Rondo — iterative refrain ABACA [v115]
        Theme-and-variations — same melody, different timbres [v119]
        Canon/round — voices chase in perpetual imitation [v120]
        Dissolution — starts at max, decays to nothing [v121]
        Concerto grosso — solo group vs full orchestra [v122]
        Sonata — two themes, development, recapitulation [v123]
        Ricercare — slow searching drone meditation [v124]
        Passamezzo — repeating ground bass, obsessive [v125]
        Micropolyphony — dense cloud, no melody [v126]
        Minimalism phase shifting — patterns drift in and out [v127]
        Spectral — overtone-derived harmony [v128]
        Aleatoric — chance/indeterminate, performer choice [v129]
        Twelve-tone serialism — atonal, all 12 pitches equal [v130]
        Stochastic — probability-density, Gaussian distributions [v131]
        Col Legno Structural Arc — three bow-contact states: col legno battuto → sul ponticello tremolo → arco return; acoustic climax is the *return* of normal tone [v206]
        Asymmetric Metric Arc — 7-beat 3+4 pulse withholds beat-1 arrival for ~2 min, releases it fused with half-step modulation; rhythmic + tonal resolution delivered as single blow [v207]
        French Overture — Baroque tri-part: slow over-dotted ceremonial march → fast fugal/imitative middle → brief slow over-dotted return as elegy; form-as-drama via tempo/texture pivot, first sustained major-key arc [v208]
        Orchestral Collapse-to-Solo — theme swells to full tutti then HARD-CUTS to one solo voice; the cut IS the climax (grief), inverse half-step DOWN modulation; inverts "silence before climax" — beauty-first not technique-first [v209]
        Neo-Soul Orchestral Fusion — extended jazz harmony (9ths/11ths/13ths) on a slow-burn sighing groove, orchestra sinks INTO the groove; warmth that aches; scored 100/100 — best of the v207-v210 run, validates beauty-first over form-as-engine [v210]
        Euphoric Orchestral Hardstyle Breakdown — genre's anthemic breakdown realized with live orchestra, kick removed; octave-leap melody, relative-major lifts, half-step lift = dawn-flood payoff; marimba replaces the kick [v211]
        Build-silence-return — standard linear [v93-v108]
      Prompt craft
        Timestamps — explicit time anchors in style
        Purpose phrase — film score for X scene
        850-950 chars — sweet spot
        Genre first, mood second, instruments third
        Conversational flow not tag lists
        Uppercase featured instruments
        Specificity over abstraction
      Control layers
        Three-layer instrument control
        Exclude styles field
        4+ inline No-X negatives
        1-2 genre stacking max
        Cultural-trigger exclusions — Chinese folk, Hungarian folk, West African folk, zen meditation, new age, tango
    Techniques — What DOESN'T work
      Duration language
        total duration X to Y — IGNORED by Suno
        ends at X never longer — IGNORED
        [End] metatag in lyrics — IGNORED
        Tested v113-v117, all failed
        Suno duration is NOT prompt-controllable
        Only path — post-generation crop
      Placeholder matching
        Style field placeholder rotates randomly
        Hard kick, smooth vocals, dissonant harmonies — all seen
        Must identify by elimination not text match
      JS click on off-screen buttons
        Silent failure — no error, just nothing happens
        Fix — scroll_to then ref-based left_click
    Genre fusions tried
      Synthesis era — electronic + orchestra
        Dubstep v93, Trance v94, Trap v95
        Progressive house v96, Breakbeat v97
        Psytrance v98, IDM v99, 2-step garage v100
        Footwork v101, Grime v102, Ambient v103
        Drill v104, Synthwave v105, Amapiano v106
        Reggaeton v107, Vaporwave v108, Chillhop v109
        Future garage v116
      Technique fusion — new category
        Orchestral glitch v118 — first technique not genre
        Theme-and-variations v119 — triple deep revival
      Pattern-breaking batch v120-v121
        Canon v120 — MAJOR key, DUO, joyful, 152 BPM
        Dissolution v121 — inverted arc, half-step DOWN
      Pure orchestral forms
        Bolero v110, Passacaglia v111
        Lone-center v112, Fugue v113
        Arch v114, Rondo v115
      Gothic symphonic
        Gothic symphonic neoclassical v117 — Evanescence arc
    References
      Interstellar — cosmic longing, cathedral scale
      Evanescence — intimate vulnerability to raw power
      Modern Classical — Richter, Arnalds, Frahm territory
      Fifth Element — otherworldly soprano
      Barber Adagio — inevitable crescendo
    Blocklist
      Trigger words
        Dune desert sand oasis — Arabic
        Epic massive explosion — rock drums
        Wall of sound metal heavy — rock
        Frisson — not a Suno term
      Unverified jargon
        Appoggiatura, Shepard tone, melisma
        ALL composer and artist names
        Artist-inspired references
    Harness
      Generation
        novelty_surface.py — instrument/genre/key/BPM registry
        judge skill — 12 criteria, score 0-100
        hourly_cycle_prompt.md — autonomous generation
        review_cycle_prompt.md — daily publish best 4
      Tracking
        results-tracker.md — per-cycle log
        evolution.md — this file, technique knowledge
        MEMORY.md — cross-session persistence
      Submission
        suno skill — browser automation
        lyrics clear before set — v114 fix
        style field by elimination — v115 fix
        title-poll verification — v113 fix
        scroll_to + ref click — v117 fix
        browser auto-reconnect — v115 fix
      Website
        build_site.py — songs.json + index.html
        suno_urls.json — embed player IDs
      Known bugs
        novelty_surface counts negatives as uses — pipe organ inflated
        title-poll needs 6-10s delay — DOM renders slowly
```

## Instrument status (refresh via `python3 scripts/novelty_surface.py`)

### Never used — available for first use
- ney, duduk (pre-synthesis, Arabic-risk — needs careful exclusion)
- wagner tuba (composer name in instrument name — blocklist edge case)
- armonica, string quartet, viola da gamba (Baroque, used in v113 — UPDATE: used once)
- spinet, virginal (harpsichord family)

### First-used this session (v112-v119)
- felt piano (v112), shakuhachi (v114), bass oboe (v114), cornet (v115), mellotron (v116)

### Revived this session (v112-v119)
- cristal baschet (v112, from v93), glass harmonica (v112, from v79)
- waterphone (v114, from v94), cimbalom (v115, from v98), frame drums (v115, from v96)
- handpan (v116, from v97), piccolo (v116, from v83)
- erhu (v117, from v102), glockenspiel (v117, from v83)
- kora (v118, from v31 — **86-version gap, deepest revival in repo**)
- subcontrabass sax (v118, from v86), celesta (v118, from v99)
- theremin (v119, from v101), tubular bells (v119, from v101), contrabassoon (v119, from v103)
- bass flute (v120, from v100), steelpan (v120, from v107)
- harpsichord (v121, from v105), bass trombone (v121, from v102), glass marimba (v121, from v103)
- cor anglais (v122, from v104), music box (v122, from v108), upright bass (v122, from v109)
- flugelhorn (v123, from v106), tenor saxophone (v123, from v107), steel tongue drum (v123, from v108)
- hardanger fiddle (v124, from v111), mbira (v124, from v109), oboe d'amore (v124, from v110)
- balafon (v125, from v106 — **18-gap, deepest revival of this session**), hurdy gurdy (v125, from v113), shakuhachi (v125, from v114)
- clavichord (v126, from v113), viola da gamba (v126, from v113), mellotron (v126, from v116)
- nyckelharpa (v127, from v111), felt piano (v127, from v112), cornet (v127, from v115)

### First-used this session (v126-v128)
- spinet (v128, FIRST USE), musical saw (v128, FIRST USE) — both never-before-used

### Deepest revival this session
- **french horn (v129, from v92 — 37-version gap, NEW RECORD)**
- bowed vibraphone (v128, from v99 — 28-version gap)

### Overexposed — use as backdrop only, never feature
- pipe organ ×50+, organ ×58+, piano ×40+
- timpani ×27, cello ×26, string orchestra ×19
- violin ×12

## Architectural forms

| Form | Version | Structure | Status |
|------|---------|-----------|--------|
| Build-silence-return | v93-v108 | Linear crescendo → silence → return | Default, overused |
| Bolero | v110 | Melody constant, orchestration grows | Done |
| Passacaglia | v111 | Bass constant, upper voices transform | Done |
| Lone-center | v112 | Piano constant, world builds around | Done |
| Fugue | v113 | Imitative voices entering, stretto | Done |
| Arch form (ABCBA) | v114 | Palindromic mirror | Done |
| Rondo (ABACA) | v115 | Iterative refrain returns | Done |
| Theme-and-variations | v119 | Same melody through different timbres | Done |
| Canon/round | v120 | Voices chase in perpetual imitation | Done |
| Dissolution (inverted) | v121 | Starts at max grandeur, decays to nothing | Done |
| Concerto grosso | v122 | Solo group (concertino) vs full orchestra (ripieno) | Done |
| Sonata | v123 | Two themes → development → recapitulation → coda | Done |
| Ricercare | v124 | Slow searching drone meditation | Done |
| Passamezzo | v125 | Repeating ground bass, obsessive | Done |
| Micropolyphony | v126 | 20th-century dense cloud, no melody | Done |
| Minimalism phase shifting | v127 | Repeated patterns drift in and out of phase | Done |
| Spectral | v128 | Harmonies derived from overtone series analysis | Done |
| Aleatoric | v129 | Indeterminate pitches/timings, performer chooses within framework | Done |
| Twelve-tone serialism | v130 | Atonal, all 12 chromatic pitches equal | Done (short-duration artifact) |
| Stochastic | v131 | Probability-density writing, Gaussian distributions over pitch/timbre | Done (tonal framing to avoid v130 duration collapse; first clip still came in 0:29) |

**Classical forms + 6 major avant-garde techniques complete.** Next frontier: musique concrète, granular synthesis, integral serialism.

## Duration experiment — CONCLUDED

**Result: Suno's song duration is NOT prompt-controllable.** Tested 5 iterations with progressively tighter language and `[End]` metatags. All failed.

| v | Prompt language | Metatag | Clip 1 | Clip 2 |
|---|----------------|---------|--------|--------|
| 113 | "total duration 1:00 to 2:00" | No | 1:08 | 0:44 |
| 114 | "total duration 1:30 to 2:00" | No | 1:12 | 2:27 |
| 115 | "ends at 1:55, never longer" | `[End]` | 1:27 | 2:24 |
| 116 | Same as v115 | `[End]` | 3:24 | 4:13 |
| 117 | Same as v115 | `[End]` | 3:03 | 2:33 |

**Decision:** Stop wasting chars on duration language. Use those ~60 chars for more scene/instrument description. For exact-length output, use Suno's Crop feature post-generation.

## Cycle technique register

| Technique | First applied | Status |
|-----------|---------------|--------|
| Silence before climax | v93+ | Default — always use |
| Half-step modulation | v93+ | Default — always use |
| Three-layer instrument control | v82+ | Default — always use |
| Conversational flowing style | v95+ | Default — always use |
| Trio (3 soloists) | v111 | Default — always use |
| Timestamps | v112 | Default — always use |
| Purpose phrase | v112 | Default — always use |
| Surface-novelty check | v112 | Default — enforced via novelty_surface.py |
| Lyrics metatags for structure | v115 | Experimental — no proven effect on Suno output |
| Cultural-trigger exclusions | v114+ | Default — add per-instrument when needed |
| Technique fusion (not genre) | v118 | New — glitch was first, explore more |
| Duration language | v113-v117 | **DEAD — stop using, zero effect** |
| Extended-technique structural arc | v206 | New — col legno→ponticello→arco as the form itself, the timbre shift is the climax |
| Pipelined team (research/novelty overlap submit) | v206 | New — suno-cycle team; next-version inputs computed while current submits |
| French overture tri-part form | v208 | New — slow over-dotted → fast fugal → slow return; confine period/pastiche + composer words to exclude_styles only |
| Orchestral collapse-to-solo | v209 | New — tutti hard-cut to lone solo as climax; inverse downward modulation; beauty-first emotional axis (deliberate break from form-as-engine run) |
| Lead enforces thematic variety | v209 | New — orchestrator rejects/redirects research that repeats the recent axis; don't just relay concepts |
| Beauty-first beats form-as-engine | v210 | Confirmed — emotional/genre-fusion axes (v209-v210) score 98-100 vs academic form pieces 97; prefer emotional payload over technique demos |
| suno_urls.json update in close-out | v211 | New — site only plays titles present in docs/suno_urls.json; add the new song's title→clip-UUIDs every close-out or it's unlistenable on http://suno.alexandrudan.com/ |
| Drafter is read-only after handoff | v211 | New — suno-drafter reliably re-edits post-FINAL (3x); forbid file edits after its completion signal, it reports changes as text, judge is sole writer |
| Sequenced submit/close-out + literal FINAL gate | v210 | New — submitter submits+reports only; lead owns logs+build+commit+push; dispatch judge only on the drafter's literal "FINAL" message |

## Last 5 prompts at a glance

| v | Title | Genre | Key | BPM | Featured trio |
|---|-------|-------|-----|-----|---------------|
| 117 | The Bell That Wept | gothic symphonic neoclassical | C#→D minor | 76 | bandoneon + erhu + glockenspiel |
| 118 | What Happens When the Music Breaks | orchestral glitch | Bb→B minor | 95 | kora + subcontrabass sax + celesta |
| 119 | The Same Story Told Three Ways | orchestral theme-and-variations | F#→G minor | 62 | theremin + tubular bells + contrabassoon |
| 120 | Every Voice Chasing the Last | orchestral canon | G→Ab MAJOR | 152 | bass flute + steelpan (DUO) |
| 121 | Beginning at the End | orchestral dissolution | Db→C MAJOR (DOWN) | 46 | harpsichord + bass trombone + glass marimba |
| 122 | What the Attic Remembers | orchestral concerto grosso | B→C MAJOR (virgin) | 78 | cor anglais + music box + upright bass |
| 123 | Two Voices in the Same Rain | orchestral noir sonata | Eb→E minor | 102 | flugelhorn + tenor sax + steel tongue drum |
| 124 | The Frequency of Still Water | orchestral ambient ricercare | F#→G MAJOR | 50 | hardanger fiddle + mbira + oboe d'amore |
| 125 | Every Step Is the Same Step | orchestral passamezzo | Bb→B minor | 124 | balafon + hurdy gurdy + shakuhachi |
| 126 | A Room That Breathes On Its Own | orchestral micropolyphony horror | Ab→A minor | 68 | clavichord + viola da gamba + mellotron |
| 127 | The Moment Before the Patterns Align | orchestral minimalism | A→Bb MAJOR | 116 | nyckelharpa + felt piano + cornet |
| 128 | Every Sound Contains a Thousand Sounds | orchestral spectral | Eb→E MAJOR | 86 | spinet + bowed vibraphone + musical saw |
| 129 | Where Each Note Decides Itself | orchestral aleatoric | Db→D minor | 82 | french horn + harp + waterphone |
| 130 | The Row That Never Repeats | orchestral twelve-tone | ATONAL | 98 | contrabass + trumpet + vibraphone |
| ... | (v131–v214 not logged in this table) | — | — | — | — |
| 215 | When the Horn Finds Open Air | brass extended-technique cuivré arc | Db→D minor | 122 | stopped horn + cristal baschet + felt piano |
| 216 | A Hall the Water Will Not Leave | bell-halo two-voice structure | Bb→B minor | 123 | nyckelharpa + tenor saxophone + mellotron |
| 217 | Every Gap an Engine | orchestral hocket (interlocking voices) | Eb→E major | 127 | ophicleide + baryton + steelpan |
| 218 | Where the Valley Loses the Light | granular shimmer cloud (timbre-first) | C#→D minor | 125 | cimbalom + bowed vibraphone + duduk |
| 219 | Light Without Fixed Source | chromatic planing (parallel chord slabs) | F#→G minor | 129 | glass marimba + oboe d'amore + singing saw |
| 220 | Every Gear Keeps Its Promise | perpetuum mobile (ceaseless 16ths, no silence/no mod) | F minor (stable) | 131 | harpsichord + glass harmonica + contrabassoon |
| 221 | Before the Floor Can Catch It | tarantella accelerando-to-collapse (hard cut-off, no resolution) | Ab minor → Ab MAJOR (parallel-major lift) | 133 | piccolo + flugelhorn + waterphone |
| 222 | What the Vellum Keeps | additive stratum scoring (irreversible accretion, no return/no mod) | D# minor (stable) | 133 | bass clarinet + trumpet + crotales |
| 223 | What One Reed Remembers | climax-at-the-front (inverted arc, single voice survives) | B minor (stable) | 139 | chalumeau + tuba + theremin |
| 224 | What the Noise Kept Hidden | musique concrete instrumentale (noise-to-pitch revelation) | E-flat minor -> E minor (half-step revelation) | 141 | harp + tubular bells + viola da gamba |
| 225 | Before the Ferryman Speaks | isorhythmic convergence (talea/color phase-lock) | G-sharp minor -> A minor (convergence half-step) | 142 | cor anglais + hurdy gurdy + handpan |
| 226 | What the Scribe Could Not Finish | stile concitato arc (concitato/molle affective switching) | C minor -> C-sharp minor (fused-finale half-step) | 146 | bass flute + celesta + glockenspiel |
| 227 | Before the Ledger Closes | ritornello form (homecoming-as-climax refrain/episodes) | D-flat minor (stable, homecoming return) | 143 | contrabass clarinet + ondes martenot + music box |
| 228 | What Color the Forge Remembers | klangfarbenmelodie (tone-color melody, timbral handoff) | A-flat major -> A major (half-step at color reunion) | 147 | prepared piano + upright bass + subcontrabass saxophone |
| 229 | Before the Flock Decides | alap-jor-jhala velocity arc (rhythmic densification climax) | B-flat minor (stable, no modulation) | 148 | ophicleide + baryton + clavichord |
| 230 | What the Fog Gives Back | granular orchestral decomposition (timbral dissolution + reconstitution-as-climax) | B major -> C major (half-step at reconstitution) | 149 | cristal baschet + tenor saxophone + french horn |
| 231 | Where the Spring Holds Still | quartal harmony arc (registral collapse-to-unison climax) | E minor (loose tonal center blurred by quartal voicings, no modulation) | 145 | nyckelharpa + bass trombone + cimbalom |
| 232 | A Scale for Difficult Mixtures | metric modulation arc (tempo-exceeded climax via subdivision pivots) | C-sharp minor -> D minor (half-step at second pivot) | 83 | duduk + cornet + singing saw |
| 233 | Light Across the Open Form | orchestral cantus firmus arc (line-shape arch climax) | G major -> A-flat major (half-step at apex) | 112 | steel tongue drum + felt piano + contrabassoon |
| 234 | What the High Pass Finally Releases | threnody-to-apotheosis arc (lament -> crisis -> blazing apotheosis) | D-sharp minor -> E minor (half-step at apotheosis) | 128 | oboe d'amore + mellotron + flugelhorn |
| 235 | When the Kiln Mouth Glows | chaconne ground-bass variations (accumulating density on repeating harmonic ground) | A-flat minor -> A minor (half-step at maximum density) | 153 | tuba + harpsichord + vibraphone |
| 236 | At the Transit Wire | double variation (alternating themes A B A' B' A'' coda) | F-sharp minor -> G minor (half-step at A'' lift) | 151 | viola + bass clarinet + tubular bells |
| 237 | What the Tide Returned | siciliano-to-cabaletta (slow lilt -> hard tempo pivot -> tutti relative-major gallop) | E-flat minor -> G-flat major (relative major at the cabaletta pivot) | 154 | viola da gamba + ophicleide + marimba |
| 238 | Cast in Bronze and Rung Once | thematic metamorphosis arc (single theme transformed across vulnerability/conflict/transfiguration) | B minor -> C minor -> C major (transfiguration in the parallel major) | 155 | cor anglais + french horn + harp |
| 239 | Indigo and Madder at the Last Light | hymn-and-fugato (chorale -> fugato eruption -> hymn return with fugato underneath) | A major -> B-flat major (half-step at hymn return) | 156 | ondes martenot + contrabass clarinet + bowed vibraphone |
| 240 | Raking Salt Before the Tide Returns | scherzo-trio-scherzo (vigorous tutti -> lyric trio retreat -> tutti return with renewed force) | F minor -> F-sharp minor (half-step at scherzo return) | 157 | double bass + subcontrabass saxophone + handpan |
| 241 | Iron and Glass at First Light | lament-bass ground (descending tetrachord ostinato with orchestrational accumulation) | G-sharp minor -> A minor (half-step at cycle 6 tutti) | 158 | baryton + bass flute + mbira |
| 242 | Curtain Rises on a Whole Melody | hocket-and-fusion (stutter-weave hocket -> unison fusion arrival) | D-flat major -> D major (half-step at fusion) | 159 | upright bass + clavichord + piccolo |
| 243 | Frost on the Deckle | barcarolle-to-grand-finale (continuous rocking 6/8 ostinato with cantilena -> chromatic B -> tutti finale) | D-flat minor -> D minor (half-step at grand finale) | 161 | bass trombone + glass marimba + prepared piano |
| 244 | When the Doves First Stir | sarabande-and-double (bare statement + ornamented double; truncated) | A major -> B-flat major (half-step at double tutti peak) | 47 | cornet + tenor saxophone + crotales |
| 245 | What Each Ward Holds | lyric tone poem (single-movement continuous cantabile thread) | C-sharp minor -> D minor (half-step at blazing return) | 162 | flugelhorn + contrabassoon + glockenspiel |
| 246 | Iron Canopy at Last Light | da capo aria (orchestral ABA with ornamented return) | B-flat minor -> B minor (half-step at bloomed return) | 152 | mellotron + viola da gamba + tubular bells |
| 247 | Dawn the Falcon Lifts | concert march with trio (fanfare -> strains -> contrasting trio -> tutti return) | B major -> C minor -> B major (trio in relative minor) | 136 | french horn + hurdy gurdy + celesta |
| 248 | Rain on the Quai | French cinematic chanson without vocals (parametrized lyrics + production tokens + two-body trio) | A minor -> F major (relative-major bridge) | 132 | accordion + harp + clarinet |
| 249 | Dopo la Chiusura | Italian neoclassical cinematic (playbook generalization test: noir chamber + 3-body trio) | F minor -> A-flat major (relative-major bridge) | 144 | harpsichord + cor anglais + bass clarinet |
| 250 | Where the Fog Parts for Iron | modern Hollywood cinematic film cue (playbook 3-body trio + production tokens + parametrized lyrics) | G minor -> B-flat major (relative-major bridge) | 150 | bass trombone + harp + oboe d'amore |
| 251 | The Keeper in January | Nordic noir cinematic (playbook generalization continues — 4 lanes confirmed) | D-sharp minor -> E minor (half-step at modulation) | 163 | trombone + viola + waterphone |
| 252 | Cortege at First Light | slow processional cinematic with Build/Silence/Drop frisson stack — pushed-duration experiment (target 4:00-6:00) | G-sharp minor -> A minor (half-step at the drop) | 164 | ophicleide + nyckelharpa + cimbalom |
| 253 | Neon sur Asphalte Mouille | cinematic orchestral-darkwave hybrid (synth experiment — Moog pad + taiko + tuba) | D minor (chromatic build, brief modal lift) | 90 | taiko + Moog analog pad + tuba |
| 254 | Lux Solstitii | cinematic neoclassical 'returning light' arc (B minor -> C major parallel-major drop, slow-to-warm) | B minor -> C major (parallel major at the drop) | 106 | chalumeau + baryton + handpan |
| 255 | Limen Descensus | modern Hollywood cinematic - descending procession (Build/Silence/Drop + BPM-aware 4:00-5:00 target) | E-flat minor -> E minor (half-step at Drop) | 135 | trumpet + contrabass clarinet + bowed vibraphone |
| 256 | Crest of the First Light | modern Hollywood cinematic - ascending heroic arc (parallel-major triumph at the Drop, inverse of v255) | F-sharp minor -> F-sharp major (parallel major at the Drop) | 165 | ondes martenot + french horn + subcontrabass saxophone |
| 257 | Linens | lyrical sweeping cinematic - 'what was lost' bittersweet arc (exposed-Drop test) | C-sharp minor -> D minor (half-step, both minor) | 138 | flugelhorn + contrabassoon + cristal baschet |
| 258 | Le Cortège | lyrical sweeping cinematic elegy - full-density Drop test (Drop-density hypothesis partially supported) | A-flat minor -> A minor (half-step, both minor — earned luminous sorrow) | 166 | mellotron + oboe + marimba |
| 259 | When the Square Fills | modern cinematic festival-arrival - forward-motion concept (Drop-density + concept-as-driver hypotheses both validated) | D-flat minor -> E major (enharmonic relative major at the Drop) | 160 | cornet + tenor saxophone + viola da gamba |
| 260 | Static | drift phonk viral pivot (first non-instrumental, vocals + 808s + cowbell) | A minor | 138 | 808 sub-bass + cowbell + slowed-vocal-chops |
| 261 | Polnoch | slap house viral cycle - Russian future rave (vocals + sidechain pluck + four-on-the-floor) | A minor -> B-flat minor (half-step lift at Final Drop) | 124 | sidechain pluck lead + female vocal + four-on-the-floor kick |
| 262 | Fumée | French dark electro-pop viral cycle - husky low-register contralto, French lyrics, voice-differentiation experiment | D minor | 96 | muted Rhodes + husky French contralto + deep sub-bass |
| 263 | Candy in the Wires | hyperpop / digicore / glitchpop viral cycle - pitched-up kawaii female, bitcrushed glitch | E major | 160 | supersaw lead + pitched-up kawaii vocal + glitched hi-hats |
| 264 | Tóxico | neoperreo / dembow / Latin trap viral cycle - raspy mid-register Latina sing-rap | Bb minor | 110 | distorted 808 sub + dembow groove + midrange synth lead |
| 265 | Fervo | funk carioca / baile funk / tamborzão viral cycle - shouty female Portuguese MC | G minor | 150 | tamborzão 808 kick + tambor/surdo + baile siren |
| 266 | Sgubhu | amapiano / South African house / log drum viral cycle - relaxed Zulu-English male spoken-sung | C minor | 115 | log drum + four-on-the-floor kick + sax-pad chord stab |
| 267 | Pind | modern Punjabi pop / P-Pop / R&B-infused viral cycle - smooth Punjabi male sing-rap | F# minor | 92 | 808 sub + Rhodes electric piano + dhol-accent + tumbi-riff |
| 268 | Bbang | modern 4th-gen K-pop / NewJeans-adjacent hyperdance viral cycle - multi-voice female group harmony | B minor | 132 | four-on-the-floor kick + retro pop bass + sparkly synth arpeggio |
| 269 | Halo | liquid drum and bass / 2026 understated wave viral cycle - ethereal breathy female solo | E minor | 174 | Amen breakbeat + reese sub-bass + Rhodes atmospheric pad |
| 270 | Wahala | Afrobeats / Nigerian Afro-fusion / Afropop viral cycle - male falsetto-mix Pidgin-Yoruba-English | F minor | 105 | Yoruba talking drum + 808 sub + electric piano |
| 271 | Boteco | sertanejo universitário / sofrência ballad viral cycle - male duo close harmony caipira PT | G major | 88 | violão + sanfona + upright bass |
| 272 | Yalla | Mahraganat / electro-shaabi / Egyptian street pop viral cycle - male autotuned chesty Arabic street | C# minor | 100 | darbuka percussion + sawtooth synth (mizmar timbre) + sub-bass |
| 273 | Kangen | Modern dangdut koplo / hip-dut viral cycle - female melismatic Indonesian belt with Auto-Tune sob | A major | 120 | kendang koplo drum + suling bamboo flute + 808 sub |
| 274 | Boliche | RKT / urbano argentino / Buenos Aires street trap viral cycle - male laid-back porteño nasal flow | G# minor | 98 | RKT syncopated kick + plucky reggaeton synth + 808 sub |
| 275 | Yue | Modern Mandopop ballad / R&B-infused Mandarin pop viral cycle - male crooner with falsetto flips | F# major | 78 | Steinway piano + warm string pads + 808 sub |
| 276 | Saavan | Modern Bollywood ballad / Hindi pop monsoon-romance viral cycle - female Hindustani playback-singer melismatic | D major | 90 | nylon acoustic guitar + tabla pulse + harmonium pad |
| 277 | Yoru | Modern Japanese city-pop / future-funk-adjacent viral cycle - female warm 80s-inflected cool-girl solo | Bb major | 108 | Roland Juno-60 analog pads + slap bass + Rhodes electric piano |
| 278 | Gece | Modern Türk trap / Turkish trap viral cycle - male chesty Anatolian with makam-modal Auto-Tune | Eb minor | 140 | 808 trap kit + saz lute + ney reed flute |
| 279 | Kalt | Modern Berlin tech-house / minimal techno viral cycle - German sprechgesang deadpan monotone | A minor | 128 | tech-house pluck synth + acid-303 bassline + sub-bass |
| 280 | Bay | Vinahouse / V-pop / Vietnamese electronic dance viral cycle - female husky whisper-belt with Vietnamese tonal contours | D minor | 144 | Vinahouse rolling bass + rave synth stabs + heavy sub |
| 281 | Tma | Russian phonk / drift phonk / Russian-language hyperpop viral cycle - male shouty distorted Russian MC | F minor | 155 | 808 cowbell + bitcrushed kick + cathedral organ pad |

## Next-cycle priorities

**ARC DIVERSIFYING (v220–v221):** v216–v219 all shared the entry → build → [Silence] ~2:00 → half-step-up return skeleton; the judge was docking concept-novelty for it. v220 (perpetuum mobile) broke it first — flat kinetic tension, no silence/no modulation, winding down in stable F minor (judge 94). v221 (tarantella accelerando-to-collapse, judge 95) is the second new arc: continuous acceleration through terraced surges to a hard cut-off at peak velocity, with the harmonic payoff delivered by a **parallel-major lift (Ab minor → Ab major)** instead of a half-step modulation — a genuinely different "brighten at climax" device worth reusing. Arcs still untried: arch (ABCBA), climax-at-the-front, true terraced/through-composed without acceleration.

**⚠ SHORT-DURATION WATCH — UPDATE (v221 → v222 → v223):** v221 rendered 0:42 + 1:34 (both short) with a 7-line scaffold + "cut-off" terminal language. v222 rendered 2:53 + 3:07 (both in target) after switching to a 10-section scaffold and a sustained-fade ending. v223 with the SAME 10-section + sustained-fade safeguards rendered 2:49 + **1:26** — clip 1 in target, clip 2 short. So the fix is real but not deterministic; Suno still terminates the second variant short some of the time. Next probes: (a) does an even longer scaffold (12–14 sections) raise the floor on clip 2, or does it stall at "first variant gets it, second doesn't"? (b) does the "climax-at-the-front" arc itself bias toward early truncation because the dramatic peak is at the open and Suno may interpret late material as outro-eligible? (c) worth comparing v222 (additive-accretion peak at the END) vs v223 (peak at the START) clip-2 durations across more cycles. Tentative hypothesis: front-loaded arcs are more truncation-prone because the model sees "climax done" early.

1. ~~Apply timestamps~~ ✅ (v112+)
2. ~~Apply purpose phrase~~ ✅ (v112+)
3. ~~Use novelty_surface.json before drafting~~ ✅ (v112+)
4. ~~Try fugue, arch form, rondo~~ ✅ (v113, v114, v115)
5. ~~Revive pre-synthesis instruments~~ ✅ (kora v118 = deepest at 86-version gap)
6. ~~Return to electronic fusion~~ ✅ (v116 future garage, v118 glitch)
7. ~~Try theme-and-variations or sonata form~~ ✅ (v119 theme-and-variations)
8. ~~Try a duo (2 instruments) instead of trio~~ ✅ (v120 bass flute + steelpan duo)
9. Fix novelty_surface.py negative-prompt counting bug
10. Codify /suno skill submission fixes (5 fixes logged in results-tracker)
11. Stop including duration language in new prompts — use freed chars for better description
12. Research one new 2026 Suno technique per cycle
13. Update this file with each cycle's learning ← YOU ARE HERE
