from pathlib import Path
import sys,json
W=Path(__file__).resolve().parent;sys.path.insert(0,str(W/'snapshot'))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
r=json.loads((W/'revisions.json').read_text());q=json.loads((W/'release-validation.json').read_text());selected=set(sys.argv[1:])
for id in dict.fromkeys(v['id'] for v in r.values()):
 if selected and id not in selected:continue
 if not selected and q.get(id,{}).get('status')=='pass':continue
 a=inspect_icon(create(id));q[id]={k:a.get(k) for k in ['status','errors','warnings','advisories']};print(id, json.dumps(q[id]),flush=True)
 (W/'release-validation.json').write_text(json.dumps(q,indent=2))
