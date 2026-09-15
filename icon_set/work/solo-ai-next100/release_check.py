from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
w=Path(__file__).parent;out=[]
for r in json.loads((w/'batch.json').read_text()):
 q=inspect_icon(create(r['icon_id']));out.append(q)
 if q['status']!='valid':print(r['parent'],q.get('status'),q.get('errors'),q.get('warnings'),flush=True)
(w/'release-check.json').write_text(json.dumps(out,indent=2))
print('Statuses', {s:sum(q['status']==s for q in out) for s in set(q['status'] for q in out)})
