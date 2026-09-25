"""Prepare the explicitly user-approved main-icon exceptions; preserve raw QA."""
from pathlib import Path
import ast, json, hashlib, re
from datetime import datetime, timezone
from icon_set.model.icons.solo._base import Solo48
from icon_set.validation.library_qa import inspect_icon
ROOT=Path.cwd()
OUT=ROOT/'icon_set/work/exception-acceptance/20260925-main-repairs'
rows=json.loads(Path('/tmp/main-exception-candidates.json').read_text())
(OUT/'candidates.json').write_text(json.dumps(rows,indent=2))
prepared=[]
def load(text,path):
 text=text.replace('from ...keyshapes import','from icon_set.model.keyshapes import').replace('from ._base import','from icon_set.model.icons.solo._base import').replace('from ...primitives import','from icon_set.model.primitives import')
 ns={'__file__':str(path.resolve()),'__name__':'_approved_main'};exec(compile(text,str(path),'exec'),ns)
 classes=[(n,v) for n,v in ns.items() if isinstance(v,type) and issubclass(v,Solo48) and v is not Solo48 and v.__module__=='_approved_main']
 if len(classes)!=1:return text,None,None
 name,cls=classes[0];return text,name,cls()
for item in rows:
 source=ROOT/item['module'];text,name,icon=load(source.read_text(),source)
 fallback=None
 if icon is None:
  fallback='Latest run is a standalone non-SOLO48 SVG author; retain and approve the registered 48px drawing.'
  source=ROOT/item['drawings'][0]['python_source'];text,name,icon=load(source.read_text(),source)
 if icon is None:raise RuntimeError(item['concept']+' has no SOLO48 drawing')
 drawings=item['drawings'];match=next((d for d in drawings if d['icon_id']==icon.icon_id),None)
 if match is None:match=next((d for d in drawings if Path(d['python_source']).name==source.name),drawings[0])
 target=ROOT/match['python_source'];old=target.read_text();old_id=match['icon_id']
 text=re.sub(r"(\bicon_id\s*=\s*)(['\"])([^'\"]+)\2",lambda m:m[1]+repr(old_id),text,count=1)
 text,name,icon=load(text,source)
 svg=icon.to_svg();sha=hashlib.sha256(svg.encode()).hexdigest()
 approval={'reason':'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.','approved_by':'user','approved_on':datetime.now(timezone.utc).date().isoformat(),'svg_sha256':sha,'approval_scope':'47 repaired side-main sources identified in this task','source_uuid':item['source_uuid']}
 icon.exception=approval
 qa=inspect_icon(icon)
 if qa['status']!='pass':raise RuntimeError(item['concept']+': '+str(qa['errors']))
 registered=text.replace('from icon_set.model.keyshapes import Keyshape','from ...keyshapes import Keyshape').replace('from icon_set.model.icons.solo._base import Solo48','from ._base import Solo48')
 registered+='\n# Explicit user approval for this exact SVG; changes invalidate the exception.\n'+name+'.exception = '+repr(approval)+'\n'
 folder=OUT/item['source_uuid'];folder.mkdir(exist_ok=True)
 (folder/'previous.py.txt').write_text(old);(folder/target.name).write_text(registered)
 (folder/'qa.json').write_text(json.dumps({k:v for k,v in qa.items() if k!='_svg'},indent=2))
 (folder/'exception.json').write_text(json.dumps(approval,indent=2));(folder/(old_id+'.svg')).write_text(svg)
 prepared.append({**item,'target':str(target.relative_to(ROOT)),'staged':str((folder/target.name).relative_to(ROOT)),'previous_sha256':hashlib.sha256(old.encode()).hexdigest(),'icon_id':old_id,'exception':approval,'automatic_status':qa['automatic_status'],'fallback':fallback})
 print(old_id,qa['automatic_status'],'-> exception',flush=True)
(OUT/'prepared.json').write_text(json.dumps(prepared,indent=2))
print('Prepared',len(prepared),'without modifying registered drawings.')
