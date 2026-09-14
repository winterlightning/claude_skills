from pathlib import Path
import json,sys,re,importlib
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons import registry
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/too-short-repair/queue.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;mapping=[]
for r in json.loads((W/'queue.json').read_text()):
 p,i,s=prepare_variant(r['id'],'solo','Height envelope and full spacing repair');m=re.search(r"SOURCE_ICON_ID = ['\"]([^'\"]+)",s)
 if m:p=p.with_name(p.stem+'_'+m[1].replace('-','_')+'.py')
 s=re.sub(r"AUTHOR = .*","AUTHOR = 'gpt-6'",s)
 with p.open('x') as f:f.write(s)
 mapping.append({'original':r['id'],'id':i,'file':str(p.relative_to(ROOT))});module=importlib.import_module('.'.join(p.relative_to(ROOT).with_suffix('').parts));factory=next(v for v in vars(module).values() if isinstance(v,type) and getattr(v,'icon_id',None)==i);registry._FACTORIES[i]=factory
(W/'mapping.json').write_text(json.dumps(mapping,indent=2))
