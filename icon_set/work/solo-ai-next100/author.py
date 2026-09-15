"""Second group of fifty: individually planned SOLO48 review variants."""
from pathlib import Path
import ast,json,sys,textwrap,runpy
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons.registry import factories
SOURCE_ICON_ID=None # Exact per-icon identities are retained in selected.json and each module.
SOURCE_PATH='icon_set/work/solo-ai-next100/selected.json'
AUTHOR='gpt-6'
WORK=Path(__file__).parent
HELPERS=runpy.run_path(str(ROOT/'icon_set/work/solo-ai-first50/author_batch.py'))['HELPERS']
D={}
def design(name,key,ref,plan,body):D[name]=(key,ref,plan,textwrap.dedent(body))
exec((WORK/'designs.py').read_text())

def main():
 rows=json.loads((WORK/'selected.json').read_text());reg=factories();prior={r['parent']:r for r in json.loads((WORK/'batch.json').read_text())} if (WORK/'batch.json').exists() else {};out=[]
 for row in rows:
  name=row['icon_id'];key,ref,plan,body=D[name]
  if name in prior:p=ROOT/prior[name]['path'];new=prior[name]['icon_id'];tree=ast.parse(p.read_text())
  else:
   dest,new,source=prepare_variant(name,'solo','AI review · next 100');tree=ast.parse(source);uuid=getattr(sys.modules[reg[name].__module__],'SOURCE_ICON_ID',None);p=dest.with_name(dest.stem+'_'+uuid.replace('-','_')+'.py') if uuid else dest
  cls=next(n for n in tree.body if isinstance(n,ast.ClassDef));tree.body=[n for n in tree.body if not isinstance(n,ast.Expr)]
  for n in tree.body:
   if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUTHOR' for t in n.targets):n.value=ast.Constant(AUTHOR)
  for n in cls.body:
   if isinstance(n,ast.Assign):
    for t in n.targets:
     if isinstance(t,ast.Name) and t.id=='keyshape':n.value=ast.Attribute(ast.Name('Keyshape',ast.Load()),key,ast.Load())
     if isinstance(t,ast.Name) and t.id=='keywords':n.value=ast.Tuple([ast.Constant(x) for x in tuple(row.get('keywords',[]))+('solo-ai-next100',)],ast.Load())
  cls.body=[n for n in cls.body if not isinstance(n,ast.FunctionDef)]
  func='    def build(self):\n        # Plan: '+plan+'\n        # Reference: '+('Lucide '+ref+' original and atomic-debug construction.' if ref else 'No useful exact Lucide match; supplied original silhouette.')+'\n'+HELPERS+textwrap.indent(body.strip(),'        ')+'\n'
  cls.body.append(ast.parse(textwrap.dedent(func)).body[0]);ast.fix_missing_locations(tree);src=ast.unparse(tree);src=src[:src.index('    def build(')]+func;output=f'"""{name}: next hundred AI review; original preserved."""\n'+src
  if not p.exists() or p.read_text()!=output:p.write_text(output)
  out.append(dict(parent=name,icon_id=new,path=str(p.relative_to(ROOT)),keyshape=key,reference=ref,plan=plan))
 (WORK/'batch.json').write_text(json.dumps(out,indent=2));print('Authored',len(out))
if __name__=='__main__':main()
