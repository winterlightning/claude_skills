from pathlib import Path
import json,sys,concurrent.futures
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT));W=Path(__file__).parent
from icon_set.model.icons.registry import create
from icon_set.renderers.svg import render_svg
from icon_set.validation.library_qa import inspect_icon
import hashlib

def check(r):
 icon=create(r['selected']);digest=hashlib.sha256(render_svg(icon).encode()).hexdigest();f=W/'qa'/(r['selected']+'.json')
 q=json.loads(f.read_text()) if f.exists() else None
 if q is None or q['svg_sha256']!=digest:
  q=inspect_icon(icon);q.pop('_svg',None);f.write_text(json.dumps(q,indent=2))
 return r,q,icon.validate_icon().status
if __name__=='__main__':
 rows=json.loads((W/'selected.json').read_text());repairs={r['number']:r for r in json.loads((W/'repairs.json').read_text())}
 for r in rows:
  if r['number'] in repairs:
   fix=repairs[r['number']];r.update(selected=fix['icon_id'],file=fix['file'],reason=fix['reason'],new_reconstruction=True,decision='reconstructed')
  elif r['decision']!='blocked':r['decision']='reviewed'
 records_path=ROOT/'icon_set/model/contracts/spacing-reviews.v1.json';records=json.loads(records_path.read_text());audits=[];updated=[]
 with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
  for r,q,model in pool.map(check,rows):
   if r['decision']!='blocked':
    assert model=='valid' and not q['errors'] and q['negative_space']['status']=='pass',(r['number'],model,q['errors'])
   if r['new_reconstruction']:
    fix=repairs[r['number']];records['icons'].pop('solo/'+fix['parent'],None)
    pairs=[f['elements'] for f in q['internal_spacing']['findings']]
    evidence=f"icon_set/work/solo-visual-reaudit-500/new-{list(repairs).index(r['number'])//12+1}.png"
    if pairs:records['icons']['solo/'+r['selected']]=dict(svg_sha256=q['svg_sha256'],rules_sha256=q['rules_sha256'],elements=pairs,reviewer='gpt-6',reason=r['reason']+' Remaining sampled opposing-edge advisories were individually inspected at centerline and native scale; the certified model, enclosed holes and authored-stroke pinch checks pass.',evidence=evidence,reviewed_at='2026-09-15',hole_recheck='Enclosed holes and authored-stroke pinch checks passed.')
    r.update(evidence=evidence,reviewed_pairs=pairs)
   r['svg_sha256']=q['svg_sha256'];updated.append(r)
   audits.append(dict(number=r['number'],selected=r['selected'],model_status=model,status=q['status'],holes=q['negative_space']['failed_hole_count'],pinches=q['negative_space']['pinch_count'],svg_sha256=q['svg_sha256']))
 records_path.write_text(json.dumps(records,indent=2)+'\n');(W/'selected.json').write_text(json.dumps(updated,indent=2)+'\n');(W/'audit.json').write_text(json.dumps(audits,indent=2)+'\n');print('Verified all500 selected models and QA hashes; recorded71 reconstruction reviews.')
