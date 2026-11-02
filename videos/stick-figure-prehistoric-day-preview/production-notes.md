# Production notes

Original 352-word American English script, eight segments. Kokoro 0.9.4, hexgrad/Kokoro-82M on PyTorch CPU, voice am_michael, speed 1.02. Native narration 145.95 seconds including 0.3-second segment pauses; final container 145.958333 seconds (2:26). No additional tempo change or music.

Three new AI-generated 4×4 contact sheets (48 panels), using the first sheet as the character/style reference for subsequent sheets. Forty distinct panels selected. Source images 1672×941; small source panels are enlarged for a 1280×720 export, not native HD illustration. Black stick limbs, round heads, hide clothes and expressive faces; backgrounds retain the prior earthy illustrated look. This is a first stick-figure style experiment, not a fully animated character film.

Grid gutters measured using cross-panel pixel variance near expected boundaries, reviewed on all source sheets; 11-pixel insets remove borders. Aspect-preserving fixed crops and Lanczos resizing, no camera motion. Exact crops in project/grid-crops.json and shots.json. Selected shots average 3.649 seconds, range 3.042–4.583 seconds, all simple illustrative scenes. Cuts use nearby caption boundaries when compatible with pacing, not exhaustive word-level visual alignment.

Forty static frames, straight cuts, no header/counter/zoom/pan. 49 subtitle cues from Kokoro token timestamps; one short orphan cue merged into its preceding cue. Caption text matches the complete narration after whitespace normalization. White bold DejaVu Sans with dark outline, no permanent black strip. One longer opening caption uses three lines.

Two-pass loudness normalization measured on this narration. Final AAC mono 48 kHz / nominal 128 kbps measures -16.62 LUFS and -1.72 dBTP. Encoding: H.264, CRF 21, preset fast, yuv420p, 24 fps. Source normalization measurements in project/normalization-settings.json. MP4 faststart enabled.

Source-board review plus final samples at 4, 28, 52, 78, 115 and 139 seconds. Complete MP4 decode, streams, duration, continuous frame timing, unique selected panels, caption bounds/order/full text and final AAC loudness checked. Not exhaustive human listening. FFmpeg frame-duplication messages are expected when holding still images; full final decode completed without errors.

The named characters, failed hunt and exact daily sequence are invented. Stone tools, bone needles, hide-working, gathering and social life have museum references in SOURCES.md. Clothing colors, plant shapes and detailed scenery are artistic decisions. No food identification instructions, dinosaurs, guaranteed hunt outcomes or universal daily schedule.

To rebuild: install the recorded Python packages with CPU PyTorch, make FFmpeg with libass/libx264 available, run project/narrate.py then project/render.py. Set HF_HOME/HF_HUB_DISABLE_XET for the local environment as needed. Source assets and code are retained. Original WAV/cache/temporary frames are kept in this execution workspace rather than committed; narration can be regenerated or extracted from the MP4 when making visual-only revisions. Rebuilding regenerates runtime-specific concat paths. No older videos were modified and no YouTube upload or schedule was performed.
