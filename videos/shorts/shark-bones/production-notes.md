# Production notes — Shark Bones Short

Approved American English comedy script,121 words, seven segments. Kokoro0.9.4 / hexgrad/Kokoro-82M, am_michael speed1.07 on CPU. Native audio51.15 seconds including short segment pauses; final MP4 51.166667 seconds. No extra tempo adjustment or third-party music. Dry delivery, absurd question, factual explanation and customer-service punchline.

Two newly generated portrait4×4 sheets,32 panels,20 unique selected shots. The earlier stick-figure sheet supplied drawing/character reference, while clothing and setting changed to red swim shorts and a turquoise modern beach. The generic gray shark and smooth peach stomach pouch are simplified cartoons. Source boards reviewed: no attack, bitten person, gore, readable text or specimen photographs. A toy skeleton appears only in an imagination bubble. The sock/headset/desk are explicit visual jokes.

Actual nonuniform source grid boundaries measured,9px inset, fixed aspect-preserving crop, Lanczos scale to720×1280. Lower-resolution source panels enlarged; no native-HD illustration claim. Static shots last 1.875–3.042 seconds. No zoom/pan/shake or independent character motion. Complex biological details are not presented as precise anatomical measurements.

MP4 contains only H.264 video and AAC audio; no captions, Illustration labels, headers, counters or embedded subtitle track. Rendering filter is fps=24 only. A separate matching SRT has 21 cues from actual Kokoro token timing. Short orphan captions merged, ellipsis typography and spaces before punctuation cleaned; normalized text matches the full script. Owner handles caption appearance and application.

Own-audio two-pass normalization followed by192kHz oversampled limiting (limit0.65, level=false, latency=true), resampling to48kHz, AAC mono192kbps. Final measurement -17.18 LUFS, -3.71 dBTP. H.264 CRF21/presetfast/yuv420p/24fps/faststart. No prior AAC used as an audio encoding source.

Checks: complete final decode, streams/duration, continuous frame boundaries, unique source panels, SRT time/order/full text, no subtitle stream or text filters, final AAC loudness, six final-frame comparisons with clean source illustrations and visual review at1,10,20,30,40,50.17 seconds. Sample mean RGB compression errors 1.48–1.71/255. Not exhaustive human listening.

Scientific limits in SOURCES.md: some bone can break down; large indigestible material can remain and be regurgitated; stomach eversion occurs in some sharks. No species-wide guarantee, digestion time, actual human case or assertion of a whole skeleton in feces. Do not treat the pouch drawing as a tongue, or the schematic as a measured anatomical cutaway. Commentary and visual metaphors are not biological mechanisms.

Original WAVs/cache/temp frames stay in this workspace. Source artwork, SRT/timing, measured crop data and scripts retained in repository. Install recorded packages with CPU PyTorch and FFmpeg/libx264, then run project/narrate.py, render.py and validate.py to rebuild; local concat paths regenerate. Older videos unchanged. Prepared for owner upload; no YouTube publication/scheduling.
