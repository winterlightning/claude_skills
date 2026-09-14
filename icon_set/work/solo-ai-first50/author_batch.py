"""AI re-authoring of 50 explicitly selected json_to_solo subjects."""
from pathlib import Path
import json, ast, sys, textwrap, inspect
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons.registry import factories
SOURCE_ICON_ID=None # Each exact ID is retained in selected.json and its output module.
SOURCE_PATH='icon_set/work/solo-ai-first50/selected.json'
AUTHOR='gpt-6'
WORK=Path(__file__).parent
HELPERS='''
        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L":
                    self.add_line(ident, here, end)
                elif kind == "A":
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == "C":
                    c1, c2 = args
                    self.add_bezier(ident, here, (c1, c2, end))
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [("A",(cx+r,cy),r,r,True), ("A",(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0+r,y0), [
                ("L",(x1-r,y0)), ("A",(x1,y0+r),r,r,True),
                ("L",(x1,y1-r)), ("A",(x1-r,y1),r,r,True),
                ("L",(x0+r,y1)), ("A",(x0,y1-r),r,r,True),
                ("L",(x0,y0+r)), ("A",(x0+r,y0),r,r,True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate("connect",a,b)
'''
D={}
def design(names,key,ref,plan,body):
 for name in names.split(): D[name]=(key,ref,plan,textwrap.dedent(body))
design('acorn','VRECT_L','nut','A symmetric cap owns its midpoint stem and two body attachments; a single smooth nut tapers to the bottom extreme. Removed conversion wiggles.', '''
axis = 24
path('cap', (8,24), [('A',(axis,12),16,12,True),('A',(40,24),16,12,True),('L',(36,24)),('L',(12,24)),('L',(8,24))],True)
path('nut',(12,24), [('C',(24,44),(12,37),(18,40)),('C',(36,24),(30,40),(36,37))])
line('stem',(24,4),(24,12))
join('stem','cap'); join('nut','cap')
''')
design('adjustable-lamp-2','VRECT_L','lamp','Symmetric shade and upright base beneath a smooth semicircular upper arc. Removed the tiny conversion kink at the shade.', '''
path('upper',(8,20), [('A',(40,20),16,16,True)])
poly('shade',(19,20),(29,20),(33,33),(24,33),(15,33),closed=True)
line('stand',(24,33),(24,44))
poly('base',(17,44),(24,44),(31,44))
join('stand','shade');join('stand','base')
''')
design('airchair','VRECT_L','armchair','A shared vertical axis controls the arched back, continuous arm-and-seat outline, and paired legs. Removed traced dents.', '''
path('back',(12,21), [('L',(12,16)),('A',(36,16),12,12,True),('L',(36,21))])
poly('seat',(12,21),(8,21),(10,36),(12,36),(36,36),(38,36),(40,21),(36,21),(32,21),(32,28),(16,28),(16,21),(12,21),closed=True)
for x in (12,36):
 line(f'leg-{x}',(x,36),(x-2 if x<24 else x+2,44));join(f'leg-{x}','seat')
join('seat','back')
''')
design('airplane airplane-other','SQUARE','plane','A diagonal airplane keeps its directional silhouette, with a smooth nose and deliberate wing and tail corners. The two copies retain the same subject.', '''
path('plane',(6,31), [('L',(12,28)),('L',(18,30)),('L',(26,22)),('L',(14,10)),('L',(20,6)),('L',(32,14)),('L',(36,10)),('C',(42,14),(41,5),(44,9)),('C',(38,22),(42,18),(40,20)),('L',(18,42)),('L',(12,42)),('L',(6,31))],True)
''')
design('alcove','VRECT_L',None,'Two concentric semicircular arches share an axis; the inner doorway meets the broad threshold with exact endpoints. Removed uneven arch radii.', '''
path('outer',(8,44), [('L',(8,20)),('A',(40,20),16,16,True),('L',(40,44)),('L',(8,44))],True)
path('inner',(16,36), [('L',(16,20)),('A',(32,20),8,8,True),('L',(32,36)),('L',(16,36))],True)
line('threshold-left',(8,44),(16,36));line('threshold-right',(40,44),(32,36))
for n in ('threshold-left','threshold-right'):
 join(n,'inner');join(n,'outer')
''')
design('amfitheater-in-delphi-top archway','HRECT_L',None,'Concentric tangent arches form one continuous architectural outline. A shared center and radii keep the passage equally wide.', '''
path('arch',(4,40), [('L',(4,28)),('A',(44,28),20,20,True),('L',(44,40)),('L',(36,40)),('L',(36,28)),('A',(12,28),12,12,False),('L',(12,40)),('L',(4,40))],True)
''')
design('anklet','SQUARE',None,'An open circular band and detached circular charm share the vertical axis. The charm has a clear four-unit ink gap instead of touching the band.', '''
path('band',(8,6), [('C',(6,16),(6,8),(6,12)),('C',(24,28),(6,24),(14,28)),('C',(42,16),(34,28),(42,24)),('C',(40,6),(42,12),(42,8))])
circle('charm',24,39,3)
''')
design('ant-uncategorized-03','VRECT_L','bug','A central head, thorax and abdomen define the ant; paired antennae and legs are derived from one axis. Simplified overlapping internal divisions.', '''
circle('head',24,13,5)
path('body',(18,27), [('C',(24,23),(18,24),(20,23)),('C',(30,27),(28,23),(30,24)),('L',(30,38)),('A',(18,38),6,6,True),('L',(18,27))],True)
for side in (-1,1):
 x=lambda d:24+side*d
 poly(f'antenna-{side}',(x(4),8),(x(10),4))
 poly(f'leg-top-{side}',(x(6),27),(x(12),24),(x(16),28))
 poly(f'leg-bottom-{side}',(x(6),38),(x(12),36),(x(16),44))
 join(f'leg-top-{side}','body');join(f'leg-bottom-{side}','body')
''')
design('antique-axe','SQUARE','axe','One diagonal handle joins a geometric axe head; the blade is a smooth broad arc. Preserved its intentional diagonal orientation.', '''
line('handle',(6,42),(28,20))
path('head',(24,16), [('L',(32,6)),('C',(42,16),(32,12),(37,16)),('C',(32,28),(41,22),(37,27)),('L',(28,20)),('L',(24,16))],True)
join('handle','head')
''')
design('apartment-balcony-glass','HRECT_L',None,'A centered two-pane window rises above a continuous balcony rail; paired posts share spacing. Omitted small reflection slashes to protect the openings.', '''
poly('window',(12,28),(12,8),(24,8),(36,8),(36,28))
line('mullion',(24,8),(24,28));join('mullion','window')
poly('rail',(4,28),(12,28),(24,28),(36,28),(44,28))
join('rail','window');join('rail','mullion')
for x in (12,36):
 line(f'post-{x}',(x,28),(x,40));join(f'post-{x}','rail')
poly('base',(12,40),(36,40));join('base','post-12');join('base','post-36')
''')
design('archery-bow','SQUARE','bow-arrow','A taut angular string and one smooth bow curve meet a diagonal arrow. Kept the purposeful diagonal and removed tiny traced bends.', '''
path('bow',(6,6), [('C',(42,42),(28,6),(42,20))])
poly('string',(6,6),(6,42),(42,42))
poly('arrow',(6,42),(24,24),(38,10))
poly('arrowhead',(30,10),(38,10),(38,18))
join('bow','string');join('bow','arrow');join('arrow','string');join('arrow','arrowhead')
''')
design('architecture-fence','HRECT_L','fence','Two matching pickets use shared heights and width; two rails attach at exact endpoints. Removed uneven picket corners.', '''
for x in (8,30):
 poly(f'picket-{x}',(x,40),(x,24),(x,16),(x,14),(x+5,8),(x+10,14),(x+10,16),(x+10,24),(x+10,40),closed=True)
for y in (16,24):
 for j,(a,b) in enumerate(((4,8),(18,30),(40,44))):
  line(f'rail-{y}-{j}',(a,y),(b,y))
  if j<2:join(f'rail-{y}-{j}','picket-8')
  if j>0:join(f'rail-{y}-{j}','picket-30')
''')
design('archive','HRECT_L','archive','A wide lid and centered handle sit on a rounded storage box. Shared rim nodes preserve real attachment; corners use equal radii.', '''
poly('lid',(4,8),(44,8),(44,16),(40,16),(8,16),(4,16),closed=True)
path('body',(8,16), [('L',(8,36)),('A',(12,40),4,4,False),('L',(36,40)),('A',(40,36),4,4,False),('L',(40,16))])
line('handle',(20,27),(28,27));join('lid','body')
''')
design('archive-drawer','HRECT_L','archive','One storage drawer with a raised back and a central handle cut into its front edge. Rounded outer corners replace the traced polygon.', '''
poly('back',(8,24),(8,8),(40,8),(40,24))
path('front',(8,24), [('L',(18,24)),('L',(18,32)),('L',(30,32)),('L',(30,24)),('L',(40,24)),('A',(44,28),4,4,True),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,28)),('A',(8,24),4,4,True)],True)
join('back','front')
''')
design('armchair','VRECT_L','armchair','A smooth round back rises above a broad upholstered seat. Paired short arms and legs share dimensions; the small arm loops are opened for clarity.', '''
path('back',(12,26), [('L',(12,16)),('A',(36,16),12,12,True),('L',(36,26))])
path('seat',(8,36), [('A',(16,28),8,8,True),('L',(32,28)),('A',(40,36),8,8,True),('L',(40,36)),('L',(36,36)),('L',(12,36)),('L',(8,36))],True)
for x in (12,36):
 line(f'leg-{x}',(x,36),(x,44));join(f'leg-{x}','seat')
# The back is attached to the seat via straight side strokes.
line('arm-left',(8,20),(8,36));line('arm-right',(40,20),(40,36))
join('arm-left','seat');join('arm-right','seat')
''')
design('ascot','VRECT_L','shirt','A symmetric broad neckband joins one tapered fabric blade. Kept angular fabric corners and removed conversion bumps.', '''
poly('band',(8,4),(40,4),(32,14),(16,14),closed=True)
poly('blade',(16,14),(8,36),(24,44),(40,36),(32,14))
join('band','blade')
''')
design('atom-other','HRECT_L','atom','Two diagonal orbital loops share exact crossing nodes, with a centered nucleus. Replaced faceted loops with coherent tangent curves.', '''
path('orbit-one',(4,12), [('C',(24,16),(4,4),(14,8)),('C',(44,36),(34,24),(44,28)),('C',(24,32),(44,44),(34,40)),('C',(4,12),(14,24),(4,20))],True)
path('orbit-two',(4,36), [('C',(24,16),(4,28),(14,24)),('C',(44,12),(34,8),(44,4)),('C',(24,32),(44,20),(34,24)),('C',(4,36),(14,40),(4,44))],True)
self.add_dot('nucleus',(24,24));join('orbit-one','orbit-two')
''')
design('award-medal award-medal-rewards','VRECT_L','medal','A symmetric ribbon attaches to two exact top-quarter points of a circular medal. A broad open ribbon replaces the crowded inner stripe.', '''
path('medal',(16,24), [('A',(32,24),10,10,True),('A',(34,30),10,10,True),('A',(14,30),10,10,True),('A',(16,24),10,10,True)],True)
poly('ribbon',(16,24),(8,4),(40,4),(32,24))
join('medal','ribbon')
''')
design('bag bag-1e030fe3 bag-44d13a4d bag-bf5296da bag-d97bc915 bag-e213494f bag-photography bag-shopping','VRECT_L','shopping-bag','A symmetric shopping bag uses one smooth arched handle and a tapered body; the handle meets shared rim nodes. Removed conversion dents and inconsistent corners.', '''
axis, half_handle = 24, 8
path('handle',(axis-half_handle,16), [('L',(16,12)),('A',(32,12),8,8,True),('L',(axis+half_handle,16))])
path('bag',(12,16), [('L',(16,16)),('L',(32,16)),('L',(36,16)),('L',(40,38)),('C',(34,44),(40,42),(38,44)),('L',(14,44)),('C',(8,38),(10,44),(8,42)),('L',(12,16))],True)
join('bag','handle')
''')
design('ball','CIRCLE','volleyball','A true circular ball with two smooth sweeping seams. Seams meet the perimeter at exact cardinal nodes; no faceted conversion curves.', '''
path('outline',(4,24), [('A',(24,4),20,20,True),('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True)],True)
path('seam-top',(24,4), [('C',(44,24),(24,15),(33,24))])
path('seam-bottom',(4,24), [('C',(24,44),(15,24),(24,33))])
join('seam-top','outline');join('seam-bottom','outline')
''')
design('ball-with-lines','CIRCLE',None,'A circular football owns a central pentagonal panel and five radial seams. Paired lower seams mirror about x=24.', '''
path('outline',(24,4), [('A',(44,24),20,20,True),('A',(36,40),20,20,True),('A',(12,40),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
poly('panel',(24,15),(34,23),(30,33),(18,33),(14,23),closed=True)
for j,(a,b) in enumerate((((24,4),(24,15)),((44,24),(34,23)),((36,40),(30,33)),((12,40),(18,33)),((4,24),(14,23)))):
 line(f'seam-{j}',a,b);join(f'seam-{j}','outline');join(f'seam-{j}','panel')
''')
design('bandaid','SQUARE','bandage','Two crossed bandages are constructed as one joined silhouette around a broad diamond pad. Smooth end caps replace the faceted source.', '''
path('cross',(6,12), [('A',(16,6),7,7,True),('L',(24,14)),('L',(32,6)),('A',(42,16),7,7,True),('L',(34,24)),('L',(42,32)),('A',(32,42),7,7,True),('L',(24,34)),('L',(16,42)),('A',(6,32),7,7,True),('L',(14,24)),('L',(6,16)),('L',(6,12))],True)
poly('pad',(24,14),(34,24),(24,34),(14,24),closed=True)
join('cross','pad')
''')
design('barrier','HRECT_L','construction','A broad striped road barrier with paired legs. Reduced the stripes to two spacious diagonals and removed floating top dots.', '''
poly('board',(4,8),(20,8),(36,8),(44,8),(44,24),(36,24),(20,24),(12,24),(4,24),closed=True)
line('stripe-1',(4,24),(20,8));line('stripe-2',(20,24),(36,8))
for n in ('stripe-1','stripe-2'):join(n,'board')
for x in (12,36):
 line(f'leg-{x}',(x,24),(x,40));join(f'leg-{x}','board')
''')
design('basket','HRECT_L','shopping-basket','A symmetric basket has one tapered bowl and paired outward handle strokes, all on shared attachment nodes.', '''
poly('basket',(4,20),(12,20),(36,20),(44,20),(38,40),(10,40),closed=True)
for side in (-1,1):
 x=lambda d:24+side*d
 line(f'handle-{side}',(x(12),20),(x(6),8));join(f'handle-{side}','basket')
''')
design('basketball basketball-ball','CIRCLE','volleyball','A true circular basketball has orthogonal central seams and two mirror curved side seams. Their shared intersections preserve a balanced panel layout.', '''
path('outline',(24,4), [('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
poly('vertical',(24,4),(24,24),(24,44))
poly('horizontal',(4,24),(14,24),(24,24),(34,24),(44,24))
for side in (-1,1):
 x=lambda d:24+side*d
 path(f'curve-{side}',(x(12),8), [('C',(x(10),24),(x(4),12),(x(10),17)),('C',(x(12),40),(x(10),31),(x(4),36))])
 join(f'curve-{side}','horizontal')
join('vertical','horizontal');join('vertical','outline');join('horizontal','outline')
''')
design('batch-05-ribbon-tie','HRECT_L','shirt','A centered bow-tie knot controls two mirrored fabric wings; omitted the crowded interior creases.', '''
poly('knot',(19,16),(29,16),(29,32),(19,32),closed=True)
poly('left',(19,16),(4,8),(4,40),(19,32))
poly('right',(29,16),(44,8),(44,40),(29,32))
join('left','knot');join('right','knot')
''')
design('battery','VRECT_L','battery','A vertical cell has a rounded body and a broad terminal, with exact terminal-to-body attachments.', '''
path('body',(12,12), [('L',(16,12)),('L',(32,12)),('L',(36,12)),('A',(40,16),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,16)),('A',(12,12),4,4,True)],True)
poly('terminal',(16,12),(16,4),(32,4),(32,12));join('terminal','body')
''')
design('battery-1 battery-photography','HRECT_L','battery','A horizontal cell uses four equal body radii and one centered broad terminal. The terminal reuses split side-wall endpoints.', '''
path('body',(8,8), [('L',(32,8)),('A',(36,12),4,4,True),('L',(36,16)),('L',(36,32)),('L',(36,36)),('A',(32,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,12)),('A',(8,8),4,4,True)],True)
poly('terminal',(36,16),(44,16),(44,32),(36,32));join('terminal','body')
''')
design('beach-palm-water','SQUARE','umbrella','A tilted beach umbrella stands above three smooth water scallops. Preserved its tilt; enlarged the umbrella-to-water separation.', '''
path('canopy',(10,24), [('C',(36,10),(10,9),(28,1)),('L',(23,17)),('L',(10,24))],True)
line('pole',(23,17),(28,30));join('pole','canopy')
path('water',(6,42), [('C',(18,42),(10,42),(10,36)),('C',(30,42),(22,48),(26,36)),('C',(42,42),(34,48),(38,42))])
''')
design('beaker','VRECT_L','flask-round','A round flask flows tangentially into its narrow neck. The neck and lip share nodes; omitted extra liquid decoration absent from the source.', '''
path('flask',(19,4), [('L',(19,12)),('C',(8,28),(19,18),(8,18)),('A',(40,28),16,16,False),('C',(29,12),(40,18),(29,18)),('L',(29,4))])
poly('lip',(15,4),(19,4),(29,4),(33,4));join('lip','flask')
''')
design('bed bed-symbol','HRECT_L','bed','A clear bed frame has a tall head post, a broad mattress band and two legs. Both horizontal rails meet split post nodes.', '''
poly('head',(4,8),(4,24),(4,32),(4,40))
poly('foot',(44,24),(44,32),(44,40))
line('top',(4,24),(44,24));line('bottom',(4,32),(44,32))
for n in ('top','bottom'):join(n,'head');join(n,'foot')
''')
design('bell-77ec3808','HRECT_L','bell','A symmetric bell shoulder flows into a gently flared skirt; retained the uncluttered silhouette without adding a clapper.', '''
path('bell',(4,40), [('C',(12,24),(10,34),(12,31)),('L',(12,20)),('A',(36,20),12,12,True),('L',(36,24)),('C',(44,40),(36,31),(38,34)),('L',(4,40))],True)
''')
design('bell-symbol','HRECT_L','bell','A smooth domed bell shares a center axis with its crown and broad base. Equal shoulder radii replace the faceted conversion.', '''
path('dome',(8,40), [('L',(8,24)),('A',(24,8),16,16,True),('A',(40,24),16,16,True),('L',(40,40))])
poly('base',(4,40),(8,40),(40,40),(44,40));join('base','dome')
''')
design('bench','HRECT_L',None,'A picnic bench keeps two sloping trestle legs and two level planks. All four plank-leg junctions are exact shared nodes.', '''
poly('top',(8,8),(16,8),(32,8),(40,8))
poly('seat',(4,24),(12,24),(36,24),(44,24))
poly('left-leg',(16,8),(12,24),(8,40))
poly('right-leg',(32,8),(36,24),(40,40))
for n in ('left-leg','right-leg'):join(n,'top');join(n,'seat')
''')
design('bendy-bus','HRECT_L','bus','A bus body owns two equal wheels, a spacious window band and three pillars. Wheel centers and axle height share parameters; removed the tilted rear-window kink.', '''
path('body',(4,32), [('L',(4,12)),('A',(8,8),4,4,True),('L',(16,8)),('L',(28,8)),('L',(36,8)),('A',(44,16),8,8,True),('L',(44,24)),('L',(44,32)),('L',(38,32)),('L',(30,32)),('L',(18,32)),('L',(10,32)),('L',(4,32))],True)
poly('window-base',(4,24),(16,24),(28,24),(44,24));join('window-base','body')
for x in (16,28):
 line(f'pillar-{x}',(x,8),(x,24));join(f'pillar-{x}','body');join(f'pillar-{x}','window-base')
for x in (14,34):
 circle(f'wheel-{x}',x,36,4)
''')
design('bikini','HRECT_L',None,'A bikini top has mirrored smooth cups and crossed shoulder ties, derived from one axis. Opened the cramped lower junction.', '''
path('left-cup',(4,32), [('C',(10,20),(4,27),(7,22)),('L',(20,28)),('C',(20,38),(23,33),(24,38)),('C',(4,32),(14,42),(4,40))],True)
path('right-cup',(44,32), [('C',(38,20),(44,27),(41,22)),('L',(28,28)),('C',(28,38),(25,33),(24,38)),('C',(44,32),(34,42),(44,40))],True)
poly('left-tie',(10,20),(24,8),(30,8))
poly('right-tie',(38,20),(24,8),(18,8))
join('left-tie','left-cup');join('right-tie','right-cup');join('left-tie','right-tie')
''')
design('binocular','HRECT_L','binoculars','Two identical circular objective lenses share one baseline; tapered barrels rise to paired eyepieces and a connecting bridge.', '''
for x in (14,34):
 circle(f'lens-{x}',x,30,10)
 path(f'barrel-{x}',(x-10,30), [('L',(x-5,8)),('L',(x+3,8)),('L',(x+6,22))])
 join(f'barrel-{x}',f'lens-{x}')
line('bridge',(17,16),(31,16))
''')


# Refinements from native-size review and exact validation findings.
design('airplane airplane-other','SQUARE','plane','A diagonal airplane keeps purposeful wing and tail corners; the nose is a single tangent curve whose right extreme is exactly x=42.', """
path('plane',(6,31), [('L',(12,28)),('L',(18,30)),('L',(26,22)),('L',(14,10)),('L',(20,6)),('L',(32,14)),('L',(36,10)),('C',(42,14),(40,6),(42,8)),('C',(38,22),(42,18),(40,20)),('L',(18,42)),('L',(12,42)),('L',(6,31))],True)
""")
design('ant-uncategorized-03','VRECT_L','bug','A circular ant head has exact 3-4-5 antenna junctions; an eight-unit centerline gap separates it from the rounded segmented body. Paired limbs derive from one axis.', """
path('head',(21,9), [('A',(27,9),5,5,True),('A',(29,13),5,5,True),('A',(19,13),5,5,True),('A',(21,9),5,5,True)],True)
path('body',(18,30), [('A',(24,26),6,4,True),('A',(30,30),6,4,True),('L',(30,38)),('A',(18,38),6,6,True),('L',(18,30))],True)
for side in (-1,1):
 x=lambda d:24+side*d
 line(f'antenna-{side}',(x(3),9),(x(10),4));join(f'antenna-{side}','head')
 poly(f'leg-top-{side}',(x(6),30),(x(12),26),(x(16),30))
 poly(f'leg-bottom-{side}',(x(6),38),(x(12),36),(x(16),44))
 join(f'leg-top-{side}','body');join(f'leg-bottom-{side}','body')
""")
design('armchair','VRECT_L','armchair','A rounded back joins a continuous upholstered arm-and-seat contour at matching nodes. Shared dimensions keep both armrests and legs equal; removed tiny arm loops.', """
path('back',(12,20), [('L',(12,16)),('A',(36,16),12,12,True),('L',(36,20))])
path('seat',(12,20), [('L',(8,20)),('L',(8,32)),('A',(12,36),4,4,False),('L',(36,36)),('A',(40,32),4,4,False),('L',(40,20)),('L',(36,20)),('L',(32,20)),('L',(32,28)),('L',(16,28)),('L',(16,20)),('L',(12,20))],True)
join('back','seat')
for x in (12,36):
 line(f'leg-{x}',(x,36),(x,44));join(f'leg-{x}','seat')
""")
design('atom-other','HRECT_L','atom','Two smooth diagonal orbital loops use cardinal outer extrema and shared crossing nodes. Omitted the nucleus to maintain clear central negative space.', """
path('orbit-one',(4,12), [('C',(8,8),(4,9),(5,8)),('C',(24,16),(13,8),(19,12)),('C',(44,36),(36,24),(44,30)),('C',(40,40),(44,39),(43,40)),('C',(24,32),(35,40),(29,36)),('C',(4,12),(12,24),(4,18))],True)
path('orbit-two',(4,36), [('C',(24,16),(4,30),(12,24)),('C',(40,8),(29,12),(35,8)),('C',(44,12),(43,8),(44,9)),('C',(24,32),(44,18),(36,24)),('C',(8,40),(19,36),(13,40)),('C',(4,36),(5,40),(4,39))],True)
join('orbit-one','orbit-two')
""")
design('award-medal award-medal-rewards','VRECT_L','medal','A broad symmetric ribbon connects at two exact 3-4-5 points on a circular medal. Removed the cramped ribbon stripe and used one true medal radius.', """
path('medal',(16,28), [('A',(32,28),10,10,True),('A',(34,34),10,10,True),('A',(14,34),10,10,True),('A',(16,28),10,10,True)],True)
poly('ribbon',(16,28),(8,4),(40,4),(32,28));join('medal','ribbon')
""")
design('bandaid','SQUARE','bandage','Two crossed bandages form a unified outline with smooth capsule ends and a central diamond pad; all quadrant extrema lie exactly on the square envelope.', """
path('cross',(6,12), [('C',(12,6),(6,8),(8,6)),('C',(17,9),(14,6),(15,7)),('L',(24,16)),('L',(31,9)),('C',(36,6),(33,7),(34,6)),('C',(42,12),(40,6),(42,8)),('C',(39,17),(42,14),(41,15)),('L',(32,24)),('L',(39,31)),('C',(42,36),(41,33),(42,34)),('C',(36,42),(42,40),(40,42)),('C',(31,39),(34,42),(33,41)),('L',(24,32)),('L',(17,39)),('C',(12,42),(15,41),(14,42)),('C',(6,36),(8,42),(6,40)),('C',(9,31),(6,34),(7,33)),('L',(16,24)),('L',(9,17)),('C',(6,12),(7,15),(6,14))],True)
poly('pad',(24,16),(32,24),(24,32),(16,24),closed=True);join('cross','pad')
""")
design('beach-palm-water','SQUARE','umbrella','A deliberately tilted beach umbrella sits above a regular wave run. The canopy reaches its exact top extreme with a smooth tangent; omitted the tiny top spike.', """
path('canopy',(10,24), [('C',(29,6),(10,13),(20,6)),('C',(38,12),(33,6),(36,8)),('L',(24,18)),('L',(10,24))],True)
line('pole',(24,18),(29,30));join('pole','canopy')
path('water',(6,42), [('C',(12,38),(9,42),(9,38)),('C',(18,42),(15,38),(15,42)),('C',(24,38),(21,42),(21,38)),('C',(30,42),(27,38),(27,42)),('C',(36,38),(33,42),(33,38)),('C',(42,42),(39,38),(39,42))])
""")
design('bendy-bus','HRECT_L','bus','A rounded bus body has integrated wheel arches and two matching circular wheels. The chassis joins exact left/right wheel endpoints; windows share one horizontal band.', """
path('body',(4,32), [('L',(4,12)),('A',(8,8),4,4,True),('L',(16,8)),('L',(28,8)),('L',(36,8)),('A',(44,16),8,8,True),('L',(44,24)),('L',(44,32)),('L',(40,32)),('L',(32,32)),('L',(16,32)),('L',(8,32)),('L',(4,32))],True)
poly('window-base',(4,24),(16,24),(28,24),(44,24));join('window-base','body')
for x in (16,28):
 line(f'pillar-{x}',(x,8),(x,24));join(f'pillar-{x}','body');join(f'pillar-{x}','window-base')
for x in (12,36):
 path(f'wheel-{x}',(x-4,32), [('L',(x-4,36)),('A',(x+4,36),4,4,False),('L',(x+4,32))])
 join(f'wheel-{x}','body')
""")
design('basketball basketball-ball','CIRCLE','volleyball','A true circular ball has orthogonal seams and two smooth mirrored side curves, with exact perimeter junctions. Removed the conversion kinks.', """
path('outline',(24,4), [('A',(36,8),20,20,True),('A',(44,24),20,20,True),('A',(36,40),20,20,True),('A',(24,44),20,20,True),('A',(12,40),20,20,True),('A',(4,24),20,20,True),('A',(12,8),20,20,True),('A',(24,4),20,20,True)],True)
poly('vertical',(24,4),(24,24),(24,44));poly('horizontal',(4,24),(14,24),(24,24),(34,24),(44,24))
for side in (-1,1):
 x=lambda d:24+side*d
 path(f'curve-{side}',(x(12),8), [('C',(x(10),24),(x(10),12),(x(10),18)),('C',(x(12),40),(x(10),30),(x(10),36))])
 join(f'curve-{side}','horizontal');join(f'curve-{side}','outline')
join('vertical','horizontal');join('vertical','outline');join('horizontal','outline')
""")
design('bag-1e030fe3 bag-d97bc915 bag-e213494f','VRECT_L','shopping-bag','A structured shopping bag retains its straight-sided base; paired tapered walls and a semicircular handle use shared rim nodes. Removed the faceted handle.', """
path('handle',(16,16), [('L',(16,12)),('A',(32,12),8,8,True),('L',(32,16))])
poly('bag',(12,16),(16,16),(32,16),(36,16),(40,44),(8,44),closed=True);join('handle','bag')
""")

design('ant-uncategorized-03','VRECT_L','bug','A circular head has exact antenna junctions; a generous gap separates it from the rounded body. Paired antennae and legs are derived from one axis.', """
path('head',(21,9), [('A',(27,9),5,5,True),('A',(29,13),5,5,True),('A',(19,13),5,5,True),('A',(21,9),5,5,True)],True)
path('body',(18,31), [('A',(24,27),6,4,True),('A',(30,31),6,4,True),('L',(30,38)),('A',(18,38),6,6,True),('L',(18,31))],True)
for side in (-1,1):
 x=lambda d:24+side*d
 line(f'antenna-{side}',(x(3),9),(x(10),4));join(f'antenna-{side}','head')
 poly(f'leg-top-{side}',(x(6),31),(x(12),27),(x(16),31))
 poly(f'leg-bottom-{side}',(x(6),38),(x(12),36),(x(16),44))
 join(f'leg-top-{side}','body');join(f'leg-bottom-{side}','body')
""")
design('binocular','HRECT_L','binoculars','Two equal objective lenses have four units of ink clearance. Tapered barrels and a short bridge use exact shared endpoints; removed the crowded center overlap.', """
for side in (-1,1):
 x=lambda d:24+side*d
 cx=x(12)
 circle(f'lens-{side}',cx,32,8)
 path(f'barrel-{side}',(x(20),32), [('L',(x(16),8)),('L',(x(8),8)),('L',(x(4),20)),('L',(x(4),32))])
 join(f'barrel-{side}',f'lens-{side}')
line('bridge',(20,20),(28,20));join('bridge','barrel--1');join('bridge','barrel-1')
""")
design('bikini','HRECT_L',None,'Two mirrored smooth cups have a clear center bridge and crossed shoulder ties. Rebalanced the cups to remove the pinched central opening.', """
for side in (-1,1):
 x=lambda d:24+side*d
 path(f'cup-{side}',(x(14),20), [('C',(x(4),32),(x(8),24),(x(4),27)),('C',(x(12),40),(x(4),38),(x(7),40)),('C',(x(20),32),(x(17),40),(x(20),38)),('C',(x(14),20),(x(20),27),(x(17),22))],True)
 poly(f'tie-{side}',(x(14),20),(24,8),(x(-6),8));join(f'tie-{side}',f'cup-{side}')
line('bridge',(20,32),(28,32));join('bridge','cup--1');join('bridge','cup-1');join('tie--1','tie-1')
""")

design('archery-bow','SQUARE','bow-arrow','A taut string and smooth bowed limb share endpoints. The arrow crosses at an exact shared node, with its head moved clear of the bow to remove tiny enclosed gaps.', """
path('bow',(6,6), [('C',(30,18),(16,6),(24,12)),('C',(42,42),(36,24),(42,32))])
poly('string',(6,6),(6,42),(42,42))
poly('arrow',(6,42),(30,18),(42,6))
poly('arrowhead',(32,6),(42,6),(42,16))
join('bow','string');join('bow','arrow');join('arrow','string');join('arrow','arrowhead')
""")

def main():
 rows=json.loads((WORK/'selected.json').read_text()); reg=factories();result=[]
 prior={r['parent']:r for r in json.loads((WORK/'batch.json').read_text())} if (WORK/'batch.json').exists() else {}
 for row in rows:
  name=row['icon_id']; key,ref,plan,body=D[name]
  if name in prior:
   p=ROOT/prior[name]['path'];newid=prior[name]['icon_id']; tree=ast.parse(p.read_text())
  else:
   dest,newid,source=prepare_variant(name,'solo','AI stroke review · first 50')
   tree=ast.parse(source)
   mod=sys.modules[reg[name].__module__];sourceid=getattr(mod,'SOURCE_ICON_ID',None)
   p=dest.with_name(dest.stem+'_'+sourceid.replace('-','_')+'.py') if sourceid else dest
  cls=next(n for n in tree.body if isinstance(n,ast.ClassDef))
  tree.body=[n for n in tree.body if not (isinstance(n,ast.Expr) and isinstance(n.value,ast.Constant) and isinstance(n.value.value,str))]
  for n in tree.body:
   if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUTHOR' for t in n.targets):n.value=ast.Constant(AUTHOR)
  for n in cls.body:
   if isinstance(n,ast.Assign):
    for t in n.targets:
     if isinstance(t,ast.Name) and t.id=='keyshape':n.value=ast.Attribute(value=ast.Name(id='Keyshape',ctx=ast.Load()),attr=key,ctx=ast.Load())
     if isinstance(t,ast.Name) and t.id=='keywords':n.value=ast.Tuple(elts=[ast.Constant(v) for v in tuple(row.get('keywords',[]))+('solo-ai-first50',)],ctx=ast.Load())
  cls.body=[n for n in cls.body if not isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))]
  header=f'    def build(self):\n        # Plan: {plan}\n        # Reference: '+(f'Lucide original/{ref}.svg and atomic-debug/{ref}.svg.' if ref else 'No useful exact Lucide match; geometric construction from the supplied subject.')+'\n'
  func=header+HELPERS+textwrap.indent(body.strip(),'        ')+'\n'
  cls.body.append(ast.parse(textwrap.dedent(func)).body[0]);ast.fix_missing_locations(tree)
  # Keep the compact authored body readable, including the construction plan.
  rendered=ast.unparse(tree); pos=rendered.index('    def build(');rendered=rendered[:pos]+func
  p.write_text(f'"""{name}: AI stroke review; parent retained for comparison."""\n'+rendered+'\n')
  result.append(dict(parent=name,icon_id=newid,path=str(p.relative_to(ROOT)),keyshape=key,reference=ref,plan=plan))
 (WORK/'batch.json').write_text(json.dumps(result,indent=2));print(f'Authored {len(result)} variants')
if __name__=='__main__': main()
