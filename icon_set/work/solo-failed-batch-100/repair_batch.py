from pathlib import Path
import sys,json,ast
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-failed-batch-100/before.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
rows=json.loads((W/'before.json').read_text())
repairs={
6:[("self.add_line('m-leg-0', (28, 31), (28, 20))", "self.add_polyline('m-leg-0', (28, 31), (28, 24), (28, 20))"),("self.add_line('m-leg-1', (36, 31), (36, 20))", "self.add_line('m-leg-1', (36, 24), (36, 20))")],
16:[("self.add_line('low-bead-0', p_25_31, p_31_31)", "self.add_line('low-bead-0', p_25_31, p_28_31)\n        self.add_line('low-bead-0b', p_28_31, p_31_31)"),("'low-bead', 'low-bead-0', 'low-bead-1'", "'low-bead', 'low-bead-0', 'low-bead-0b', 'low-bead-1'")],
17:[("self.add_polyline('support',(10,22),(10,40),(32,40),(32,22))", "self.add_line('support-left',(10,22),(10,40))\n        self.add_polyline('support',(32,40),(32,31),(32,22))\n        self.relate('connect','support-left','left-jaw')\n        self.relate('connect','support-left','base')"),("self.relate('connect','support','left-jaw')", ""),("self.add_line('base',(6,40),(38,40))", "self.add_polyline('base',(6,40),(10,40),(32,40),(38,40))")],
18:[("P('walls', (36, 16), (36, 36), (12, 36), (12, 16))", "L('wall-right', (36,16), (36,36))\n        L('walls', (12,36), (12,16))\n        J('wall-right','arch')\n        J('wall-right','base')"),("P('base', (8, 36), (40, 36), (40, 44), (8, 44), closed=True)","P('base', (8,36), (12,36), (36,36), (40,36), (40,44), (8,44), closed=True)")],
24:[("('L',(34,8))","('L',(26,8)),('L',(34,8))"),("('L',(8,40))],True)","('L',(30,40)),('L',(8,40))],True)")],
28:[("poly('building',(12,44),(12,10),(36,24),(36,44),(28,44),(20,44),(12,44))", "poly('building',(12,44),(12,10),(36,24),(36,44))"),("join('door','building')", "join('door','ground')"),("poly('ground',(8,44),(12,44),(36,44),(40,44))", "poly('ground',(8,44),(12,44),(20,44),(28,44),(36,44),(40,44))")],
31:[("(22, 42), (29, 42), (33, 28)", "(22, 42))\n        self.add_polyline('right-butte', (29,42), (33, 28)"),("self.add_line('ground', (6, 42), (42, 42))", "self.add_polyline('ground', (6,42), (22,42), (29,42), (42,42))\n        self.relate('connect','right-butte','ground')")],
42:[("self.add_polyline('grip',(14,22),(10,32),(22,32),(26,22))", "self.add_line('grip',(14,22),(10,32))\n        self.add_line('grip-right',(22,32),(26,22))\n        self.relate('connect','grip-right','motor')\n        self.relate('connect','grip-right','battery')")],
54:[("(33,4),(36,16),(12,16))", "(33,4),(36,16))")],
73:[("(30,12),(36,20),(10,20))", "(30,12),(36,20))")],
75:[("circle('reel',20,24,16)", "arc('reel-upper-left',(20,40),(4,24),16)\n        arc('reel-upper-right',(4,24),(20,8),16)\n        arc('reel-bottom-right',(20,8),(36,24),16)\n        arc('reel-bottom-left',(36,24),(20,40),16)\n        self.add_contour('reel','reel-upper-left','reel-upper-right','reel-bottom-right','reel-bottom-left',closed=True)")],
85:[("a('fork-bottom',(6,18),(22,18),8,sweep=False)", "a('fork-bottom-left',(6,18),(14,26),8,sweep=False)\n        a('fork-bottom-right',(14,26),(22,18),8,sweep=False)"),("'fork-left','fork-bottom','fork-right'", "'fork-left','fork-bottom-left','fork-bottom-right','fork-right'")],
93:[("self.add_arc('finger-curl',(34,14),(34,30),radius_x=8)", "self.add_arc('finger-curl',(34,14),(42,22),radius_x=8)\n        self.add_arc('finger-curl-lower',(42,22),(34,30),radius_x=8)"),("'finger-inner','finger-curl','finger-return'", "'finger-inner','finger-curl','finger-curl-lower','finger-return'"),("self.add_line('hand-outside',(42,18),(42,42))", "self.add_polyline('hand-outside',(42,18),(42,22),(42,42))"),("self.add_contour('back','finger-tip-top','knuckle','hand-outside')", "self.add_contour('back','finger-tip-top','knuckle','hand-outside-1','hand-outside-2')")]
}
# Both fork models use the same geometry vocabulary.
r86=Path(rows[85]['file']).read_text()
print('fork86 deferred different source layout')
results=[]
for number,replacements in repairs.items():
 row=rows[number-1]; source=Path(row['file']).read_text()
 for old,new in replacements:
  if old not in source:raise ValueError((number,old))
  source=source.replace(old,new)
 dest,newid,text=prepare_variant(row['id'],'solo','Shared ink reconstruction')
 tree=ast.parse(text); edited=ast.parse(source)
 ec=next(n for n in edited.body if isinstance(n,ast.ClassDef))
 tc=next(n for n in tree.body if isinstance(n,ast.ClassDef))
 build=next(n for n in ec.body if isinstance(n,ast.FunctionDef) and n.name=='build')
 build.body.insert(0,ast.Expr(value=ast.Constant('Centerline review: preserve the silhouette; remove duplicated ink and split real attachments into shared nodes.')))
 tc.body=[build if isinstance(n,ast.FunctionDef) and n.name=='build' else n for n in tc.body]
 for n in tree.body:
  if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUTHOR' for t in n.targets):n.value=ast.Constant(AUTHOR)
 ast.fix_missing_locations(tree)
 # Retain supplied reference UUID in every new module filename.
 metadata={t.id:n.value.value for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.value,ast.Constant) for t in n.targets if isinstance(t,ast.Name)}
 dest=dest.with_name(dest.stem+'_'+metadata['SOURCE_ICON_ID'].replace('-','_')+'.py')
 dest.write_text(ast.unparse(tree)+'\n')
 results.append(dict(number=number,parent=row['id'],icon_id=newid,file=str(dest.relative_to(ROOT))))
(W/'repairs.json').write_text(json.dumps(results,indent=2))
print('Created',len(results),'independent variants')
