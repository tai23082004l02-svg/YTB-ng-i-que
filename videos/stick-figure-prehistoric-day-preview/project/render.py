from pathlib import Path
import json, shutil, subprocess, re
import numpy as np
from PIL import Image, ImageOps, ImageDraw, ImageFont

root=Path(__file__).resolve().parents[1]
assets=root/'assets'; frames=root/'frames'; frames.mkdir(exist_ok=True)
paths=['exec-259047f5-65ed-436b-b960-010eca20c85b.png','exec-c8082e9e-4875-4c75-ac55-1f4bcc43d67d.png','exec-06562862-a6b8-4f86-88a8-ea3c937737b5.png']
grids={}; sheets={}
for i,p in enumerate(paths,1):
    target=assets/f'sheet-{i:02}.png'
    if not target.exists(): shutil.copyfile('/workspace/generated_images/'+p,target)
    im=Image.open(target).convert('RGB'); a=np.asarray(im); h,w=a.shape[:2]
    bounds=[]
    for axis,n in [(0,w),(1,h)]:
        score=a.std(axis=axis).mean(axis=1); edges=[0]
        for k in range(1,4):
            lo=round(n*k/4)-15; edges.append(lo+int(score[lo:lo+31].argmin()))
        edges.append(n); bounds.append(edges)
    grids[i]=dict(x=bounds[0],y=bounds[1],inset=11); sheets[i]=im
(root/'project/grid-crops.json').write_text(json.dumps(grids,indent=2))
timeline=json.loads((root/'project/timeline.json').read_text())
caps=json.loads((root/'project/captions.json').read_text())
shots=[]; concat=['ffconcat version 1.0']; prev=0
for sec in timeline:
    left=round(sec['start']*24); right=round(sec['end']*24)
    # Prefer nearby caption boundaries, while preserving 3-5 seconds for each image.
    cuts=[left]
    for j in range(1,5):
        ideal=round(left+(right-left)*j/5)
        candidates=[round(c[t]*24) for c in caps for t in ['start','end'] if abs(c[t]*24-ideal)<=8]
        allowed=[n for n in candidates if 68<=n-cuts[-1]<=122 and right-n>=(5-j)*68]
        cuts.append(min(allowed,key=lambda n:abs(n-ideal)) if allowed else ideal)
    cuts.append(right)
    for j,(sheet,cell) in enumerate(sec['panels']):
        idx=len(shots); grid=grids[sheet]; x=cell%4;y=cell//4; pad=grid['inset']
        box=(grid['x'][x]+pad,grid['y'][y]+pad,grid['x'][x+1]-pad,grid['y'][y+1]-pad)
        im=ImageOps.fit(sheets[sheet].crop(box),(1280,720),method=Image.Resampling.LANCZOS)
        path=frames/f'scene-{idx:03}.png';im.save(path)
        n=cuts[j+1]-cuts[j]
        shots.append(dict(index=idx,sheet=sheet,cell=cell,crop=box,start_frame=cuts[j],end_frame=cuts[j+1],frames=n,duration=n/24))
        concat.extend([f"file '{path}'",'option framerate 24',f'duration {n/24:.9f}'])
concat.extend([f"file '{path}'",'option framerate 24'])
(root/'project/shots.json').write_text(json.dumps(shots,indent=2))
(root/'project/frames.ffconcat').write_text('\n'.join(concat)+'\n')
ImageOps.fit(sheets[1].crop((11,11,409,225)),(1280,720),method=Image.Resampling.LANCZOS).save(root/'thumbnail.jpg',quality=95)
total=right/24
first=subprocess.run(['ffmpeg','-hide_banner','-i',str(root/'narration.wav'),'-af','loudnorm=I=-16:TP=-2:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
measure=json.loads(re.findall(r'\{[^{}]*\}',first.stderr)[-1])
(root/'project/normalization-settings.json').write_text(json.dumps(measure,indent=2))
af=f"loudnorm=I=-16:TP=-2:LRA=11:measured_I={measure['input_i']}:measured_TP={measure['input_tp']}:measured_LRA={measure['input_lra']}:measured_thresh={measure['input_thresh']}:offset={measure['target_offset']}:linear=true"
subprocess.run(['ffmpeg','-v','error','-i',str(root/'narration.wav'),'-af',af,'-ar','48000','-y',str(root/'narration-normalized.wav')],check=True)
cmd=['ffmpeg','-v','warning','-f','concat','-safe','0','-i',str(root/'project/frames.ffconcat'),'-i',str(root/'narration-normalized.wav'),'-vf',f"subtitles={root/'subtitles.srt'}:force_style='FontName=DejaVu Sans,FontSize=22,Bold=1,Outline=2,Shadow=1,MarginV=18,MarginL=30,MarginR=30'",'-r','24','-fps_mode','cfr','-c:v','libx264','-preset','fast','-crf','21','-threads','2','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-ar','48000','-t',str(total),'-movflags','+faststart','-y',str(root/'A-Day-in-the-Stone-Age-Preview.mp4')]
print('Rendering',total,'seconds',len(shots),'scenes',flush=True)
subprocess.run(cmd,check=True)
print('RENDER COMPLETE',flush=True)
