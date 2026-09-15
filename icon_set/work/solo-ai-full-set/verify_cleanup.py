from pathlib import Path
import sys,json,hashlib
from io import BytesIO
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
from icon_set.renderers.png import render_png
from PIL import Image,ImageChops,ImageStat
AUTHOR='gpt-6';SOURCE_ICON_ID=None;SOURCE_PATH='icon_set/work/solo-ai-full-set/construction-cleanup.json'
w=Path(__file__).parent;out=[]
for r in json.loads((w/'construction-cleanup.json').read_text()):
 a=create(r['parent']);b=create(r['icon_id']);q=inspect_icon(b);diff=[]
 for scale in [1,2]:
  ai=Image.open(BytesIO(render_png(a,scale=scale))).convert('RGBA');bi=Image.open(BytesIO(render_png(b,scale=scale))).convert('RGBA');diff.append(sum(ImageStat.Stat(ImageChops.difference(ai,bi)).sum)/255)
 out.append(dict(parent=r['parent'],icon_id=r['icon_id'],status=q['status'],errors=q['errors'],warnings=q['warnings'],pixel_difference=diff,anchors_match=a.anchors==b.anchors))
 if q['status']!='pass' or max(diff)>4:print(out[-1],flush=True)
(w/'cleanup-verification.json').write_text(json.dumps(out,indent=2));print('Verified',len(out),'pass',sum(r['status']=='pass' for r in out),'max pixel diff',max(max(r['pixel_difference']) for r in out),'anchors',all(r['anchors_match'] for r in out))
