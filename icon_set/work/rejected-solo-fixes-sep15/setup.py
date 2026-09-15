from pathlib import Path
import sys,ast,json,shutil
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons.registry import factories
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/rejected-solo-review-50-sep15/review.json'
AUTHOR='gpt-6'
rows=json.loads(Path(SOURCE_PATH).read_text());snap={i['icon_id']:i for i in json.loads(Path('icon_set/work/rejected-solo-review-50-sep15/snapshot.json').read_text())}
(W/'before').mkdir(exist_ok=True)
plans=[]
for r in rows:
 if r['verdict']=='good':continue
 old=r['icon_id'];source=Path(r['source_path']);shutil.copy2(source,W/'before'/source.name)
 meta={}
 for n in ast.parse(source.read_text()).body:
  if isinstance(n,ast.Assign):
   for t in n.targets:
    if isinstance(t,ast.Name) and t.id in ['SOURCE_ICON_ID','SOURCE_PATH']:
     try:meta[t.id]=ast.literal_eval(n.value)
     except:pass
 dest,new,text=prepare_variant(old,'solo','Redrawn after rejected solo visual review')
 sid=meta.get('SOURCE_ICON_ID')
 if sid:dest=dest.with_name(dest.stem+'_'+sid.replace('-','_')+'.py')
 dest.write_text(text)
 cls=next(n.name for n in ast.parse(text).body if isinstance(n,ast.ClassDef) and any(isinstance(t,ast.Assign) and any(isinstance(a,ast.Name) and a.id=='icon_id' for a in t.targets) for t in n.body))
 plans.append({**r,'new_id':new,'new_path':str(dest.relative_to(Path.cwd())),'class_name':cls,'meta':meta,'baseline_sha256':snap[old]['review_sha256']})
(W/'plan.json').write_text(json.dumps(plans,indent=2))
heads={}
for p in Path('icon_set/model/icons/solo').glob('*.py'):
 s=p.read_text()
 if 'SOURCE_HEAD_ICON_ID' not in s:continue
 for n in ast.parse(s).body:
  if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='SOURCE_HEAD_ICON_ID' for t in n.targets):
   try:heads[ast.literal_eval(n.value)]=str(p)
   except:pass
for r in plans:
 if r['action']=='avatar':print(r['icon_id'],heads.get(r['icon_id']))
(W/'avatar-sources.json').write_text(json.dumps({r['icon_id']:heads.get(r['icon_id']) for r in plans if r['action']=='avatar'},indent=2))
print(len(plans),'solo variant files prepared')
