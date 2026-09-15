from edit_batch import revise,remove_named
SOURCE_ICON_ID=None
SOURCE_PATH='/Users/jakesdev/Downloads/feedback-briefs 2/solo'
AUTHOR='gpt-6'
revise(35,'Give the Merlion a rounded mane and projecting muzzle, a smoother fish body, and a curved spout that visibly leaves its mouth.',keyshape='SQUARE',body="""
path('lion-fish',(14,16),[('L',(20,16)),('L',(20,10)),('A',(28,6),8,4,True),('C',(42,20),(37,6),(42,12)),('L',(42,28)),('C',(28,42),(42,36),(36,42)),('L',(14,42)),('L',(24,32)),('L',(24,26)),('L',(14,26)),('A',(14,16),5,5,True)],True)
dot('eye',(30,17))
path('water',(9,21),[('C',(6,36),(6,25),(6,31))]);join('water','lion-fish')
""",ref='Lucide cat and fish: rounded head mass and a coherent aquatic body; asymmetric statue profile')
revise(58,'Rebuild the seated baby as a larger circular head, short upright torso and bent arms and legs, replacing the cloud-like body outline.',keyshape='SQUARE',body="""
oval('head',24,13,7,7)
line('torso',(24,28),(24,34))
for name,side in [('left',-1),('right',1)]:
 poly('arm-'+name,(24,28),(24+side*10,32),(24+side*14,24))
 poly('leg-'+name,(24,34),(24+side*10,42),(24+side*18,42))
 join('arm-'+name,'torso');join('leg-'+name,'torso')
join('arm-left','arm-right');join('leg-left','leg-right')
self.mark_human_figure('baby',head='head',torso='torso',torso_junction='start')
""",ref='Shared full_body_ref.png: circular head, bent seated limbs, exact 4-unit head-to-torso ink gap')
revise(82,'Replace the segmented shell with one true oval, give it a centered seam, and attach matching leg fans to its sides.',keyshape='VRECT_L',body="""
oval('head',24,10,6,6);oval('shell',24,30,10,14);join('head','shell')
line('seam',(24,16),(24,44));join('seam','shell');join('seam','head')
for side in [-1,1]:
 for j,y in enumerate([20,30,40]):
  n=f'leg-{side}-{j}';line(n,(24+side*10,30),(24+side*16,y));join(n,'shell')
 for a,b in [(0,1),(0,2),(1,2)]:join(f'leg-{side}-{a}',f'leg-{side}-{b}')
""",ref='Lucide bug: one shell, a center seam and repeated mirrored legs')
revise(87,'Use exact paired quarter-ellipses for the opposing claws, broaden the upper body curve, and give each leg a shared side attachment.',keyshape='SQUARE',body="""
path('body',(12,27),[('A',(36,27),12,8,True),('A',(12,27),12,11,True)],True)
for side in [-1,1]:
 x=lambda d:24+side*d
 path(f'claw-{side}',(x(18),6),[('A',(x(12),16),6,10,side==1),('A',(x(6),6),6,10,side==1)])
 line(f'arm-{side}',(x(12),27),(x(12),16));join(f'arm-{side}','body');join(f'arm-{side}',f'claw-{side}')
 poly(f'leg-{side}',(x(12),27),(x(18),34),(x(18),42));join(f'leg-{side}','body');join(f'leg-{side}',f'arm-{side}')
""")
revise(91,'Enlarge the bill and round the breast and tail into a coherent duck outline; place the eye inside the round head.',keyshape='HRECT_L',body="""
path('duck',(20,18),[('A',(30,8),10,10,True),('A',(38,16),8,8,True),('L',(44,16)),('L',(44,24)),('L',(38,24)),('C',(24,40),(38,34),(32,40)),('C',(4,24),(12,40),(4,34)),('L',(4,20)),('C',(14,28),(8,26),(10,28)),('C',(20,22),(18,28),(20,27)),('L',(20,18))],True)
dot('eye',(30,18))
""",ref='Lucide bird: round head, dot eye, and one coherent silhouette')
revise(92,'Round the raised wing and simplify the flying bird into a swept wing, small head, projecting bill and curved belly.',keyshape='SQUARE',body="""
path('bird',(6,30),[('L',(6,6)),('C',(24,18),(14,8),(20,12)),('L',(26,24)),('C',(30,20),(29,26),(30,24)),('A',(38,20),4,6,True),('L',(42,24)),('L',(38,27)),('C',(24,42),(38,36),(33,42)),('C',(6,30),(14,42),(6,38))],True)
""",ref='Lucide bird: distinguish the bill and head from the larger wing and belly')
revise(93,'Connect the open jaw to the muzzle through a smooth throat return, closing the broken head contour without a detached line.',patch=lambda s:s+"\n    path('throat',(31,30),[('C',(31,39),(27,30),(27,37))])\n    join('throat','head')\n    join('throat','jaw')\n",ref='Lucide dog: one connected head outline with a clearly projecting muzzle')
revise(94,'Enlarge the upper tail lobe by six units while preserving the broad lower lobe and geometric hammer-shaped head.',patch=lambda s:s.replace('(42, 22)','(42, 16)'))
revise(95,'Broaden the lower jaw toward the face and replace its short arc with a smooth, deep curve so the open mouth is unmistakable.',patch=lambda s:s.replace("self.add_arc('lower-jaw-1', (42, 32), (35, 42), radius_x=11)","self.add_bezier('lower-jaw-1',(42,32),((42,40),(34,42),(28,42)))").replace("(35, 42), (22, 42)","(28,42),(14,42)"))
revise(96,'Widen the ear group and deepen its central notch; bring the back of the neck into the enlarged head.',patch=lambda s:s.replace('(30, 14)','(26, 14)').replace('(30, 6)','(26, 6)').replace('(36, 10)','(34, 12)'),ref='Lucide dog and cat: clear ear silhouettes; deliberate howling profile')
revise(99,'Rebuild the wolf head with a broad pointed ear, sloping forehead, long muzzle and defined lower jaw; keep one clear eye.',keyshape='SQUARE',body="""
poly('profile',(6,42),(8,24),(14,6),(24,16),(32,18),(36,24),(42,26),(38,34),(30,34),(22,42))
dot('eye',(22,25))
""",ref='Lucide dog and cat: sparse facial features and a strong ear/muzzle silhouette')
revise(101,'Make the cockatoo crest distinct and extend its hooked beak; round the crown and neck while keeping a single dot eye.',keyshape='VRECT_L',body="""
path('head',(8,44),[('L',(8,23)),('C',(16,10),(8,16),(12,10)),('L',(12,4)),('C',(28,12),(22,4),(26,8)),('A',(34,24),8,12,True),('C',(40,28),(40,24),(40,26)),('L',(40,36)),('C',(32,34),(36,36),(34,35)),('A',(22,44),10,10,True)])
dot('eye',(23,23))
""",ref='Lucide bird: coherent head contour and dot eye; preserve the cockatoo crest and hook')
revise(106,'Replace the uncertain left body curvature with an exact quarter-circle and a tangent vertical join; keep the bill and dorsal fin distinct.',patch=lambda s:s.replace("self.add_arc('body-1', (8, 22), (20, 12), radius_x=32, radius_y=26, sweep=True)","self.add_arc('body-1',(6,26),(20,12),radius_x=14,radius_y=14,sweep=True)").replace("self.add_bezier('body-9', (6, 30), *(((6, 27.04328859), (6.24779087, 23.94368014), (8, 22)),))","self.add_line('body-9',(6,30),(6,26))").replace("(8, 22), (7, 6)","(6,26),(7,6)"),ref='Lucide fish: coherent body curves with deliberate angular fins')
revise(110,'Give the penguin a rounder forward belly and a sharper downward-pointing bill, opening up its left profile.',patch=lambda s:s.replace("((15, 39), (14, 29), (15, 25))","((10,42),(10,32),(14,28))").replace('(15, 25), (8, 26)','(14,28),(8,26)'),ref='Lucide bird: a clear bill and one open inner wing curve')
revise(115,'Round the seated fox back and hindquarters, and make the raised tail flow into the base with a continuous tangent.',patch=lambda s:s.replace("self.add_arc('base-right', (42, 30), (27, 42), radius_x=16, radius_y=16, sweep=True)","self.add_bezier('base-right',(42,30),((42,38),(35,42),(27,42)))").replace("self.add_line('back', (6, 41), (6, 19))","self.add_bezier('back',(6,41),((6,34),(8,26),(6,19)))"),ref='Lucide cat: pointed ears above a simple curved body')
revise(119,'Rebuild the snake with a larger round head, a short forked tongue and two generous S-bends with tangent straight runs.',keyshape='SQUARE',body="""
oval('head',30,12,6,6)
path('body',(24,12),[('L',(14,12)),('A',(14,26),8,7,False),('L',(28,26)),('A',(28,42),8,8,True),('L',(12,42))]);join('head','body')
line('tongue',(36,12),(38,12));poly('fork',(42,8),(38,12),(42,16));join('head','tongue');join('tongue','fork')
""")
revise(121,'Open the web into a taller six-spoke construction with one scalloped outer ring and no inner polygon; derive every spoke from the same center.',keyshape='CIRCLE',body="""
from itertools import combinations
points=[(24,4),(40,12),(40,36),(24,44),(8,36),(8,12)]
controls=[((28,10),(34,13)),((33,18),(33,30)),((34,35),(28,38)),((20,38),(14,35)),((15,30),(15,18)),((14,13),(20,10))]
nodes=[]
for j,(a,b) in enumerate(zip(points,points[1:]+points[:1])):
 c,d=controls[j];path(f'web-{j}',a,[('C',b,c,d)]);line(f'ray-{j}',a,(24,24));nodes.extend([(f'web-{j}',{a,b}),(f'ray-{j}',{a,(24,24)})])
for (a,p),(b,q) in combinations(nodes,2):
 if p&q:join(a,b)
""")
revise(123,'Simplify the fox head to a pointed ear and one clear triangular muzzle; remove the small forehead and jaw curves.',patch=lambda s:remove_named(s,{'forehead','ear','brow','muzzle','jaw','upper'}).replace("self.add_arc('chest', (36, 34), (32, 38), radius_x=4, radius_y=4, sweep=False)","self.add_arc('chest',(34,32),(32,38),radius_x=6,radius_y=6,sweep=False)")+"\n    self.add_polyline('head-new',(26,16),(28,6),(34,18),(42,24),(34,32))\n    self.add_contour('upper','hip-top','back','neck','head-new-1','head-new-2','head-new-3','head-new-4','chest','foreleg')\n    self.relate('connect','upper','tail')\n    self.relate('connect','upper','belly')\n",ref='Lucide cat: economical pointed ears and muzzle')
revise(125,'Make both owl ear tufts truly triangular and mirrored; round the lower face symmetrically and center the eyes and beak.',keyshape='SQUARE',body="""
path('owl',(6,24),[('L',(6,6)),('L',(16,12)),('L',(32,12)),('L',(42,6)),('L',(42,24)),('A',(24,42),18,18,True),('A',(6,24),18,18,True)],True)
for x in [16,32]:dot('eye-'+str(x),(x,24))
poly('beak',(22,31),(24,33),(26,31))
""",ref='Lucide cat: paired triangular ears and mirrored dot eyes')
revise(128,'Replace the plain oval sheep body with broad wool scallops, a dropped oval head and two short legs attached to a level belly.',keyshape='SQUARE',body="""
path('fleece',(36,26),[('C',(28,38),(36,34),(32,38)),('L',(16,38)),('C',(6,26),(10,38),(6,32)),('C',(12,16),(6,20),(8,16)),('C',(22,10),(10,10),(16,6)),('C',(28,10),(24,6),(28,6))])
path('head',(28,10),[('C',(36,26),(28,18),(30,26)),('C',(42,10),(40,26),(42,18)),('C',(28,10),(42,6),(28,6))],True);join('head','fleece')
line('ear',(42,10),(42,6));join('ear','head')
for x in [16,28]:line('leg-'+str(x),(x,38),(x,42));join('leg-'+str(x),'fleece')
""")
revise(131,'Enlarge and round the whale forehead, then flow its back into the raised tail with matching tangents and a broad smooth belly.',patch=lambda s:s.replace("('C', (16, 20), (6, 24), (10, 20)), ('C', (32, 24), (24, 20), (32, 32))","('C',(18,18),(6,23),(11,18)),('C',(32,24),(25,18),(32,30))"),ref='Lucide fish: one smooth body contour with a distinct tail')
revise(132,'Rebuild the mirrored wings and join the abdomen to exact shared nodes on their inner edges, eliminating the offset body endpoints.',keyshape='SQUARE',body="""
poly('thorax',(18,12),(30,12),(30,20),(18,20),closed=True)
line('antenna-left',(18,12),(14,6));line('antenna-right',(30,12),(34,6));join('thorax','antenna-left');join('thorax','antenna-right')
for side in [-1,1]:
 x=lambda d:24+side*d
 path(f'wing-{side}',(x(6),20),[('C',(x(18),36),(x(14),24),(x(18),31)),('L',(x(10),40)),('L',(x(8),30)),('L',(x(6),20))],True);join(f'wing-{side}','thorax')
path('abdomen',(16,30),[('A',(32,30),8,12,False)]);join('abdomen','wing--1');join('abdomen','wing-1')
""",ref='Lucide bug: body and mirrored limbs meet at shared construction nodes')
revise(133,'Enlarge the lion head into a rounded mane with a projecting side muzzle; simplify the wing and remove its crowded inner seam.',keyshape='SQUARE',body="""
path('lion',(12,18),[('L',(12,10)),('L',(12,6)),('L',(18,10)),('C',(24,24),(26,8),(26,18)),('L',(30,10)),('L',(42,6)),('C',(36,28),(42,16),(40,24)),('C',(42,34),(40,28),(42,30)),('L',(42,42)),('L',(36,42)),('L',(32,34)),('L',(22,34)),('L',(18,42)),('L',(10,42)),('L',(14,34)),('L',(12,30)),('A',(6,24),6,6,True),('A',(12,18),6,6,True)],True)
""",ref='Lucide cat and dog: a projecting muzzle and rounded head; deliberate side profile')
revise(135,'Add a clearly positioned dot eye below the horns, giving the triceratops head a readable face while preserving its frill and horn silhouette.',patch=lambda s:s+"\n    self.add_dot('eye',(25,32))\n",ref='Lucide animal icons: a single well-spaced dot eye anchors a complex silhouette')
revise(158,'Enlarge the forked tail and projecting pectoral fin, preserving a broad curved back and a clear inner belly.',patch=lambda s:s.replace('(26, 42)','(32, 42)').replace('(14, 39)','(18, 38)').replace('(27, 16)','(30, 14)'),ref='Lucide fish: angular fins attached to a coherent curved body')
revise(161,'Replace the flattened head with a true vertical oval, mirror both oval ears, and attach a simple curled trunk below the face.',keyshape='SQUARE',body="""
oval('face',24,18,10,12)
for n,x in [('left',10),('right',38)]:oval('ear-'+n,x,18,4,12);join('ear-'+n,'face')
path('trunk',(24,30),[('L',(24,36)),('A',(30,42),6,6,False),('A',(36,36),6,6,False)]);join('trunk','face')
""")
revise(162,'Replace the zero-length eye line with a centered dot and rebuild the crown and hooked beak using fewer smooth curves.',keyshape='SQUARE',body="""
path('head',(6,42),[('L',(6,24)),('C',(24,6),(6,14),(14,6)),('C',(36,14),(30,6),(34,9)),('C',(28,28),(36,22),(32,26)),('L',(28,30)),('L',(28,42))])
path('beak',(36,14),[('C',(42,30),(42,16),(42,24)),('L',(28,30))]);join('head','beak');dot('eye',(23,17))
""",ref='Lucide bird: a dot eye inside a coherent round head')
revise(170,'Widen each pin neck to eight centerline units, stagger the larger center pin below the rear pair, and use level collars with clear enclosed gaps.',keyshape='HRECT_L',body="""
for n,cx in [('left',8),('right',40)]:
 path(n,(cx-4,12),[('A',(cx+4,12),4,4,True),('L',(cx+4,18)),('L',(cx+4,24)),('A',(cx-4,24),4,4,True),('L',(cx-4,18)),('L',(cx-4,12))],True)
 line(n+'-collar',(cx-4,18),(cx+4,18));join(n,n+'-collar')
path('center',(20,22),[('A',(28,22),4,4,True),('L',(28,28)),('L',(28,30)),('C',(29,36),(28,32),(29,34)),('C',(24,40),(29,40),(27,40)),('C',(19,36),(21,40),(19,40)),('C',(20,30),(19,34),(20,32)),('L',(20,28)),('L',(20,22))],True)
line('center-collar',(20,28),(28,28));join('center','center-collar')
""")
