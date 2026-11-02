from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import subprocess,json,hashlib,re
import numpy as np
root=Path(__file__).resolve().parents[1];video=root/'Stone-Age-Toothache-Short.mp4'
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(video)]))
duration=float(probe['format']['duration'])
decode=subprocess.run(['ffmpeg','-v','error','-i',str(video),'-f','null','-'],capture_output=True,text=True)
assert decode.returncode==0 and not decode.stderr,decode.stderr
run=subprocess.run(['ffmpeg','-hide_banner','-i',str(video),'-af','loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
measure=json.loads(re.findall(r'\{[^{}]*\}',run.stderr)[-1])
captions=json.loads((root/'project/captions.json').read_text());shots=json.loads((root/'project/shots.json').read_text())
assert 45<=duration<=60
assert all(0<=c['start']<c['end']<=duration for c in captions)
assert all(a['end']<=b['start']+.001 for a,b in zip(captions,captions[1:]))
assert re.sub(r'\s+',' ',(root/'script.txt').read_text()).strip()==re.sub(r'\s+',' ',' '.join(c['text'] for c in captions)).strip()
assert shots[0]['start_frame']==0 and all(a['end_frame']==b['start_frame'] for a,b in zip(shots,shots[1:]))
assert len({(s['sheet'],s['cell']) for s in shots})==len(shots)
assert float(measure['input_tp'])<=-1.5,measure
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',41)
srt=(root/'subtitles.srt').read_text();lines=[line for line in srt.splitlines() if line and not line.isdigit() and '-->' not in line]
assert max(font.getlength(line) for line in lines)<554
early=[]
for i,t in enumerate([0.1,1.0,1.8]):
    path=root/f'project/caption-timing-{i}.png'
    subprocess.run(['ffmpeg','-v','error','-ss',str(t),'-i',str(video),'-frames:v','1','-y',str(path)],check=True)
    early.append(np.asarray(Image.open(path).convert('RGB')).astype(float))
changes=[int((np.abs(a[900:1040]-b[900:1040]).max(axis=2)>35).sum()) for a,b in zip(early,early[1:])]
assert all(n>500 for n in changes),('Burned captions failed to update within held scene',changes)
assert np.abs(early[0][:750]-early[2][:750]).mean()<3,'Unexpected scene motion'
report=dict(status='passed',duration_seconds=duration,resolution=[probe['streams'][0]['width'],probe['streams'][0]['height']],fps=probe['streams'][0]['r_frame_rate'],video_codec=probe['streams'][0]['codec_name'],audio_codec=probe['streams'][1]['codec_name'],audio_sample_rate_hz=probe['streams'][1]['sample_rate'],scenes=len(shots),source_panels=32,selected_unique_panels=len(shots),subtitle_cues=len(captions),subtitle_full_text_matches=True,max_caption_line_width_pixels=round(max(font.getlength(line) for line in lines),2),full_decode_exit_code=decode.returncode,integrated_loudness_lufs=float(measure['input_i']),true_peak_dbtp=float(measure['input_tp']),scene_seconds_range=[min(s['duration'] for s in shots),max(s['duration'] for s in shots)],mean_scene_seconds=duration/len(shots),mp4_bytes=video.stat().st_size,sha256=hashlib.sha256(video.read_bytes()).hexdigest(),review_scope='Full decode, streams, caption full text/timing/line widths, frame continuity, unique panels, final AAC loudness, source-board review and sampled final-frame visual review. Not exhaustive human listening.')
(root/'validation-summary.json').write_text(json.dumps(report,indent=2)+'\n')
report['burned_caption_changes_within_static_scene']=True
report['caption_region_changed_pixels_at_sample_boundaries']=changes
(root/'validation-summary.json').write_text(json.dumps(report,indent=2)+'\n')
contact=Image.new('RGB',(900,2*560),'#f7eedc');draw=ImageDraw.Draw(contact)
for i,t in enumerate([1,13,22,32,43,49]):
    path=root/f'project/check-{i}.jpg';subprocess.run(['ffmpeg','-v','error','-ss',str(t),'-i',str(video),'-frames:v','1','-y',str(path)],check=True)
    im=Image.open(path).resize((300,533));contact.paste(im,((i%3)*300,(i//3)*560));draw.text(((i%3)*300+10,(i//3)*560+538),f'{t} seconds',fill='black')
contact.save(root/'project/final-review.jpg');print(json.dumps(report,indent=2))
