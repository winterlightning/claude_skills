from pathlib import Path
import sys,ast,json,runpy,textwrap
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons.registry import factories
AUTHOR='gpt-6';SOURCE_ICON_ID=None;SOURCE_PATH='icon_set/work/solo-ai-full-set/batch.json'
w=Path(__file__).parent
HELPERS=runpy.run_path(str(ROOT/'icon_set/work/solo-ai-first50/author_batch.py'))['HELPERS']
D={}
D['arrange-number']=('VRECT_L','Equal-height numerals','Both numerals share a 16-unit centerline height and 4-unit stroke; keep a rounded 9 with clear spacing.',"""
line('arrow',(13,10),(13,35));path('head',(8,29),[('L',(13,35)),('L',(18,29))]);join('arrow','head')
# Both digits use a shared 16-unit cap height and the same stroke.
digit_height = 16
one_top, nine_bottom = 4, 44
nine_top = nine_bottom - digit_height
poly('one', (32, 7), (36, one_top), (36, one_top + digit_height))
circle('nine-bowl', 36, nine_top + 4, 4)
path('nine-stem', (40, nine_top + 4), [('L', (40, 42)), ('C', (38, nine_bottom), (40, 43), (39, nine_bottom))])
join('nine-bowl', 'nine-stem')
""")
for name,side in [('arrow-circle-bottom-4','down'),('arrow-circle-left-4','left')]:
 D[name]=('SQUARE','Open ring with clear arrow spacing','Lucide circle-arrow-down: coherent circular arcs and a mirrored arrowhead. Keep the attached shaft; the free ring end is ten centerline units from it, and the tip is ten units from the opposite rim.',f"""
def pt(x,y):return (48-y,x) if '{side}'=='left' else (x,y)
path('ring',pt(24,6),[('A',pt(6,24),18,18,False),('A',pt(24,42),18,18,False),('A',pt(42,24),18,18,False),('C',pt(34,9),pt(42,17),pt(39,11))])
line('shaft',pt(24,6),pt(24,32));join('shaft','ring')
path('head',pt(17,25),[('L',pt(24,32)),('L',pt(31,25))]);join('head','shaft')
""")
old={r['parent']:r for r in json.loads((w/'batch.json').read_text())} if (w/'batch.json').exists() else {}
latest={r['parent']:r for r in json.loads((ROOT/SOURCE_PATH).read_text())};reg=factories();out=[]
for n,(key,label,plan,body) in D.items():
 prev=old[n]['previous'] if n in old else latest[n]['icon_id']
 if n in old:p=ROOT/old[n]['path'];new=old[n]['icon_id'];tree=ast.parse(p.read_text())
 else:
  dest,new,src=prepare_variant(prev,'solo',label);mod=sys.modules[reg[prev].__module__];p=dest.with_name(dest.stem+'_'+mod.SOURCE_ICON_ID.replace('-','_')+'.py');tree=ast.parse(src)
 for node in tree.body:
  if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUTHOR' for t in node.targets):node.value=ast.Constant(AUTHOR)
 cls=next(n for n in tree.body if isinstance(n,ast.ClassDef));cls.body=[x for x in cls.body if not isinstance(x,ast.FunctionDef)]
 for node in cls.body:
  if isinstance(node,ast.Assign):
   for t in node.targets:
    if isinstance(t,ast.Name) and t.id=='keyshape':node.value=ast.Attribute(ast.Name('Keyshape',ast.Load()),key,ast.Load())
 func='    def build(self):\n        # Plan: '+plan+'\n'+HELPERS+textwrap.indent(textwrap.dedent(body).strip(),'        ')+'\n';cls.body.append(ast.parse(textwrap.dedent(func)).body[0]);ast.fix_missing_locations(tree)
 s=ast.unparse(tree);s=s[:s.index('    def build(')]+func;p.write_text(s)
 out.append(dict(parent=n,previous=prev,icon_id=new,path=str(p.relative_to(ROOT)),keyshape=key,label=label,plan=plan))
(w/'batch.json').write_text(json.dumps(out,indent=2))
print('Authored',len(out))
