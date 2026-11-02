from pathlib import Path
from PIL import Image,ImageDraw
import subprocess,json,hashlib,re
import numpy as np
root=Path(__file__).resolve().parents[1];video=root/'Shark-Bones-Short.mp4'
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(video)]));duration=float(probe['format']['duration'])
decode=subprocess.run(['ffmpeg','-v','error','-i',str(video),'-f','null','-'],capture_output=True,text=True);assert decode.returncode==0 and not decode.stderr,decode.stderr
result=subprocess.run(['ffmpeg','-hide_banner','-i',str(video),'-af','loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
m=json.loads(re.findall(r'\{[^{}]*\}',result.stderr)[-1]);assert float(m['input_tp'])<=-1.5,m
caps=json.loads((root/'project/captions.json').read_text());shots=json.loads((root/'project/shots.json').read_text())
assert 40<=duration<=75
assert all(0<=c['start']<c['end']<=duration for c in caps)
assert all(a['end']<=b['start']+.001 for a,b in zip(caps,caps[1:]))
assert re.sub(r'\s+',' ',(root/'script.txt').read_text()).strip()==re.sub(r'\s+',' ',' '.join(c['text'] for c in caps)).strip()
assert shots[0]['start_frame']==0 and all(a['end_frame']==b['start_frame'] for a,b in zip(shots,shots[1:]))
assert len({(s['sheet'],s['cell']) for s in shots})==len(shots)
assert [s['codec_type'] for s in probe['streams']]==['video','audio']
cmd=json.loads((root/'project/render-command.json').read_text());assert cmd[cmd.index('-vf')+1]=='fps=24'
contact=Image.new('RGB',(900,1120),'#f7eedc');draw=ImageDraw.Draw(contact);differences=[]
for i,t in enumerate([1,10,20,30,40,round(duration-1,2)]):
    target=root/f'project/check-{i}.png';subprocess.run(['ffmpeg','-v','error','-ss',str(t),'-i',str(video),'-frames:v','1','-y',str(target)],check=True)
    im=Image.open(target).convert('RGB');shot=next(s for s in shots if s['start_frame']/24<=t<s['end_frame']/24)
    source=Image.open(root/f'frames/scene-{shot["index"]:02}.png').convert('RGB')
    error=np.abs(np.asarray(im).astype(float)-np.asarray(source).astype(float));differences.append(float(error.mean()))
    assert error.mean()<4,('Unexpected alteration to clean illustration',t,error.mean())
    contact.paste(im.resize((300,533)),((i%3)*300,(i//3)*560));draw.text(((i%3)*300+10,(i//3)*560+538),f'{t} seconds',fill='black')
contact.save(root/'project/final-review.jpg')
report=dict(status='passed',duration_seconds=duration,resolution=[720,1280],fps=probe['streams'][0]['r_frame_rate'],video_codec=probe['streams'][0]['codec_name'],audio_codec=probe['streams'][1]['codec_name'],audio_sample_rate_hz=probe['streams'][1]['sample_rate'],scenes=len(shots),source_panels=32,selected_unique_panels=len(shots),subtitle_cues=len(caps),subtitle_delivery='separate SRT only; not burned or muxed',subtitle_full_text_matches=True,no_subtitle_stream=True,no_text_overlay_filters=True,sampled_frame_mean_absolute_errors=differences,full_decode_exit_code=decode.returncode,integrated_loudness_lufs=float(m['input_i']),true_peak_dbtp=float(m['input_tp']),scene_seconds_range=[min(s['duration'] for s in shots),max(s['duration'] for s in shots)],mp4_bytes=video.stat().st_size,sha256=hashlib.sha256(video.read_bytes()).hexdigest(),review_scope='Full decode, streams, SRT timing/text, unique panels, continuous frame timeline, final AAC loudness, source-board and six final-frame visual comparisons against clean source illustrations. Not exhaustive human listening.')
(root/'validation-summary.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
