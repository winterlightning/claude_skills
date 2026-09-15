from pathlib import Path
import sys,json,hashlib,collections
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.renderers.svg import render_svg
W=Path(__file__).parent;D=ROOT/'icon_set/dist';out=[];restored=[]
for r in json.loads((W/'selected.json').read_text()):
 icon=create(r['selected']);doc=render_svg(icon);sha=hashlib.sha256(doc.encode()).hexdigest();q=json.loads((D/'qa/solo'/r['selected']/'metrics.json').read_text());blocked=r['decision']=='blocked'
 assert sha==q['svg_sha256']==r['svg_sha256'],(r['number'],'hash mismatch')
 assert q['status']==('fail' if blocked else 'pass'),(r['number'],q['status'])
 if not blocked:assert icon.validate_icon().status=='valid' and not q['errors'] and q['negative_space']['status']=='pass',r['number']
 f=D/('failed/solo48' if blocked else 'solo48')/(r['selected']+'.svg')
 if not f.exists():f.write_text(doc);restored.append(r['selected'])
 assert hashlib.sha256(f.read_bytes()).hexdigest()==sha,r['number']
 out.append(dict(number=r['number'],selected=r['selected'],status=q['status'],holes=q['negative_space']['failed_hole_count'],pinches=q['negative_space']['pinch_count'],svg_sha256=sha))
(W/'final-export-check.json').write_text(json.dumps(out,indent=2)+'\n');(W/'restored-previews.json').write_text(json.dumps(restored,indent=2)+'\n');print(collections.Counter(r['status'] for r in out),'restored',len(restored),'missing canonical SVGs')
