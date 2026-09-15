"""Focused revisions requested after the first fifty review."""
from pathlib import Path
import ast,json,sys,textwrap,runpy
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons.registry import factories
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-ai-next50/batch.json'
AUTHOR='gpt-6'
WORK=Path(__file__).parent
HELPERS=runpy.run_path(str(ROOT/'icon_set/work/solo-ai-first50/author_batch.py'))['HELPERS']
DESIGNS={}
def design(name,key,label,ref,plan,body): DESIGNS[name]=(key,label,ref,plan,textwrap.dedent(body))
design('binoculars','HRECT_L','Tapered barrels','binoculars','Mirrored broad eyepieces taper out to round objectives. Shared lens radii and an upper bridge preserve the original binocular proportions.', """
for side in (-1,1):
 x=lambda d:24+side*d
 circle(f'lens-{side}',x(12),32,8)
 path(f'barrel-{side}',(x(20),32),[('C',(x(16),14),(x(20),26),(x(16),20)),('C',(x(10),8),(x(16),10),(x(14),8)),('C',(x(4),14),(x(6),8),(x(4),10)),('L',(x(4),18)),('L',(x(4),32))])
 join(f'barrel-{side}',f'lens-{side}')
line('bridge',(20,18),(28,18))
join('bridge','barrel--1');join('bridge','barrel-1')
""")
design('bread','SQUARE','Broad bread slice',None,'A wide slice body retains the original proportion. A low softly domed crown has shallow shoulders, with matching sides and softly rounded bottom corners; no decorative crumbs.', """
# Shared axis owns the left and right sides of the slice.
right=[('C',(42,14),(38,6),(42,10)),('C',(39,20),(42,17),(40,19)),('L',(39,39)),('A',(36,42),3,3,True),('L',(24,42))]
path('slice',(24,6),right+[('L',(12,42)),('A',(9,39),3,3,True),('L',(9,20)),('C',(6,14),(8,19),(6,17)),('C',(24,6),(6,10),(10,6))],True)
""")
design('brain-f98adc76','SQUARE','Rounded anatomical lobes','brain','The original side-view brain retains its high lobed crown, small lower-left lobe and larger right lobe. Two curved sulci describe those masses instead of generic vertical slots. Deliberate anatomical asymmetry.', """
path('brain',(6,28),[
 ('C',(11,18),(6,23),(7,20)),
 ('C',(20,7),(11,11),(14,7)),
 ('C',(25,9),(22,7),(24,8)),
 ('C',(31,6),(27,7),(29,6)),
 ('C',(37,14),(35,6),(37,10)),
 ('C',(42,25),(41,15),(42,20)),
 ('C',(39,34),(42,29),(39,30)),
 ('C',(33,42),(39,39),(37,42)),
 ('C',(27,39),(30,42),(28,40)),
 ('C',(22,41),(25,41),(24,41)),
 ('C',(16,37),(19,41),(17,39)),
 ('C',(12,38),(14,38),(13,38)),
 ('C',(6,28),(8,38),(6,34))],True)
path('upper-fold',(25,9),[('C',(21,22),(22,12),(21,18))]);join('upper-fold','brain')
path('lower-fold',(27,39),[('C',(29,24),(24,33),(26,27))]);join('lower-fold','brain')
""")

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
     if isinstance(t,ast.Name) and t.id=='keywords':n.value=ast.Tuple([ast.Constant('solo-ai-next50-refine'),ast.Constant('solo-ai-next50'),ast.Constant(name)],ast.Load())
  cls.body=[n for n in cls.body if not isinstance(n,ast.FunctionDef)]
  header=f'    def build(self):\n        # Plan: {plan}\n        # Reference: '+(f'Lucide {ref}: original and atomic-debug geometry.' if ref else 'Original football; exact mirrored panel construction.')+'\n'
  func=header+HELPERS+textwrap.indent(body.strip(),'        ')+'\n';cls.body.append(ast.parse(textwrap.dedent(func)).body[0]);ast.fix_missing_locations(tree)
  rendered=ast.unparse(tree);rendered=rendered[:rendered.index('    def build(')]+func
  p.write_text(f'"""{name}: {label}; earlier revisions preserved."""\n'+rendered)
  out.append(dict(parent=name,previous=parent,icon_id=new,path=str(p.relative_to(ROOT)),keyshape=key,label=label,reference=ref,plan=plan))
 (WORK/'batch.json').write_text(json.dumps(out,indent=2));print('Authored',len(out))
if __name__=='__main__':main()
