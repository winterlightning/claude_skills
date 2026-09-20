import json,sys,hashlib,inspect
from pathlib import Path
W=Path(__file__).resolve().parent;sys.path.insert(0,str(W.parents[2]))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
out=json.loads((W/"release-qa.json").read_text()) if (W/"release-qa.json").exists() else {}
for k,r in json.loads((W/'candidates.json').read_text()).items():
 try:
  model=create(r['icon']); sha=hashlib.sha256(model.to_svg().encode()).hexdigest()
  model_sha=hashlib.sha256(Path(inspect.getsourcefile(type(model))).read_bytes()).hexdigest()
  if out.get(k,{}).get('svg_sha256')==sha and out.get(k,{}).get('model_sha256')==model_sha:continue
  q=inspect_icon(model);q.pop('_svg',None);q['model_sha256']=model_sha;out[k]=q
  print(k,r['icon'],q['status'],str(q.get('errors'))[:1000],str(q.get('warnings'))[:600],flush=True)
 except Exception as e:out[k]={'status':'fail','exception':str(e)};print(k,e,flush=True)
 (W/'release-qa.json').write_text(json.dumps(out,indent=2))
