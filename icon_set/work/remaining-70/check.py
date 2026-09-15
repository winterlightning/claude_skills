from pathlib import Path
import json,sys,concurrent.futures
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
import qa_overlays
AUTHOR='gpt-6';SOURCE_ICON_ID=None;SOURCE_PATH='icon_set/work/remaining-70/plan.json'
W=Path(__file__).parent

def check(g):
 n=g['root'];q=inspect_icon(create(n));svg=q.pop('_svg',None)
 if svg:
  p=W/(n+'.svg');p.write_text(svg);a,*_=qa_overlays.analyze_distance(str(p));q['overlay_distance']=a['lowest_distance'];q['overlay_min_gap']=a['min_gap']
 (W/(n+'.qa.json')).write_text(json.dumps(q,indent=2));return n,q['status'],q.get('overlay_distance'),q['errors'],q['warnings'],q.get('overlay_min_gap')
if __name__=='__main__':
 p=json.loads((W/'plan.json').read_text());s=set(sys.argv[1:]);p=[g for g in p if Path(g['target_file']).exists() and (not s or g['root'] in s or str(g['number']) in s)]
 with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
  for r in pool.map(check,p):print(*r,flush=True)
