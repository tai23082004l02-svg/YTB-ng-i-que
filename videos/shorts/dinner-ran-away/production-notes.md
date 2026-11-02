# Production notes — Dinner Ran Away

Approved script, 101 words, American English. Kokoro 0.9.4 / hexgrad/Kokoro-82M on CPU, am_michael speed1.07, no additional tempo adjustment. Native audio45.05 seconds including 0.3-second segment pauses; final MP4 45.041667 seconds (45 seconds). No third-party music.

Two newly generated portrait4×4 contact sheets,32 source panels,20 unique scenes selected. The earlier stick-figure sheet established Kai/Ena/child identity; new compositions are portrait rather than crops of an older widescreen film. Nonuniform gutter boundaries measured across the actual sheets, inset9px, fixed aspect-preserving crops and Lanczos enlargement to720×1280. Source panels are lower resolution than export; no native-HD artwork claim.

Simple scenes 1.958–2.792 seconds. The short knowledge and chore narration segments share one continuous visual sequence to keep scene pacing natural. Static illustrations, straight cuts, fps24; no zoom/pan/shake or independent character animation.

USER PREFERENCE: no burned captions, no muxed subtitle track, no Illustration label, header, counter or other text overlay. Render filter is fps=24 only. Twenty SRT cues from actual Kokoro token timing delivered separately; whitespace-normalized caption text exactly matches narration. The owner handles caption styling and application. No ASS used in rendering.

Loudness measured on this audio with two-pass normalization, followed by a192kHz oversampled limiter (limit0.65, level=false, latency=true) and return to48kHz before AAC192kbps mono. Final measured -17.14 LUFS, -3.65 dBTP. Audio encoded from PCM; rejected intermediate AAC was not used as the source. Video copied during final audio refinement. H.264 CRF21/presetfast/yuv420p,24fps,faststart. Limiter and normalization settings are specific to this narration.

Validation: complete decode, stream/duration checks, continuous scene frame boundaries, distinct source cells, SRT timing/order/full text, absence of subtitle streams and overlay filters, final AAC measurement, six decoded frame comparisons against clean source illustrations. Final samples at1,10,20,30,40,44seconds reviewed; text-free and no gutters visible. Sampled mean RGB errors from compression were 1.57–2.01/255. Not exhaustive human listening.

Characters, failed hunt, food portions, camp and job assignments are fictional examples. Food availability varies; no guaranteed catch or universal prehistoric menu. Generic plant/root illustrations are not identified species or food-identification guidance. See SOURCES.md. Reconstruction explanations are in documents and description, never overlaid on the video.

Original WAVs/cache/temporary frames remain in this workspace rather than the repository. Artwork, captions, timeline, crop data and Python scripts retained. To rebuild, install recorded packages with CPU PyTorch and FFmpeg/libx264, then run project/narrate.py, project/render.py and project/validate.py. Machine-specific concat paths are regenerated. Older MP4s unchanged. Prepared for owner upload; no YouTube publication or scheduling.
