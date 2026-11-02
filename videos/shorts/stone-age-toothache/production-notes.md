# Production notes — Stone Age Toothache Short

Original American English script: 122 words, five segments. Kokoro 0.9.4 / hexgrad/Kokoro-82M, voice am_michael, speed 1.07 on CPU. Native audio 50.275 seconds including 0.3-second segment pauses; final MP4 50.291667 seconds. No tempo adjustment or third-party music.

Two newly generated portrait 4×4 contact sheets, 32 panels, 18 unique selected scenes. Earlier stick-figure preview sheet used as character/style reference; compositions newly created for vertical framing. All source boards visually reviewed. Actual nonuniform row/column boundaries measured and recorded, with 9-pixel inset to remove dividers. Fixed aspect-preserving crop and Lanczos enlargement to 720×1280. Source panels are lower resolution than the export; no native-HD artwork claim.

Mean scene 2.794 seconds; range 2.083–4.500 seconds. Research/tooth/scratch observations held about 4–4.5 seconds, simpler scenes mostly 2–3 seconds. Straight cuts and static characters: no pan, zoom, shake, header or scene counter.

25 caption cues derived from actual Kokoro token timings, with balanced line breaks measured in the final font. Native ASS canvas 720×1280, DejaVu Sans bold 41px, outline2.5px, shadow1px, margins left50/right110/bottom250. Maximum measured text line width 545.12px within a 560px text area. No permanent black background strip. SRT and ASS retained.

The still-image input is expanded with the fps=24 video filter BEFORE ASS rendering. This makes burned captions update throughout each held image. A rejected intermediate build held captions per scene; it was replaced. Validation compares decoded pixels at 0.1, 1.0 and 1.8 seconds within the first static scene to confirm captions appear and change while the illustration stays still. Final text and all cue times also checked.

Two-pass loudness normalization measured on this narration, followed by -0.35dB extra headroom before AAC. Final AAC mono48kHz / nominal128kbps: -17.0 LUFS, -2.06 dBTP. Final audio encoded from normalized PCM, not from the rejected AAC. H.264 CRF21, preset fast, yuv420p, 24fps, faststart. Measurement settings are specific to this audio.

Tooth/micrograph/flint research views are stylized diagrams, not the real Villabruna specimen or actual microscope data; they carry Illustration labels. No living-mouth procedure is shown. Kai, Ena, clothing, camp, expressions and modern clinic joke are fictional. Villabruna evidence and limits are in SOURCES.md; no earliest-dentistry or successful-cure claim.

Checks: complete final MP4 decode, streams and duration, unique panels and continuous frame boundaries, caption text/time/width, captions changing within a held scene, final AAC measurement, sampled final frames at 1,13,22,32,43,49 seconds. Not exhaustive human listening. Source WAVs/cache and temporary frames remain in this workspace; committed data, artwork and Python scripts support reconstruction. Run project/narrate.py, project/render.py, project/validate.py with the recorded Python packages and FFmpeg/libass/libx264. The renderer regenerates machine-specific concat paths. Existing older MP4s were not changed. Prepared for owner upload, not published or scheduled on YouTube.
