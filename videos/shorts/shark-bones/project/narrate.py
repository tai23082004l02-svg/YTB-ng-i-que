import json, os, re, textwrap
from pathlib import Path
os.environ.setdefault('HF_HOME', '/workspace/work/video-tools/cache/huggingface')
os.environ.setdefault('HF_HUB_DISABLE_XET', '1')
import torch
torch.set_num_threads(2)
from kokoro import KPipeline
import numpy as np
import soundfile as sf

root=Path(__file__).resolve().parents[1]
sections=json.loads((root/'project/sections.json').read_text())
pipe=KPipeline(lang_code='a',repo_id='hexgrad/Kokoro-82M',device='cpu')
waves=[]; captions=[]; timeline=[]; offset=0.0
for i,sec in enumerate(sections):
    start=offset
    for result in pipe(sec['text'],voice='am_michael',speed=1.07):
        wave=result.audio.numpy()
        group=[]
        def flush():
            if not group: return
            text=''.join(t.text+t.whitespace for t in group).strip()
            captions.append(dict(start=offset+group[0].start_ts,end=offset+group[-1].end_ts,text=text))
            group.clear()
        for token in result.tokens or []:
            if token.start_ts is None or token.end_ts is None:
                if group: group[-1].text+=token.text
                continue
            if group and (len(''.join(t.text+t.whitespace for t in group))+len(token.text)>42 or token.end_ts-group[0].start_ts>2.8): flush()
            group.append(token)
            if re.search(r'[.!?]$',token.text): flush()
        flush()
        waves.append(wave); offset+=len(wave)/24000
    pause=np.zeros(7200,dtype=np.float32)
    waves.append(pause); offset+=0.3
    timeline.append(dict(index=i,name=sec['name'],start=start,end=offset,panels=sec['panels']))
    print(i,sec['name'],round(offset-start,2),flush=True)
merged=[]
for cue in captions:
    if merged and cue['end']-cue['start']<1.15 and cue['start']-merged[-1]['end']<0.15 and cue['end']-merged[-1]['start']<5.5 and len(merged[-1]['text'])+len(cue['text'])<65:
        merged[-1]['text']+=' '+cue['text']; merged[-1]['end']=cue['end']
    else:
        merged.append(cue)
captions=merged
for cue in captions:
    cue['text']=re.sub(r'\.\s*\.\s*\.', '...', cue['text']).strip()
for cue in captions:
    cue['text']=re.sub(r'\s+([,.!?;:])', r'\1', cue['text'])
sf.write(root/'narration.wav',np.concatenate(waves),24000)
(root/'script.txt').write_text('\n\n'.join(s['text'] for s in sections)+'\n')
(root/'project/captions.json').write_text(json.dumps(captions,indent=2))
(root/'project/timeline.json').write_text(json.dumps(timeline,indent=2))
def stamp(t):
    ms=round(t*1000); return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(root/'subtitles.srt').write_text('\n\n'.join(f'{i+1}\n{stamp(c["start"])} --> {stamp(c["end"])}\n'+ '\n'.join(textwrap.wrap(c['text'],width=32)) for i,c in enumerate(captions))+'\n')
print('TOTAL',offset,'WORDS',sum(len(s['text'].split()) for s in sections),'CUES',len(captions),flush=True)
