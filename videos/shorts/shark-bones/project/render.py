from pathlib import Path
import json, subprocess, re
import numpy as np
from PIL import Image, ImageOps

root=Path(__file__).resolve().parents[1];frames=root/'frames';frames.mkdir(exist_ok=True)
grids={};sheets={}
for i in [1,2]:
    im=Image.open(root/f'assets/sheet-{i:02}.png').convert('RGB');a=np.asarray(im);h,w=a.shape[:2];bounds=[]
    for axis,n in [(0,w),(1,h)]:
        score=a.std(axis=axis).mean(axis=1);edges=[0]
        for k in range(1,4):
            lo=round(n*k/4)-int(n*.07);hi=round(n*k/4)+int(n*.07)
            lowest=score[lo:hi].min();ids=np.flatnonzero(score[lo:hi]<lowest+.6)+lo
            edges.append(int(np.median(ids)))
        edges.append(n);bounds.append(edges)
    grids[i]={'x':bounds[0],'y':bounds[1],'inset':9};sheets[i]=im
(root/'project/grid-crops.json').write_text(json.dumps(grids,indent=2))
timeline=json.loads((root/'project/timeline.json').read_text())
caps=json.loads((root/'project/captions.json').read_text());shots=[];concat=['ffconcat version 1.0']
for sec in timeline:
    start=round(sec['start']*24);end=round(sec['end']*24);count=len(sec['panels']);cuts=[start]
    for j in range(1,count):
        ideal=round(start+(end-start)*j/count)
        nearby=[round(c[t]*24) for c in caps for t in ['start','end'] if abs(c[t]*24-ideal)<=6]
        allowed=[n for n in nearby if n-cuts[-1]>=42 and end-n>=(count-j)*42]
        cuts.append(min(allowed,key=lambda n:abs(n-ideal)) if allowed else ideal)
    cuts.append(end)
    for j,(sheet,cell) in enumerate(sec['panels']):
        g=grids[sheet];x=cell%4;y=cell//4;pad=g['inset']
        box=(g['x'][x]+pad,g['y'][y]+pad,g['x'][x+1]-pad,g['y'][y+1]-pad)
        im=ImageOps.fit(sheets[sheet].crop(box),(720,1280),method=Image.Resampling.LANCZOS)
        idx=len(shots);path=frames/f'scene-{idx:02}.png';im.save(path)
        n=cuts[j+1]-cuts[j];shots.append(dict(index=idx,sheet=sheet,cell=cell,crop=box,start_frame=cuts[j],end_frame=cuts[j+1],frames=n,duration=n/24))
        concat.extend([f"file '{path}'",'option framerate 24',f'duration {n/24:.9f}'])
concat.extend([f"file '{path}'",'option framerate 24']);(root/'project/frames.ffconcat').write_text('\n'.join(concat)+'\n')
(root/'project/shots.json').write_text(json.dumps(shots,indent=2))
g=grids[2];box=(g['x'][3]+9,g['y'][3]+9,g['x'][4]-9,g['y'][4]-9)
ImageOps.fit(sheets[2].crop(box),(720,1280),method=Image.Resampling.LANCZOS).save(root/'cover.jpg',quality=95)
result=subprocess.run(['ffmpeg','-hide_banner','-i',str(root/'narration.wav'),'-af','loudnorm=I=-16:TP=-2.5:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
m=json.loads(re.findall(r'\{[^{}]*\}',result.stderr)[-1]);(root/'project/normalization-settings.json').write_text(json.dumps(m,indent=2))
af=f"loudnorm=I=-16:TP=-2.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,aresample=192000,alimiter=limit=0.65:level=false:latency=true,aresample=48000"
subprocess.run(['ffmpeg','-v','error','-i',str(root/'narration.wav'),'-af',af,'-ar','48000','-y',str(root/'narration-normalized.wav')],check=True)
# User preference: no subtitles, labels, headers, or other text overlays in the MP4.
cmd=['ffmpeg','-v','warning','-f','concat','-safe','0','-i',str(root/'project/frames.ffconcat'),'-i',str(root/'narration-normalized.wav'),'-vf','fps=24','-r','24','-fps_mode','cfr','-c:v','libx264','-preset','fast','-crf','21','-threads','2','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-t',str(end/24),'-movflags','+faststart','-y',str(root/'Shark-Bones-Short.mp4')]
(root/'project/render-command.json').write_text(json.dumps(cmd,indent=2))
print('RENDER',end/24,'seconds',len(shots),'scenes; clean picture, separate SRT',flush=True)
subprocess.run(cmd,check=True);print('DONE',flush=True)
