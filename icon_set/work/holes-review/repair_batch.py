"""Scoped opening repairs; original IDs and source metadata remain in each variant."""
from pathlib import Path
import ast,json,sys,textwrap
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/holes-review/queue.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
M=json.loads((W/'mapping.json').read_text()); trees={}; notes={}
for m in M:
 p=ROOT/m['file']; backup=W/'draft-sources'/p.name;backup.parent.mkdir(exist_ok=True)
 if not backup.exists():backup.write_text(p.read_text())
 trees[m['original']]=ast.parse(backup.read_text())
def cls(n):return next(x for x in trees[n].body if isinstance(x,ast.ClassDef))
def build(n):return next(x for x in cls(n).body if isinstance(x,ast.FunctionDef) and x.name=='build')
def callid(c):
 return c.args[0].value if isinstance(c,ast.Call) and c.args and isinstance(c.args[0],ast.Constant) else None
def edits(n,e,coords=None,**kw):
 for c in ast.walk(build(n)):
  if isinstance(c,ast.Call) and callid(c)==e:
   if coords is not None:c.args=[c.args[0]]+[ast.parse(repr(v),mode='eval').body for v in coords]
   for k,v in kw.items():
    c.keywords=[a for a in c.keywords if a.arg!=k]+[ast.keyword(arg=k,value=ast.parse(repr(v),mode='eval').body)]
def drop(n,*ids):
 b=build(n); b.body=[s for s in b.body if not (isinstance(s,ast.Expr) and isinstance(s.value,ast.Call) and any(isinstance(a,ast.Constant) and a.value in ids for a in s.value.args))]
def body(n,s):build(n).body=ast.parse(textwrap.dedent(s)).body
def add(n,s):build(n).body+=ast.parse(textwrap.dedent(s)).body
def pts(n,mp):
 class T(ast.NodeTransformer):
  def visit_Tuple(self,x):
   try:v=ast.literal_eval(x)
   except Exception:return self.generic_visit(x)
   return ast.parse(repr(mp[v]),mode='eval').body if v in mp else self.generic_visit(x)
 T().visit(build(n))
def note(n,s):notes[n]=s
# 1-2. Lower beam, sharing attachment nodes with walls.
n='cologne-cathedral-v3'
for e in ['outline','tower']:
 for c in ast.walk(build(n)):
  if isinstance(c,ast.Call) and callid(c)==e:
   vals=[ast.literal_eval(a) for a in c.args[1:]]
   if e=='tower':vals=[(6,27),(16,27),(16,42)]
   else:
    vals.insert(vals.index((6,23)),(6,27));vals.insert(vals.index((16,31)),(16,27))
   edits(n,e,vals)
for n in ['cologne-cathedral-v2','cologne-cathedral-v3']:note(n,'Lowered the tower crossbeam to enlarge the spire opening; preserved the outer silhouette.')
# Turtle head becomes a genuine oval; broaden paired front flippers.
n='sea-turtle'
for e in ['head-left','head-right']:edits(n,e,radius_x=4,radius_y=4)
# The front pair shares one construction; reducing arc radius opens both lobes.
for c in ast.walk(build(n)):
 if isinstance(c,ast.Call) and isinstance(c.func,ast.Attribute) and c.func.attr=='add_arc' and c.args and isinstance(c.args[0],ast.BinOp):
  if 'front' in ast.unparse(c.args[0]):
   for k in c.keywords:
    if k.arg=='radius_x':k.value=ast.Constant(6)
note(n,'Round head and broader mirrored front flippers replace thin lens-shaped pockets.')
n='ba-letters-underlined'
drop(n,'a-bowl-right','a-bowl-left','a-bowl','a-stem')
add(n,"""
self.add_arc('a-top',(44,24),(38,18),radius_x=6,sweep=False)
self.add_arc('a-left',(38,18),(38,30),radius_x=6,sweep=False)
self.add_arc('a-bottom',(38,30),(44,24),radius_x=6,sweep=False)
self.add_contour('a-bowl','a-top','a-left','a-bottom',closed=True)
self.add_polyline('a-stem',(44,18),(44,24),(44,30))
self.relate('connect','a-bowl','a-stem')
""")
note(n,'Moved the lowercase a stem to the bowl tangent, eliminating the narrow overlapping sliver.')
n='baby-head-v2'
body(n,"""
# Plan: circular blank head with one inward curl, sharing its crown node.
self.add_arc('head-left',(24,6),(24,42),radius_x=18,sweep=False)
self.add_arc('head-right',(24,42),(24,6),radius_x=18,sweep=False)
self.add_contour('head','head-left','head-right',closed=True)
self.add_arc('curl-down',(24,6),(30,12),radius_x=6)
self.add_arc('curl-in',(30,12),(24,18),radius_x=6)
self.add_contour('curl','curl-down','curl-in')
self.relate('connect','head','curl')
""")
note(n,'Rebuilt the intended round head and inward curl so the curl no longer crosses the forehead.')
n='bobble-hat-with-seams-v2'
for e in ['bobble-a','bobble-b']:edits(n,e,radius_x=4,radius_y=4)
note(n,'Made the bobble a true circle with an open centre.')
for n,cy,x in [('bridge-pose',30,40),('crow-pose',23,8),('downward-stretch',26,9),('low-plank-pose',11,40)]:
 edits(n,'head-top',[(x-3,cy),(x+3,cy)],radius_x=3,radius_y=3)
 edits(n,'head-bottom',[(x+3,cy),(x-3,cy)],radius_x=3,radius_y=3)
 note(n,'Replaced the flattened head lens with a genuine circular head; retained the pose.')
n='circular-steampunk-ornament'
# Retain unusual disc and wave layout, but use circular outer geometry to keep them apart.
edits(n,'disc-a',[(4,24),(44,24)],radius_x=20,radius_y=20)
edits(n,'disc-b',[(44,24),(4,24)],radius_x=20,radius_y=20)
edits(n,'spoke-ne',[(30,21),(44,24)])
edits(n,'spoke-top',[(26,17),(24,4)])
# wave becomes an interior S whose endpoints stay clear of the rim.
drop(n,'wave-a','wave-b','wave-c','wave')
add(n,"""
self.add_arc('wave-a',(15,15),(15,25),radius_x=6,sweep=False)
self.add_arc('wave-b',(15,25),(23,33),radius_x=8,sweep=True)
self.add_contour('wave','wave-a','wave-b')
""")
note(n,'Restored a circular rim and rebalanced the inner wavy trace to remove crossing pockets.')
n='compact-disc-with-partition-segment-v2'
for j,(a,b) in enumerate([((24,4),(44,24)),((44,24),(24,44)),((24,44),(4,24)),((4,24),(24,4))]):edits(n,f'rim-{j}',[a,b],radius_x=20,radius_y=20)
edits(n,'sector-right',[(44,24),(35,24)])
edits(n,'sector-turn',[(35,24),(24,35)],radius_x=11,radius_y=11)
edits(n,'sector-bottom',[(24,35),(24,44)])
note(n,'Restored the circular disc rim and widened the lower-right partition band.')
n='deer-antlers'
# Tiny duplicate tip arcs fold back into the beam; retain three visible main tines.
drop(n,'left-upper-tine','right-upper-tine')
note(n,'Removed the tiny folded-back tip strokes; retained the main antler beams and visible side tines.')
n='dragonfly'
for e in ['head-1','head-2']:edits(n,e,radius_x=3,radius_y=3)
note(n,'Rebuilt the head as a true circle; preserved all four wings and their divisions.')
n='error-404-xxx-label'
edits(n,'four-right-arm',[(36,8),(36,16),(42,16)])
note(n,'Opened the right numeral 4, retaining 404 and the XXX row without a pinched triangular counter.')
n='five-leaf-hanging-vine'
for e in ['upper-right-a','upper-right-b']:edits(n,e,radius_x=11,radius_y=11)
for e in ['terminal-a','terminal-b']:edits(n,e,radius_x=9,radius_y=9)
note(n,'Broadened the upper-right and terminal leaves by changing each paired arc definition together.')
n='flooded-house-interior'
pts(n,{(8,36):(8,33),(24,36):(24,33),(40,36):(40,33)})
note(n,'Raised the lower waterline to leave a clear opening above the floor.')
n='hanging-flower-pair'
for e in ['leaf-a','leaf-b']:edits(n,e,radius_x=9,radius_y=9)
note(n,'Broadened the hanging leaf while retaining the separate flower and unequal stems.')
n='leaning-tower-of-pisa'
# Keep three bands; rebalance vertical floor positions so the bottom cell is useful.
pts(n,{(13,36):(14,32),(29,40):(30,36),(15,26):(16,24),(31,30):(32,28),(17,16):(18,16),(33,20):(34,20)})
note(n,'Raised the lower floor band and respaced the other bands to enlarge the bottom opening.')
n='moon-rain-cloud'
edits(n,'moon-outer',[(28,22),(42,8)],radius_x=10,radius_y=12)
edits(n,'moon-inner',[(42,8),(42,30)],radius_x=5,radius_y=11)
edits(n,'moon-tip',[(42,30),(36,26)])
note(n,'Broadened the crescent by rebalancing its inner and outer curves.')
n='necklace-with-three-beads-v2'
for e in ['main-bead-a','main-bead-b']:edits(n,e,radius_x=5,radius_y=6)
note(n,'Made the central pendant a broader oval, keeping the cord attachments fixed.')
for n in ['paw-print-v2','paw-print-small-outer-toes-v2']:
 for side in ['left','right']:
  for suffix in ['top','bottom']:edits(n,f'outer-{side}-{suffix}',radius_x=3,radius_y=3 if n=='paw-print-v2' else 4)
 note(n,'Rebuilt the two outer toes as open circles/ovals, preserving paired proportions and the central pad.')
n='person-with-bindle'
# Pole and bundle right edge coincided only at apex then nearly crossed. Route pole from bag side junction.
edits(n,'pole',[(18,16),(26,26)])
note(n,'Joined the carrying pole at the bundle’s lower-right node, eliminating a tiny crossing pocket.')
n='rainbow-between-clouds'
edits(n,'rainbow-outer',[(6,34),(42,34)],radius_x=18,radius_y=26)
edits(n,'rainbow-inner',[(16,34),(32,34)],radius_x=8,radius_y=16)
note(n,'Made both rainbow arcs share a centred ellipse construction so their crowns no longer cross.')
n='shock-absorber'
for e in ['eye-right','eye-left']:edits(n,e,radius_x=3,radius_y=3)
note(n,'Made the lower mounting eye circular instead of a thin lens.')
n='singing-bird'
edits(n,'beak-crown',[(18,14),(25,4)])
edits(n,'beak-rise',[(25,4),(30,22)])
note(n,'Raised and widened the crown triangle to give its opening room.')
# Whorls: tangent half-circles with a consistent 9-unit pitch, avoiding self-crossing lenses.
for n in ['snail-shell-spiral','spiral-shell']:
 body(n,"""
# Plan: one open spiral, four tangent half-circles; each turn reduces its diameter by 9.
self.add_arc('outer-upper',(6,24),(42,24),radius_x=18)
self.add_arc('outer-lower',(42,24),(15,24),radius_x=14,radius_y=14)
self.add_arc('middle-upper',(15,24),(33,24),radius_x=9)
self.add_arc('inner-lower',(33,24),(24,24),radius_x=5,radius_y=5)
self.add_contour('spiral','outer-upper','outer-lower','middle-upper','inner-lower')
""")
 note(n,'Rebuilt the whorl as a coherent open spiral with wider turn spacing, removing intersecting loops.')
n='snow-capped-mountain-with-sun'
for e in ['sun-top','sun-bottom']:edits(n,e,radius_x=3,radius_y=3)
note(n,'Made the sun a true circular opening; retained the mountain and snowline.')
n='soldier-behind-sandbags'
# Enlarge the helmet/head together; omit brim which partitions the head into two thin slivers.
drop(n,'brim')
# Helper calls use numeric third radius argument.
for c in ast.walk(build(n)):
 if isinstance(c,ast.Call) and callid(c) in ['helmet','face'] and len(c.args)>3:c.args[3]=ast.Constant(6)
note(n,'Removed the thin central brim divider and made the helmeted head rounder; kept the rifle and both bags.')
n='three-bead-drop-earring-v2'
drop(n,'stud-right','stud-left','stud','drop-right','drop-left','drop')
add(n,"""
self.add_line('stud',(24,6),(24,10))
self.add_line('drop',(24,38),(24,42))
self.relate('connect','stud','upper-link')
self.relate('connect','drop','lower-link')
""")
note(n,'Replaced visually solid end-bead slivers with clean solid strokes; preserved the open central oval and links.')
n='trophy-on-ladder'
# Deep rounded handles reach the cup bottom; use shared nodes at lower cup junction.
edits(n,'handle-left-top',[(16,6),(8,6)])
edits(n,'handle-left',[(8,6),(16,18)],radius_x=8,radius_y=12,sweep=False)
edits(n,'handle-right',[(40,6),(32,18)],radius_x=8,radius_y=12,sweep=True)
# Re-author cup as deeper bowl with bottom y22, tangent quarter arcs.
edits(n,'cup-left',[(24,22),(16,14)],radius_x=8,radius_y=8)
edits(n,'cup-wall-left',[(16,14),(16,6)])
edits(n,'cup-wall-right',[(32,6),(32,14)])
edits(n,'cup-right',[(32,14),(24,22)],radius_x=8,radius_y=8)
edits(n,'stem',[(24,24),(24,22)])
# Attach handles to wall endpoints instead of nonmatching curved wall points.
edits(n,'handle-left',[(8,6),(16,14)],radius_x=8,radius_y=10,sweep=False)
edits(n,'handle-right',[(40,6),(32,14)],radius_x=8,radius_y=10,sweep=True)
note(n,'Deepened the cup handles and bowl together to enlarge both handle openings.')
n='tuk-tuk-side-view'
# Terminate fork at rim top; avoid drawing the fork through the wheel counter.
edits(n,'front-frame',[(28,8),(34,18),(38,28)])
note(n,'Stopped the front fork at the wheel rim, leaving the wheel counter open.')
n='unequal-balance-scale'
drop(n,'left-rim','right-rim')
note(n,'Removed the redundant horizontal pan dividers, leaving two clear bowl-and-suspension contours.')
n='user-with-gear'
edits(n,'head-left',[(24,24),(24,6)],radius_x=9,radius_y=9)
note(n,'Made the organic half-head a true semicircle, enlarging its opening beside the centre axis.')
n='visibility-distance'
edits(n,'zero-right-top',[(34,36),(42,36)],radius_x=4,radius_y=4)
edits(n,'zero-right-bottom',[(42,36),(34,36)],radius_x=4,radius_y=4)
note(n,'Widened the right zero into a true circle, keeping the 100 legend legible.')
# More individual repairs below.
n='analogue-wristwatch-v2'
pts(n,{(19,6):(19,4),(29,6):(29,4),(19,42):(19,44),(29,42):(29,44)})
note(n,'Extended both strap ends equally to enlarge their openings, preserving the dial and hands.')
n='crawling-baby'
for e in ['head-top','head-bottom']:edits(n,e,radius_x=6,radius_y=6)
note(n,'Made the baby’s head circular, preserving the crawling body silhouette.')
n='curled-raccoon'
drop(n,'ear-2','ear')
# Keep an inward ear tick rather than the tiny triangular counter.
note(n,'Opened the tiny ear triangle into a single inward ear mark; retained the curled tail and stripes.')
for n in ['pelican-on-water','pelican-on-water-v2']:
 edits(n,'pouch-2',radius_x=7,radius_y=6)
 note(n,'Deepened the bill pouch into a smooth half-ellipse, retaining the bent neck and wing.')
n='potted-branching-leaf-plant'
for e in ['top-left-a','top-left-b','top-right-a','top-right-b']:edits(n,e,radius_x=8,radius_y=8)
for e in ['middle-left-a','middle-left-b','middle-right-a','middle-right-b','lower-left-a','lower-left-b']:edits(n,e,radius_x=9,radius_y=9)
pts(n,{(17,39):(17,35),(24,39):(24,35),(31,39):(31,35)})
note(n,'Broadened all five leaf pairs and deepened the pot opening; kept the branching arrangement.')
n='sea-lion'
edits(n,'body-4',[(28,19),(42,34)],radius_x=18,radius_y=18)
edits(n,'body-5',[(42,34),(42,42)])
edits(n,'body-6',[(42,42),(34,42)],radius_x=8,radius_y=4,sweep=True)
edits(n,'body-7',[(34,42),(36,34)])
edits(n,'body-8',[(36,34),(32,30)])
edits(n,'body-9',[(32,30),(25,34)],radius_x=20,radius_y=12)
note(n,'Broadened the rear flipper and removed the crossing at its tip.')
n='seal-balancing-ball'
for e in ['ball-1','ball-2']:edits(n,e,radius_x=6,radius_y=6)
note(n,'Made the balanced ball round, preserving its nose contact and the seal’s silhouette.')
n='sheep-jumping-fence'
drop(n,'ground-mid')
note(n,'Opened the redundant strip beneath the fence rail while retaining both posts and the ground on either side.')
n='stepped-office-block-with-flag'
edits(n,'flag',[(23,20),(23,14),(23,6),(37,6),(37,14),(23,14)])
note(n,'Deepened the rooftop flag from four to eight units, retaining the stepped building.')
n='turreted-chateau-hotel-v2'
for c in ast.walk(build(n)):
 if isinstance(c,ast.Call) and callid(c)=='outline':
  v=[ast.literal_eval(a) for a in c.args[1:]];v.insert(v.index((6,27)),(6,32));edits(n,'outline',v)
edits(n,'turret-eave',[(6,32),(14,32),(14,42)])
# Add attachment on the return edge at x14; outer roof already joins that same wall run.
note(n,'Lowered the turret crossbeam to open the small spire counter.')
n='watered-planter'
edits(n,'potarc',radius_x=18,radius_y=8)
note(n,'Deepened the bowl using a true half-ellipse; retained the foliage and droplet.')
n='birds-in-nest'
edits(n,'bowl',radius_x=18,radius_y=13)
note(n,'Deepened the nest bowl, retaining both chicks and their eyes.')
n='capped-glue-stick'
body(n,"""
# Plan: tube with equal eight-unit cap/base bands and one centred square label.
left,right,top,bottom=8,40,4,44
self.add_polyline('body',(left,top),(right,top),(right,12),(right,36),(right,bottom),(left,bottom),(left,36),(left,12),closed=True)
self.add_line('cap',(left,12),(right,12))
self.add_line('base',(left,36),(right,36))
self.relate('connect','cap','body')
self.relate('connect','base','body')
self.add_polyline('label',(20,20),(28,20),(28,28),(20,28),closed=True)
""")
note(n,'Rebalanced the tube with equal deeper cap/base bands and a centred label; fits the vertical keyshape.')
n='castle-tower-with-pennant-v2'
edits(n,'flag',[(22,20),(22,14),(22,6),(38,6),(34,10),(38,14),(22,14)])
note(n,'Deepened the pennant and rebuilt its notch without the folded-back top segment.')
n='grand-canyon-with-river'
edits(n,'sun-top',[(34,10),(42,10)],radius_x=4,radius_y=4)
edits(n,'sun-bottom',[(42,10),(34,10)],radius_x=4,radius_y=4)
note(n,'Made the sun circular; preserved the canyon walls and river.')
n='leaping-antelope'
# Replace doubled front hoof outline by one bent leg stroke, preserving the extension.
for c in ast.walk(build(n)):
 if isinstance(c,ast.Call) and callid(c)=='silhouette':
  v=[ast.literal_eval(a) for a in c.args[1:]];start=v.index((38,24));v=v[:start+1]+v[start+6:];edits(n,'silhouette',v)
add(n,"""
self.add_polyline('front-leg',(38,24),(42,22),(42,34))
self.relate('connect','front-leg','silhouette')
""")
note(n,'Opened the thin doubled foreleg into a bent single stroke, preserving the leaping pose.')
n='mosquito'
# Increase paired wing depth, retaining their shared thorax attachment.
edits(n,'wing-left-2',[(6,31),(8,42)],radius_x=6,radius_y=9,sweep=False)
edits(n,'wing-left-3',[(8,42),(24,21)])
edits(n,'wing-right-2',[(42,31),(40,42)],radius_x=6,radius_y=9,sweep=True)
edits(n,'wing-right-3',[(40,42),(24,21)])
note(n,'Broadened both wings symmetrically to open their pointed counters.')
for n in ['painted-wall-mural-panel-v2','painted-wall-mural-panel']:
 # A solid coping stroke preserves the visible cap without a tiny hollow strip.
 edits(n,'cap',[(6,6),(42,6)],closed=False)
 if n.endswith('-v2'):edits(n,'panel',[(7,6),(7,42),(41,42),(41,6)],closed=False)
 else:edits(n,'panel',[(10,6),(10,42),(38,42),(38,6)],closed=False)
 # Split cap at wall attachment points for honest connections.
 edits(n,'cap',[(6,6),(7 if n.endswith('-v2') else 10,6),(41 if n.endswith('-v2') else 38,6),(42,6)],closed=False)
 note(n,'Replaced the thin hollow coping band with one solid cap stroke; retained the mural.')
n='platypus'
# Open bill at authored width 10 and depth 8; shift shared body/bill nodes together.
pts(n,{(18,38):(18,34),(28,38):(28,34),(8,38):(8,34),(40,38):(40,34)})
edits(n,'bill-2',[(28,34),(28,42)],radius_x=5,radius_y=4)
edits(n,'bill-4',[(18,42),(18,34)],radius_x=5,radius_y=4)
note(n,'Deepened the bill and moved its shared body attachments together.')
n='stacking-ring-toy'
# Use three roomy tiers in the original total height instead of a fourth compressed base tier.
drop(n,'ring-four-top','ring-four-right','ring-four-bottom','ring-four-left','ring-four')
edits(n,'ring-three-right',[(36,30),(36,42)],radius_x=6,radius_y=6)
edits(n,'ring-three-bottom',[(36,42),(12,42)])
edits(n,'ring-three-left',[(12,42),(12,30)],radius_x=6,radius_y=6)
note(n,'Merged the compressed bottom two tiers into one roomy base ring; retained the bear crown and stacking rhythm.')
for n in ['star-labelled-bottle','star-labelled-bottle-v2']:
 # Retain cap: eight-unit band, shoulder junction moved down as one owner.
 pts(n,{(16,12):(16,14),(32,12):(32,14),(16,11):(16,14),(32,11):(32,14)})
 edits(n,'cap-bottom',[(16,14),(32,14)])
 edits(n,'shoulder-right',[(32,14),(40,22)],radius_x=8)
 edits(n,'body-right',[(40,22),(40,40)])
 edits(n,'body-left',[(8,40),(8,22)])
 edits(n,'shoulder-left',[(8,22),(16,14)],radius_x=8)
 # Ensure band endpoints are explicit on neck.
 edits(n,'neck',[(16,14),(16,6),(32,6),(32,14)])
 note(n,'Deepened the cap band, moving both shoulder junctions together and retaining the star label.')
n='baby-girl-face'
# Broader outer bow loops with true oval half-ends, preserving knot contacts.
edits(n,'bow-left-top',[(21,8),(10,4)])
edits(n,'bow-left-end',[(10,4),(10,16)],radius_x=4,radius_y=6,sweep=False)
edits(n,'bow-left-bottom',[(10,16),(21,8)])
edits(n,'bow-right-top',[(27,8),(38,4)])
edits(n,'bow-right-end',[(38,4),(38,16)],radius_x=4,radius_y=6,sweep=True)
edits(n,'bow-right-bottom',[(38,16),(27,8)])
edits(n,'temple-left',[(8,24),(10,16)],radius_x=14,radius_y=14)
edits(n,'temple-right',[(38,16),(40,24)],radius_x=14,radius_y=14)
note(n,'Enlarged the mirrored bow loops and moved their temple attachments together; retained the smiling face.')
n='bell-shaped-stupa-v2'
# Deepen plinth upward, shortening the dome but preserving shared corner geometry.
pts(n,{(9,38):(9,34),(39,38):(39,34),(6,38):(6,34),(42,38):(42,34)})
edits(n,'dome-right',radius_x=8,radius_y=18)
edits(n,'dome-left',radius_x=8,radius_y=18)
note(n,'Deepened the plinth upward, preserving the spire and bell-shaped dome.')
n='jellyfish-group'
# Shared dome definition: true elliptical half-arcs, not shallow arcs with mismatched radius.
for i in range(3):edits(n,f'bell-{i}-dome',radius_x=9,radius_y=6)
note(n,'Rebuilt all three bells from the same deeper half-ellipse definition.')
n='scorpion'
# Open pincers: remove the closing jaw bridge rather than retaining triangular pockets.
for side in ['l','r']:
 drop(n,f'jaw-{side}-inner',f'jaw-{side}-outer',f'claw-{side}')
 add(n,f"self.add_contour('claw-{side}','claw-{side}-outer','claw-{side}-inner')\nself.relate('connect','arm-{side}','claw-{side}')")
note(n,'Opened both pincers by removing their closing jaw bridges; preserved the paired arms and curled tail.')
# Second visual/spacing pass: preserve the opening fixes without introducing crowding.
n='sea-turtle'
pts(n,{(34,26):(34,28),(14,26):(14,28)})
for c in ast.walk(build(n)):
 if isinstance(c,ast.Call) and isinstance(c.func,ast.Attribute) and c.args and isinstance(c.args[0],ast.BinOp):
  label=ast.unparse(c.args[0])
  if 'front-upper' in label:
   c.keywords=[ast.keyword(arg='radius_x',value=ast.Constant(8)),ast.keyword(arg='sweep',value=ast.Name(id='flip',ctx=ast.Load()))]
  elif 'front-lower' in label:
   c.func.attr='add_line';c.keywords=[]
   c.args[2]=ast.parse('p(14,28)',mode='eval').body
n='bridge-pose'
edits(n,'head-top',[(38,30),(44,30)],radius_x=3,radius_y=3)
edits(n,'head-bottom',[(44,30),(38,30)],radius_x=3,radius_y=3)
pts(n,{(6,8):(4,8)})
n='downward-stretch'
edits(n,'head-top',[(5,26),(11,26)],radius_x=3,radius_y=3)
edits(n,'head-bottom',[(11,26),(5,26)],radius_x=3,radius_y=3)
pts(n,{(6,40):(4,40),(42,40):(44,40)})
n='error-404-xxx-label'
edits(n,'four-right-arm',[(36,8),(36,16),(44,16)])
edits(n,'four-right-stem',[(44,8),(44,16),(44,20)])
pts(n,{(6,29):(4,29),(6,40):(4,40)})
n='flooded-house-interior'
pts(n,{(8,25):(8,23),(24,25):(24,23),(40,25):(40,23),(24,6):(24,4),(8,42):(8,44),(40,42):(40,44)})
n='circular-steampunk-ornament'
edits(n,'wave-a',[(14,18),(14,24)],radius_x=8,sweep=False)
edits(n,'wave-b',[(14,24),(16,30)],radius_x=6,sweep=True)
for n in ['paw-print-v2','paw-print-small-outer-toes-v2']:
 y=37 if n=='paw-print-v2' else 38
 pts(n,{(15,y):(16,y),(33,y):(32,y)})
 edits(n,'pad-crown',radius_x=8,radius_y=10 if y==37 else 9)
 edits(n,'pad-left-lobe',radius_x=4)
 edits(n,'pad-right-lobe',radius_x=4)
n='grand-canyon-with-river'
edits(n,'sun-top',[(36,9),(42,9)],radius_x=3,radius_y=3)
edits(n,'sun-bottom',[(42,9),(36,9)],radius_x=3,radius_y=3)
n='jellyfish-group'
body(n,"""
# Plan: three staggered equal bells; each owns two evenly spaced tentacles.
# The two outer bells lean left by placement; the middle bell sits to the right.
for index,(left,rim_y,ends) in enumerate(((6,12,(6,14)),(26,25,(34,42)),(6,38,(6,14)))):
    right=left+16
    dome=f'bell-{index}-dome'
    rim=f'bell-{index}-rim'
    contour=f'bell-{index}'
    self.add_arc(dome,(left,rim_y),(right,rim_y),radius_x=8,radius_y=6)
    nodes=sorted(set((left,right)+ends),reverse=True)
    for j in range(1,len(nodes)):
        self.add_line(f'{rim}-{j}',(nodes[j-1],rim_y),(nodes[j],rim_y))
    self.add_contour(contour,dome,*[f'{rim}-{j}' for j in range(1,len(nodes))],closed=True)
    end_y=(18,29,42)[index]
    for j,x in enumerate(ends):
        name=f'tentacle-{index}-{j}'
        self.add_line(name,(x,rim_y),(x,end_y))
        self.relate('connect',name,contour)
""")
note(n,'Rebuilt three deeper bells and reduced each to two evenly spaced tentacles to avoid new crowding.')

for n in ['snail-shell-spiral','spiral-shell']:
    edits(n,'outer-lower',[(42,24),(16,24)],radius_x=13,radius_y=18)
    edits(n,'middle-upper',[(16,24),(32,24)],radius_x=8,radius_y=8)
    edits(n,'inner-lower',[(32,24),(26,24)],radius_x=3,radius_y=3)
    if n=='spiral-shell':
        pts(n,{(6,24):(42,24),(42,24):(6,24),(16,24):(32,24),(32,24):(16,24),(26,24):(22,24)})
        for c in ast.walk(build(n)):
            if isinstance(c,ast.Call) and isinstance(c.func,ast.Attribute) and c.func.attr=='add_arc':
                c.keywords=[k for k in c.keywords if k.arg!='sweep']+[ast.keyword(arg='sweep',value=ast.Constant(False))]
    note(n,'Rebuilt the whorl from tangent half-ellipses with wider turn spacing and exact square bounds.')
for m in M:
 n=m['original'];tree=trees[n]
 # Every repair records its scope directly in the owning build routine.
 build(n).body.insert(0,ast.Expr(value=ast.Constant('Opening repair: '+notes.get(n,'Enlarged opening.'))))
 for item in tree.body:
  if isinstance(item,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUTHOR' for t in item.targets):item.value=ast.Constant(AUTHOR)
 ast.fix_missing_locations(tree)
 (ROOT/m['file']).write_text('# Review candidate; original preserved.\n'+ast.unparse(tree)+'\n')
(W/'notes.json').write_text(json.dumps(notes,indent=2))
print('Repaired',len(M),'candidate models')
