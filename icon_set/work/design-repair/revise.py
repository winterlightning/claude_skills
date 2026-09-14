from pathlib import Path
import sys,json,re,ast
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/broken-geometry-repair/queue.json'
AUTHOR='gpt-6'
if not (W/'mapping.json').exists():
 rows=json.loads((ROOT/'icon_set/work/broken-geometry-repair/results.json').read_text());mapping=[]
 for row in rows:
  if row['valid']:mapping.append({'original':row['id'],'id':row['id'],'file':row['file'],'changed':False});continue
  dest,new,src=prepare_variant(row['id'],'solo','Design rules: exact bounds and open spacing')
  old=(ROOT/row['file']).read_text();sid=re.search(r"SOURCE_ICON_ID = ['\"]([^'\"]+)",old)[1]
  dest=dest.with_name(dest.stem+'_'+sid.replace('-','_')+'.py');dest.write_text(src)
  mapping.append({'original':row['id'],'id':new,'file':str(dest.relative_to(ROOT)),'changed':True})
 (W/'mapping.json').write_text(json.dumps(mapping,indent=2))
print('Variant mapping ready')
