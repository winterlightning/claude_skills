from pathlib import Path
import sys,json,hashlib,inspect
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-ai-full-set/batch.json'
AUTHOR='gpt-6'
w=Path(__file__).parent;out=[]
old={r['icon_id']:r for r in json.loads((w/'release-check.json').read_text())} if (w/'release-check.json').exists() else {}
rule_sha=hashlib.sha256(b''.join(p.read_bytes() for p in sorted((ROOT/'icon_set/validation').glob('*.py')))).hexdigest()
for r in json.loads((w/'batch.json').read_text()):
 i=create(r['icon_id']);sha=hashlib.sha256(Path(inspect.getfile(type(i))).read_bytes()).hexdigest()
 q=old.get(r['icon_id'],{})
 if q.get('_source_sha')!=sha or q.get('_rule_sha')!=rule_sha:q=inspect_icon(i)
 q.update(_source_sha=sha,_rule_sha=rule_sha);out.append(q)
 if q['status']!='pass':print(r['parent'],q['status'],q.get('errors'),q.get('warnings'),flush=True)
(w/'release-check.json').write_text(json.dumps(out,indent=2))
print('Statuses',{s:sum(q['status']==s for q in out) for s in set(q['status'] for q in out)})
