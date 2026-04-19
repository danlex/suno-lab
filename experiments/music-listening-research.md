# What Makes People Listen to Music?

**Comprehensive Research Report for Suno AI Prompt Engineering**
*Compiled: 2026-04-18*

This document synthesizes neuroscience, psychology, musicology, and platform analytics research to understand what drives music listening behavior and engagement. Every finding here is actionable for crafting Suno prompts that genuinely captivate listeners.

---

## Table of Contents

1. [Neuroscience of Music Listening](#1-neuroscience-of-music-listening)
2. [Psychology of Musical Preference](#2-psychology-of-musical-preference)
3. [Structural Hooks and Musical Elements](#3-structural-hooks-and-musical-elements)
4. [Emotional Engagement](#4-emotional-engagement)
5. [Production Quality Factors](#5-production-quality-factors)
6. [Platform and Algorithmic Factors](#6-platform-and-algorithmic-factors)
7. [Cultural and Social Factors](#7-cultural-and-social-factors)
8. [Synthesis: Actionable Principles for Suno](#8-synthesis-actionable-principles-for-suno)

---

## 1. Neuroscience of Music Listening

### 1.1 Dopamine and Reward Circuits

- **Dual dopamine release**: PET scanning shows endogenous dopamine release in the striatum during peak emotional arousal. Crucially, dopamine is released in two distinct phases:
  - **Anticipation phase** (caudate nucleus): dopamine fires when the listener *expects* the rewarding moment
  - **Consummatory phase** (nucleus accumbens): dopamine fires during the actual peak experience
- **Pharmacological proof**: Levodopa (dopamine precursor) *enhances* musical pleasure; risperidone (D2 inhibitor) *impairs* it. This is causal evidence that dopamine mediates musical reward.
- **Same circuits as food and sex**: Music activates the mesolimbic dopaminergic system -- the same ancient reward pathway triggered by food, sex, and drugs. Music is an "abstract reward" that hijacks survival-oriented circuits.

*Source: Salimpoor et al., Nature Neuroscience (2011); Ferreri et al., PNAS (2019)*

### 1.2 The Prediction-Reward Loop

- **The brain is a prediction machine**: Listeners possess internal predictive models built from lifetime music exposure. When predictions are confirmed, there is comfort; when violated, there is arousal.
- **Prediction error = pleasure**: When surprise deviates from prediction, the brain's reward system activates, releasing dopamine. But this only works within a "manageable" range of surprise.
- **The sweet spot**: Listeners consistently prefer music of **intermediate predictive complexity**. Too predictable = boring. Too chaotic = aversive. The optimal zone is "reducible uncertainty" -- the listener can *almost* predict what comes next, but not quite.
- **Inverted U-shape**: Pleasure follows an inverted U-curve with predictive complexity, confirmed by pupil dilation studies (2024). In uncertain/chaotic contexts, preferences shift toward *more* predictable outcomes.

*Source: Gold et al., Journal of Neuroscience (2019); Cheung et al., Current Biology (2019); Predictive processes shape individual musical preferences, PMC (2025)*

### 1.3 Frisson / Musical Chills

- **Prevalence**: ~50% of people experience physical chills (goosebumps, shivers, tingling) during music listening
- **Brain wiring**: People who experience frisson have **higher white matter density** connecting auditory cortex to emotional processing areas -- literally more neural fibers linking hearing to feeling
- **Neural signature**: Simultaneous activation of orbitofrontal cortex (emotion), supplementary motor area (movement impulse), and right temporal lobe (auditory processing)
- **Personality correlation**: Frisson experiencers score higher on Openness to Experience, creativity, and intellectual curiosity

#### What Triggers Frisson:
1. **Expectation violation**: Unexpected harmony, sudden new voice/instrument, key change
2. **Silence before climax**: Build to 80%, drop to near-silence, then deliver climax exceeding expectations
3. **Crescendo from quiet**: Gradual dynamic build creates unbearable anticipation
4. **New timbral entry**: A solo voice or instrument entering unexpectedly
5. **Appoggiaturas**: "Leaning notes" that create brief dissonance before resolving (e.g., Adagio for Strings)
6. **Enharmonic modulation**: Key change, especially half-step up after silence

*Source: Sachs et al. (2016), Oxford Academic; Huron (2006); Grewe et al., Music Perception*

### 1.4 ASMR and Autonomous Sensory Responses

- **Tingling sensation**: ASMR produces scalp/neck tingling, relaxation, and well-being -- overlaps with but is distinct from frisson
- **Auditory triggers dominate**: Whispering, crisp sounds, close-miked detail, and lower-pitched complex sounds are especially effective
- **Brain activation**: Nucleus accumbens (reward), insular cortex (interoception), middle frontal gyrus
- **Physiological**: Increased skin conductance, decreased heart rate -- a paradox of arousal + calm
- **Relevance to music**: Intimate, close-miked, detailed sonic textures with spatial qualities can trigger ASMR-adjacent responses

### 1.5 Rhythmic Entrainment

- **Neural synchronization**: The brain's oscillations physically synchronize with musical rhythm (neural entrainment). This is involuntary.
- **Body-music coupling**: Sub-bass frequencies (20-60 Hz) bypass hearing entirely -- they vibrate the chest cavity, bones, and organs through bone conduction. Listeners *feel* rather than hear these frequencies.
- **Endorphin release**: Bass-heavy music triggers endorphin release; low frequencies create sensations of power, excitement, or anxiety
- **Chest resonance**: 23-35 Hz resonates the human chest cavity; 125-160 Hz creates the "chest thump" sensation
- **Adrenaline**: Physical vibration syncs with the body's natural rhythms, stimulating the nervous system and increasing adrenaline

---

## 2. Psychology of Musical Preference

### 2.1 Familiarity vs. Novelty: The Central Tension

- **Mere exposure effect**: Repeated exposure to any stimulus increases preference for it. This is one of the most robust findings in psychology, and it applies powerfully to music.
- **Monotonic increase with familiarity**: One study found liking increased monotonically with repeated listening across *all* levels of complexity -- suggesting familiarity may be the **single most important predictor** of music liking, independent of genre, timbre, or structure.
- **Berlyne's inverted U (the Wundt curve)**: The classic theory says preference peaks at intermediate complexity/familiarity, then declines. 87.7% of 57 studies were compatible with this model.
- **The resolution**: Both are true at different scales. Familiarity drives liking of individual pieces; novelty drives exploration and discovery of new favorites. The ideal song feels *almost* familiar on first listen.

**Practical implication**: Use common melodic contours (what listeners expect from the genre) but with unexpected interval leaps or timbral surprises within that familiar frame.

### 2.2 Earworms: What Gets Stuck

The APA "Dissecting an Earworm" study (Jakubowski et al., 2016) identified specific musical features that predict involuntary musical imagery:

1. **Common global melodic contour**: Earworm melodies follow the most typical melodic shapes in Western pop music (e.g., rise-then-fall pattern of "Twinkle, Twinkle Little Star")
2. **Unusual interval structure within that common contour**: Unexpected leaps or more repeated notes than average create memorability
3. **Faster tempo**: Earworm tunes had faster average tempi than non-earworm tunes
4. **Song popularity**: More exposure = more earworms (mutually reinforcing with catchiness)
5. **Repetition**: Repeating the hook solidifies it in memory. The brain "replays" patterns it hasn't fully resolved.

**Formula**: Common shape + unusual intervals + faster tempo + repetition = earworm

### 2.3 Why People Replay Songs

- **Incomplete processing**: We replay songs we haven't fully "figured out" -- unresolved musical tension keeps the brain returning
- **Mood regulation**: The #1 reason people listen to music is to manage/regulate their moods
- **Aesthetic appreciation**: 98% of listeners cite aesthetic appreciation as a reason for listening
- **Nostalgia**: Music-evoked nostalgia elevates self-esteem, instills youthfulness, augments optimism. Nostalgia is the most frequently evoked emotion from music.
- **Relaxation**: 92% cite relaxation
- **Motivation**: 90% cite motivation

### 2.4 The Three Dimensions of Music Listening Functions

Research (Schäfer et al., PMC) identifies three core dimensions:

1. **Arousal and mood regulation** -- managing emotional states, energy levels
2. **Self-awareness** -- self-reflection, identity exploration, understanding one's own emotions
3. **Social relatedness** -- belonging, connection, shared experience

---

## 3. Structural Hooks and Musical Elements

### 3.1 Melodic Contour

- **Rise-and-fall**: The most universally engaging melodic shape rises in the first phrase and falls in the second
- **Arch contour**: Creates natural tension (rise) and resolution (fall)
- **Singability**: Melodies that listeners can internally "sing along" to are more engaging, even in instrumental music
- **Step motion with occasional leaps**: Predominantly stepwise motion (small intervals) punctuated by surprising leaps creates the ideal balance of predictability and surprise

### 3.2 Harmonic Tension and Resolution

- **Prediction error as pleasure**: Music appreciation depends not on total surprise but on the **contrast** between high-surprise and low-surprise sections
- **Optimal pattern**: Build tension through surprising harmonic elements, then relieve it through resolution. The cycle of tension-release IS the engine of musical engagement.
- **Moderate surprise optimal**: Excessive harmonic surprises do not increase preference -- there is a ceiling effect
- **Neural processing**: The brain processes unexpected chords similarly to syntactic errors in language -- it triggers the same "that's wrong/interesting" response (early right anterior negativity on EEG)

### 3.3 Tempo and Rhythm

- **Fast tempo (120-156 BPM)**: Associated with excitement, liveliness, happiness, joy, pleasure. Highest arousal levels.
- **Medium tempo (~106 BPM)**: Matches breathing/heart rate rhythms. Lowest arousal but highest comfort/familiarity.
- **Slow tempo (~56 BPM)**: Linked to calmness, dignity, tenderness, sadness. Moderate arousal (higher than medium -- a surprising "V-shape" arousal pattern).
- **Syncopation**: Offbeat rhythms create tension, make songs stand out, engage the prediction system
- **Rhythmic entrainment**: The body physically locks to the beat -- this is involuntary and creates a feeling of "being moved"

### 3.4 Dynamic Contrast

- **The #1 engagement tool**: Alternating between soft and loud passages keeps the listener engaged. Without dynamic contrast, songs feel flat and fatiguing.
- **Silence before climax**: A sudden silence followed by a loud crescendo is the single most powerful dramatic tool. The pause creates unbearable tension; the return delivers cathartic release.
- **Crescendo and anticipation**: As music gradually gets louder, the brain expects something important. This builds anticipation. When the climax arrives, the listener experiences satisfaction and release.
- **Film analogy**: Dynamic range is to music what lighting contrast is to cinematography. Without it, everything feels monotone.

### 3.5 Key Modulation

- **Half-step up (truck driver modulation)**: Shifting up one semitone (e.g., D major to Eb major) near the end of a section creates a burst of renewed energy and emotional intensity
- **Emotional reset**: A key change gives the sensation of "almost starting again" with fresh energy
- **Timing**: Most effective after a bridge or moment of silence, before a final climactic section
- **Caution**: Overuse has made this somewhat cliched in pop -- works best when earned through prior buildup

### 3.6 Timbre and Orchestration

- **Genre identification in <1 second**: Listeners can identify genres and often specific artists in under one second based purely on timbre
- **Timbral contrast marks structure**: Sections in music are often defined by changes in timbre/texture, not just melody or harmony
- **Heterogeneous instrument combinations**: Mixing different instrument families creates stronger perceptual segregation and interest than homogeneous textures
- **Emotional processing**: The brain can **automatically and preattentively** process emotional information through timbre -- it happens before conscious awareness
- **Timbral salience**: Certain timbres naturally attract attention and occupy the perceptual foreground. Novel or unusual timbres are inherently attention-grabbing.

### 3.7 Shepard Tones and Auditory Illusions

- **Endlessly rising pitch illusion**: Superposition of sine waves separated by octaves, with volume crossfading, creates the perception of infinitely ascending pitch
- **Psychological effect**: Evokes severe dread, unease, or exhilarating forward momentum depending on context
- **Tension building**: Used in film scores and electronic music to create seemingly endless buildup (e.g., Hans Zimmer's Dunkirk score)
- **Brain confusion**: The brain cannot resolve the ascending pattern, creating persistent engagement/agitation

---

## 4. Emotional Engagement

### 4.1 The BRECVEMA Framework (Juslin)

Eight distinct mechanisms by which music induces emotion:

| Mechanism | How It Works | Suno Relevance |
|-----------|-------------|----------------|
| **B**rain stem reflexes | Sudden, loud, fast, or dissonant sounds trigger automatic alarm | Sudden dynamic shifts, sforzando |
| **R**hythmic entrainment | Body synchronizes with beat | Strong, clear pulse in the groove |
| **E**valuative conditioning | Association with past positive/negative experiences | Genre cues that trigger learned associations |
| **C**ontagion | Music "expresses" emotion, listener "catches" it | Emotional performance quality, vibrato, phrasing |
| **V**isual imagery | Music triggers mental images/scenes | Cinematic, descriptive, evocative timbres |
| **E**pisodic memory | Music triggers specific autobiographical memories | Nostalgic era-specific sounds, retro elements |
| **M**usical expectancy | Tension from confirmed/violated expectations | Harmonic surprise, deceptive cadences |
| **A**esthetic judgment | Appreciation of beauty, skill, originality | Craft, complexity, novel combinations |

**Key insight**: Music has unusually strong emotional effects because it can activate ALL EIGHT mechanisms simultaneously. No other stimulus does this.

### 4.2 Emotion Regulation Through Music

- **Down-regulation**: Music reduces negative emotions, lowers anxiety and stress responses
- **Up-regulation**: Music can elevate energy, arousal, and positive mood
- **Safe container**: Music provides a safe environment to confront and process difficult emotions (catharsis)
- **Mood management is #1**: The desire to manage emotions is the single most common reason people actively choose to listen to music

### 4.3 The Paradox of Sad Music

Why do people seek out sad music?

1. **Dissociation**: Sadness is experienced at a safe aesthetic distance -- "not my sadness"
2. **Fantasy induction**: Sad music creates vivid imaginative scenarios
3. **Connection**: Feeling understood; the music "gets" what you're going through
4. **Aesthetic value**: Sad music is perceived as having higher artistic quality
5. **Biochemistry**: Sad music triggers prolactin (comfort hormone) and oxytocin (bonding hormone), in addition to dopamine -- a cocktail that produces bittersweet pleasure
6. **Catharsis**: Emotional release and purification through safe exposure

### 4.4 Nostalgia

- **Most frequent music-evoked emotion**: Nostalgia is triggered by music more than any other stimulus
- **Psychological benefits**: Elevates self-esteem, creates sense of youthfulness, augments optimism and inspiration
- **Self-regulation tool**: People use nostalgic music to boost mood when feeling down, especially during times of stress or transition
- **Social connectedness**: Nostalgic music increases feelings of social belonging, even when listening alone
- **Neural activation**: Music-evoked nostalgia activates default mode network and reward networks across the lifespan

---

## 5. Production Quality Factors

### 5.1 Loudness and Dynamic Range

- **The loudness war is over (mostly)**: Streaming platforms normalize loudness, so crushing dynamic range for volume no longer provides competitive advantage
- **Dynamic range = engagement**: Higher peak-to-loudness ratio (PLR) indicates more dynamic tracks with greater contrast between loud and soft moments, creating more engaging listening
- **Loudness range (LRA)**: Increased LRA engages listeners at a subconscious level -- humans are wired to tune out static/constant sounds. Volume variation holds attention.
- **Listener fatigue**: Over-compressed, overly loud music causes listener fatigue and disengagement

### 5.2 Frequency Spectrum

- **Sub-bass (<150 Hz) amplification**: Intensifies emotional response even when listeners aren't consciously aware of the change
- **Bass sculpting over brute loudness**: Emotional impact comes from sculpting the frequency spectrum, especially bass, rather than raw volume
- **Full spectrum**: Engaging music typically uses the full frequency range, with each register contributing to the emotional palette
- **Presence frequencies (1-5 kHz)**: Where human hearing is most sensitive; clarity here = perceived quality

### 5.3 Spatial Audio and Immersion

- **3D audio market growing 11.5% CAGR**: Spatial audio is a major trend, expected to reach $17.22B by 2033
- **Deeper emotional engagement**: Immersive audio enables creators to craft richer experiences that resonate on a deeper emotional level
- **Glass harmonica phenomenon**: Frequencies in the 1-4 kHz range from instruments like glass harmonica create spatial disorientation -- the brain can't locate the sound source, creating an ethereal, otherworldly quality
- **Personalization**: Apple's Personalized Spatial Audio, Dolby Dynamic Mix -- the industry is moving toward individualized spatial experiences

### 5.4 Production Trends That Increase Engagement

- **Intimate close-miking**: Creates ASMR-adjacent sensation of closeness and presence
- **Textural detail**: Subtle sonic details (room tone, breath, string buzz) create authenticity and intimacy
- **Contrast in production density**: Sparse sections make dense sections feel more impactful
- **Frequency "holes"**: Leaving space in the frequency spectrum creates anticipation for when it's filled

---

## 6. Platform and Algorithmic Factors

### 6.1 The Critical First 30 Seconds

- **Spotify counts a "stream" only after 30 seconds** of playback. Anything shorter is invisible.
- **Most skipping occurs in the first few seconds**: Listeners make aesthetic judgments almost instantly
- **Target skip rate: <20%** in the first 30 seconds for favorable algorithmic treatment
- **Skip = negative signal**: Spotify interprets skips as "this song isn't interesting" or "bad recommendation"

### 6.2 Hook Placement Strategy

- **Hit the hook in 5-15 seconds**: The most compelling element (main vocal line, signature riff, catchy beat) must arrive within 5-15 seconds
- **Don't bury the lead**: Long ambient intros are algorithmic poison on streaming platforms
- **Front-load the best moment**: Consider starting with the chorus or most memorable element rather than a traditional slow build
- **Immediate engagement required**: Early skip rates carry heavy algorithmic penalties

### 6.3 Retention Signals (2026 Spotify)

- **Saves > Streams**: In 2026, Spotify's algorithm increasingly weights save rate over raw stream count -- retention and repeat behavior matter more than passive plays
- **Playlist adds**: Another strong positive signal
- **Completion rate**: Songs listened to all the way through signal quality
- **Repeat listens**: When users replay a song, it's a powerful algorithmic signal

### 6.4 Implications for Song Structure

- **Front-loaded structure**: The most engaging element within 10 seconds
- **2:30-3:30 optimal length**: Long enough for emotional arc, short enough for completion rate
- **Multiple hooks**: Several memorable moments spread throughout maintain engagement
- **Strong ending**: Completion rate matters -- a compelling ending prevents late-song skips

---

## 7. Cultural and Social Factors

### 7.1 Music as Social Identity

- **Identity signaling**: People use music preferences to signal group affiliations and to infer the social identity of others
- **Stronger response from in-group performers**: Music elicits stronger emotional responses when performed by individuals who share a listener's group identity
- **Genre as tribe**: Musical taste functions as a tribal marker -- people bond over shared taste and feel alienated by mismatched preferences

### 7.2 Shared Experience and Social Bonding

- **Neurochemistry of togetherness**: Music triggers dopamine, endorphins, and oxytocin -- chemicals linked to pleasure, bonding, and social connection
- **Self-other merging**: Shared musical experiences create a sense of boundary dissolution between self and others
- **Collective identity**: Music contributes to the development of collective identities; shared references create bonds between strangers
- **Live music**: Systematic review shows live music events produce measurable social outcomes: increased trust, belonging, and prosocial behavior

### 7.3 Pseudo-Social Listening

- **Listening alone but feeling connected**: Even solo listeners experience "pseudo-social" connections through music -- feeling connected to the performer, to an imagined community of fellow listeners, or to humanity broadly
- **Parasocial relationships**: Listeners form one-sided emotional bonds with performers/composers through their music

### 7.4 Cultural Variation

- **Collectivist cultures**: Use music more for expressing values and cultural identity
- **Individualist cultures**: Use music more for personal emotional regulation
- **Universal functions**: Emotion regulation, aesthetic appreciation, and social bonding appear cross-culturally, though their relative importance varies

---

## 8. Synthesis: Actionable Principles for Suno

### The Hierarchy of Listener Engagement

Based on all research reviewed, here is a ranked hierarchy of what makes people want to listen:

#### Tier 1: Non-Negotiable (Must Have)

1. **Immediate hook (0-10 seconds)**: The most compelling timbral or melodic element must appear within the first 10 seconds. No slow builds to open.
2. **Dynamic contrast**: Alternating loud/soft, dense/sparse, tense/resolved throughout. Without this, everything else fails.
3. **Emotional resonance**: The piece must trigger at least one BRECVEMA mechanism strongly -- ideally visual imagery, contagion, or musical expectancy for instrumental music.
4. **Timbral interest**: Unusual, beautiful, or novel timbral combinations that grab attention preattentively.

#### Tier 2: High Impact (Strong Differentiators)

5. **Silence before climax**: Build to 80% intensity, drop to near-silence, then deliver a climax that exceeds all prior intensity. This is the #1 frisson trigger.
6. **Predictability-surprise balance**: Common overall structure (familiar genre contours) with unexpected internal details (unusual intervals, timbral shifts, harmonic surprises).
7. **Half-step key modulation at climax**: After the silence, return in a key one semitone higher. Neurological goosebump multiplier.
8. **Crescendo arcs**: Long, patient builds that create anticipation through the prediction-reward loop.

#### Tier 3: Enhancers (Compound Effect)

9. **Sub-bass presence**: Frequencies below 60 Hz create physical/bodily engagement that bypasses conscious processing.
10. **Tempo sweet spot**: 120-140 BPM for energy/excitement; ~100 BPM for emotional depth; ~70 BPM for intimacy.
11. **Timbral variety across sections**: Different instrument families marking different sections keeps the ear "refreshed."
12. **Spatial/ethereal elements**: Glass harmonica, reverb tails, Shepard tones -- sounds the brain can't quite locate create wonder.

#### Tier 4: Meta-Level (Long-Term Listener Building)

13. **Almost-familiar on first listen**: Use common genre frameworks so the piece feels accessible immediately, but with enough novelty to reward re-listening.
14. **Unresolved elements**: Leave something slightly unresolved -- the brain will want to return to "figure it out," creating replay impulse.
15. **Emotional arc**: The piece should take the listener on a journey -- not just sustain a single mood, but move through contrasting emotional states.
16. **Nostalgia activation**: Timbral or stylistic references to emotionally loaded musical eras/genres.

### The Golden Formula

```
ENGAGEMENT = (Immediate Hook) 
           x (Dynamic Contrast Range) 
           x (Prediction Sweet Spot: familiar structure + surprising details)
           x (Silence-Climax-Modulation Arc)
           x (Timbral Novelty + Beauty)
```

### Anti-Patterns to Avoid

- **Flat dynamics**: Constant loudness = listener fatigue and disengagement
- **Buried hooks**: Important elements arriving after 30+ seconds = algorithmic death
- **Too predictable**: Pure genre conformity without any surprise = boring, no dopamine
- **Too chaotic**: Excessive surprise without familiar anchoring = aversive, listener leaves
- **Timbral monotony**: Same instruments/textures throughout = attention decay
- **No emotional arc**: Static mood = no reason to keep listening
- **Overly long intros**: Front-load the goods; extended ambient openings kill retention

---

## Sources

### Neuroscience
- [Anatomically distinct dopamine release during anticipation and experience of peak emotion to music - Nature Neuroscience](https://www.nature.com/articles/nn.2726)
- [Dopamine modulates the reward experiences elicited by music - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6397525/)
- [From perception to pleasure: Music and its neural substrates - PNAS](https://www.pnas.org/doi/10.1073/pnas.1301228110)
- [The transformative power of music: Insights into neuroplasticity, health, and disease - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765015/)
- [Predictability and Uncertainty in the Pleasure of Music: A Reward for Learning? - Journal of Neuroscience](https://www.jneurosci.org/content/39/47/9397)
- [Neural Mechanism of Musical Pleasure Induced by Prediction Errors - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11592396/)
- [Predictive processes shape individual musical preferences - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12304940/)

### Frisson and Chills
- [The neurobiology of aesthetic chills - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11233292/)
- [Musical chills: why they give us thrills - McGill University](https://www.mcgill.ca/newsroom/channels/news/musical-chills-why-they-give-us-thrills-170538)
- [What Getting Chills from Music Says About Your Brain - Discovery](https://www.discovery.com/science/Getting-Chills-from-Music)
- [Why Music Gives You Chills: The Shocking Brain Science Behind Frisson - Classicalite](https://www.classicalite.com/articles/1725266/20260402/why-music-gives-you-chills-shocking-brain-science-behind-frisson.htm)
- [Who gets musical chills and why? - Music Psychology](https://musicpsychology.co.uk/who-gets-musical-chills-and-why/)

### ASMR
- [Autonomous Sensory Meridian Response: a flow-like mental state - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4380153/)
- [Sensory determinants of ASMR: understanding the triggers - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5633022/)
- [Brain function effects of ASMR video viewing - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9909086/)

### Earworms and Musical Preference
- [Dissecting an Earworm: Melodic Features and Song Popularity - APA](https://www.apa.org/pubs/journals/releases/aca-aca0000090.pdf)
- [Psychologists identify key characteristics of earworms - APA](https://www.apa.org/news/press/releases/2016/11/earworms)
- [The song that never ends: Repeated exposure and earworm development - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10585939/)
- [Back to the inverted-U for music preference - Chmiel & Schubert](https://journals.sagepub.com/doi/full/10.1177/0305735617697507)
- [Repeated Listening Increases Liking Regardless of Complexity - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5374342/)

### Harmonic Tension and Surprise
- [Harmonic Surprise and Preference Over Time in Popular Music - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8121146/)
- [A Statistical Analysis of Harmonic Surprise and Preference - Frontiers](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2017.00263/full)
- [Contextual prediction modulates musical tension - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0278262621000919)

### Emotion and Music
- [The psychological functions of music listening - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3741536/)
- [Music-Evoked Nostalgia Activates Default Mode and Reward Networks - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11907061/)
- [Scoping Review on Music for Emotion Regulation - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11428991/)
- [The Psychological Benefits of Nostalgic Music - Psychology Today](https://www.psychologytoday.com/us/blog/science-of-choice/202402/the-psychological-benefits-of-nostalgic-music)
- [How Music Affects Us Emotionally - Psychology Today](https://www.psychologytoday.com/us/blog/science-of-choice/202309/how-music-affects-us-emotionally)

### Production and Audio
- [Understanding the Loudness War in Mastering 2025 - iMusician](https://imusician.pro/en/resources/blog/mastering-and-the-loudness-war-an-update)
- [The Deeper Impact: Emotion, Bass, and Future of Sound Design - L-Acoustics](https://www.l-acoustics.com/theartofsound/journal/the-deeper-impact-emotion-bass-and-the-future-of-sound-design/)
- [Bass Frequencies and Body Physics - Relentless Beats](https://relentlessbeats.com/2026/02/bass-frequencies-body-physics-why-you-feel-certain-songs-in-your-chest/)
- [The power of dynamics and silence in music - Splice](https://splice.com/blog/dynamics-and-silence-in-music/)

### Platform and Streaming
- [Spotify Algorithm 2026: Retention Revolution - Chartlex](https://www.chartlex.com/blog/streaming/spotify-algorithm-2026-retention-revolution)
- [The skipping behavior of music streaming users - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7526936/)
- [Decoding the Spotify Algorithm: Skip Rate, Save Rate - Artistrack](https://artistrack.com/spotify-algorithm-skip-rate-save-rate/)

### Social and Cultural
- [Music and social bonding: self-other merging and neurohormonal mechanisms - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4179700/)
- [Music, Identity, and Social Bonding - Columbia University](https://scienceandsociety.columbia.edu/news/music-identity-and-social-bonding)
- [Association between music experience and social identity - Springer](https://link.springer.com/article/10.1007/s12144-025-08007-3)
- [Beyond the music itself: Social bond with performers affects liking - Oxford Academic](https://academic.oup.com/scan/article/20/1/nsaf106/8284941)

### Timbre and Orchestration
- [Timbre Perception, Representation, and Neuroscientific Exploration - arXiv](https://arxiv.org/html/2405.13661v1)
- [Instrument Timbre Enhances Perceptual Segregation - Music Perception](https://online.ucpress.edu/mp/article/38/5/473/117149/Instrument-Timbre-Enhances-Perceptual-Segregation)
- [Research Themes - McGill Music Perception and Cognition Lab](https://www.mcgill.ca/mpcl/research)

### Tempo and Rhythm
- [Music tempo modulates emotional states - Nature Scientific Reports](https://www.nature.com/articles/s41598-025-92679-1)
- [Effects of Musical Tempo on Emotional Experience - Frontiers](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.02118/full)

### BRECVEMA Framework
- [Measuring emotional music experience: BRECVEMA mechanisms - Völker 2022](https://journals.sagepub.com/doi/abs/10.1177/03057356211010224)
- [Emotional Responses: Arousal Mechanisms - Sonata Secrets](https://www.sonatasecrets.com/9-emotional-responses)
