"""Focused revisions requested after the first fifty review."""
from pathlib import Path
import ast,json,sys,textwrap,runpy
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons.registry import factories
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-ai-next100/batch.json'
AUTHOR='gpt-6'
WORK=Path(__file__).parent
HELPERS=runpy.run_path(str(ROOT/'icon_set/work/solo-ai-first50/author_batch.py'))['HELPERS']
DESIGNS={}
def design(name,key,label,ref,plan,body): DESIGNS[name]=(key,label,ref,plan,textwrap.dedent(body))
exec((WORK/'designs.py').read_text())

def main():
 old={r['parent']:r for r in json.loads((ROOT/SOURCE_PATH).read_text())}
 prior={r['parent']:r for r in json.loads((WORK/'batch.json').read_text())} if (WORK/'batch.json').exists() else {}
 reg=factories();out=[]
 for name,(key,label,ref,plan,body) in DESIGNS.items():
  parent=old[name]['icon_id']
  if name in prior:
   p=ROOT/prior[name]['path']; new=prior[name]['icon_id'];tree=ast.parse(p.read_text())
  else:
   dest,new,source=prepare_variant(parent,'solo',label);tree=ast.parse(source)
   uuid=getattr(sys.modules[reg[parent].__module__],'SOURCE_ICON_ID');p=dest.with_name(dest.stem+'_'+uuid.replace('-','_')+'.py')
  cls=next(n for n in tree.body if isinstance(n,ast.ClassDef))
  tree.body=[n for n in tree.body if not isinstance(n,ast.Expr)]
  for n in cls.body:
   if isinstance(n,ast.Assign):
    for t in n.targets:
     if isinstance(t,ast.Name) and t.id=='keyshape':n.value=ast.Attribute(ast.Name('Keyshape',ast.Load()),key,ast.Load())
     if isinstance(t,ast.Name) and t.id=='variant_label':n.value=ast.Constant(label)
     if isinstance(t,ast.Name) and t.id=='keywords':n.value=ast.Tuple([ast.Constant('solo-ai-shapes-refine'),ast.Constant('solo-ai-next100'),ast.Constant(name)],ast.Load())
  cls.body=[n for n in cls.body if not isinstance(n,ast.FunctionDef)]
  header=f'    def build(self):\n        # Plan: {plan}\n        # Reference: '+(f'Lucide {ref}: original and atomic-debug geometry.' if ref else 'Original football; exact mirrored panel construction.')+'\n'
  func=header+HELPERS+textwrap.indent(body.strip(),'        ')+'\n';cls.body.append(ast.parse(textwrap.dedent(func)).body[0]);ast.fix_missing_locations(tree)
  rendered=ast.unparse(tree);rendered=rendered[:rendered.index('    def build(')]+func
  p.write_text(f'"""{name}: {label}; earlier revisions preserved."""\n'+rendered)
  out.append(dict(parent=name,previous=parent,icon_id=new,path=str(p.relative_to(ROOT)),keyshape=key,label=label,reference=ref,plan=plan))
 (WORK/'batch.json').write_text(json.dumps(out,indent=2));print('Authored',len(out))
if __name__=='__main__':main()
