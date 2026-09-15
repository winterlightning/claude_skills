from pathlib import Path
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.svg import render_svg
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-remaining-repair/review-decisions.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;D=ROOT/'icon_set/dist';restored=[]
for r in json.loads((W/'review-decisions.json').read_text()):
 if r['decision']=='blocked':continue
 p=D/'solo48'/(r['selected']+'.svg')
 if p.exists():continue
 q=json.loads((D/'qa/solo'/r['selected']/'metrics.json').read_text());assert q['status']=='pass'
 doc=render_svg(create(r['selected']));sha=hashlib.sha256(doc.encode()).hexdigest();assert sha==q['svg_sha256']==r['svg_sha256']
 p.write_text(doc);restored.append(r['selected'])
(W/'restored-previews.json').write_text(json.dumps(restored,indent=2)+'\n');print('Regenerated',len(restored),'missing SVGs; every hash matches the successful build record.')
