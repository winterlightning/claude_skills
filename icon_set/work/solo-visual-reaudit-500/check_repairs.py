from pathlib import Path
import sys,json,concurrent.futures
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-remaining-repair/before.json'
AUTHOR='gpt-6'
W=Path(__file__).parent

def check(item):
 from icon_set.model.icons.registry import create
 from icon_set.validation.library_qa import inspect_icon
 number,row=item;icon=create(row['icon_id']);q=inspect_icon(icon);q.pop('_svg',None)
 (W/'repaired-qa'/f'{row["icon_id"]}.json').write_text(json.dumps(q,indent=2))
 return {'number':number,'icon_id':row['icon_id'],'status':q['status'],'errors':q['errors'],'warnings':q['warnings'],'holes':q['negative_space'].get('failed_hole_count'), 'pinches':q['negative_space'].get('pinch_count')}
if __name__=='__main__':
 (W/'repaired-qa').mkdir(exist_ok=True);rows=json.loads((W/'repairs.json').read_text());out=[]
 with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
  tasks=[pool.submit(check,item) for item in ((r['number'],r) for r in rows)]
  for done in concurrent.futures.as_completed(tasks):
   out.append(done.result())
   if len(out)%5==0:
    (W/'repair-audit.json').write_text(json.dumps(sorted(out,key=lambda r:r['number']),indent=2));print('Checked',len(out),'of',len(rows),flush=True)
 (W/'repair-audit.json').write_text(json.dumps(sorted(out,key=lambda r:r['number']),indent=2))
