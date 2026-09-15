"""Check that the gallery release is the exact reviewed geometry."""
from pathlib import Path
import json,hashlib
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/nonhuman-reconstruction/audit.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
A=json.loads((W/'audit.json').read_text())
dist=Path('icon_set/dist')
manifest=json.loads((dist/'solo48/manifest.json').read_text())
passed={i['icon_id'] for i in manifest['icons']}
failed={i['icon_id'] for i in json.loads((dist/'failed/solo48/manifest.json').read_text())['icons']}
checked=[]
for i in A:
 if i['audit_status']!='reconstructed':continue
 n=i['icon_id'];assert n in passed and n not in failed,n
 svg=(W/(n+'.svg')).read_bytes();shipped=(dist/'solo48'/(n+'.svg')).read_bytes();assert svg==shipped,('stale SVG',n)
 metrics=json.loads((Path('icon_set/work/qa_overlays/solo48')/(n+'.metrics.json')).read_text())
 digest=hashlib.sha256(svg).hexdigest();assert metrics['svg_sha256']==digest,n
 assert metrics['distance_passed'] and metrics['negative_space_passed'],n
 checked.append({'icon_id':n,'svg_sha256':digest,'lowest_distance':metrics['lowest_distance'],'distance_measured':metrics['distance_measured'],'status':'pass'})
assert len(checked)==83
(W/'published-verification.json').write_text(json.dumps(checked,indent=2))
print('83/83 published SVGs match the reviewed models and passing overlay fingerprints.')
print('Solo release:',len(passed),'passing;',len(failed),'failed.')
