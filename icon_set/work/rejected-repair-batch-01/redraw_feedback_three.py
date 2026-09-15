"""Redraw the three user-rejected batch candidates; preserve earlier candidates."""
import ast,json,textwrap,shutil
from pathlib import Path
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/rejected-repair-batch-01/batch.json'
AUTHOR='gpt-6'
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2]
rows=json.loads((OUT/'batch.json').read_text())
HELPERS=ast.literal_eval(next(a.value for a in ast.parse((OUT/'refine_centerlines.py').read_text()).body if isinstance(a,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='HELPERS' for t in a.targets)))
D={
4:('VRECT_L','Rebuild the ant with a continuous head, thorax and rounded abdomen, six paired legs, and short antennae; remove the stick-figure proportions.',"""
# Three body regions share a vertical axis. Six legs attach in three equally spaced rows.
path('body',(20,8),[('A',(24,4),4,4,True),('A',(28,8),4,4,True),('L',(28,12)),('C',(32,20),(28,16),(32,16)),('L',(32,28)),('L',(32,36)),('A',(24,44),8,8,True),('A',(16,36),8,8,True),('L',(16,28)),('L',(16,20)),('C',(20,12),(16,16),(20,16)),('L',(20,8))],True)
line('abdomen-joint',(16,28),(32,28));join('abdomen-joint','body')
for side in (-1,1):
 x=lambda d:24+side*d
 for k,y,tip_y in [('front',20,12),('middle',28,28),('rear',36,44)]:
  line(f'{k}-leg-{side}',(x(8),y),(x(16),tip_y));join(f'{k}-leg-{side}','body')
 line(f'antenna-{side}',(x(4),8),(x(10),4));join(f'antenna-{side}','body')
"""),
33:('SQUARE','Restore an upward-pointing cannon barrel seated directly on a broad wheeled carriage, with a compact breech and clear muzzle.',"""
# Broad inclined tube, one wheel in front, and a low block carriage behind it.
path('barrel',(16,28),[('L',(6,20)),('L',(38,6)),('L',(42,16)),('L',(32,28))])
circle('wheel',24,32,10);join('barrel','wheel')
poly('carriage',(14,32),(6,40),(6,42),(24,42));join('carriage','wheel')
dot('hub',(24,32))
"""),
42:('SQUARE','Rebuild the aircraft around one diagonal fuselage with mirrored swept wings and tailplanes, replacing the uneven zigzag silhouette.',"""
# Mirror corresponding wings about y=48-x; the rounded nose points northeast.
path('plane',(36,6),[('C',(42,12),(40,6),(42,8)),('L',(32,22)),('L',(32,38)),('L',(24,42)),('L',(22,30)),('L',(16,36)),('L',(16,42)),('L',(6,42)),('L',(6,32)),('L',(12,32)),('L',(18,26)),('L',(6,24)),('L',(10,16)),('L',(26,16)),('L',(36,6))],True)
""")}
D[4]=('VRECT_L','Give the ant a larger round head, a compact waist, and a broad tapered abdomen; angle the two leg pairs outward, following the four-leg reduction in the supplied reference.',"""
circle('head',24,10,6)
path('abdomen',(20,24),[('L',(24,24)),('L',(28,24)),('A',(32,28),4,4,True),('L',(32,36)),('A',(24,44),8,8,True),('A',(16,36),8,8,True),('L',(16,28)),('A',(20,24),4,4,True)],True)
line('waist',(24,16),(24,24));join('waist','head');join('waist','abdomen')
for side in (-1,1):
 x=lambda d:24+side*d
 line(f'antenna-{side}',(x(6),10),(x(16),4));join(f'antenna-{side}','head')
 line(f'front-leg-{side}',(x(8),28),(x(16),20));join(f'front-leg-{side}','abdomen')
 line(f'rear-leg-{side}',(x(8),36),(x(16),44));join(f'rear-leg-{side}','abdomen')
""")
D[33]=('SQUARE','Round the cannon breech and tilt the barrel upward from a compact wheeled carriage. The wheel meets the barrel at exact shared points, removing the detached support assembly.',"""
path('barrel',(16,26),[('C',(6,20),(10,26),(6,26)),('C',(12,12),(6,16),(8,14)),('L',(38,6)),('L',(42,16)),('L',(32,26))])
circle('wheel',24,32,10);join('barrel','wheel')
poly('carriage',(14,32),(6,40),(6,42),(24,42));join('carriage','wheel')
dot('hub',(24,32))
""")
D[42]=('SQUARE','Give the climbing airliner a diagonal fuselage with equal swept wings and tailplanes. Use a rounded nose and consistent body width, preserving the upward flight direction.',"""
# Mirrored about x+y=48. Fuselage edges use x+y=42 and 54 for true diagonal clearance.
path('plane',(34,8),[('C',(38,6),(36,6),(36,6)),('C',(42,10),(40,6),(42,8)),('C',(40,14),(42,12),(42,12)),('L',(34,20)),('L',(42,36)),('L',(36,42)),('L',(24,30)),('L',(18,36)),('L',(20,42)),('L',(12,42)),('L',(6,36)),('L',(6,28)),('L',(12,30)),('L',(18,24)),('L',(6,12)),('L',(12,6)),('L',(28,14)),('L',(34,8))],True)
""")
for n,(key,note,body) in D.items():
 r=rows[n-1];old=ROOT/r['variant_path'];backup=OUT/'previous-candidates'/old.name;backup.parent.mkdir(exist_ok=True)
 if not backup.exists():shutil.copy2(old,backup)
 tree=ast.parse(old.read_text());cls=next(x for x in tree.body if isinstance(x,ast.ClassDef))
 vid=r['icon_id']+'-redraw-v3';dest=OUT/'drafts'/(Path(r['original_model']).stem+'_redraw_v3.py')
 for a in cls.body:
  if isinstance(a,ast.Assign):
   names=[t.id for t in a.targets if isinstance(t,ast.Name)]
   if 'icon_id' in names:a.value=ast.Constant(vid)
   if 'keyshape' in names:a.value=ast.parse('Keyshape.'+key,mode='eval').body
   if 'variant_label' in names:a.value=ast.Constant('Batch 01: user feedback redraw')
 cls.body=[a for a in cls.body if not isinstance(a,ast.FunctionDef) or a.name!='build']
 cls.body.append(ast.parse('def build(self):\n'+textwrap.indent(HELPERS+body,'    ')).body[0]);tree.body[0]=ast.Expr(ast.Constant(note));ast.fix_missing_locations(tree);dest.write_text(ast.unparse(tree)+'\n')
 r.update(variant_id=vid,variant_path=str(dest.relative_to(ROOT)),repair_note=note,feedback_redraw=True)
(OUT/'batch.json').write_text(json.dumps(rows,indent=2));print('Redrew ant, cannon-block-carriage, climbing-airliner.')
