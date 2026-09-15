"""Focused revisions requested after the first fifty review."""
from pathlib import Path
import ast,json,sys,textwrap,runpy
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons.registry import factories
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-ai-first50/batch.json'
AUTHOR='gpt-6'
WORK=Path(__file__).parent
HELPERS=runpy.run_path(str(ROOT/'icon_set/work/solo-ai-first50/author_batch.py'))['HELPERS']
DESIGNS={}
def design(name,key,label,ref,plan,body): DESIGNS[name]=(key,label,ref,plan,textwrap.dedent(body))
design('airplane','SQUARE','Swept wings · diagonal','plane','One complete airplane outline mirrors across x+y=48. Both swept wings and both tailplanes are present, with a tangent circular nose. Square bounds keep a generous diagonal wingspan.', '''
# Half of the plane defines every paired wing and tail coordinate.
half=[(24,16),(8,12),(6,16),(18,24),(12,30),(6,28),(6,36),(12,36)]
reflect=lambda p:(48-p[1],48-p[0])
commands=[('C',half[0],(32,6),(30,10))]
commands += [('L',p) for p in half[1:]]
commands += [('L',reflect(p)) for p in reversed(half[:-1])]
commands += [('C',(42,12),(38,18),(42,16)),('A',(36,6),6,6,False)]
path('airframe',(36,6),commands,True)
''')
design('airplane-other','SQUARE','Airliner · top view','plane','A front-to-back axis owns a round nose, broad swept wings, and a distinct tailplane. Mirrored coordinates make a second airplane design; deliberate upright orientation.', '''
right=[(28,10),(28,18),(42,28),(42,36),(28,28),(28,35),(34,39),(34,42),(24,40)]
mirror=lambda p:(48-p[0],p[1])
commands=[('L',p) for p in right[1:]]+[('L',mirror(p)) for p in reversed(right[:-1])]+[('A',(28,10),4,4,True)]
path('airframe',right[0],commands,True)
''')
design('antique-axe','SQUARE','Broad blade · rounded grip','axe','A broad curved blade balances an outlined diagonal handle, with exact shared shoulder nodes. The handle has a rounded grip and sufficient interior width; square bounds retain the original diagonal stance.', '''
path('head',(18,12),[('L',(24,6)),('L',(32,14)),('L',(42,14)),('C',(30,34),(42,27),(36,34)),('L',(30,24)),('L',(24,18)),('L',(18,12))],True)
path('handle',(24,18),[('L',(8,34)),('C',(6,38),(6,36),(6,36)),('A',(10,42),4,4,False),('C',(14,40),(12,42),(13,41)),('L',(30,24))])
join('handle','head')
''')
design('atom-other','SQUARE','Balanced orbits · nucleus','atom','Two rounded diagonal orbits mirror around x=24 and y=24, with a restored central nucleus. Shared crossing nodes and wider central space preserve the atom reading; square bounds balance both loops.', '''
commands=[('A',(12,6),6,6,True),('C',(24,12),(16,6),(20,8)),('L',(36,24)),('C',(42,36),(40,28),(42,32)),('A',(36,42),6,6,True),('C',(24,36),(32,42),(28,40)),('L',(12,24)),('C',(6,12),(8,20),(6,16))]
path('orbit-a',(6,12),commands,True)
mirror=lambda p:(48-p[0],p[1])
mirrored=[]
for kind,end,*args in commands:
 if kind=='A': mirrored.append((kind,mirror(end),args[0],args[1],not args[2]))
 elif kind=='C':mirrored.append((kind,mirror(end),mirror(args[0]),mirror(args[1])))
 else:mirrored.append((kind,mirror(end)))
path('orbit-b',mirror((6,12)),mirrored,True)
self.add_dot('nucleus',(24,24));join('orbit-a','orbit-b')
''')
design('bag','SQUARE','Soft everyday tote','handbag','A wide softly rounded tote with a broad arch handle. The square silhouette and generous lower radii distinguish it from the tall carriers.', '''
path('handle',(16,18),[('L',(16,14)),('A',(32,14),8,8,True),('L',(32,18))])
path('body',(10,18),[('L',(16,18)),('L',(32,18)),('L',(38,18)),('C',(42,30),(40,22),(42,26)),('C',(30,42),(42,39),(38,42)),('L',(18,42)),('C',(6,30),(10,42),(6,39)),('C',(10,18),(6,26),(8,22))],True)
join('handle','body')
''')
design('bag-1e030fe3','VRECT_L','Paper carrier · inset handle','shopping-bag','A paper carrier with sloped folded shoulders and an inset U-shaped handle. Tall rectangular bounds retain shopping-bag proportions while changing its construction.', '''
poly('body',(8,14),(16,4),(32,4),(40,14),(40,44),(8,44),closed=True)
line('fold',(8,14),(40,14));join('fold','body')
path('handle',(17,24),[('A',(31,24),7,7,False)])
''')
design('bag-44d13a4d','HRECT_L','Wide barrel handbag','handbag','A low wide handbag has a tall squared arch handle and a rounded barrel-shaped body. HRECT bounds distinguish its horizontal proportions.', '''
path('handle',(16,20),[('L',(16,12)),('A',(20,8),4,4,True),('L',(28,8)),('A',(32,12),4,4,True),('L',(32,20))])
path('body',(10,20),[('L',(16,20)),('L',(32,20)),('L',(38,20)),('C',(44,30),(42,20),(44,25)),('C',(34,40),(44,37),(40,40)),('L',(14,40)),('C',(4,30),(8,40),(4,37)),('C',(10,20),(4,25),(6,20))],True)
join('body','handle')
''')
design('bag-bf5296da','VRECT_L','Long-handle shopper','handbag','A tall narrow handle and broad tapered base create a long-handle shopper. Shared axis and square base corners keep a distinct silhouette.', '''
path('handle',(18,24),[('L',(18,10)),('A',(30,10),6,6,True),('L',(30,24))])
poly('body',(12,24),(18,24),(30,24),(36,24),(40,44),(8,44),closed=True)
join('body','handle')
''')
design('bag-d97bc915','VRECT_L','Structured gusset tote','paper-bag','A tall box-shaped tote has an angular handle and one functional side gusset. The side panel is intentionally asymmetric, eight units wide, rather than decorative variation.', '''
poly('handle',(16,16),(16,4),(28,4),(28,16))
poly('body',(8,16),(16,16),(28,16),(32,16),(40,24),(40,44),(32,44),(8,44),closed=True)
line('gusset',(32,16),(32,44));join('gusset','body');join('handle','body')
''')
design('bag-e213494f','VRECT_L','Rounded bucket bag','handbag','A bucket-shaped bag has a broad rounded bottom and a low circular handle. The continuous bowl-shaped base contrasts with the straight-bottom totes.', '''
path('handle',(16,16),[('L',(16,12)),('A',(32,12),8,8,True),('L',(32,16))])
path('body',(8,16),[('L',(16,16)),('L',(32,16)),('L',(40,16)),('L',(38,32)),('C',(24,44),(37,40),(30,44)),('C',(10,32),(18,44),(11,40)),('L',(8,16))],True)
join('handle','body')
''')
design('bag-photography','HRECT_L','Camera satchel · full flap','briefcase-business','A wide camera satchel has a short carry handle and a broad curved protective flap. The flap is structural and the lower compartment retains ample space.', '''
poly('handle',(16,16),(16,8),(32,8),(32,16))
path('body',(8,16),[('L',(16,16)),('L',(32,16)),('L',(40,16)),('A',(44,20),4,4,True),('L',(44,24)),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,24)),('L',(4,20)),('A',(8,16),4,4,True)],True)
path('flap',(4,24),[('C',(24,30),(10,28),(17,30)),('C',(44,24),(31,30),(38,28))])
join('handle','body');join('flap','body')
''')
design('bag-shopping','VRECT_L','Folded grocery sack','paper-bag','A folded paper grocery sack uses a rolled upper flap and a side gusset instead of an external loop handle. Intentional perspective distinguishes this bag variant.', '''
poly('flap',(12,4),(34,4),(40,12),(20,12),(12,4))
path('body',(12,4),[('L',(8,20)),('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,24)),('L',(36,12))])
poly('gusset',(12,4),(16,20),(16,44))
join('flap','body');join('gusset','flap');join('gusset','body')
''')
design('ball-with-lines','CIRCLE','Mirrored football panels',None,'A true circular ball owns a six-sided central panel and six radial seams. The geometry is derived from shared axes so both horizontal and vertical reflections match exactly; no unequal lower panels.', '''
axis=24
ring=[(24,4),(40,12),(44,24),(40,36),(24,44),(8,36),(4,24),(8,12)]
path('outline',ring[0],[('A',p,20,20,True) for p in ring[1:]+ring[:1]],True)
# One upper-right panel quadrant owns all paired vertices.
panel=[(axis,12),(34,18),(34,30),(axis,36),(14,30),(14,18)]
poly('panel',*panel,closed=True)
ends=[(24,4),(40,12),(40,36),(24,44),(8,36),(8,12)]
for j,(a,b) in enumerate(zip(panel,ends)):
 line(f'seam-{j}',a,b);join(f'seam-{j}','panel');join(f'seam-{j}','outline')
''')

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
     if isinstance(t,ast.Name) and t.id=='keywords':n.value=ast.Tuple([ast.Constant('solo-ai-refine'),ast.Constant('solo-ai-first50'),ast.Constant(name)],ast.Load())
  cls.body=[n for n in cls.body if not isinstance(n,ast.FunctionDef)]
  header=f'    def build(self):\n        # Plan: {plan}\n        # Reference: '+(f'Lucide {ref}: original and atomic-debug geometry.' if ref else 'Original football; exact mirrored panel construction.')+'\n'
  func=header+HELPERS+textwrap.indent(body.strip(),'        ')+'\n';cls.body.append(ast.parse(textwrap.dedent(func)).body[0]);ast.fix_missing_locations(tree)
  rendered=ast.unparse(tree);rendered=rendered[:rendered.index('    def build(')]+func
  p.write_text(f'"""{name}: {label}; earlier revisions preserved."""\n'+rendered)
  out.append(dict(parent=name,previous=parent,icon_id=new,path=str(p.relative_to(ROOT)),keyshape=key,label=label,reference=ref,plan=plan))
 (WORK/'batch.json').write_text(json.dumps(out,indent=2));print('Authored',len(out))
if __name__=='__main__':main()
