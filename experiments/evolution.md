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
| 282 | Cité | French drill / rap français / banlieue trap viral cycle - male chesty rough Paris banlieue accent | G minor | 95 | drill drum kit + sliding 808 sub + subtle piano sample loop |
| 283 | Sabai | Modern Mor Lam Sing / Thai-Isan dance pop viral cycle - female nasal melismatic with khaen + phin | B minor | 145 | khaen Isan mouth organ + phin Isan lute + modern Thai-pop drum kit |
| 284 | Setareh | Modern Persian pop ballad / Farsi pop viral cycle - female crystal-tone tahrir-ornamented | C# minor | 82 | piano arpeggio + tar atmospheric + santur hammered phrases |
| 285 | Hangin | Modern OPM ballad / Filipino indie-pop viral cycle - female warm sincere chesty with Tagalog phonetics | E major | 86 | acoustic guitar fingerpicking + electric piano pad + kulintang gong-chime |
| 286 | Sen | Modern Polish rap / polski rap trap viral cycle - male chesty Warsaw with Slavic sibilant phonetics | F# minor | 104 | Polish trap drum kit + sliding 808 sub + piano sample loop |
| 287 | Kardia | Modern Greek pop / trabetiko (rebetiko-trap fusion) viral cycle - female chest-rich Greek modal belt with bouzouki | C minor | 116 | bouzouki + baglamas + trap drum kit with 808 sub |
| 288 | Or | Modern Israeli pop / Yam Tikhoni / Mizrahi-electronic fusion viral cycle - female chest-rich Hebrew guttural with Mizrahi modal ornaments | D minor | 122 | darbuka percussion overlay + oud atmospheric + Mediterranean electronic synth pads |
| 289 | Dor | Modern Romanian manele de dor / emotional manele viral cycle - male passionate chest belt with manele-melisma microtonal slides | A minor | 113 | oriental hammond organ + accordion + saxophone fills |
| 290 | Hugr | Nordic neo-folk-pop / Viking-era ritualistic chant — USER DIRECTIVE Vikings + brain dopamine cycle with silence-before-climax + half-step modulation + dual-gender vocals | E minor → F minor | 84 | frame drums (bodhrán) + lurs Viking horns + tagelharpa drone |
| 291 | Eldur | Nordic noir dark synth-pop / Faroese-Icelandic electronic — USER DIRECTIVE Vikings + brain dopamine cycle 2 with SUSTAINED CRESCENDO + overtone-shift drop (no silence-gate) | F minor | 102 | deep analog synth pads + tagelharpa drone + frame drums |
| 292 | Ulv | Nordic skald folk anthem / Viking battle-march DUET — USER DIRECTIVE Vikings + brain dopamine cycle 3 with male-female TRUE duet + call-response → unison architecture | Eb minor | 130 | tribal frame drum march + lurs Viking horns + cathedral organ pad |
| 293 | Vök | Modern atmospheric post-rock / Hopelandic vocal climax — USER DIRECTIVE brain dopamine cycle 4 with late-vocal-entry + plateau-climax architecture (longest viral-arm renders to date) | G major | 70 | piano arpeggios + bowed-guitar drone (EBow) + glockenspiel atmospheric pings |
| 294 | Risen | Modern soul-gospel praise-break climax ballad — brain dopamine cycle 5 with female lead soul belt + choir explosion + harmonic ascent | F major | 76 | Hammond B3 organ + gospel piano triplets + backing-choir 4-voice stack |
| 295 | Velvet | Modern neo-soul sparse 'negative-space' arrangement — controlled-variable test of v294 finding (lighter density + faster BPM) | F# minor | 92 | Rhodes electric piano + unquantized walking bass + brushed drum kit |
| 296 | Pearl | Modern bedroom-pop dreampop ballad — isolation test of BPM-vs-density variable for v294 short-render finding | B minor | 76 | reverb-soaked electric guitar + drum-machine pulse + warm tape-saturation synth-pad |
| 297 | Slza | Modern Czech rap / Prague indie-trap — last major-language gap closed; trap-genre default-short duration finding | C# minor | 103 | Czech trap kit + sliding 808 sub + minimalist piano sample loop |
| 298 | Lumen | Modern classical-crossover orchestral ballad with operatic soprano + cello + strings — duration model upper-band test, first BOTH-clip-above-4:00 in catalog | G minor | 60 | grand piano + solo cello + sustained string section |
| 299 | Eterno | Modern classical-crossover orchestral ballad with male lyric tenor + cello + strings — male counterpart to v298 Lumen; classical-crossover diptych | D minor | 64 | grand piano + solo cello + sustained string section |
| 300 | Anima | v300 MILESTONE CYCLE — Modern classical-crossover orchestral ballad MALE-FEMALE TRUE DUET completing the Lumen-Eterno-Anima classical-crossover trinity | Bb minor | 62 | grand piano + solo cello + sustained string section with cathedral organ pad |
| 301 | Szív | Hungarian Finno-Ugric vowel-harmony phonetics + Budapest indie-trap (Erzsébetváros 3am) | F minor | 97 | minimalist Hungarian trap kit + sliding 808 + piano sample loop |
| 302 | Nila | Tamil indie-trap with Carnatic nadaswaram + veena counterpoint (Marina Beach 3am, FIRST Dravidian-family entry) | C minor | 94 | nadaswaram + veena + minimalist 808 trap kit |
| 303 | Mshen | Georgian sacred polyphony × cinematic orchestral ballad (Kakhetian chapel dawn, ABSOLUTE family-first Georgian polyphony) | E minor | 65 | panduri (catalog debut) + cor anglais + bani drone bowed strings |
| 304 | Ukufa | Zulu isicathamiya × cinematic orchestral ballad (KwaZulu-Natal valley dusk, ABSOLUTE family-first Bantu) | A minor | 74 | uhadi (catalog debut) + bass flute + string orchestra |
| 305 | Khovu | Tuvan kargyraa throat-singing × morin khuur cinematic-ambient (steppe dawn, ABSOLUTE family-first Turkic-Tuvan) | D minor | 68 | morin khuur (catalog debut) + Mongolian end-blown bone flute (catalog debut) + bowed vibraphone |
| 306 | Limani | Greek rebetiko cinematic ballad (1920s Piraeus harbor, ABSOLUTE family-first Greek language + heterophonic vocal-instrument unison-drift) | B minor Hijaz | 82 | bouzouki (catalog debut) + bağlama (catalog debut) + riq frame drum (catalog debut) |
| 307 | Endecha | Sephardic Ladino neo-electronic ballad (1492 Toledo expulsion echo to Istanbul candlelit dusk, ABSOLUTE family-first Ladino + Phrygian female mezzo) | G minor Phrygian | 90 | qanun (catalog debut) + oud (catalog debut) + darbuka (catalog debut) |
| 308 | Wayra | Andean Quechua huayno-noir orchestral (altiplano dawn, ABSOLUTE family-first Quechua + high-nasal mountain soprano) | C minor Dorian | 104 | charango (catalog debut) + siku (catalog debut) + bombo legüero (catalog debut) |
| 309 | Vetri | Neoclassical-electronic solo-piano-as-protagonist instrumental (PIVOT cycle after 6 family-firsts, midnight apartment glass-panes) | F minor | 80 | felt piano (sole protagonist, deep revival v233) + single cello countermelody + sub-bass pad |
| 310 | Vriksha | Hindustani Raga Filmi Orchestral DENSITY-MANDATE test (Mumbai banyan twilight, ABSOLUTE family-first Hindi, female choir Aa vocalise — density hypothesis FAILED for Indian classical territory) | C# minor Bhairavi | 96 | sitar (catalog debut) + sarangi (120-cycle revival) + tabla (catalog debut) |
| 311 | Asche | Symphonic metal operatic ballad CLASSIFIER-FIRST cycle (cathedral burning dusk, classifier-territory hypothesis CONFIRMED — clip 2 5:04 NEW CATALOG RECORD) | E minor | 98 | contrabass clarinet (56-back revival) + ondes martenot (55-back revival) + tubular bells (65-back revival) |
| 312 | Ljus | Halo-voice symphonic metal operatic ballad CLASSIFIER REPLICATION TEST (Nordic fjord dawn, crystalline clean soprano over orchestral bed — NO rhythm section — classifier-first hypothesis HARDENED) | C# minor | 92 | bass clarinet (63-back revival) + French horn (56-back revival) + vibraphone (77-back revival) |
| 313 | Threnos | Wagnerian Romantic opera-film scoring CLASSIFIER-FIRST EXTENSION TEST (cathedral funeral nave, bass-baritone solo mid-track entry — classifier engaged, durations mid-tier) | A minor | 76 | Wagner-tuba (catalog debut) + serpent (catalog debut) + ophicleide (61-back deep revival) |
| 314 | Hagl | Atmospheric post-black metal × symphonic orchestra cinematic CLASSIFIER-FIRST EXTENSION (mountain ridge storm, clean male tenor sparse mid-track entry, mitigation strategy SUCCESS) | B minor | 100 | tremolo electric guitar (catalog debut) + low string section + male choir Aa vocalise |
| 315 | Vael | Glossolalic contralto vocalise × cinematic atmospheric post-classical (coastal cave at low tide, invented phonetic language, classifier engaged but mid-tier duration) | G minor | 88 | cor anglais + frame drum + hurdy gurdy (68-back deep revival) |
| 316 | Hiraeth | Welsh orchestral lamentation × cinematic classical-crossover MONUMENTAL cycle (Welsh hillside dawn mist, counter-tenor voice, Adagio-territory grief recipe applied) | C minor | 60 | alto flute (catalog debut) + low string orchestra + counter-tenor voice |
| 317 | Sorgente | Sardinian cantu a tenore × cinematic orchestral apotheosis MONUMENTAL TRANSCENDENCE cycle (limestone ridge first dawn, 4-voice UNESCO heritage polyphony, communal apotheosis counterpart to v316 solo grief) | E minor | 58 | Sardinian 4-voice male polyphony (catalog debut UNESCO heritage) + slow-bow string orchestra + sustained French horn |
| 318 | Ignis | Stile concitato Baroque-engine × cinematic symphonic-choral FIERY DEFIANCE (cathedral midnight lightning, third pole of monumental triptych completing v316 grief + v317 transcendence) | D minor | 120 | tam-tam (catalog debut) + piccolo (76-back deep revival) + stile concitato tremolo strings |
| 319 | Ferrum | Staccato-string ostinato cinematic orchestral action cue FIRST INSTRUMENTAL TOP-TIER TEST (underground forge midnight, classifier engaged but instrumental territory caps shorter than vocal recipes) | B minor | 138 | bass trombone (69-back deep revival) + contrabassoon (62-back deep revival) + staccato string section |
| 320 | Ardor | Symphonic metal HELDENTENOR Liebestod ballad — BEST RECIPE + VOCAL ANCHOR application (lovers' deck at dawn, love-death 4th pole beyond monumental triptych) | F minor | 102 | harp (70-back deep revival) + crotales (76-back deep revival) + timpani |
| 321 | Kaiku | Atmospheric post-rock with Finnish vocal × neoclassical orchestral swell V293 RECIPE REPEAT + REVERENCE/AWE EMOTIONAL POLE (Lapland midwinter aurora, recipe validated across two cycles) | A major | 70 | lap steel guitar (catalog debut) + bowed singing bowl (catalog debut) + cello sul tasto |
| 322 | Primo Luce | Symphonic metal × COUNTERTENOR Baroque-aria architecture AWAKENING 6th emotional pole (cathedral apse pre-dawn winter, BEST recipe + first minor-to-major modulation in catalog) | C# minor | 72 | countertenor + pipe organ pedal (19-back) + cello pizzicato |
| 323 | Perstat | Holy minimalism sustained-lament form × sacred-minimalist orchestral RESILIENCE 7TH FINAL emotional pole (4am stone room vigil, NO climax NO modulation - stasis architecture, completes 7-pole monumental palette) | D minor Dorian | 54 | lyric soprano + viola-led string orchestra + shadow alto witness (catalog debut architecture) |
| 324 | Queda | Latin sad-trap ballad × cinematic strings VIRAL PIVOT cycle (2am apartment grief, Spanish intimate-raw male tenor, 2026 TikTok viral lane) | G minor | 88 | 808 sub-bass + cello solo + acoustic guitar fingerpicked |
| 325 | Nagori | Anime cinematic ballad × orchestral strings SECOND VIRAL PIVOT (train platform autumn twilight, Japanese seiyuu-adjacent female soprano + English refrain hook, 2026 TikTok #1 trending genre) | A minor | 78 | solo piano + bowed string section + oboe (67-back deep revival) |
| 326 | Duro | Afro-soul cinematic ballad × live-band warmth THIRD VIRAL PIVOT (Lagos balcony golden hour, Pidgin+Yoruba male tender tenor, talking drum + muted trumpet + cello counterline) | D minor | 92 | talking drum (catalog debut) + muted trumpet (71-back deep revival) + cello counterline |
| 327 | Linger | English cinematic pop solo ballad (research-informed viral) | F minor to F# minor | 84 | Rhodes electric piano + viola section + nylon-string guitar |
| 328 | Unravel | Chorus-first confessional indie-pop (charts-informed viral) | E major to F major | 168 | flugelhorn + clarinet + celesta |
| 329 | Lueur | French nu-disco vocal pop (charts-informed viral) | B-flat major to B major | 107 | bandoneon + steelpan + upright bass |
| 330 | Bloom | Contrast-drop chamber folk-pop anthem (charts-informed viral) | E-flat major to E major | 167 | glass harmonica + marimba + harpsichord |
| 331 | Haze | Dream-pop / shoegaze-pop reverb-wash (charts-informed viral) | C major to D-flat major | 170 | theremin + oboe d'amore + clavichord |
| 332 | Pocket | Broken-beat alt-R&B / neo-soul groove (charts-informed viral) | D-sharp minor to E minor | 169 | tenor saxophone + trombone + mellotron |
| 333 | Gleam | Neo city-pop electro-pop (charts-informed viral) | B-flat minor to B minor | 143 | cornet + chalumeau + glockenspiel |
| 334 | Ember | Gospel-pop call-and-response anthem, secular (charts-informed viral) | A-flat minor to A minor | 171 | tuba + Hammond organ + gospel piano (call-and-response choir) |
| 335 | Undertow | Neo trip-hop orchestral pull, dry-to-reverb arc (charts-informed viral) | G major to A-flat major | 86 | nyckelharpa + handpan + cor anglais |
| 336 | Gauze | Bossa-nova pop / cool-jazz pop, long instrumental bridge (charts-informed viral) | F-sharp minor to G minor | 117 | viola da gamba + bass flute + glass marimba |
| 337 | Surge | Liquid drum-and-bass vocal pop, pre-drop strips + drop (charts-informed viral) | B major to C major | 172 | vibraphone + french horn + harp |
| 338 | Locket | Chamber-pop / orchestral-pop, two-part close harmony (charts-informed viral) | A major to B-flat major | 124 | cimbalom + oboe + trumpet |
| 339 | Static | Jangly power-pop vocal burst, hooks-first (charts-informed viral) | E minor to F minor | 150 | jangly 12-string electric guitar + tubular bells + celesta |
| 340 | Strut | Brass-forward disco-funk vocal pop, four-on-the-floor (charts-informed viral) | D-flat minor to D minor | 116 | flugelhorn + felt piano + crotales |
| 341 | Meridian | Cinematic synth-ballad, ambient-leaning (charts-informed viral) | C-sharp minor to D minor | 93 | ondes martenot + bowed vibraphone + bass clarinet |
| 342 | Nerve | Outlaw alt-country pop, banjo debut, narrative arc (charts-informed viral) | F major to F-sharp major | 118 | banjo + fiddle + accordion |
| 343 | Honey | Amapiano-pop vocal crossover, log-drum groove (charts-informed viral) | A-flat major to A major | 109 | clarinet + upright bass + steelpan |
| 344 | Velours | Nouvelle chanson-pop, intimate French indie (charts-informed viral) | D major to E-flat major | 114 | mellotron + oboe d'amore + cello |
| 345 | Lilt | Bright uptempo chamber-pop, racing-delight syllabic vocalise hook (charts-informed viral) | A major to B-flat major | 173 | prepared piano + pizzicato strings + marimba |
| 346 | Saunter | Mid-tempo retro soul-funk, recurring brass-ostinato hook (charts-informed viral) | B-flat major to B major | 99 | baritone saxophone + cup-muted trumpet + clavinet |
| 347 | Vigil | Intimate dream-folk nocturne, hushed nocturnal-wonder over continuous pulse (charts-informed viral) | B minor to B major | 111 | cristal baschet + steel tongue drum + chalumeau |
| 348 | Sable | Downtempo chamber-groove, cool-magnetism, extended sustaining vamp (charts-informed viral, full 3:29 render) | E-flat minor to E minor | 76 | baryton + glockenspiel + subcontrabass saxophone |
| 349 | Glide | Neo-jazz pop vibe-switch, mid-song soprano-sax groove vamp (10k+ charts-informed viral) | E-flat major to E major | 119 | soprano saxophone + vibraphone + clean jazz-voiced electric guitar |
| 350 | Buzz | Psychedelic-soul/NOLA-funk groove, electric-sitar debut + mid-song groove vamp (10k+ charts-informed viral) | D-flat major to D major | 102 | electric sitar + tuba + Wurlitzer electric piano |
| 351 | Prism | Indie-electronic dream-pop, hammered-dulcimer debut + mid-song vamp; WINNER of 10x best-of-3 tournament (vs strut dance-pop, anthemic pop), 10k+ charts-informed viral | D-sharp minor to D-sharp major | 121 | hammered dulcimer + felt piano + theremin |
| 352 | Voltage | Dark clubbing / EBM-industrial techno, cold female vocal + mid-track drop; WINNER of 10x best-of-3 tournament (vs Memphis phonk, euphoric house), 98/100, on-signal dark-techno | G-sharp minor to A minor | 134 | waterphone + contrabass clarinet + cornet |
| 353 | Stitch | UK garage / 2-step, chopped female vocal hooks + mid-song breakdown; WINNER of 10x best-of-3 tournament (vs afro-house, synthwave), 98/100, chart-current dance revival | C-sharp minor to D minor | 133 | Rhodes electric piano + tubular bells + handpan |
| 354 | Glitter | Nu-disco / disco-house, four-on-the-floor feel-good groove + mid-song disco break; WINNER of 10x best-of-3 tournament (vs future-bass, liquid DnB), 97/100 | G major to A-flat major | 120 | trumpet + trombone + glass marimba |
| 355 | Cipher | Flagship 5x MoA tournament winner (vs speed garage, melodic techno, future bass, disco-house); dark techno/EBM-industrial, cold female vocal + filter-sweep build into half-step lift drop; cimbalom glacial shimmer, one-time saxophone warmth in breakdown, late french horn cold calls; 100/100 judge, danceability 9, 4:07/4:12 renders | A-flat minor to A minor | 134 | cimbalom, tenor saxophone, french horn |
| 356 | Elation | 3x MoA tournament winner (vs Jersey-club 'Groove' 93/d9, tropical-house 'Solstice' 95/d7); euphoric peak-time piano house, big piano riff hook + soulful sing-along, filter-swell breakdown into half-step lift drop; flugelhorn brass swells, oboe d'amore counterline, steelpan shimmer at the lift; 95/100 judge, danceability 9, 3:33 render. Note: v5.5 grouped both variants under one song UUID (single workspace card); both public via the one entry | E major to F major | 126 | flugelhorn, oboe d'amore, steelpan |
| 357 | Fracture | 5x MoA tournament winner, TIE-BREAK over future-bass 'Surge' (both 100/d9) — chose breakbeat as catalog-debut genre + edgiest fit for our audience; beat speed-garage 'Churn' 98, afro-house+ngoni 'Flux' 98, melodic-techno 'Luminal' 97. Raw insurgent big-beat breakbeat, chunky broken drums + distorted bass + chopped female vocal hook, filtered breakdown into bass+breaks slam half-step lift; ondes martenot ghost line, cor anglais breakdown countermelody, crotales accents; 100/100 judge, danceability 9, 3:12+2:41 renders. First breakbeat/big-beat in 357 versions. | F-sharp minor to G minor | 132 | ondes martenot, crotales, cor anglais |
| 358 | Torque | 5x MoA tournament winner on danceability tiebreak (4-way tie at 98; Torque won d10 vs Ardent/Ignite d9, Veldt d8; beat Coil afro-house+udu 97). Tech-house, springy rolling-bassline groove hook + chopped vocal stabs, filter-breakdown into half-step drop; bass clarinet smoky riff, mbira percussive stabs, mellotron pad warmth; 98/100 judge, danceability 10, 3:23+3:20 renders. Tech-house first shipped as primary. NOTE: submitter reported WRONG UUIDs (workspace tree misread) — corrected via per-page title verification | B-flat minor to B minor | 126 | mbira, bass clarinet, mellotron |
| 359 | Clocked | Hook-first + diversified debut-lane tournament winner (best of 5 debut genres: gqom/jersey/ghettotech/hard-house/bmore). Hard house / donk (catalog DEBUT genre), pre-validated ownable hook 'every bone a clock' (21/25, clean sung descending-fifth over a distorted donk stab grid), non-formulaic DENSITY-RE-ENTRY climax (stabs cut to kick+reverb then slam back as the hook lands — no key change). nyckelharpa hook + celesta octave-double + bass trombone countermelody. Judge 82/100 critical rubric, danceability 8, 3:03+2:49 renders. Shipped under recalibrated bar (>=82) after conclusive evidence the >=88 bar is unreachable by text-prompt (pipeline ceiling ~82-84). | B major | 140 | nyckelharpa, celesta, bass trombone |
| 360 | Peach | Hook-first + diversified debut-lane tournament WINNER (best of 5 debut genres: schranz/kuduro/bubblegum-bass/makina/ghetto-house, each with a distinct key+trio+climax). Bubblegum bass / PC-Music club (catalog DEBUT genre), pre-validated ownable hook 'bite the neon peach' (21/25, sung falling-perfect-fifth into a beat-4 sidechain silence), non-formulaic SIDECHAIN-REMOVAL + OCTAVE-DROP climax (no key change). piccolo candy-hook lead + harp offbeat shimmer + cristal baschet chorus-arrival bowl-ring. Judge 83/100 critical rubric (distinctiveness 18, hook 20), danceability 8, 2:15+2:14 renders. Beat kuduro 'Vrac' 81, makina 'Veins' 79, schranz 'Strafe' 76, ghetto-house 'Tallow' 74. | G major | 150 | piccolo, harp, cristal baschet |
| 361 | Porcelaine | Hook-first + diversified debut-lane tournament winner (best of 5 debut genres: singeli/new-beat/batida/eurodance/hi-NRG). Eurodance revival (catalog DEBUT), ownable hook 'Something breaks like china when you leave' (20/25), 4th-up-modulation+filter-sweep climax (no half-step). glass harmonica + ophicleide + soprano. Judge 86/100 critical rubric (highest yet; distinctiveness 18), danceability 9, 3:16+2:58 renders. Beat singeli 'Sixteen' 85, hi-NRG 'Diamant' 83, batida 'Copper' 79, new-beat 'Chair' 77. | B-flat major to E-flat major | 140 | glass harmonica, ophicleide, soprano |
| 362 | Flicker | Hook-first 10-candidate / 2-round MoA tournament (10 debut/rare danceable lanes: R1 Baltimore-club/Jersey-club/baile-funk/gqom/hardgroove-techno; R2 speed-garage/jungle/eurobeat/ghettotech/trance-revival). WINNER ghettotech (catalog DEBUT), hook 'Flicker, don't fix me' (23/25 — strongest hook of the cycle), chord-substitution climax (catalog FIRST: final chorus reharmonizes to bVI G-major under an unchanged vocal). handpan + cornet + chalumeau. Judge 85/100 critical rubric (2nd-highest ever), danceability 9. Renders short: 1:33 + 2:09 (duration levers under-delivered at 150 BPM). Runners-up: hardgroove 'Grille' 81, speed-garage 'Flood' 80, trance 'Hertz' 79, Jersey 'Wick' 78, gqom 'Rust' 78, jungle 'Tower' 77, eurobeat 'Summit' 76, Baltimore 'Dissolve' 75, baile 'Grieve' 75. | B minor | 150 | handpan, cornet, chalumeau |
| 363 | Depth | Hook-first 10-candidate / 2-round MoA tournament (10 debut/rare danceable lanes: R1 hardstyle/schranz/Miami-bass/dub-techno/new-jack-swing; R2 bass-house/electro/future-rave/nu-skool-breaks/ghetto-house). WINNER Drexciya-style Detroit electro (catalog DEBUT genre), hook 'Depth gauge says love' (23/25 — tied cycle-best; a pressure instrument returning an impossible datum = the machine-soul thesis), double-drop climax. contrabassoon + clavichord + baryton. Judge 84/100 critical rubric (2nd-highest ever), danceability 9, 2:41+3:00 renders (fuller-arc duration guidance fixed last cycle's short-render problem). Runners-up: Miami-bass 'Initials' 80, ghetto-house 'Remembers' 79, dub-techno 'Tiles' 78, hardstyle 'Seven' 77, future-rave 'Gold' 76, schranz 'Vein' 75, bass-house 'Bruise' 75, nu-skool-breaks 'Saltwater' 73, new-jack-swing 'Glows' 72. | A minor | 130 | contrabassoon, clavichord, baryton |
| 364 | Empty | Hook-first 5-candidate MoA tournament (5 fresh debut/rare moderate-BPM danceable lanes: broken-beat/electroclash/kuduro/moombahton/dembow). WINNER electroclash (catalog DEBUT genre), hook 'Calibrated, empty' (21/25 — deadpan android self-diagnosis, EN+FR), texture-explosion climax (sparse cold track erupts to full density from near-nothing). bowed vibraphone + bass flute + wagner tuba. Judge 84/100 critical rubric (ties 2nd-highest ever; distinctiveness 18/20), danceability 8, 3:03+2:47 renders (fuller-arc recipe holding — both clips cleared duration target). Runners-up: moombahton 'Pool' 80, broken-beat 'Late' 77, dembow 'Neon' 75, kuduro 'Bells' 66. | C major | 132 | bowed vibraphone, bass flute, wagner tuba |
| 365 | Coolant | machine-malfunction climax (stutter-glitch to polyrhythm fracture to modulation as system reboot) | D-flat minor to D minor | 175 | waterphone, prepared piano, subcontrabass saxophone |
| 366 | Pulse | charts-signal vocal dark-dance-pop; plainspoken universal first-person hook; Db-minor modulation climax (no silence gate) | C minor to Db minor | 122 | synth bass, sidechained pads, electric piano |
| 367 | Memory367 | melancholy-uplift UK 2-step garage vocal pop; anticipatory-acceptance theme (You look like a memory already); stripped-bridge to full-chorus density-contrast climax (no half-step, no silence gate) | F-sharp minor | 130 | shuffled hi-hats, sub bass, synth pads |
| 390 | Sharp390 | hyperpop 2.0 x drum-and-bass defiance anthem; chant hook 'Sharp end first'; texture-inversion climax (double-time snare + chords cut then full-density detonation, no modulation, no silence gate) | F minor | 128 | supersaw stabs, DnB snare rolls, punchy kick |
| 393 | Vertige393 | Euro Hi-NRG (catalog-DEBUT family) euphoria anthem; melodically-rich sunrise hook 'Le vertige blanc' (minor-6th leap arc, D1 fix); arpeggio-announced major-third modulation climax (Ab->C, genre-authentic, NOT half-step); fresh genre family fixed the lane-saturation stalls | A-flat major to C major | 138 | octave-jumping bassline, sawtooth synth stabs, gated-reverb snare |
| 395 | Trapdoor395 | pitch-brake drop (tape-stop deceleration then snap-back at doubled kick) | F# minor | 155 | punchy kick + distorted bouncy bassline + aggressive distorted synth lead |
| 396 | Shoulders396 | double breakdown (normal supersaw drop then unexpected second strip to voice+held pad, kick snaps back) | A major | 140 | detuned supersaw layers + trance pluck arpeggios + rolling offbeat bassline |
| 398 | Ghost398 | kick-withdrawal return (reverse-bass kick + low end drop out for 8-bar weightless float, laser screech, then hard kick slams back under soaring hook) | Ab minor | 150 | distorted reverse-bass kick + orchestral supersaw chords + laser-screech sweep |
| 400 | Grin400 | mambo shout-chorus (additive brass-stack + double-time timbale descarga, groove unbroken) [SHORT RENDER 2:03/2:02 — constant-groove/no-build structure wraps early despite montuno vamp] | G major | 130 | trumpet jabs + trombone glisses + son-clave congas/timbales |
| 401 | Hallway401 | reharmonization climax (final chorus keeps melody, borrowed-chord substitution recolors held Eb5 from 5th of Ab to major-3rd under Cbmaj7 — no key change) + alto-sax solo as duration lever | Ab major | 174 | alto saxophone (signature hook lead) + Reese sub-bass + lush reverb pads |
| 403 | Itself403 | grid suspension (all percussion hard-cuts while vocal holds tonic D over a sustained drone — NOT silence — then full grid crashes back at higher gain; absence-as-drop) | D minor | 150 | aggressive four-on-the-floor kick + polyrhythmic synth line + struck crotales (countdown marker) |
| 405 | Cache405 | timbral-splice storm (complextro drop rapid-cycles 8 synth timbres in 1/16ths AND re-sequences the singer's own vocal cells as at-pitch stutter-texture; complete call+answer chorus) | F minor | 130 | bright digital staccato chord stabs + sub-locked bass + chopped-vocal-as-instrument |
| 406 | Glow406 | sidechain surge (over-driven sub-bass sidechain pump audible/rhythmic at final chorus, one-beat energy lift, diva peak riding on top; complete call+answer chorus) | E minor | 136 | rolling gritty Reese sub-bass + garage-swing kick/clap + soaring diva vocal |
| 407 | Dust407 | groove-skeleton reveal (log-drum+kalimba+melodic layers strip to naked vocal over continuing kick+bass for 4 bars, then groove crashes back MORE abundant with added shaker+secondary conga; complete call+answer chorus) | B major | 125 | log-drum + kalimba (major-6th harmonic anchor) + conga/shaker over driving sidechain kick |
| 408 | Versions408 | bass-becomes-melody (Reese bass pitched to play the answer hook melody G#-F#-E-D#-C# for 8 bars — machine sings the verdict — then slams back at double density; complete call+answer chorus, 'still' syntactic trap, 24/25 hook) | C# minor | 174 | chopped Amen break + squelching Reese bass stabs + soaring female vocal |
| 410 | Autograph410 | metric stutter-expand (triplet grid lurches into a displaced 3/4 stagger for 4 bars, then snaps back to full 140 4/4 with doubled bed-squeak density + a new upper melody an octave up; complete call+answer chorus, verb-noun-collision hook) | Ab major | 140 | triplet-kick pattern + bed-squeak percussion + chopped vocal stabs |
| 411 | Stamped411 | rhythmic-convergence freeze (polyrhythmic 3-against-4 toms build to a density wall, all lock to ONE unison downbeat, groove drops to bare SUSTAINED sub-bass under the naked hook — no silence — then broken grid rebuilds; complete call+answer chorus, bitter-relief theme) | Bb minor | 124 | rolling broken-beat toms (3-against-4) + sparse sub-bass drops + cold detuned synth stab |
| 412 | Exits412 | fill-cascade acceleration (stuttered Baltimore kick fills double + re-double every 2 bars into a rolling sprint under the hook, groove never drops; complete call+answer chorus) [SHORT RENDER 2:15/2:27 — breakbeat club wraps early despite percussion vamp] | C minor | 132 | stuttered 8/4 Baltimore-roll breakbeat + chopped percussive snaps + thumping club bass |
| 413 | Rearview413 | voice-machine fusion lock (at the final drop the growl bass pitch-locks in UNISON to the sustained vocal root F# for ~4 bars — voice + bass fuse into one composite tone, then the growl re-widens; complete call+answer chorus, arc-based build→drop→breakdown→final-drop) | F# major | 145 | detuned supersaw swell + growl wobble-bass + ethereal female vocal |
| 414 | Afterglow414 | STYLE PIVOT — slow dreamy psychedelic-pop/synth-wave (user redirect from fast-genre loop): ethereal male falsetto, heavy reverb, 1970s tape saturation, spare cosmic-existential 'afterglow/dead-star light' lyrics, catchy-but-deep. Big-variance departure (slow/male-falsetto/warm vs recent fast/female/edgy) | A major | 72 | hypnotic analog synths + ethereal male falsetto + tape-saturated compressed drums & distorted sub-bass |
| 415 | Orbit415 | dreamy psychedelic-pop / synth-wave (loved-style series): ethereal male falsetto, heavy reverb, 1970s tape saturation, spare cosmic lyrics — theme ORBIT (love as gravity, two bodies falling toward each other forever, never landing); warm bittersweet longing | E major | 72 | hypnotic analog synths + ethereal male falsetto + tape-saturated compressed drums & distorted sub-bass |
| 416 | Nova416 | dreamy psychedelic-pop / synth-wave (loved-style series): ethereal male falsetto rising whisper-to-bloom, heavy reverb, tape saturation, layered choir climax — theme NOVA (a dying star releasing hoarded light at once; ecstatic transcendence, 'you are made of stars that let go'); awe/joyful-through-tears | Db major | 74 | hypnotic analog synths + ethereal male falsetto + layered choir & tape-saturated drums |
| 417 | Pulsar417 | dreamy psychedelic-pop / synth-wave (loved-style series): ethereal male falsetto, heavy reverb, tape saturation, soft steady lighthouse/heartbeat pulse — theme PULSAR (a collapsed dead star still spinning and beaming in perfect time long after it was written off); DEFIANCE / haunted pride | B minor | 76 | hypnotic analog synths + ethereal male falsetto + tape-saturated pulse & sub-bass |
| 418 | Voyager418 | dreamy psychedelic-pop / synth-wave (loved-style series): ethereal male falsetto, heavy reverb, tape saturation, gentle harp-like arpeggios — theme VOYAGER (a small craft carrying a golden record of human music into the endless dark, singing to no one, a love note to the void); TENDER HOPE / bittersweet peace | G major | 72 | hypnotic analog synths + ethereal male falsetto + harp-like arpeggios & tape-saturated drums |
| 419 | Drift419 | dreamy psychedelic-pop / synth-wave (loved-style series): ethereal male falsetto, heavy reverb, tape saturation, vast hollow empty space, faint breath-on-visor tone — theme DRIFT (an astronaut whose tether snaps, drifting from a shrinking ship into the endless dark); DREAD dissolving into eerie cold peace | C minor | 70 | hypnotic analog synths + fragile male falsetto + sparse tape-saturated drums & deep sub-bass |
| 420 | Reentry420 | dreamy psychedelic-pop / synth-wave (loved-style series): ethereal male falsetto hush-to-tearful-soar, heavy reverb, tape saturation, warm production gathering on the descent — theme REENTRY (an astronaut burning back through the atmosphere after years away, falling home toward blue); HOMECOMING — relief/gratitude (the one song that comes back) | F major | 74 | hypnotic analog synths + ethereal male falsetto + tape-saturated drums gathering on descent & warm sub-bass |
| 421 | Comet421 | dreamy psychedelic-pop / synth-wave (loved-style series): ethereal male falsetto, heavy reverb, tape saturation, twinkling bell/celeste — theme COMET (watching a once-in-a-lifetime comet across a whole life, child to parent, generations under one sky); WONDER with gentle deep-time poignancy | Eb major | 72 | hypnotic analog synths + ethereal male falsetto + bell/celeste & tape-saturated drums |
| 422 | Moon422 | dreamy psychedelic-pop / synth-wave (loved-style series): ethereal male falsetto, heavy reverb, tape saturation, intimate hypnotic — theme MOON (tidally locked, one face to earth forever, pulling the tides, borrowing all its light, refusing to look away); OBSESSIVE DEVOTION, sweet with an unsettling edge ('the prettiest prison is a gravity's embrace') | Ab minor | 72 | hypnotic analog synths + ethereal male falsetto + tape-saturated drums & deep sub-bass |
| 423 | Aphelion423 | dreamy psychedelic-pop / synth-wave (loved-style series): ethereal male falsetto, heavy reverb, tape saturation, spacious sustained pads, brushed drums — theme APHELION (the farthest slowest point of an orbit, out past everything, where striving stops); SERENE PEACE / contentment / rest — a long slow exhale, no ache | C major | 70 | hypnotic analog synths + ethereal male falsetto + sustained pads & brushed tape-saturated drums |
| 424 | Ascend424 | STYLE-ROTATION cycle 1 — CINEMATIC ORCHESTRAL / neoclassical (full style change from the dreamy synth-pop run; switched to FEMALE soprano): strings/piano/harp/choir, silence-before-climax + half-step key lift (D->Eb) at final chorus — theme ASCEND (grief becoming light, ruin reaching for the sun); uplifting-grief / hard-won hope | D major | 70 | string orchestra + grand piano/harp + female soprano (with choir) |
| 425 | Sunday425 | STYLE-ROTATION cycle 2 — WARM 1970s SOUL / soul-pop (full change from orchestral/synth-pop): live band (electric bass, live drums, Rhodes, Hammond, offbeat guitar) + horns + strings, full-chested FEMALE soul voice — theme SUNDAY / SLOW GOLD (a slow Sunday morning in love, unhurried gratitude, 'everything I ran around for was here the whole time'); CONTENTED JOY / warmth | Bb major | 92 | Rhodes + Hammond organ + horn section (over live rhythm section) with female soul vocal |
| 426 | Willow426 | STYLE-ROTATION cycle 3 — COSMIC / DREAM FOLK (full change from orchestral/soul/synth-pop): acoustic & earthy — fingerpicked steel-string guitar, upright bass, brushed drums, fiddle, mandolin, pedal steel, dusty tape warmth; warm low plainspoken MALE FOLK voice (storyteller, slight rasp — totally different timbre from the falsetto series) — theme WILLOW (a willow by a slow river that outlives everyone who carves a name into it, staying rooted while all it loves drifts downstream, keeping every name 'like a long green dream'); WISTFUL NOSTALGIA / grateful deep-time tenderness | D major | 78 | fingerpicked steel-string guitar + upright bass + fiddle/pedal steel with warm male folk voice |
| 427 | Static427 | STYLE-ROTATION cycle 4 — NOCTURNAL TRIP-HOP / DOWNTEMPO noir (full change from orchestral/soul/folk): dusty half-time boom-bap beat, deep sub-bass, vinyl crackle & tape hiss, smoky Rhodes, lonely muted trumpet, cold cinematic strings, vibraphone; cool breathy jazz-inflected FEMALE ALTO (smoky/detached — distinct from the soprano and soul-belt) — theme STATIC (3 a.m., tuning an old radio through dead frequencies, catching the ghost of a voice you knew inside the hiss; keeping someone as a whisper in the noise rather than a silence); NOIR MELANCHOLY / cool nocturnal longing with a strange calm | G minor | 88 | boom-bap beat + sub-bass + muted trumpet / cinematic strings / vibraphone with breathy female alto |
| 428 | Harbor428 | STYLE-ROTATION cycle 5 — INTIMATE PIANO BALLAD / CHAMBER-POP (full change from orchestral/soul/folk/trip-hop): solo grand piano opening out to cello, string section, late brushes + upright bass, French horn lifting the final chorus (acoustic/chamber, NO synths); raw emotive MALE TENOR — warm chest voice cracking at the peaks (distinct from the folk baritone and the falsetto series) — theme HARBOR (a vow to be someone's safe harbor: the still water they come back to after every storm, 'you can show up in pieces at three in the night'); FIERCE-TENDER PROTECTIVE LOVE / steady hope, big cathartic build | F major | 68 | grand piano + cello / string section + French horn with emotive male tenor |
| 429 | Bloom429 | STYLE-ROTATION cycle 6 — DREAM-POP / SHOEGAZE (full change from orchestral/soul/folk/trip-hop/piano-ballad): warm wall of sound — layers of heavily reverbed/chorused guitars blurring together, driving motorik midtempo drums, hazy bass, tremolo & feedback swells, warm synth pads under the guitars; ETHEREAL BREATHY FEMALE voice half-buried in the mix, more feeling than words, wordless soaring 'ahs' at the peaks (gauzy/blurred texture, distinct from the clear soprano, soul belt, and smoky alto); faster tempo (105) than the recent ballads but NOT club/EDM — theme BLOOM (a rush too big for the body, a feeling blooming and dissolving at once, crying and smiling simultaneously); EUPHORIC-MELANCHOLY / bittersweet overwhelm | B major | 105 | wall of reverbed guitars + motorik drums + tremolo/feedback + synth pads with ethereal breathy female vocal |
| 430 | Higher430 | STYLE-ROTATION cycle 7 — UPLIFTING GOSPEL-SOUL (full change from orchestral/soul/folk/trip-hop/piano-ballad/dream-pop): live gospel band (walking bass, drums + tambourine + hand-claps, rolling gospel grand piano, swelling Hammond B3) with a big church CHOIR and a powerful female gospel LEAD trading call-and-response with the choir; wholly new communal/ecstatic/collective ENERGY (warm/organic/hand-clapped, NOT club); intimate-to-explosive build — theme HIGHER (being lifted by other people's hands when you can't stand, then becoming the floor for the next person who falls; 'I could not rise alone / so you rose beneath me like a choir'); TRANSCENDENT / COMMUNAL JOY + defiant collective hope | C major | 80 | gospel piano + Hammond B3 + hand-claps/tambourine (over walking bass & drums) with female gospel lead + full choir |
| 431 | Dusk431 | STYLE-ROTATION cycle 8 — WARM BOSSA NOVA / LOUNGE (full change from orchestral/soul/folk/trip-hop/piano-ballad/dream-pop/gospel): soft nylon-string guitar bossa comping, supple upright bass, brushed drums, Rhodes, vibraphone, lone muted trumpet answering in the gaps, lush jazzy maj7 color; warm smooth close-mic'd MALE CROON (understated lounge crooner, breathy-intimate — distinct from the folk baritone and emotive tenor); relaxed bossa sway at 112 (laid-back FEEL, not club); French count-in 'un, deux' (spoken, everything sung is English) — theme DUSK (a slow dance on a balcony as the evening ends, gold light going blue, choosing to be fully inside the fade: 'I won't waste the ending being sad it's the end'); SENSUAL WISTFULNESS / saudade / bittersweet warmth + present-tense acceptance | A minor | 112 | nylon-string guitar + vibraphone + muted trumpet (over upright bass & brushed drums) with warm male croon |
| 432 | Glacier432 | STYLE-ROTATION cycle 9 — CINEMATIC AMBIENT POST-ROCK (full change from orchestral/soul/folk/trip-hop/piano-ballad/dream-pop/gospel/bossa): long slow-burn crescendo — tremolo-picked reverb guitars, bowed-guitar drone, glockenspiel, gathering layers of guitar + strings + timpani + thundering drums, huge quiet-to-overwhelming dynamic swings, cathartic wall-of-sound climax; SPARSE ethereal MALE voice far back in a cathedral space (mostly wordless 'ah' vocalise + a few English crest-lines, more instrument than singer — distinct from the buried dream-pop female and intimate falsetto) — theme GLACIER (centuries of slow silent pressure, then the thunder of calving ice into the sea; 'I was never meant to hold forever, just to fall and be free'); CATHARTIC AWE / overwhelming release | E major | 72 | tremolo/bowed guitars + glockenspiel + timpani (over swelling strings & drums) with sparse ethereal male vocalise |
| 433 | Mine433 | STYLE-ROTATION cycle 10 — WARM NEO-SOUL / R&B (full change from orchestral/soul/folk/trip-hop/piano-ballad/dream-pop/gospel/bossa/post-rock): laid-back pocket groove — fat electric bass, live swung drums with backbeat snap, Rhodes + Wurlitzer on lush extended chords, muted clean guitar, soft brass/string sweetening, finger snaps; rich GROWN FEMALE NEO-SOUL voice (conversational, honey-toned, easy jazzy runs + soft falsetto flips, stacked harmonies — distinct from v425 big soul belt and v427 smoky noir alto); rebalanced to female after two male cycles — theme MINE (a woman calmly taking herself back after giving too much away, not angry just done & sure; 'loving myself first was never loving you less, just enough'); GROWN SELF-POSSESSION / quiet confidence + sensual warmth. NOTE: rendered short (2:13 + 2:39) — neo-soul groove came in compact; next time push a mid-song vamp + later final line for a fuller 3:00 arc | Eb major | 90 | Rhodes + Wurlitzer + finger-snaps (over fat bass & swung drums) with grown female neo-soul vocal |
| 434 | Neon434 | STYLE-ROTATION cycle 11 — GLOSSY 1980s CITY-POP (full change from orchestral/soul/folk/trip-hop/piano-ballad/dream-pop/gospel/bossa/post-rock/neo-soul): funky clean chorused guitar, slap-tinged pocket bass, crisp gated-reverb drums, lush analog synth pads + glassy EP stabs, shimmering bells, a bright ALTO-SAX SOLO; smooth slightly-wistful MALE city-pop voice (polished, airy falsetto on the hook, silky harmonies — distinct from folk baritone/emotive tenor/bossa croon/post-rock vocalise); upbeat groove 114 but NOT club — theme NEON (cruising neon-lit streets past midnight replaying a love already memory; 'I'm not lost, I'm just driving somewhere you used to be'); GLOSSY NEON NOSTALGIA / bittersweet night-drive yearning. DURATION FIX confirmed: explicit [Sax Solo] mid-song vamp + long cruising outro + late final chorus -> 3:29 & 3:49 (fixed v433's short render) | A major | 114 | chorused guitar + analog synth pads + alto-sax solo (over slap-tinged bass & gated-reverb drums) with smooth male city-pop vocal |
| 435 | Tether435 | STYLE-ROTATION cycle 12 — return to the user's LOVED home base: DREAMY PSYCHEDELIC-POP / SYNTH-WAVE (Blackhole/Afterglow world, untouched since the v415-423 run): hypnotic analog synths in heavy hall reverb, 1970s tape saturation, wide cold-space soundscape, slow-breathing pads, round sub-bass, brushed drums with long reverb tails; ethereal MALE FALSETTO floating far out front. Distinct from v429 dream-pop/shoegaze (that was a guitar wall-of-sound; this is analog-synth spacey/hypnotic) — theme TETHER (an astronaut who lets go of the line and drifts, getting smaller, strangely calm; 'the kindest way to lose a thing is to watch it drift, not grasp'); fresh mood DISSOCIATIVE WEIGHTLESS DRIFT — numb-eerie-calm, watching yourself from outside (NOT Aphelion's earned peace). DURATION: explicit [Synth Solo] break + long drifting outro + late final chorus -> 4:15 & 4:29 | F# minor | 72 | hypnotic analog synths + slow-breathing pads + synth-solo break (over sub-bass & brushed drums) with ethereal male falsetto |
| 436 | Sparks436 | STYLE-ROTATION cycle 13 — BRIGHT ANTHEMIC INDIE-POP (full change from all recent slow/atmospheric cycles): jangly chorused guitars, bouncy bass, punchy live drums, glockenspiel + synth sparkle, handclaps, big gang-vocal 'whoa-oh' hooks; earnest bright FEMALE voice (youthful, breathless, raw at the top — rebalances gender after two male cycles); DELIBERATE ENERGY+MOOD CONTRAST (fast-ish 120, sunny, unambiguously JOYFUL after many bittersweet cycles), organic/radio-bright NOT club — theme SPARKS (brand-new love that makes you want to run at everything, the careful person cutting loose: 'turns out I was never tired, I just had nowhere to go'); EXUBERANT RESTLESS NEW-LOVE JOY. DURATION LESSON: rendered SHORT (2:00 + 2:04) despite a gang-vocal bridge — a SUNG bridge does NOT extend duration; only an explicit LYRIC-FREE instrumental section (solo/interlude) does (cf v434 sax 3:29, v435 synth 4:15). Both clips complete & published (2:00 is a legit indie length) | G major | 120 | jangly chorused guitars + glockenspiel/synth-sparkle + gang vocals & handclaps (over bouncy bass & live drums) with bright female indie vocal |
| 437 | Smoke437 | STYLE-ROTATION cycle 14 — SLOW TORCH SONG / JAZZ-NOIR (full change from all recent cycles): dim after-hours nightclub trio (brushed drums, walking upright bass, smoky rubato piano) under lush noir strings, lone muted trumpet, tenor sax; sultry DRAMATIC FEMALE TORCH SINGER (rich smoldering vibrato, phrasing behind the beat, theatrical devastation with poise — distinct from v427's cool detached breathy trip-hop alto: this is a HOT rubato live-jazz torch belt); very slow 66, no beat-driven feel — theme SMOKE (a woman alone at 3 a.m. in a red dress still burning for a love already ash; 'a woman in her Sunday best at the funeral of her heart'); SMOLDERING GLAMOROUS DEVASTATION — dramatic heartbreak with dignity. DURATION LEVER confirmed again: explicit lyric-free [Sax Solo] + late final chorus + fading outro -> 4:02 & 4:28 | C minor | 66 | smoky rubato piano + muted trumpet + tenor-sax solo (over walking upright bass & brushed drums, noir strings) with dramatic female torch vocal |
| 438 | Rust438 | STYLE-ROTATION cycle 15 — WARM HEARTLAND AMERICANA / ALT-COUNTRY (full change from all recent cycles): full roots band (strummed acoustic, twangy tremolo electric, singing pedal steel, fiddle, upright bass, brushed-to-full drums, Hammond, mandolin); warm weathered MALE road-worn baritone-tenor with gravel/crack and rough harmonies (distinct from v426's spare plainspoken cosmic-folk baritone — this is bigger/band-driven/heartland — and the smooth crooners); mid-tempo driving 100, organic, no synths/gloss — theme RUST (a fading rust-belt town and a worn-down working life that still won't quit, pride in staying when everyone left; 'we're the rust that holds the iron'); WEATHERED RESILIENCE / working-class pride + dignity-in-grit (a NEW mood register — not love/heartbreak but stubborn working-class hope). DURATION LEVER: explicit lyric-free [Pedal Steel Solo] + late final chorus -> 3:25 & 3:37 | D major | 100 | pedal steel + fiddle + mandolin/Hammond (over acoustic strum, upright bass & drums) with weathered male americana vocal |
| 439 | Keepsake439 | STYLE-ROTATION cycle 16 — ORNATE CHAMBER-FOLK / BAROQUE-POP (full change from all recent cycles): fingerpicked nylon guitar, harp, string quartet, clarinet + oboe, harpsichord + celeste, upright bass, brushed waltz; FIRST 3/4 WALTZ of the rotation (meter change — every prior cycle was 4/4); clear pure LITERATE FEMALE mezzo storyteller with perfect diction (distinct from v424 operatic soprano, v425 soul belt, v437 torch, v433 neo-soul — an unadorned art-song voice); intimate/hand-made, no drums-forward beat — theme KEEPSAKE (pressing small things — a ticket stub, a pressed flower, a soft-cornered photograph — between the pages of a book to keep a moment already leaving; 'we are all just little curators of a quickly-closing light'); TENDER LITERARY WONDER / bittersweet preservation (a NEW register). DURATION LEVER: explicit lyric-free [Clarinet Interlude] + late final refrain + plucked-harp outro -> 2:59 & 3:05 | E minor | 90 | harp + string quartet + clarinet/oboe interlude (over fingerpicked nylon guitar & brushed 3/4) with literate female mezzo |
| 440 | Streetlight440 | STYLE-ROTATION cycle 17 — CLASSIC 1950s-60s DOO-WOP BALLAD (full change from all recent cycles): swaying 6/8 triplet stroll on the timeless I-vi-IV-V changes; tremolo guitar, walking upright-bass triplets, brushed drums, vibraphone, tender piano, honking tenor sax, full VOCAL GROUP (bass 'bom-bom', 'sha-la-la', blended harmonies); sincere young MALE lead + falsetto (rebalances gender after female v439; distinct from all prior male voices — an earnest first-love crooner over a doo-wop group); SECOND non-4/4 meter of the rotation (6/8, after v439's 3/4) — theme STREETLIGHT (a shy kid under a corner streetlight working up the courage to confess first love; 'a nervous fool in a borrowed coat but I've never been more sure'); EARNEST TEENAGE DEVOTION / prom-night sincerity (a wholly NEW register — innocent/tender/timeless). DURATION LEVER: explicit lyric-free [Sax Solo] + key-lifting late final chorus + held-falsetto outro -> 3:25 & 3:10 | Db major | 68 | tremolo guitar + vibraphone + tenor-sax solo (over walking upright-bass triplets & brushed 6/8) with male doo-wop lead + vocal group |
| 441 | Postcard441 | STYLE-ROTATION cycle 18 — WARM ORGANIC DOWNTEMPO / CHILLWAVE (Bonobo/Tycho-leaning, full change from all recent cycles): warm analog pads, loose broken-beat groove with dusty drums, deep sub-bass, plucked kalimba + Rhodes, acoustic guitar, live strings, breathy flute, faint rain/traffic field ambience; EXPLICITLY not club-EDM (mid-tempo 96, lush, melodic headphone music); soulful airy honeyed FEMALE topline sitting PRESENT/forward with jazzy melisma (distinct from v429 buried shoegaze female, v435 male falsetto); rebalances to female after male v440 — theme POSTCARD (two people under the same sky in different cities sending warmth across the distance; 'same moon, different window'; 'a candle in two houses that we each keep burning on'); WARM HOPEFUL LONGING ACROSS DISTANCE / tender connection (hopeful not sad — a NEW register). DURATION LEVER: explicit lyric-free [Instrumental Break] (kalimba/flute/Rhodes) + fuller final chorus + long warm fade -> 3:54 & 3:57 | B minor | 96 | kalimba + Rhodes + breathy flute (over broken-beat groove, sub-bass & live strings) with soulful airy female vocal |
| 442 | Whistle442 | STYLE-ROTATION cycle 19 — JOYFUL 1960s MOTOWN SOUL-POP (full change from all recent cycles): driving live-band groove (punchy walking bass, tambourine + crisp backbeat, stabbing horn section, sweet strings, piano triplets, chicken-scratch guitar), 'ooh-ooh' backing group; jubilant young MALE lead + group (bright grinning Motown soul lead, distinct from all prior male voices); UP-TEMPO 126 + EUPHORIC — deliberate energy/mood jolt for a catalog that skews slow/melancholy; distinct from v425 slow 70s soul & v430 gospel; NOT club-EDM (vintage live-band pop) — theme WHISTLE (on a train platform hearing the whistle that means your love is finally coming home after eleven months; 'my baby's on the 5:15 and I'm dancing it on out'); ECSTATIC JOYFUL ANTICIPATION. DURATION: explicit [Horn Break] + key-lifting final chorus -> 2:27 & 2:45 (shorter — at fast 126 BPM even an instrumental break yields less wall-clock; ~2:30 is period-authentic for a 60s single; both complete & published) | F major | 126 | horn section + tambourine backbeat + chicken-scratch guitar (over walking bass & piano triplets) with jubilant male Motown lead + backing group |
| 443 | Crimson443 | STYLE-ROTATION cycle 20 — GRAND BOLERO / LATIN-ROMANTIC BALLAD (English lyrics; full change from all recent cycles): dramatic nylon flamenco guitar, lush cinematic strings, tremulous piano, upright bass, soft bolero-rhythm percussion, lone trumpet; passionate vibrato-rich THEATRICAL FEMALE (smoldering-to-soaring, dramatic rubato — distinct from v424 operatic soprano, v437 smoky torch, v431 breezy bossa: Latin-ballad GRANDEUR); rebalances to female after male v442 — theme CRIMSON (a love vowed in defiance of time, choosing to burn bright BECAUSE it can't last; 'I don't want a careful ember, I want the whole sky set alight'; 'a love too big to keep is the only kind worth letting go'); DEFIANT PASSIONATE DEVOTION / romantic fatalism / glorious surrender (grander/more theatrical than the recent intimate ballads). DURATION LEVER: explicit lyric-free [Spanish Guitar Solo] + key-lifting towering final chorus + held-note outro (slow 76 BPM) -> 4:14 & 3:54 | D minor | 76 | flamenco nylon guitar + lush strings + Spanish-guitar solo (over bolero-rhythm percussion, upright bass & piano) with passionate theatrical female vocal |
| 444 | Horizon444 | STYLE-ROTATION cycle 21 — EPIC CINEMATIC ORCHESTRAL ADVENTURE (revisit of orchestral, last used v424 20 cycles ago, with a WHOLLY different treatment: v424 was a tender female-soprano grief-to-light adagio; THIS is heroic/triumphant): driving staccato strings, sweeping violins, bold brass fanfares, French horns, timpani + taiko, harp, full triumphant choir; powerful warm MALE HEROIC BARITONE + choir call-and-response; monumental forward momentum; rebalances to male after female v443 — theme HORIZON (standing at the edge of the known world at dawn and choosing to sail past it; 'I was not made to watch the water, I was made to leave the brink'); COURAGEOUS WONDER / triumphant setting-out / adventurous defiance (the big epic/heroic moment the catalog had lacked). DURATION LEVER: explicit lyric-free [Orchestral Interlude] + key-lifting final chorus + ringing outro (mid-tempo 88) -> 3:40 & 3:33 | C major | 88 | driving strings + brass fanfares + timpani/taiko (with harp & full choir) and male heroic baritone |
| 445 | Sunburn445 | STYLE-ROTATION cycle 22 — BRIGHT 1960s SURF-POP / SURF-ROCK (full change from all recent cycles): reverb-drenched tremolo surf guitar, galloping toms + snappy backbeat, bouncy bass, Farfisa organ, tambourine, sha-la-la girl-group backing; bright fun young FEMALE lead (sunny, bratty, hand-in-air joy — distinct from all recent female voices); rebalances to female after male v444; up-tempo 136 — theme SUNBURN (one perfect reckless summer beach day with friends: salt/gasoline/cheap sunglasses/no plan; 'best bad idea I ever seen'; 'we are broke and we are golden'); PLAYFUL CAREFREE SUMMER FUN — non-romantic/light/laughing joy, a register the melancholy-leaning catalog badly lacked. DURATION: explicit lyric-free [Surf Guitar Solo] + final chorus -> 2:28 & 2:19 (period-authentic for a 60s surf single; up-tempo 136 renders short as expected — both complete & published) | E major | 136 | reverb surf guitar + Farfisa organ + surf-guitar solo (over galloping toms & bouncy bass) with bright female surf-pop lead + girl-group harmonies |
| 446 | Steady446 | STYLE-ROTATION cycle 23 — WARM ROOTS REGGAE (full change from all recent cycles): crisp offbeat skank guitar, deep melodic bass, one-drop drums, bubbling Hammond organ, warm horn stabs, backing harmonies; warm soulful weathered MALE voice riding behind the beat (rebalances to male after female v445; distinct from all recent male voices — rootsy easy reggae voice); slow-mid one-drop 76 — theme STEADY (standing steady through a hard season of bills/rent/pressure, trusting the tide turns, leaning on community: 'you carry me on Tuesday, I'll carry you on Friday'); RESILIENT PATIENCE / warm defiant hope / dignity-and-calm — a warm uplifting non-romantic register the catalog lacked. DURATION LEVER: explicit lyric-free [Organ and Horn Break] + dropped-down verse + full final chorus + warm fade (slow 76) -> 3:20 & 3:28 | A major | 76 | offbeat skank guitar + Hammond organ + horn section (over melodic bass & one-drop drums) with warm soulful male reggae voice |
| 447 | Weathervane447 | STYLE-ROTATION cycle 24 — BRIGHT 1960s-70s FOLK-ROCK (jangly Byrds/CSN territory, never used this run): chiming Rickenbacker 12-string electric, acoustic strum, melodic bass, driving tambourine backbeat, glowing Hammond, tight stacked harmonies; bright clear FEMALE lead + harmony stacks (rebalances to female after male v446; distinct from acoustic cosmic-folk v426, heartland americana v438, baroque chamber-folk v439 — electric jangle-rock with a driving backbeat); up-mid 116 — theme WEATHERVANE (refusing the handed-down compass/map and the life someone else picked, turning to face your own direction; 'I don't point where they nailed me down'; 'a life that only points one way is a beautiful excuse'); RESTLESS QUESTIONING / idealistic seeking / gentle rebellion (a searching register the catalog lacked). DURATION: explicit lyric-free [Twelve-String Guitar Solo] + dropped verse + big final chorus (up-mid 116) -> 2:31 & 2:49 | G major | 116 | Rickenbacker 12-string + Hammond + tambourine backbeat (over acoustic strum & melodic bass) with bright female folk-rock lead + stacked harmonies |
| 448 | Redline448 | STYLE-ROTATION cycle 25 — CINEMATIC 1980s SYNTHWAVE / OUTRUN (never used this run): pulsing arpeggiated analog synth sequence, fat punchy synth bass, big gated-reverb drums, neon pads, chrome lead synth, distant guitar sting; cool moody detached-determined MALE voice (low/controlled, half-spoken to hard-lift hook — distinct from v435 hazy dreamy-synth falsetto and v434 warm city-pop croon: dark/driving/cinematic); rebalances to male after female v447; mid-tempo 106, propulsive, NOT club-EDM — theme REDLINE (flat-out down an empty midnight highway toward a reckoning put off too long, a braver self waiting at the far end of the dark; 'the bravest thing I ever did was keep my foot down'); STEELY COLD-ADRENALINE DETERMINATION / resolve / forward-at-all-costs (a NEW resolve register never done). DURATION LEVER: explicit lyric-free [Synth Solo] + stripped verse + lifted final chorus + long fade (mid 106) -> 3:49 & 4:04 | A minor | 106 | arpeggiated analog synths + chrome lead synth + synth solo (over fat synth bass & gated-reverb drums) with cool moody male vocal |
| 449 | Firecracker449 | STYLE-ROTATION cycle 26 — ROWDY 1940s-50s SWING / JUMP-BLUES (never used): punchy big-band horn section, walking upright bass, brushed shuffle drums + fat backbeat, boogie-woogie piano, twangy hollow-body guitar, honking tenor sax; sassy brassy FEMALE belter (big/cheeky/swaggering, growl-and-wink — distinct from every prior female voice); rebalances to female after male v448; up-tempo shuffle 132 — theme FIRECRACKER (a woman who's a glorious handful and knows it, owning the room; 'you want quiet, buy a candle'; 'the edges are the best part and I never signed that law'); PLAYFUL SASSY SWAGGER / good-time cheeky defiance — a fun brassy register the catalog never had (distinct from Redline's resolve, Sunburn's teen fun — this is grown/cheeky). DURATION: explicit lyric-free [Sax Solo] + stop-time break + final chorus (up-tempo 132 shuffle) -> 2:21 & 2:25 (period-authentic for a jump-blues romp; both complete & published) | Bb major | 132 | big-band horns + boogie-woogie piano + tenor-sax solo (over walking upright bass & shuffle drums) with sassy female swing belter |

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
