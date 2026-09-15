from pathlib import Path
import json,sys,concurrent.futures
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT));W=Path(__file__).parent
AUTHOR='gpt-6'
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-remaining-repair/review-decisions.json'
def check(row):
 from icon_set.model.icons.registry import create
 from icon_set.validation.library_qa import inspect_icon
 icon=create(row['selected']);q=inspect_icon(icon);q.pop('_svg',None)
 (W/'qa'/f'{row["selected"]}.json').write_text(json.dumps(q,indent=2)+'\n')
 return dict(number=row['number'],icon_id=row['icon_id'],selected=row['selected'],file=row['file'],new_reconstruction=row['new_reconstruction'],model_status=icon.validate_icon().status,status=q['status'],errors=q['errors'],warnings=q['warnings'],holes=q['negative_space']['failed_hole_count'],pinches=q['negative_space']['pinch_count'],svg_sha256=q['svg_sha256'])
if __name__=='__main__':
 old=json.loads((ROOT/SOURCE_PATH).read_text());repairs={r['number']:r for r in json.loads((W/'repairs.json').read_text())};rows=[]
 for row in old:
  r=repairs.get(row['number']);row={**row,'new_reconstruction':bool(r)}
  if r:row.update(selected=r['icon_id'],file=r['file'],reason=r['reason'])
  rows.append(row)
 (W/'selected.json').write_text(json.dumps(rows,indent=2)+'\n');(W/'qa').mkdir(exist_ok=True)
 out=[]
 with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
  tasks=[pool.submit(check,r) for r in rows]
  for done in concurrent.futures.as_completed(tasks):
   out.append(done.result())
   if len(out)%25==0:
    print('Verified',len(out),'of500',flush=True);(W/'audit.json').write_text(json.dumps(sorted(out,key=lambda r:r['number']),indent=2)+'\n')
 (W/'audit.json').write_text(json.dumps(sorted(out,key=lambda r:r['number']),indent=2)+'\n')
