from pathlib import Path
import sys,json,ast,re
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import factories
from icon_set.scripts.create_variant import prepare_variant
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/dist/gallery/failures.html#rule=bounds&kind=Ink+box+too+narrow+%26+too+tall'
AUTHOR='gpt-6'
W=Path(__file__).parent;rows=json.loads((W/'targets.json').read_text());f=factories();groups={}
for r in rows:
 cls=f[r['id']]
 while getattr(cls,'variant_of',None):cls=f[cls.variant_of]
 groups.setdefault(cls.icon_id,[]).append(r)
results=[]
for root,group in groups.items():
 src=group[-1];p,ident,s=prepare_variant(src['id'],'solo','Exact keyshape envelope and clear spacing')
 t=ast.parse(s);meta={n.targets[0].id:ast.literal_eval(n.value) for n in t.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ('SOURCE_ICON_ID','SOURCE_PATH')}
 if meta.get('SOURCE_ICON_ID'):p=p.with_name(p.stem+'_'+meta['SOURCE_ICON_ID'].replace('-','_')+'.py')
 s=re.sub(r"AUTHOR = .*","AUTHOR = 'gpt-6'",s)
 if 'SOURCE_ICON_ID =' not in s:s=s.replace('AUTHOR =',f"SOURCE_ICON_ID = None\nSOURCE_PATH = {src['file']!r}\nAUTHOR =")
 s=s.replace('Keyshape.HRECT_XL','Keyshape.SQUARE').replace('Keyshape.VRECT_M','Keyshape.VRECT_L').replace('Keyshape.VRECT_S','Keyshape.VRECT_L')
 t=ast.parse(s)
 for node in ast.walk(t):
  if isinstance(node,(ast.Module,ast.ClassDef,ast.FunctionDef)) and node.body and isinstance(node.body[0],ast.Expr) and isinstance(node.body[0].value,ast.Constant) and isinstance(node.body[0].value.value,str):node.body.pop(0)
 s='# Independent revision; parent models preserved.\n'+ast.unparse(t)+'\n'
 with p.open('x') as out:out.write(s)
 results.append({'original':src['id'],'originals':[r['id'] for r in group],'root':root,'id':ident,'file':str(p.relative_to(ROOT)),'note':'Corrected keyshape selection to match the existing square proportions.'})
(W/'results.json').write_text(json.dumps(results,indent=2));print(len(results),'variants covering',sum(len(r['originals']) for r in results),'entries')
