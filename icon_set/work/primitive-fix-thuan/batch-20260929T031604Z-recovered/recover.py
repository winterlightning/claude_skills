from pathlib import Path
import json,shutil,sys
from icon_set.scripts import primitive_fix as p,work_queue as w
B=Path(__file__).resolve().parent
base=w.default_base_url();worker='thuan-mac'
old=json.loads((B/'recovered-claims.json').read_text())
journal=B/'additional-claims.json'
new=json.loads(journal.read_text()) if journal.exists() else []
original=w.call
# Persist every successful claim immediately, including a partial failed request.
def durable_call(base_url,method,path,*args,**kwargs):
 r=original(base_url,method,path,*args,**kwargs)
 if method=='POST' and path=='/api/work/claim':
  new.append(r);journal.write_text(json.dumps(new,indent=2)+'\n')
 return r
w.call=durable_call
if len(new)<5:
 w.take_next(base,worker,family='solo',limit=5-len(new),offset=0,reason='meaning')
assert len(new)==5
claims=[dict(item=e,work=e['work']) for e in old]+new
(B/'all-claims.json').write_text(json.dumps(claims,indent=2)+'\n')
# Stage every claim record before making any download/upload request.
for c in claims:
 key=c['item']['key'];run=p.primitive_fix_results_dir()/p.key_folder(key)/'20260929T031604Z-recovered-thuan-mac'
 run.mkdir(parents=True,exist_ok=True);(run/'before').mkdir(exist_ok=True)
 (run/'claim.json').write_text(json.dumps(c,indent=2)+'\n')
 (run/'brief.txt').write_text(w.brief(c['item'],c['work']))
for i,c in enumerate(claims,1):
 item=c['item'];key=item['key'];run=p.primitive_fix_results_dir()/p.key_folder(key)/'20260929T031604Z-recovered-thuan-mac';before=run/'before'
 src=item.get('python_source',{}).get('path');module=None
 if src and Path(src).is_file():module=before/Path(src).name;shutil.copy2(src,module)
 svg=before/(item['icon_id']+'.svg')
 if not svg.exists():svg.write_text(p.fetch_svg(base,item))
 if not (run/'before-upload.json').exists():
  upload=w.upload_result(base,worker,key,item['svg_sha256'],'before',svg,module,note='Original rejected drawing; recovered interrupted claim without re-claiming.')
  (run/'before-upload.json').write_text(json.dumps(upload,indent=2)+'\n')
 refs=list((run/'reference').glob('*.svg'))
 ref=refs[0] if refs else p.stage_reference(base,item,run/'reference')
 if ref is None:ref=p.stage_current_as_reference(item,svg,run/'reference')
 print(i,key,ref,flush=True)
print('Staged exactly 20 claims (15 recovered + 5 additional).',flush=True)
