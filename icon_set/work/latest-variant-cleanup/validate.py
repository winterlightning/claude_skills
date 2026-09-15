from pathlib import Path
import json,concurrent.futures,sys,os
from icon_set.model.icons.registry import create,icon_ids
from icon_set.validation.library_qa import inspect_icon
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/latest-variant-cleanup/applied-plan.json'
AUTHOR='gpt-6'
W=Path(__file__).resolve().parent

def check(n):
 q=inspect_icon(create(n));s=q.pop('_svg',None)
 if s:(W/(n+'.svg')).write_text(s)
 (W/(n+'.qa.json')).write_text(json.dumps(q,indent=2))
 return n,q['status'],q['errors'],q['warnings']
if __name__=='__main__':
 p=json.loads((W/os.environ.get('ICON_CLEANUP_PLAN','applied-plan.json')).read_text())
 if len(sys.argv)>1:p=[g for g in p if g['root'] in sys.argv[1:]]
 with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
  for n,status,errors,warnings in pool.map(check,[g['root'] for g in p]):
   print(n,status,errors,warnings,flush=True)
