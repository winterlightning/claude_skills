"""Individual visual repairs for the first 100-icon review. Each variant retains its source ID."""
import ast,json,textwrap
from pathlib import Path
from icon_set.scripts.create_variant import prepare_variant
SOURCE_ICON_ID = None  # Per-icon IDs are preserved in batch.json and each authored module.
SOURCE_PATH = 'icon_set/work/rejected-repair-batch-01/batch.json'
AUTHOR = 'gpt-6'
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
rows=json.loads((OUT/'batch.json').read_text())
HELPERS='''
def path(n, start, commands, closed=False):
    here=start; members=[]
    for j,(kind,end,*args) in enumerate(commands):
        name=f'{n}-{j}'
        if kind=='L': self.add_line(name,here,end)
        elif kind=='A': self.add_arc(name,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
        elif kind=='C': self.add_bezier(name,here,(args[0],args[1],end))
        here=end;members.append(name)
    self.add_contour(n,*members,closed=closed)
def circle(n,x,y,r):
    path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
line=self.add_line
poly=self.add_polyline
dot=self.add_dot
join=lambda a,b:self.relate('connect',a,b)
'''
# index: keyshape, diagnosis, Lucide reference (if useful), build body
D={
2:('SQUARE','Restore a round watch dial; angle the paired straps to preserve readable proportions.','watch', '''
# Plan: circular dial, opposed diagonal straps, and one joined hand stroke.
circle('dial',24,24,12)
poly('upper-strap',(12,24),(6,12),(12,6),(24,12))
poly('lower-strap',(36,24),(42,36),(36,42),(24,36))
join('upper-strap','dial');join('lower-strap','dial')
poly('hands',(24,21),(24,24),(27,26))
'''),
14:('VRECT_L','Give the feeding teat a clear, taller profile and a consistent collar band.','milk', '''
# Plan: symmetric bottle body, collar with 8-unit band, curved nipple.
path('body',(8,20),[('L',(8,36)),('A',(16,44),8,8,False),('L',(32,44)),('A',(40,36),8,8,False),('L',(40,20))])
line('collar',(8,20),(40,20))
join('body','collar')
path('teat',(8,20),[('L',(8,12)),('L',(16,12)),('L',(16,8)),('A',(24,4),8,4,True),('A',(32,8),8,4,True),('L',(32,12)),('L',(40,12)),('L',(40,20))])
join('teat','body')
join('teat','collar')
'''),
15:('SQUARE','Restore a clear beak and eye; smooth the head, belly, and raised tail.','bird', '''
# Plan: one chick silhouette with shared head/beak node, one eye and one wing.
path('chick',(6,22),[('L',(12,16)),('A',(24,6),12,10,True),('A',(36,18),12,12,True),('L',(42,18)),('L',(42,26)),('A',(26,42),16,16,True),('L',(22,42)),('A',(6,26),16,16,True),('L',(6,22))],True)
dot('eye',(23,17))
path('wing',(22,28),[('A',(29,32),7,4,False)])
'''),
19:('SQUARE','Replace the rectangular insect with a curved beetle body and distinct legs.','bug', '''
# Plan: open shell spiral enclosing one oval beetle with two paired leg rows.
path('shell',(24,6),[('A',(42,24),18,18,True),('A',(24,42),18,18,True),('A',(6,24),18,18,True)])
path('beetle',(20,19),[('A',(28,19),4,4,True),('L',(28,29)),('A',(20,29),4,4,True),('L',(20,19))],True)
for side,x,ex in [('left',20,16),('right',28,31)]:
    for y in (19,29):
        line(f'{side}-leg-{y}',(x,y),(ex,y));join(f'{side}-leg-{y}','beetle')
line('antenna-left',(20,19),(17,12));line('antenna-right',(28,19),(28,16))
join('antenna-left','beetle');join('antenna-right','beetle')
'''),
20:('VRECT_L','Restore the rounded bell dome with a centered finial and a broad plinth.','bell', '''
# Plan: round bell dome, central finial, broad attached base.
path('dome',(8,36),[('L',(8,28)),('A',(24,12),16,16,True),('A',(40,28),16,16,True),('L',(40,36))])
line('finial',(24,4),(24,12));join('finial','dome')
# Finial is a continuous addition meeting the dome only at its apex node.
poly('base',(8,36),(8,44),(40,44),(40,36),(8,36))
join('dome','base')
'''),
21:('VRECT_L','Add the missing top finial and give the bell a balanced upright silhouette.','bell', '''
# Plan: symmetric dome with continuous sides, top finial and shared rim endpoints.
path('dome',(8,44),[('L',(8,28)),('A',(24,12),16,16,True),('A',(40,28),16,16,True),('L',(40,44))])
line('rim',(8,44),(40,44));join('rim','dome')
line('finial',(24,4),(24,12));join('finial','dome')
'''),
31:('SQUARE','Give the buffalo broader curved horns and a tapered muzzle instead of a flat forehead.','', '''
# Plan: paired sweeping horns share the cheek nodes; smooth tapered face and eyes.
path('face',(12,18),[('C',(18,39),(10,26),(12,35)),('A',(30,39),6,3,False),('C',(36,18),(36,35),(38,26))])
path('horns',(6,6),[('C',(12,18),(6,15),(8,18)),('C',(24,14),(16,18),(18,14)),('C',(36,18),(30,14),(32,18)),('C',(42,6),(40,18),(42,15))])
join('face','horns')
dot('left-eye',(20,24));dot('right-eye',(28,24));line('muzzle',(23,32),(25,32))
'''),
32:('HRECT_L','Add the missing lens and replace segmented corners with four matching arcs.','camera', '''
# Plan: symmetric camera outline with raised prism, radius-4 corners, centered lens.
path('camera',(18,8),[('L',(30,8)),('L',(34,14)),('L',(40,14)),('A',(44,18),4,4,True),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,18)),('A',(8,14),4,4,True),('L',(14,14)),('L',(18,8))],True)
circle('lens',24,26,5)
'''),
34:('HRECT_L','Replace the front-facing windshield with a recognizable asymmetric side profile.','car', '''
# Plan: side-facing roof and hood, two equal wheels sharing the body baseline.
path('body',(12,28),[('L',(4,28)),('L',(4,20)),('L',(12,8)),('L',(24,8)),('L',(32,20)),('L',(40,20)),('A',(44,24),4,4,True),('L',(44,28)),('L',(36,28))])
circle('rear-wheel',12,34,6);circle('front-wheel',36,34,6)
line('sill',(18,34),(30,34));join('sill','rear-wheel');join('sill','front-wheel');join('body','rear-wheel');join('body','front-wheel')
line('window-base',(4,20),(32,20));join('window-base','body')
'''),
37:('VRECT_L','Make the toe pads read as a paw instead of a two-eyed face.','paw-print', '''
# Plan: three rounded toes and a broad paw pad; preserve the open leg sides.
path('outline',(8,44),[('L',(8,18)),('A',(16,10),8,8,True),('A',(24,4),8,6,True),('A',(32,10),8,6,True),('A',(40,18),8,8,True),('L',(40,44))])
for x,y in [(17,21),(24,15),(31,21)]:dot(f'toe-{x}',(x,y))
path('pad',(17,37),[('A',(24,31),7,6,True),('A',(31,37),7,6,True),('A',(24,41),7,4,True),('A',(17,37),7,4,True)],True)
'''),
41:('SQUARE','Replace the arrow-like valve with a rounded scallop fan and radiating ribs.','', '''
# Plan: fan-shaped clam, wide curved crown, narrow hinge, paired radiating ribs.
path('shell',(18,42),[('L',(8,26)),('C',(6,18),(6,23),(6,21)),('C',(24,6),(6,10),(15,6)),('C',(42,18),(33,6),(42,10)),('C',(40,26),(42,21),(42,23)),('L',(30,42)),('L',(18,42))],True)
poly('rib-left',(16,18),(24,32),(32,18))
line('rib-center',(24,15),(24,32));join('rib-center','rib-left')
'''),
45:('VRECT_L','Widen the cobra hood and taper the neck so it no longer reads as a skull.','', '''
# Plan: cobra hood owns mirrored shoulders, narrow neck, paired eyes, and mouth.
path('hood',(24,4),[('C',(40,20),(36,4),(40,10)),('C',(30,34),(40,28),(32,30)),('L',(30,44)),('L',(18,44)),('L',(18,34)),('C',(8,20),(16,30),(8,28)),('C',(24,4),(8,10),(12,4))],True)
dot('eye-left',(19,16));dot('eye-right',(29,16));poly('mouth',(21,25),(24,28),(27,25))
'''),
55:('SQUARE','Give the eagle a centered, recognizable hooked beak and cleaner feather tips.','bird', '''
# Plan: symmetrical eagle head, paired angular brow runs, and a separate hooked beak.
path('head',(6,24),[('A',(24,6),18,18,True),('A',(42,24),18,18,True),('L',(42,38)),('L',(32,36)),('L',(24,42)),('L',(16,36)),('L',(6,38)),('L',(6,24))],True)
poly('brow-left',(15,20),(24,24),(33,20))
path('beak',(24,24),[('L',(27,28)),('A',(24,31),3,3,True)])
join('brow-left','beak')
'''),
60:('VRECT_L','Curve the flamingo neck and turn down the beak; preserve the bent standing pose.','bird', '''
# Plan: oval body, continuous curved neck and beak, one vertical and one bent leg.
path('body',(8,29),[('A',(19,24),11,5,True),('A',(30,29),11,5,True),('A',(19,34),11,5,True),('A',(8,29),11,5,True)],True)
path('neck',(30,29),[('L',(30,16)),('C',(34,4),(30,10),(28,4)),('A',(40,10),6,6,True),('L',(40,13))])
join('body','neck')
line('leg',(19,34),(19,44));poly('bent-leg',(19,34),(8,42))
join('body','leg');join('body','bent-leg')
'''),
64:('SQUARE','Give the giraffe a clearer muzzle and eye while preserving its long neck and ear.','', '''
# Plan: open neck, rounded muzzle and forehead, a short horn and one ear.
path('outline',(6,42),[('L',(14,18)),('L',(18,14)),('L',(18,6)),('L',(26,6)),('L',(26,14)),('L',(34,14)),('L',(42,26)),('L',(42,34)),('L',(26,34)),('L',(18,42))])
poly('ear',(14,18),(6,10),(6,6));join('ear','outline')
dot('eye',(26,24))
'''),
67:('SQUARE','Add visible blade teeth and rebalance the guard and handle so the tool reads as a circular saw.','', '''
# Plan: circular upper guard with shared shoe nodes, handle, toothed exposed lower blade.
path('guard',(10,26),[('A',(26,16),16,10,True),('A',(42,26),16,10,True)])
poly('shoe',(6,26),(10,26),(14,26),(26,26),(38,26),(42,26));join('guard','shoe')
poly('handle',(10,26),(6,18),(6,6),(26,6),(26,16));join('handle','guard');join('handle','shoe')
poly('blade',(38,26),(38,34),(34,34),(34,39),(28,37),(26,42),(22,38),(16,38),(16,34),(14,34),(14,26))
join('blade','shoe')
'''),
73:('SQUARE','Refine the horse’s ear, muzzle, and chest so the head reads less like a single horn.','', '''
# Plan: continuous horse profile with raised ear, muzzle and squared hooves.
path('horse',(6,42),[('L',(6,30)),('A',(16,20),10,10,True),('L',(24,20)),('A',(30,14),6,6,False),('L',(30,6)),('L',(36,12)),('L',(42,18)),('L',(42,26)),('L',(34,23)),('L',(34,32)),('A',(32,34),2,2,True),('L',(32,42)),('L',(24,42)),('L',(24,32)),('L',(14,32)),('L',(14,42)),('L',(6,42))],True)
'''),
75:('HRECT_L','Rebuild the glue gun with a clear nozzle, grip, rear glue stick, and glue trail.','drill', '''
# Plan: sloped gun body and grip share one outline; nozzle and glue stick attach.
poly('gun',(10,16),(18,8),(32,8),(36,16),(32,24),(36,36),(26,36),(22,24),(10,24),(4,20),closed=True)
# No internal nozzle divider: the nozzle belongs to the body outline.
line('glue-stick',(36,16),(44,16));join('glue-stick','gun')
path('glue',(4,38),[('A',(12,38),4,2,False),('L',(17,38))])
'''),
84:('SQUARE','Give the intertwined snakes distinct head tips and smoother, balanced opposing curves.','', '''
# Plan: two opposed S curves crossing at a real shared center, tapered head ends.
path('snake-a',(22,12),[('L',(18,6)),('L',(16,6)),('A',(6,14),10,8,False),('C',(24,24),(6,20),(16,22)),('C',(42,34),(32,26),(42,28)),('A',(32,42),10,8,True)])
path('snake-b',(32,6),[('A',(42,14),10,8,True),('C',(24,24),(42,20),(32,22)),('C',(6,34),(16,26),(6,28)),('A',(16,42),10,8,False),('L',(18,42)),('L',(22,36))])
join('snake-a','snake-b')
'''),
89:('HRECT_L','Separate the cutting blade from the support and make its vertical cutting direction clear.','drill', '''
# Plan: rounded housing with hand slot, central support, forward blade and base shoe.
path('body',(14,8),[('L',(30,8)),('A',(36,14),6,6,True),('L',(36,26)),('L',(8,26)),('L',(8,14)),('A',(14,8),6,6,True)],True)
line('handle-slot',(18,17),(26,17))
line('blade',(10,26),(10,40));join('body','blade')
line('support',(28,26),(28,40));join('support','shoe');join('support','body')
line('shoe',(4,40),(38,40));join('blade','shoe');join('support','shoe')
line('cord',(36,18),(44,18));join('cord','body')
'''),
90:('SQUARE','Smooth the dolphin’s back and belly and define its beak, dorsal fin, and tail.','fish', '''
# Plan: one arched swimming profile; the dorsal fin and broad tail belong to the outline; omit the crowded pectoral fold.
path('dolphin',(6,22),[('C',(22,10),(9,13),(14,10)),('L',(29,6)),('L',(28,14)),('C',(38,30),(35,18),(37,24)),('C',(42,42),(39,35),(42,36)),('L',(33,38)),('L',(25,42)),('L',(29,32)),('C',(12,24),(29,28),(20,25)),('L',(6,27)),('L',(6,22))],True)
'''),
100:('SQUARE','Turn the test tube diagonally to preserve a slender tube and a rounded closed end.','', '''
# Plan: diagonal tube with two parallel sides and a radius-8 round base; straight rim.
path('tube',(28,6),[('L',(8,26)),('A',(22,40),10,10,False),('L',(42,20))])
poly('rim',(26,6),(28,6),(42,20),(42,22));join('rim','tube')
line('liquid',(20,14),(34,28));join('liquid','tube')
''')}
D[99]=('VRECT_L','Rebuild the flask with exact mirrored neck and shoulder geometry; remove small curve mismatches.','milk', '''
# Plan: mirrored flask shoulders, paired radius-6 base corners, level liquid surface.
path('flask',(16,4),[('L',(32,4)),('L',(30,8)),('L',(30,18)),('L',(36,30)),('L',(40,38)),('A',(34,44),6,6,True),('L',(14,44)),('A',(8,38),6,6,True),('L',(12,30)),('L',(18,18)),('L',(18,8)),('L',(16,4))],True)
line('liquid',(12,30),(36,30));join('liquid','flask')
''')
for n,(keyshape,note,ref,body) in D.items():
 r=rows[n-1]
 if not r.get('variant_id'):
  dest,vid,text=prepare_variant(r['icon_id'],'solo','Batch 01: visual refinement')
  # Retain the source UUID in every new module filename.
  old=ast.parse((ROOT/r['original_model']).read_text())
  source_id=next((ast.literal_eval(a.value) for a in old.body if isinstance(a,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='SOURCE_ICON_ID' for t in a.targets)),None)
  if source_id:dest=dest.with_name(dest.stem+'_'+source_id.replace('-','_')+'.py')
  dest=OUT/'drafts'/dest.name
  dest.write_text(text)
  r['variant_id']=vid;r['variant_path']=str(dest.relative_to(ROOT))
 dest=ROOT/r['variant_path'];tree=ast.parse(dest.read_text())
 for a in tree.body:
  if isinstance(a,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUTHOR' for t in a.targets):a.value=ast.Constant(AUTHOR)
 cls=next(c for c in tree.body if isinstance(c,ast.ClassDef) and any(isinstance(a,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='icon_id' for t in a.targets) and isinstance(a.value,ast.Constant) and a.value.value==r['variant_id'] for a in c.body))
 for a in cls.body:
  if isinstance(a,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='keyshape' for t in a.targets):a.value=ast.parse('Keyshape.'+keyshape,mode='eval').body
 cls.body=[a for a in cls.body if not isinstance(a,ast.FunctionDef) or a.name!='build']
 cls.body.append(ast.parse('def build(self):\n'+textwrap.indent(HELPERS+body,'    ')).body[0])
 # Replace stale inherited descriptions with this revision's actual intent.
 if isinstance(tree.body[0],ast.Expr) and isinstance(tree.body[0].value,ast.Constant):tree.body.pop(0)
 bounds={'SQUARE':'(6,6)-(42,42)','HRECT_L':'(4,8)-(44,40)','VRECT_L':'(8,4)-(40,44)'}[keyshape]
 desc=note+'\nPlan: '+body.strip().split('\n')[0].removeprefix('# Plan: ')+'\n'+keyshape+' centerline extremes '+bounds+'.\nLucide: '+(ref+'; geometric contour construction adapted to SOLO48.' if ref else 'No useful subject-specific match; supplied original guides the silhouette.')+'\nIndependent variant; original preserved.'
 tree.body.insert(0,ast.Expr(ast.Constant(desc)));ast.fix_missing_locations(tree)
 dest.write_text(ast.unparse(tree)+'\n')
 r.update(repair_note=note,lucide_reference=ref,keyshape=keyshape,action='revised')
(OUT/'batch.json').write_text(json.dumps(rows,indent=2))
print('Authored',len(D),'independent revisions.')
