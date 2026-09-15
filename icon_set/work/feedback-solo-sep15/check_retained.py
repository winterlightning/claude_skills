from pathlib import Path
import json,sys
W=Path(__file__).resolve().parent;sys.path.insert(0,str(W/'snapshot'))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
A=json.loads((W/'inventory.json').read_text());R=json.loads((W/'revisions.json').read_text());Q={}
for x in A:
 if str(x['number']) in R or not x.get('path') or x['parent'] in Q:continue
 a=inspect_icon(create(x['parent']));Q[x['parent']]={k:a.get(k) for k in ['status','errors','warnings']};print(x['number'],x['parent'],Q[x['parent']],flush=True)
 (W/'retained-validation.json').write_text(json.dumps(Q,indent=2))
