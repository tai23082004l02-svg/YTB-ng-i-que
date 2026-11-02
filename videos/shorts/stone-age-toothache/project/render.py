from pathlib import Path
import json, shutil, subprocess, re
import numpy as np
from PIL import Image, ImageOps, ImageFont

root=Path(__file__).resolve().parents[1]
frames=root/'frames';frames.mkdir(exist_ok=True)
sources=['exec-e08762f6-c40d-41b5-a8ae-efb3502f4b7d.png','exec-b083754a-be9b-4d88-9772-d4f3ddf3a717.png']
grids={};sheets={}
for i,name in enumerate(sources,1):
    path=root/f'assets/sheet-{i:02}.png'
    if not path.exists(): shutil.copyfile('/workspace/generated_images/'+name,path)
    im=Image.open(path).convert('RGB');a=np.asarray(im);h,w=a.shape[:2];bounds=[]
    for axis,n in [(0,w),(1,h)]:
        score=a.std(axis=axis).mean(axis=1);edges=[0]
        for k in range(1,4):
            lo=round(n*k/4)-int(n*.07);hi=round(n*k/4)+int(n*.07)
            lowest=score[lo:hi].min();candidates=np.flatnonzero(score[lo:hi]<lowest+.6)+lo
            edges.append(int(np.median(candidates)))
        edges.append(n);bounds.append(edges)
    grids[i]={'x':bounds[0],'y':bounds[1],'inset':9};sheets[i]=im
(root/'project/grid-crops.json').write_text(json.dumps(grids,indent=2))
caps=json.loads((root/'project/captions.json').read_text())
caption_font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',41)
def linebreak(text):
    if caption_font.getlength(text)<=530:return text
    words=text.split();splits=[(' '.join(words[:k]),' '.join(words[k:])) for k in range(1,len(words))]
    first,second=min(splits,key=lambda x:max(caption_font.getlength(t) for t in x)*3+abs(caption_font.getlength(x[0])-caption_font.getlength(x[1])))
    return first+'\n'+second
def stamp(t):
    ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(root/'subtitles.srt').write_text('\n\n'.join(f'{i+1}\n{stamp(c["start"])} --> {stamp(c["end"])}\n{linebreak(c["text"])}' for i,c in enumerate(caps))+'\n')
def ass_stamp(t):
    cs=round(t*100);return f'{cs//360000}:{cs//6000%60:02}:{cs//100%60:02}.{cs%100:02}'
ass='''[Script Info]
ScriptType: v4.00+
PlayResX: 720
PlayResY: 1280
WrapStyle: 2
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,DejaVu Sans,41,&H00FFFFFF,&H00FFFFFF,&H00101010,&H80000000,-1,0,0,0,100,100,0,0,1,2.5,1,2,50,110,250,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
for c in caps:
    text=linebreak(c['text']).replace('\n',r'\N')
    ass+=f"Dialogue: 0,{ass_stamp(c['start'])},{ass_stamp(c['end'])},Default,,0,0,0,,{text}\n"
(root/'project/subtitles.ass').write_text(ass)
timeline=json.loads((root/'project/timeline.json').read_text());shots=[];concat=['ffconcat version 1.0'];diagram_intervals=[]
for sec in timeline:
    start=round(sec['start']*24);end=round(sec['end']*24);count=len(sec['panels'])
    if sec['index']==1:
        cuts=[start,start+round(2.1*24),end-round(4.5*24),end]
    elif sec['index']==2:
        cuts=[start,start+4*24,start+8*24,end]
    else:
        cuts=[round(start+(end-start)*j/count) for j in range(count+1)]
    for j,(sheet,cell) in enumerate(sec['panels']):
        g=grids[sheet];x=cell%4;y=cell//4;pad=g['inset']
        box=(g['x'][x]+pad,g['y'][y]+pad,g['x'][x+1]-pad,g['y'][y+1]-pad)
        im=ImageOps.fit(sheets[sheet].crop(box),(720,1280),method=Image.Resampling.LANCZOS)
        idx=len(shots);path=frames/f'scene-{idx:02}.png';im.save(path)
        n=cuts[j+1]-cuts[j];shots.append(dict(index=idx,sheet=sheet,cell=cell,crop=box,start_frame=cuts[j],end_frame=cuts[j+1],frames=n,duration=n/24))
        if (sheet==1 and cell in [7,8,10,11,13]) or (sheet==2 and cell in [0,5]):diagram_intervals.append((cuts[j]/24,cuts[j+1]/24))
        concat.extend([f"file '{path}'",'option framerate 24',f'duration {n/24:.9f}'])
concat.extend([f"file '{path}'",'option framerate 24']);(root/'project/frames.ffconcat').write_text('\n'.join(concat)+'\n')
(root/'project/shots.json').write_text(json.dumps(shots,indent=2))
# Portrait cover is a generated panel with the same character, cropped without camera movement.
g=grids[2];box=(g['x'][3]+9,g['y'][3]+9,g['x'][4]-9,g['y'][4]-9)
ImageOps.fit(sheets[2].crop(box),(720,1280),method=Image.Resampling.LANCZOS).save(root/'cover.jpg',quality=95)
measure_run=subprocess.run(['ffmpeg','-hide_banner','-i',str(root/'narration.wav'),'-af','loudnorm=I=-16:TP=-2:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
m=json.loads(re.findall(r'\{[^{}]*\}',measure_run.stderr)[-1]);(root/'project/normalization-settings.json').write_text(json.dumps(m,indent=2))
af=f"loudnorm=I=-16:TP=-2:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,volume=-0.35dB"
subprocess.run(['ffmpeg','-v','error','-i',str(root/'narration.wav'),'-af',af,'-ar','48000','-y',str(root/'narration-normalized.wav')],check=True)
enable='+'.join(f'gte(t,{a})*lt(t,{b})' for a,b in diagram_intervals)
vf=f"fps=24,ass={root/'project/subtitles.ass'},drawtext=text='Illustration':fontcolor=0x30251d:fontsize=22:box=1:boxcolor=0xf7ead2@0.85:boxborderw=5:x=45:y=750:enable='{enable}'"
cmd=['ffmpeg','-v','warning','-f','concat','-safe','0','-i',str(root/'project/frames.ffconcat'),'-i',str(root/'narration-normalized.wav'),'-vf',vf,'-r','24','-fps_mode','cfr','-c:v','libx264','-preset','fast','-crf','21','-threads','2','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-ar','48000','-t',str(end/24),'-movflags','+faststart','-y',str(root/'Stone-Age-Toothache-Short.mp4')]
print('RENDER',end/24,'seconds',len(shots),'scenes',flush=True);subprocess.run(cmd,check=True);print('DONE',flush=True)
