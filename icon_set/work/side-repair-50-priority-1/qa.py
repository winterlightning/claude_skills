import json,sys,hashlib
from pathlib import Path
W=Path(__file__).resolve().parent;sys.path.insert(0,str(W.parents[2]))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
out=json.loads((W/"release-qa.json").read_text()) if (W/"release-qa.json").exists() else {}
for k,r in json.loads((W/'candidates.json').read_text()).items():
 try:
  model=create(r['icon']); sha=hashlib.sha256(model.to_svg().encode()).hexdigest()
  if out.get(k,{}).get('svg_sha256')==sha:continue
  q=inspect_icon(model);q.pop('_svg',None);out[k]=q
  print(k,r['icon'],q['status'],str(q.get('errors'))[:1000],str(q.get('warnings'))[:600],flush=True)
 except Exception as e:out[k]={'status':'fail','exception':str(e)};print(k,e,flush=True)
 (W/'release-qa.json').write_text(json.dumps(out,indent=2))
