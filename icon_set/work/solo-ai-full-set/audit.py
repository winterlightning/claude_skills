from pathlib import Path
import sys,json,hashlib,time
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-ai-full-set/inventory.json'
AUTHOR='gpt-6'
w=Path(__file__).parent
out=[]
for k,r in enumerate(json.loads((w/'inventory.json').read_text())):
 try:
  i=create(r['icon_id']);q=inspect_icon(i)
  out.append(dict(parent=r['icon_id'],status=q['status'],report=q,sha256=hashlib.sha256(i.to_svg().encode()).hexdigest()))
 except Exception as e:out.append(dict(parent=r['icon_id'],status='error',error=str(e)))
 if (k+1)%50==0:
  (w/'audit.json').write_text(json.dumps(out,indent=2));print(k+1,flush=True)
(w/'audit.json').write_text(json.dumps(out,indent=2));print('Complete',len(out),flush=True)
