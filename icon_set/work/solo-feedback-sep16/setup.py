from pathlib import Path
import sys,json,ast,inspect
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons.registry import factories
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='User feedback on rejected-solo-fixes-sep15 report'
AUTHOR='gpt-6'
names=['anteater','arched-stone-bridge','arrange-number','artillery-field-gun','artillery-gun-outriggers','baby-face-with-bow','balancing-stick-pose']
old={r['icon_id']:r for r in json.loads(Path('icon_set/work/rejected-solo-fixes-sep15/final-review.json').read_text())}
rows=[]
for name in names:
 parent=old[name]['revision_id'];factory=factories()[parent];source=Path(inspect.getsourcefile(factory));tree=ast.parse(source.read_text());meta={}
 for n in tree.body:
  if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ('SOURCE_ICON_ID','SOURCE_PATH'):meta[n.targets[0].id]=ast.literal_eval(n.value)
 dest,newid,text=prepare_variant(parent,'solo','Revised after specific drawing feedback, 16 September')
 if meta.get('SOURCE_ICON_ID'):dest=dest.with_stem(dest.stem+'_'+meta['SOURCE_ICON_ID'].replace('-','_'))
 dest.write_text(text)
 cls=next(n.name for n in ast.parse(text).body if isinstance(n,ast.ClassDef))
 (W/(name+'-before.svg')).write_bytes((Path('icon_set/dist/solo48')/(parent+'.svg')).read_bytes())
 rows.append({'icon_id':name,'parent':parent,'new_id':newid,'new_path':str(dest.relative_to(Path.cwd())),'class_name':cls,'meta':meta,'category':factory.category,'number':old[name]['number']})
(W/'plan.json').write_text(json.dumps(rows,indent=2));print([(r['icon_id'],r['new_id']) for r in rows])
