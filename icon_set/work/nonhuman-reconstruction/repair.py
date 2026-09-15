"""In-place centerline reconstruction, preserving canonical source identities."""
from pathlib import Path
import json,re,textwrap
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/nonhuman-reconstruction/audit.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
A=json.loads((W/'audit.json').read_text())
HELP='''
        # Each path owns a coherent stroke; control points preserve smooth tangents.
        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L': self.add_line(name, here, end)
                elif k == 'A': self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C': self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)
        def circle(n, x, y, r):
            path(n, (x-r,y), [('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True)], True)
        def box(n, l, t, r, b, rad=4):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
'''
def replace(name,shape,plan,body):
 i=next(i for i in A if i['icon_id']==name)
 if i['audit_status'].startswith(('held-', 'blocked-', 'removed-')): return
 p=Path(i['source_path']);old=p.read_text();backup=W/'originals'/p.name;backup.parent.mkdir(exist_ok=True)
 if not backup.exists():backup.write_text(old)
 prefix=old[:old.index('    def build(')]
 prefix=re.sub(r'keyshape = Keyshape\.\w+',f'keyshape = Keyshape.{shape}',prefix)
 prefix=re.sub(r'AUTHOR\s*=.*',"AUTHOR = 'gpt-6'",prefix)
 p.write_text(prefix+'    def build(self):\n        # Plan: '+plan+'\n'+HELP+textwrap.indent(textwrap.dedent(body).strip(),'        ')+'\n')
 i['audit_status']='reconstructed';i['plan']=plan;i['keyshape_repair']=shape
 (W/'audit.json').write_text(json.dumps(A,indent=2))

replace('airchair','VRECT_L','Lucide armchair: shared arched back and two rounded arms; broad eight-unit seat band and aligned legs.', '''
path('seat',(8,20), [('A',(12,16),4,4,True),('A',(16,20),4,4,True),('L',(16,28)),('L',(32,28)),('L',(32,20)),('A',(36,16),4,4,True),('A',(40,20),4,4,True),('L',(40,32)),('A',(36,36),4,4,True),('L',(12,36)),('A',(8,32),4,4,True),('L',(8,20))],True)
path('back',(12,16), [('A',(36,16),12,12,True)])
join('back','seat')
for x in (12,36):
 line(f'leg-{x}',(x,36),(x,44));join(f'leg-{x}','seat')
''')
for name in ('shopping-bag-with-loop-handle','handmade-bag'):
 replace(name,'VRECT_L','Lucide shopping-bag: rounded body and symmetric dome handle joined at the rim; remove cramped dangling handle ends.', '''
path('body',(12,16), [('L',(14,16)),('L',(34,16)),('L',(36,16)),('A',(40,20),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,20)),('A',(12,16),4,4,True)],True)
path('handle',(14,16), [('L',(14,14)),('A',(34,14),10,10,True),('L',(34,16))])
join('body','handle')
''')
replace('battery-charging-vertical','VRECT_L','Lucide battery-charging: broad rounded housing, shared terminal nodes and an open lightning stroke with longer turns.', '''
path('body',(12,14), [('L',(16,14)),('L',(32,14)),('L',(36,14)),('A',(40,18),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,18)),('A',(12,14),4,4,True)],True)
poly('terminal',(16,14),(16,4),(32,4),(32,14));join('terminal','body')
poly('charge',(24,23),(17,29),(31,29),(24,35))
''')
replace('pet-carrier-with-straps','SQUARE','Broad rounded carrier with parallel straps at shared rim/base stations; Lucide bag corner construction.', '''
path('body',(10,18), [('L',(16,18)),('L',(32,18)),('L',(38,18)),('A',(42,22),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(32,42)),('L',(16,42)),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,22)),('A',(10,18),4,4,True)],True)
path('handle',(16,18), [('L',(16,14)),('A',(32,14),8,8,True),('L',(32,18))])
join('handle','body')
for x in (16,32):
 line(f'strap-{x}',(x,18),(x,42));join(f'strap-{x}','body');join(f'strap-{x}','handle')
''')
replace('pencil-cup','VRECT_L','Two upright tools share the cup rim. Equal-width pencil shaft avoids tapered crowding; cup has tangent rounded corners.', '''
path('cup',(8,24), [('L',(18,24)),('L',(30,24)),('L',(40,24)),('L',(40,38)),('A',(34,44),6,6,True),('L',(14,44)),('A',(8,38),6,6,True),('L',(8,24))],True)
poly('pencil',(8,24),(8,12),(13,4),(18,12),(18,24));join('pencil','cup')
poly('ruler',(30,24),(30,4),(40,4),(40,24));join('ruler','cup')
''')
replace('brick-firewall','HRECT_L','Wall owns two eight-unit brick courses and staggered joints. One broad smooth flame replaces cramped short tongues; flame silhouette remains asymmetric.', '''
poly('wall',(4,24),(16,24),(32,24),(44,24),(44,32),(44,40),(24,40),(4,40),(4,32),closed=True)
poly('course',(4,32),(16,32),(24,32),(32,32),(44,32));join('wall','course')
for x in (16,32):
 line(f'upper-{x}',(x,24),(x,32));join(f'upper-{x}','wall');join(f'upper-{x}','course')
line('lower',(24,32),(24,40));join('lower','wall');join('lower','course')
path('flame',(16,24), [('C',(24,8),(8,18),(24,14)),('C',(32,24),(24,15),(42,17))])
join('wall','flame')
''')
replace('restaurant-fork-knife','VRECT_L','Lucide-style table cutlery: equally spaced fork tines and a coherent rounded butter-knife blade; remove the pinched blade taper.', '''
path('fork',(8,4), [('L',(8,16)),('A',(16,24),8,8,False),('A',(24,16),8,8,False),('L',(24,4))])
line('middle',(16,4),(16,24));line('fork-handle',(16,24),(16,44))
join('fork','middle');join('fork','fork-handle');join('middle','fork-handle')
path('blade',(32,8), [('A',(40,8),4,4,True),('L',(40,28)),('L',(32,28)),('L',(32,8))],True)
line('knife-handle',(32,28),(32,44));join('blade','knife-handle')
''')
replace('shopping-cart-large-open-wheels','HRECT_L','Deepen the rounded basket uniformly, preserving two large circular wheels and a shared handle attachment.', '''
path('basket',(4,14), [('L',(36,14)),('L',(44,14)),('L',(44,20)),('A',(40,24),4,4,True),('L',(8,24)),('A',(4,20),4,4,True),('L',(4,14))],True)
line('grip',(36,14),(42,8));join('grip','basket')
for j,x in enumerate((14,34)): circle(f'wheel-{j}',x,36,4)
''')
replace('three-engine-spacecraft','HRECT_L','Symmetric arched cabin, circular window and three equal eight-unit engine openings; replace narrow flared nozzle necks.', '''
path('hull',(12,20), [('A',(36,20),12,12,True),('L',(44,24)),('L',(44,32)),('L',(36,32)),('L',(28,32)),('L',(20,32)),('L',(12,32)),('L',(4,32)),('L',(4,24)),('L',(12,20))],True)
circle('window',24,20,3)
for j,x in enumerate((8,24,40)):
 poly(f'engine-{j}',(x-4,32),(x-4,40),(x+4,40),(x+4,32));join(f'engine-{j}','hull')
''')
replace('poodle-head','VRECT_L','Lucide dog: long paired ears frame one smooth face; shared ear roots replace narrow overlapping lower contours.', '''
path('face',(16,16), [('A',(32,16),8,12,True),('L',(32,32)),('A',(16,32),8,8,True),('L',(16,16))],True)
path('left-ear',(16,16), [('A',(8,16),4,4,False),('L',(8,40)),('A',(16,40),4,4,False),('L',(16,32))])
path('right-ear',(32,16), [('A',(40,16),4,4,True),('L',(40,40)),('A',(32,40),4,4,True),('L',(32,32))])
join('face','left-ear');join('face','right-ear')
# The source has no facial mark; keep the broad face counter open.
''')
replace('standing-horse','HRECT_L','Horse silhouette retains pointed ear, muzzle, two clear legs and curved tail. Paired leg widths share eight-unit spacing; directional stance remains asymmetric.', '''
poly('horse',(4,18),(12,14),(16,8),(20,20),(36,20),(36,40),(28,40),(28,28),(20,28),(20,40),(12,40),(12,28),(4,24),closed=True)
path('tail',(36,20), [('C',(44,32),(44,20),(44,24))]);join('tail','horse')
''')
# Widen the owning tail junction instead of changing the pinch rule.
i=next(i for i in A if i['icon_id']=='swimming-shark');p=Path(i['source_path']);old=p.read_text();backup=W/'originals'/p.name
if not backup.exists():backup.write_text(old)
s=backup.read_text().replace('(38, 22)','(30, 20)').replace('(38, 30)','(30, 32)')
s=s.replace('        self.add_arc(\'body-1\'', '        # Plan: move both tail roots forward together to open the crescent throat.\n        self.add_arc(\'body-1\'')
p.write_text(s);i['audit_status']='reconstructed';i['plan']='Widen tail throat at both shared roots, preserving the crescent fin and curved body.'
# Broaden the brainstem counter; keep the anatomical lobe structure.
i=next(i for i in A if i['icon_id']=='brain-side-view-with-stem');p=Path(i['source_path']);old=p.read_text();backup=W/'originals'/p.name
if not backup.exists():backup.write_text(old)
s=backup.read_text().replace("arc('right-bottom',(42,26),(32,36),10)", "arc('right-bottom',(42,26),(32,34),10,8)").replace('(32,36),(34,42),(26,42),(22,34)', '(32,34),(32,42),(24,42),(20,34)')
p.write_text(s);i['audit_status']='reconstructed';i['plan']='Broaden stem at its shared lower lobe so the interior neck has genuine clearance.'
(W/'audit.json').write_text(json.dumps(A,indent=2))
replace('three-light-ceiling-fixture','SQUARE','Three pendant shades share equal eight-unit openings and straight cords; align the pair rather than retaining cramped skewed trapezoids.', '''
line('cord',(24,6),(24,12));poly('canopy',(10,12),(24,12),(38,12));join('cord','canopy')
for j,(x,t,b) in enumerate(((10,20,28),(24,34,42),(38,20,28))):
 line(f'cord-{j}',(x,12),(x,t));join(f'cord-{j}','canopy')
 if j==1:join(f'cord-{j}','cord')
 poly(f'shade-{j}',(x-4,t),(x,t),(x+4,t),(x+4,b),(x-4,b),closed=True);join(f'cord-{j}',f'shade-{j}')
''')
replace('pointed-crystal-cluster','VRECT_L','One central crystal and a mirrored pair, with broad parallel side facets and exact shared junctions.', '''
poly('central',(16,44),(16,20),(16,12),(24,4),(32,12),(32,20),(32,44),closed=True)
poly('left',(16,20),(8,12),(8,36),(16,44));poly('right',(32,20),(40,12),(40,36),(32,44))
join('left','central');join('right','central')
''')
replace('hologram-cube-projector','VRECT_L','Increase all cube face heights together, retaining shared perspective junctions; base and projection beams remain detached with clearance.', '''
poly('cube',(14,10),(24,4),(34,10),(34,20),(24,26),(14,20),closed=True)
poly('top-face',(14,10),(24,16),(34,10));join('top-face','cube')
line('edge',(24,16),(24,26));join('edge','cube');join('edge','top-face')
poly('base',(14,34),(34,34),(34,44),(14,44),closed=True)
line('left-beam',(8,26),(8,28));line('right-beam',(40,26),(40,28))
''')
replace('folding-pocket-knife','SQUARE','A single smooth cutting edge bows away from the blade back; both blade roots share the rounded handle rim.', '''
path('handle',(12,30), [('L',(24,30)),('L',(36,30)),('A',(42,36),6,6,True),('A',(36,42),6,6,True),('L',(12,42)),('A',(6,36),6,6,True),('A',(12,30),6,6,True)],True)
path('blade',(36,30), [('L',(12,6)),('C',(24,30),(12,18),(12,22))]);join('blade','handle')
''')
replace('crescent-head-wrench','SQUARE','Broaden the diagonal shaft at its owning neck; retain crescent jaws and the rounded handle end.', '''
path('outline',(22,6), [('A',(38,22),16,16,True),('L',(36,30)),('L',(42,36)),('A',(36,42),6,6,True),('L',(30,36)),('L',(22,38)),('A',(6,22),16,16,True),('L',(6,14)),('L',(14,22)),('L',(22,14)),('L',(14,6)),('L',(22,6))],True)
''')
replace('lever-tap-with-droplet','VRECT_L','A clean single-stroke operating lever replaces the narrow outlined blade; broad tap body and rounded drop retain identity.', '''
poly('body',(8,44),(8,16),(36,16),(36,26),(18,26),(18,44),closed=True)
poly('lever',(8,16),(8,8),(40,4));join('lever','body')
path('drop',(30,40), [('L',(34,35)),('L',(38,40)),('A',(30,40),4,4,True)],True)
''')
replace('suspended-succulent-planter','VRECT_L','Raise the suspension shoulders and rebuild the succulent leaf as two coherent curves; preserve the wide elliptical bowl.', '''
poly('suspension',(8,32),(8,16),(24,4),(40,16),(40,32))
path('pot',(8,32), [('L',(16,32)),('L',(32,32)),('L',(40,32)),('A',(8,32),16,12,True)],True);join('suspension','pot')
path('leaf',(16,32), [('C',(24,20),(16,26),(20,23)),('C',(32,32),(28,23),(32,26))]);join('leaf','pot')
''')
replace('magic-wand','SQUARE','A larger regular five-point head has a broad central counter; the wand joins one exact lower point.', '''
poly('star',(30,6),(34,14),(42,14),(36,20),(38,30),(30,24),(22,30),(24,20),(18,14),(26,14),closed=True)
line('wand',(6,42),(22,30));join('wand','star')
''')
replace('star-fireworks','HRECT_L','Three symmetric open starbursts replace tiny filled star outlines; genuine shared ray centres own the trails.', '''
from itertools import combinations
for j,(x,y) in enumerate(((24,14),(10,30),(38,30))):
 centre=(x,y);ends=[(x-6,y-4),(x+6,y-4),(x-6,y+4),(x+6,y+4),(x,y-6)]
 names=[]
 for k,end in enumerate(ends):
  n=f'burst-{j}-{k}';line(n,centre,end);names.append(n)
 trail=f'trail-{j}';line(trail,centre,(x,40));names.append(trail)
 for a,b in combinations(names,2):join(a,b)
''')
# Shared-node moves: preserve existing smooth noses and improve specific crowded wings.
for name,changes,plan in [
 ('plane', [('(14,33)','(14,34)'),('(18,40)','(20,40)'),('(29,36)','(31,36)')], 'Open the rear fuselage band by moving its lower shared corner; retain the smooth nose and wing curves.'),
 ('airplane-taking-off', [('(24,13)','(28,12)')], 'Move the far-wing root forward along the fuselage and preserve the exact shared attachment.'),
 ('airplane-departing-runway', [('(24,12)','(30,10)'),('(14,6)','(22,6)'),('(18,16)','(18,14)')], 'Move the far wing away from the tailplane while preserving the diagonal body and detached runway.'),
 ('airplane-with-landing-wheel', [('(26,18)','(32,18)'),('(14,6)','(22,6)'),('(37,26),(34,26),(29,26)','(38,26),(29,26)'),('(37,18)','(38,18)'),('(37,26)','(38,26)'),('(34,','(38,'),('radius_x=5,radius_y=4','radius_x=4,radius_y=4')], 'Move the far-wing group forward to open the tail clearance; retain the wheel and its actual strut junction.'),
 ('climbing-airliner', [('(19,21)','(23,19)'),('(29,16)','(33,14)'),('(8,10),(17,8)','(10,8),(24,8)')], 'Rebuild the broad upper wing around two forward attachment nodes, preserving the rounded climbing nose.'),
 ('aircraft-releasing-bomb', [('(16,22),(24,8)','(13,22),(21,8)')], 'Broaden the main wing by moving its paired trailing-edge nodes together; preserve the bomb outline below.')]:
 i=next(i for i in A if i['icon_id']==name);p=Path(i['source_path']);old=p.read_text();backup=W/'originals'/p.name
 if not backup.exists():backup.write_text(old)
 s=backup.read_text()
 for a,b in changes:
  assert a in s,(name,a);s=s.replace(a,b)
 p.write_text(s);i['audit_status']='reconstructed';i['plan']=plan
(W/'audit.json').write_text(json.dumps(A,indent=2))
replace('airplane-diagonal','SQUARE','Lucide plane: widen both wing tips and tail fins coherently; preserve the diagonal fuselage and rounded nose.', '''
path('airframe',(34,6), [('A',(42,14),8,8,True),('L',(34,24)),('L',(42,34)),('L',(34,42)),('L',(26,30)),('L',(20,36)),('L',(22,42)),('L',(12,42)),('L',(12,36)),('L',(6,34)),('L',(6,24)),('L',(14,26)),('L',(20,20)),('L',(6,12)),('L',(12,6)),('L',(26,14)),('L',(34,6))],True)
''')
replace('airplane-other','SQUARE','An upright aircraft constructed about one axis: broaden swept wing bands and the tailplane, with a rounded nose and exact mirrored nodes.', '''
right=[(28,10),(28,12),(42,20),(42,30),(28,22),(28,32),(36,42),(24,42)]
mirror=lambda p:(48-p[0],p[1])
commands=[('L',p) for p in right[1:]]+[('L',mirror(p)) for p in reversed(right[:-1])]+[('A',(28,10),4,4,True)]
path('airframe',right[0],commands,True)
''')
replace('poodle-head','SQUARE','Lucide dog: symmetric long ears frame a broad rounded face with one nose mark. Shared roots and wider ear loops keep the counters open.', '''
path('face',(15,16), [('A',(33,16),9,10,True),('L',(33,31)),('A',(15,31),9,9,True),('L',(15,16))],True)
path('left-ear',(15,16), [('C',(6,16),(15,8),(6,8)),('L',(6,36)),('C',(15,36),(6,44),(15,44)),('L',(15,31))])
path('right-ear',(33,16), [('C',(42,16),(33,8),(42,8)),('L',(42,36)),('C',(33,36),(42,44),(33,44)),('L',(33,31))])
join('face','left-ear');join('face','right-ear');self.add_dot('nose',(24,26))
''')
replace('three-light-ceiling-fixture','HRECT_L','Three broad trapezoidal lamp shades share one canopy and equal cord stations. Stagger heights to separate shades; omit the short top cord.', '''
poly('canopy',(10,8),(24,8),(38,8))
for j,(x,t,b) in enumerate(((10,16,24),(24,32,40),(38,16,24))):
 line(f'cord-{j}',(x,8),(x,t));join(f'cord-{j}','canopy')
 poly(f'shade-{j}',(x-4,t),(x,t),(x+4,t),(x+6,b),(x-6,b),closed=True);join(f'cord-{j}',f'shade-{j}')
''')
replace('shopping-bag-with-loop-handle','VRECT_L','Preserve the tapered shopping bag using coherent curved sides tangent to the rounded base; the dome handle ends exactly at the rim.', '''
path('body',(12,16), [('L',(14,16)),('L',(34,16)),('L',(36,16)),('C',(40,40),(36,24),(40,32)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('C',(12,16),(8,32),(12,24))],True)
path('handle',(14,16), [('L',(14,14)),('A',(34,14),10,10,True),('L',(34,16))]);join('body','handle')
''')
replace('bathrobe-with-tied-belt','VRECT_L','Lucide shirt: balanced shoulders and sleeves, broad wrap panels and tangent rounded hem; belt and tie share one waist node.', '''
path('robe',(14,40), [('L',(14,30)),('L',(14,22)),('L',(12,19)),('L',(8,10)),('L',(18,4)),('L',(30,4)),('L',(40,10)),('L',(36,19)),('L',(34,22)),('L',(34,30)),('L',(34,40)),('A',(30,44),4,4,True),('L',(18,44)),('A',(14,40),4,4,True)],True)
poly('wrap',(18,4),(24,30),(30,4));join('wrap','robe')
poly('belt',(14,30),(24,30),(34,30));join('belt','robe');join('belt','wrap')
line('tie',(24,30),(24,36));join('tie','belt');join('tie','wrap')
''')
replace('damaged-shipping-box','SQUARE','Lucide box: preserve shared perspective corners; represent the torn seam with a broad visible break instead of squeezing a zigzag against the bottom edge.', '''
poly('outline',(24,6),(42,15),(42,33),(24,42),(6,33),(6,15),closed=True)
poly('lid',(6,15),(24,24),(42,15));join('outline','lid')
poly('tear-top',(24,24),(24,28),(28,30));join('tear-top','lid')
line('tear-bottom',(24,38),(24,42));join('tear-bottom','outline')
''')
replace('leaning-tower-of-pisa','SQUARE','One tilted shaft owns parallel floor stations; reduce four cramped storeys to three wider bands while preserving the lean and ground line.', '''
poly('shaft',(19,6),(35,10),(32,22),(30,30),(27,42),(10,42),(14,26),(16,18),closed=True)
line('floor-upper',(16,18),(32,22));line('floor-lower',(14,26),(30,30));join('floor-upper','shaft');join('floor-lower','shaft')
poly('ground',(6,42),(10,42),(27,42),(42,42));join('ground','shaft')
''')
replace('vr-headset-side-view','HRECT_L','Rebuild the visor with shared strap stations and consistent corner radii; widen the rear folded band and preserve the smooth overhead strap.', '''
path('visor',(28,20), [('L',(40,20)),('A',(44,24),4,4,True),('L',(44,36)),('A',(40,40),4,4,True),('L',(28,40)),('A',(24,36),4,4,True),('L',(24,26)),('L',(24,24)),('A',(28,20),4,4,True)],True)
path('head-strap',(8,26), [('A',(24,26),8,18,True)]);join('head-strap','visor')
poly('rear-strap',(24,26),(8,26),(4,32),(4,40),(12,36),(24,36));join('rear-strap','visor');join('rear-strap','head-strap')
''')
for name,changes,plan in [
 ('bathrobe',[('(7,7)','(6,8)'),('(41,7)','(42,8)')],'Lucide shirt construction: align the outer sleeve sides to preserve full clearance to the inner sleeve edges.'),
 ('cushioned-handle-pliers',[('(38,32)','(38,34)')],'Broaden the upper cushioned handle at its outer end, preserving all jaw and pivot nodes.'),
 ('curled-raccoon',[("(6, 19), (12, 25), radius_x=6", "(6, 19), (12, 24), radius_x=6, radius_y=5"),('(12, 25), (22, 25)','(12, 24), (22, 24)')],'Raise the cheek while keeping its smooth quarter-ellipse join, opening space above the curled striped tail.')]:
 i=next(i for i in A if i['icon_id']==name);p=Path(i['source_path']);backup=W/'originals'/p.name
 if not backup.exists():backup.write_text(p.read_text())
 s=backup.read_text()
 for a,b in changes:assert a in s,(name,a);s=s.replace(a,b)
 p.write_text(s);i['audit_status']='reconstructed';i['plan']=plan
(W/'audit.json').write_text(json.dumps(A,indent=2))
replace('bathrobe','SQUARE','Lucide shirt principles: open sleeve ends, a broad V collar and clean waist; curved flared hem preserves the robe silhouette without pinched folds.', '''
path('robe',(16,6), [('L',(6,8)),('L',(6,26)),('L',(14,26)),('L',(14,28)),('C',(10,38),(14,33),(10,35)),('A',(14,42),4,4,False),('L',(34,42)),('A',(38,38),4,4,False),('C',(34,28),(38,35),(34,33)),('L',(34,26)),('L',(42,26)),('L',(42,8)),('L',(32,6)),('L',(16,6))],True)
poly('lapel',(32,6),(24,20),(24,28));line('collar',(16,6),(24,20));join('lapel','robe');join('collar','robe');join('collar','lapel')
poly('belt',(14,28),(24,28),(34,28));join('belt','robe');join('belt','lapel')
line('tie',(24,28),(24,33));join('tie','belt');join('tie','lapel')
''')
# A one-unit shared torso expansion keeps the wrap panels clear through the waist.
i=next(i for i in A if i['icon_id']=='bathrobe-with-tied-belt');p=Path(i['source_path']);s=p.read_text()
for a,b in [('(14,40)','(13,40)'),('(14,30)','(13,30)'),('(14,22)','(13,22)'),('(34,22)','(35,22)'),('(34,30)','(35,30)'),('(34,40)','(35,40)'),('(30,44)','(31,44)'),('(18,44)','(17,44)')]:s=s.replace(a,b)
p.write_text(s)
replace('curled-raccoon','SQUARE','Open the face-to-tail gap, retain a clear eye and coherent circular back, and put two stripes on the broadest parts of the curl.', '''
path('outline',(6,14), [('L',(10,14)),('A',(24,6),14,8,True),('A',(42,24),18,18,True),('A',(24,42),18,18,True),('L',(14,42)),('A',(6,34),8,8,True),('L',(6,32)),('L',(10,32)),('L',(16,34)),('L',(24,34)),('A',(34,24),10,10,False)])
path('face',(6,14), [('L',(6,19)),('A',(12,24),6,5,False),('L',(22,24))]);join('face','outline')
line('ear',(24,6),(24,10));join('ear','outline')
line('stripe-lower',(24,42),(24,34));line('stripe-side',(42,24),(34,24));join('stripe-lower','outline');join('stripe-side','outline')
self.add_dot('eye',(20,15))
''')
# Keep the raccoon's ear visible without crowding the eye.
i=next(i for i in A if i['icon_id']=='curled-raccoon');p=Path(i['source_path']);p.write_text(p.read_text().replace("line('ear',(24,6),(24,10))", "line('ear',(24,6),(24,8))"))
replace('poodle-head','SQUARE','Trace the original poodle haircut: three broad crown puffs above a long face and paired ears. Shared roots preserve the silhouette and open facial counter.', '''
path('hair',(15,20), [('C',(6,18),(10,24),(6,23)),('C',(16,12),(6,12),(10,10)),('C',(24,6),(16,8),(20,6)),('C',(32,12),(28,6),(32,8)),('C',(42,18),(38,10),(42,12)),('C',(33,20),(42,23),(38,24)),('C',(24,22),(30,24),(28,24)),('C',(15,20),(20,24),(18,24))],True)
path('face',(15,20), [('L',(15,33)),('A',(33,33),9,9,False),('L',(33,20))]);join('face','hair')
path('left-ear',(6,18), [('L',(6,36)),('C',(15,36),(6,44),(15,44)),('L',(15,33))]);join('left-ear','hair');join('left-ear','face')
path('right-ear',(42,18), [('L',(42,36)),('C',(33,36),(42,44),(33,44)),('L',(33,33))]);join('right-ear','hair');join('right-ear','face')
self.add_dot('nose',(24,32))
''')
replace('whale-with-spout','SQUARE','Trace the original whale: smooth rounded body, a broad raised tail throat and a separate water spout. Preserve natural directional asymmetry.', '''
path('whale',(6,30), [('C',(16,20),(6,24),(10,20)),('C',(32,24),(24,20),(32,32)),('L',(32,16)),('A',(34,6),12,12,True),('L',(40,11)),('L',(42,6)),('L',(42,19)),('C',(24,42),(42,33),(34,42)),('C',(6,30),(14,42),(6,38))],True)
self.add_dot('eye',(15,30))
path('spout',(8,6), [('C',(16,10),(12,6),(14,7)),('C',(24,6),(18,7),(20,6))])
''')
replace('swimming-dog','HRECT_L','A domed head and smooth rump rise above four equal waves. Deepen the muzzle to provide a full eight-unit opening.', '''
path('head',(12,20), [('A',(28,20),8,12,True)])
poly('muzzle',(12,20),(4,20),(4,28),(14,28));join('muzzle','head')
path('back',(28,20), [('L',(38,20)),('A',(44,26),6,6,True)]);join('back','head')
path('water',(4,36), [('A',(14,36),5,4,False),('A',(24,36),5,4,False),('A',(34,36),5,4,False),('A',(44,36),5,4,False)])
''')
replace('sea-lion','SQUARE','Trace the sitting sea lion with a long neck and broad smooth haunch. Widen both flippers and remove the redundant cramped flipper mark.', '''
path('body',(16,6), [('A',(28,16),12,10,True),('L',(28,22)),('L',(30,22)),('A',(42,34),12,12,True),('L',(42,40)),('A',(40,42),2,2,True),('L',(32,42)),('L',(34,34)),('L',(30,32)),('A',(24,34),12,6,True),('L',(24,42)),('C',(16,38),(20,42),(16,42)),('L',(10,40)),('L',(6,38)),('L',(10,30)),('A',(8,24),14,14,True),('L',(6,18)),('L',(10,16)),('L',(6,14)),('A',(16,6),10,8,True)],True)
self.add_dot('eye',(19,15))
''')
replace('anteater','HRECT_L','Trace the original long downward snout and domed back, replacing the angular ghost-like head; the snout and two legs have shared eight-unit bands.', '''
path('animal',(4,32), [('L',(4,18)),('A',(24,8),20,10,True),('C',(44,30),(40,8),(44,16)),('L',(44,40)),('L',(36,40)),('L',(36,34)),('C',(28,28),(36,30),(32,28)),('L',(28,40)),('L',(20,40)),('L',(20,26)),('C',(12,26),(20,18),(12,18)),('L',(12,32)),('A',(4,32),4,4,True)],True)
''')
replace('dog-carrying-ball','SQUARE','Trace the rounded muzzle and flowing open jaw instead of the angular zigzag; retain the pointed ear and ball at the mouth.', '''
path('head',(42,18), [('C',(40,6),(42,12),(40,8)),('L',(34,14)),('L',(28,14)),('C',(22,24),(24,14),(22,18))])
circle('ball',14,24,8)
path('jaw',(22,24), [('L',(30,24)),('L',(30,30)),('C',(24,38),(30,34),(24,34)),('C',(34,38),(24,42),(30,42)),('L',(42,42))])
join('ball','head');join('ball','jaw');join('head','jaw')
''')
replace('dog-offering-paw','SQUARE','Trace the seated dog and raised paw with a smooth extended foreleg and rounded haunch; broaden the neck and paw counter.', '''
path('dog',(28,20), [('L',(24,6)),('L',(18,12)),('L',(10,14)),('L',(10,24)),('L',(20,24)),('L',(20,32)),('L',(12,32)),('A',(12,40),6,4,False),('L',(20,42)),('C',(38,28),(34,42),(38,34)),('L',(28,20))],True)
path('tail',(38,28), [('A',(42,16),4,12,False)]);join('tail','dog')
''')
replace('dog-wearing-recovery-cone','SQUARE','Trace the rounded muzzle and ear above the recovery cone; preserve one straight shared cone rim and open the full head counter.', '''
poly('cone',(6,28),(14,24),(34,14),(42,10),(36,32),(18,40),closed=True)
path('head',(14,24), [('L',(14,14)),('C',(22,10),(14,12),(18,10)),('L',(22,6)),('C',(34,14),(28,6),(32,10))]);join('head','cone')
line('leg-left',(18,40),(18,42));line('leg-right',(36,32),(42,42));join('leg-left','cone');join('leg-right','cone')
''')
i=next(i for i in A if i['icon_id']=='dog-jumping-through-hoop');p=Path(i['source_path']);backup=W/'originals'/p.name
if not backup.exists():backup.write_text(p.read_text())
s=backup.read_text().replace('(34,34),(26,28)','(34,38),(24,28)');p.write_text(s);i['audit_status']='reconstructed';i['plan']='Widen the forward leg as a complete paired outline, retaining the dog mid-jump through its hoop.'
(W/'audit.json').write_text(json.dumps(A,indent=2))
# Waves retain their rhythm while gaining a unit of clear space below the muzzle.
i=next(i for i in A if i['icon_id']=='swimming-dog');p=Path(i['source_path']);s=p.read_text()
for x in (4,14,24,34,44):s=s.replace(f'({x},36)',f'({x},37)')
s=s.replace(',5,4,False',',5,3,False');p.write_text(s)
replace('grizzly-head-profile','SQUARE','Trace the rounded bear ear, forehead and muzzle; separate the open lips by nine units and rebuild the lower jaw as one smooth contour.', '''
path('head',(6,17), [('L',(10,13)),('L',(8,9)),('C',(12,6),(8,7),(10,6)),('C',(18,11),(15,6),(17,8)),('L',(23,11)),('A',(35,17),13,13,True),('L',(42,22)),('L',(42,26)),('C',(31,30),(42,30),(36,30))])
path('jaw',(31,39), [('C',(15,42),(23,36),(20,40))])
path('neck',(6,17), [('L',(6,29)),('C',(15,42),(6,36),(10,40))]);join('neck','head');join('neck','jaw')
self.add_dot('eye',(28,21))
''')
replace('hyena-head-profile','HRECT_L','Trace a broad rounded upright ear and a smooth muzzle-to-jaw flow, replacing the narrow angular lower-jaw fold; keep the natural profile asymmetry.', '''
path('head',(4,8), [('L',(19,13)),('C',(26,8),(20,10),(24,8)),('C',(29,17),(32,8),(29,13)),('C',(35,25),(32,18),(33,22)),('L',(44,29)),('C',(40,36),(44,32),(43,34)),('C',(22,34),(34,40),(28,32)),('C',(10,40),(18,35),(13,36))])
self.add_dot('eye',(21,24))
''')
i=next(i for i in A if i['icon_id']=='triceratops-head-side');p=Path(i['source_path']);backup=W/'originals'/p.name
if not backup.exists():backup.write_text(p.read_text())
s=backup.read_text().replace("self.add_polyline('beak',(13,40),(6,36),(10,32),(6,30))", "self.add_line('beak',(13,40),(6,36))").replace("(6,30),(9,23)","(6,28),(9,23)").replace("        self.relate('connect','front','beak')", "        # The beak is open: the two lips have genuine clearance.")
p.write_text(s);i['audit_status']='reconstructed';i['plan']='Open the beak at its actual lips instead of retaining a cramped angular notch; keep the horn and frill curves.'
(W/'audit.json').write_text(json.dumps(A,indent=2))
replace('pencil-marking-ballot','SQUARE','Use one straight eight-unit pencil shaft and a centred tip; preserve the two ballot boxes and their cross mark.', '''
poly('empty-box',(6,6),(14,6),(14,14),(6,14),closed=True)
poly('marked-box',(6,22),(26,22),(26,42),(6,42),closed=True)
line('cross-a',(14,30),(18,34));line('cross-b',(14,34),(18,30));join('cross-a','cross-b')
poly('pencil',(34,6),(42,6),(42,18),(38,26),(34,18),closed=True)
''')
replace('pump-action-shotgun','SQUARE','Broaden the pump assembly and expose its two exact attachment nodes on the barrel; preserve the diagonal stock and long muzzle.', '''
poly('gun',(10,42),(6,30),(10,22),(36,6),(42,12),(36,16),(20,27),(16,30),(18,38),closed=True)
poly('pump',(20,27),(28,34),(38,27),(36,16));join('pump','gun')
''')
replace('satellite-with-signal-waves','SQUARE','Mirrored solar panels connect at their nearest corners to a small circular bus; longer rods replace cramped face attachments. Preserve the broadcast arc.', '''
poly('panel-a',(6,12),(12,6),(18,12),(12,18),closed=True)
poly('panel-b',(30,36),(36,30),(42,36),(36,42),closed=True)
path('bus',(24,21), [('A',(24,27),3,3,True),('A',(24,21),3,3,True)],True)
line('strut-a',(18,12),(24,21));line('strut-b',(24,27),(30,36))
join('strut-a','panel-a');join('strut-a','bus');join('strut-b','bus');join('strut-b','panel-b')
path('wave',(6,28), [('A',(20,42),14,14,False)])
''')
replace('text-flow-rows','SQUARE','Three equal rounded text nodes and a clear stepped flow; all links meet explicit nodes, with separated turns and one output arrow.', '''
def node(n,l,t):
 path(n,(l+2,t), [('L',(l+6,t)),('L',(l+10,t)),('A',(l+12,t+2),2,2,True),('L',(l+12,t+4)),('L',(l+12,t+6)),('A',(l+10,t+8),2,2,True),('L',(l+6,t+8)),('L',(l+2,t+8)),('A',(l,t+6),2,2,True),('L',(l,t+4)),('L',(l,t+2)),('A',(l+2,t),2,2,True)],True)
node('first',6,6);node('second',30,6);node('third',6,34)
line('first-link',(18,10),(30,10));join('first-link','first');join('first-link','second')
poly('return-link',(36,14),(36,24),(12,24),(12,34));join('return-link','second');join('return-link','third')
line('output',(18,38),(42,38));poly('arrow',(36,34),(42,38),(36,42));join('output','third');join('output','arrow')
''')
replace('dailybooth-logo','SQUARE','Retain the camera inside its speech bubble. Round the camera body and simplify the tiny lens to a filled mark so the nested counters fit.', '''
path('bubble',(24,6), [('A',(42,24),18,18,True),('C',(40,32),(42,28),(41,30)),('L',(42,42)),('L',(32,40)),('C',(24,42),(30,41),(28,42)),('A',(6,24),18,18,True),('A',(24,6),18,18,True)],True)
box('camera',15,15,33,33,7);self.add_dot('lens',(24,24))
''')
replace('arrow-thick-down-3','SQUARE','Preserve the downward outlined arrow, broadening its shaft and paired diagonal head bands about the vertical axis.', '''
poly('arrow',(18,6),(30,6),(30,24),(36,18),(42,26),(24,42),(6,26),(12,18),(18,24),closed=True)
''')
replace('rate-stretch-tool','SQUARE','Two mirrored rounded turns with open arrowheads replace folded duplicate segments; separate their inner endpoints by ten units.', '''
path('upper',(6,12), [('L',(18,12)),('A',(24,18),6,6,True),('L',(24,19))])
poly('upper-arrow',(12,6),(6,12),(12,18));join('upper','upper-arrow')
path('lower',(42,36), [('L',(30,36)),('A',(24,30),6,6,True),('L',(24,29))])
poly('lower-arrow',(36,42),(42,36),(36,30));join('lower','lower-arrow')
''')
for name,changes,plan in [
 ('outlined-lambda',[('(20,20)','(18,20)')],'Broaden the descending left stroke at its owning junction, keeping the lambda outline and terminal shapes.'),
 ('pyup-logo',[('(16,19),(24,15),(31,20)','(16,20),(24,16),(31,21)')],'Move the entire upper P counter down by one unit to clear the outer hexagonal border.')]:
 i=next(i for i in A if i['icon_id']==name);p=Path(i['source_path']);backup=W/'originals'/p.name
 if not backup.exists():backup.write_text(p.read_text())
 s=backup.read_text()
 for a,b in changes:assert a in s,(name,a);s=s.replace(a,b)
 p.write_text(s);i['audit_status']='reconstructed';i['plan']=plan
(W/'audit.json').write_text(json.dumps(A,indent=2))
replace('fast-train-nose','HRECT_L','Trace one streamlined nose with tangent cubic joins; move the windscreen divider to form a broad window and a full eight-unit band above the floor.', '''
path('body',(4,8), [('L',(16,8)),('L',(24,8)),('C',(40,20),(30,8),(36,14)),('C',(36,28),(44,26),(40,28)),('L',(12,28)),('L',(4,28))])
poly('windscreen',(16,8),(22,20),(40,20));join('windscreen','body')
path('wheel',(12,28), [('A',(12,40),6,6,True),('A',(12,28),6,6,True)],True);join('wheel','body')
poly('rail',(4,40),(12,40),(44,40));join('rail','wheel')
''')
replace('personal-watercraft','HRECT_L','A broad deck band, smooth stern and exact seat/post attachment replace the pinched diagonal deck; preserve the raised handle and open hull ends.', '''
poly('post',(4,36),(12,20),(18,8),(24,8))
path('shell',(12,20), [('L',(20,20)),('L',(26,26)),('L',(36,26)),('A',(44,34),8,8,True),('L',(44,36)),('C',(42,40),(44,38),(43,39))]);join('post','shell')
line('deck',(4,36),(44,36));line('hull',(4,36),(12,40));join('deck','post');join('deck','shell');join('hull','post');join('hull','deck')
''')
replace('hanging-spider','VRECT_L','One capsule body owns four equally spaced leg roots per side and a hanging thread; mirrored legs diverge to preserve clearance.', '''
path('body',(18,14), [('A',(24,8),6,6,True),('A',(30,14),6,6,True),('L',(30,22)),('L',(30,30)),('L',(30,38)),('A',(24,44),6,6,True),('A',(18,38),6,6,True),('L',(18,30)),('L',(18,22)),('L',(18,14))],True)
line('thread',(24,4),(24,8));join('thread','body')
for side in (-1,1):
 x=24+side*6;outer=24+side*16
 poly(f'upper-{side}',(x,14),(outer,10),(outer,6));join(f'upper-{side}','body')
 line(f'middle-{side}',(x,22),(outer,20));join(f'middle-{side}','body')
 line(f'lower-{side}',(x,30),(outer,32));join(f'lower-{side}','body')
 line(f'bottom-{side}',(x,38),(24+side*10,44));join(f'bottom-{side}','body')
''')
i=next(i for i in A if i['icon_id']=='jet-ski-motion');p=Path(i['source_path']);backup=W/'originals'/p.name
if not backup.exists():backup.write_text(p.read_text())
p.write_text(backup.read_text().replace('(12,10)','(12,6)').replace('(22,26)','(22,28)').replace('(30,22)','(32,22)'));i['audit_status']='reconstructed';i['plan']='Broaden the hull band by raising the upper bow station; preserve the handle, speed marks and wave.'
(W/'audit.json').write_text(json.dumps(A,indent=2))
for name in ('bowling-pins-row','bowling-pins-three'):
 replace(name,'HRECT_L','Three repeated bowling pins: small circular heads, clear narrow necks and smooth broader bodies; preserve the row and circular head exception.', '''
for j,x in enumerate((8,24,40)):
 path(f'head-{j}',(x,8), [('A',(x,14),3,3,True),('A',(x,8),3,3,True)],True)
 path(f'body-{j}',(x,22), [('A',(x,40),4,9,True),('A',(x,22),4,9,True)],True)
 line(f'neck-{j}',(x,14),(x,22));join(f'neck-{j}',f'head-{j}');join(f'neck-{j}',f'body-{j}')
''')
