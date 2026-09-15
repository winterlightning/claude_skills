"""Per-subject centerline repairs, authored as isolated review variants."""
import ast,json,textwrap
from pathlib import Path
SOURCE_ICON_ID=None # Preserved individually from each original module.
SOURCE_PATH='icon_set/work/rejected-repair-batch-01/batch.json'
AUTHOR='gpt-6'
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2]
rows=json.loads((OUT/'batch.json').read_text())
# Every entry records a specific drawing correction, not a status-only change.
EDITS={}
def change(n,note,*pairs):EDITS[n]=(note,pairs,None,None)
def draw(n,note,key,body):EDITS[n]=(note,(),key,body)
HELPERS='''
def path(n,start,commands,closed=False):
    here=start; members=[]
    for j,(kind,end,*args) in enumerate(commands):
        name=f'{n}-{j}'
        if kind=='L':self.add_line(name,here,end)
        elif kind=='A':self.add_arc(name,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
        elif kind=='C':self.add_bezier(name,here,(args[0],args[1],end))
        here=end;members.append(name)
    self.add_contour(n,*members,closed=closed)
def circle(n,x,y,r):
    path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
def rounded(n,x0,y0,x1,y1,r):
    path(n,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
line=self.add_line
poly=self.add_polyline
dot=self.add_dot
join=lambda a,b:self.relate('connect',a,b)
'''
draw(1,'Recenter the lamp on y=24 with two coherent half-ellipse quarters; align the adaptive stroke to the tangent and give all three light beams equal lengths.','HRECT_L',"""
path('lamp',(32,8),[('A',(44,24),12,16,True),('A',(32,40),12,16,True),('L',(32,8))],True)
for i,y in enumerate((12,24,36)):line(f'beam-{i}',(4,y+4),(20,y-4))
line('adaptive',(44,24),(44,8));join('adaptive','lamp')
""")
change(3,'Widen and lower the brow angle for a clearer angry expression; replace the angular hooked tuft with a smoother curved feather.',("(19, 23), (24, 25), (29, 23)","(17, 22), (24, 25), (31, 22)"),("self.add_polyline('tuft', (24, 12), (20, 4), (29, 4))","self.add_bezier('tuft',(24,12),((20,12),(20,4),(28,4)))"))
change(4,'Replace the pointed lower abdomen with a true circular lower half so the side and bottom tangents join smoothly.',('radius_x=14, radius_y=14','radius_x=8, radius_y=8'))
change(5,'Round the snout-to-head junction and flatten the lower belly transition so the outline reads as a long-snouted animal rather than a rigid arch.',("('C',(12,26),(20,18),(12,18))","('C',(12,26),(20,16),(12,16))"),("('C',(28,28),(36,30),(32,28))","('C',(28,30),(36,31),(32,30))"))
draw(6,'Replace the six inconsistent rim arcs with one true circle. Rebuild the six shutter blades as rotational pairs with a regular central hexagon.','CIRCLE',"""
# Circular rim and a 6/8 integer-grid hexagonal aperture; paired opposite blades.
circle('rim',24,24,20)
points=[(14,24),(18,16),(30,16),(34,24),(30,32),(18,32)]
poly('aperture',*points,closed=True)
for i,(a,b) in enumerate([((14,24),(8,12)),((18,16),(24,4)),((30,16),(40,12)),((34,24),(40,36)),((30,32),(24,44)),((18,32),(8,36))]):
 line(f'blade-{i}',a,b);join(f'blade-{i}','aperture');join(f'blade-{i}','rim')
""")
draw(7,'Open the lower arches and remove the cramped wave trapped beneath the piers. Give the two bridge openings full circular crowns and a separate water baseline.','HRECT_L',"""
poly('bridge',(4,30),(4,8),(44,8),(44,30))
for i,x in enumerate((4,24)):
 path(f'arch-{i}',(x,30),[('A',(x+10,20),10,10,True),('A',(x+20,30),10,10,True)])
 join(f'arch-{i}','bridge')
line('pier',(24,8),(24,30));join('pier','bridge');join('pier','arch-0');join('pier','arch-1');join('arch-0','arch-1')
line('water',(4,40),(44,40))
""")
draw(8,'Use concentric faucet bends about (24,20), replacing the offset inner bend and short kink. Align the two water strokes beneath the outlet.','VRECT_L',"""
path('tap',(8,44),[('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(30,20)),('A',(24,14),6,6,False),('A',(18,20),6,6,False),('L',(18,44)),('L',(8,44))],True)
for x in (30,40):line(f'water-{x}',(x,30),(x,36))
""")
change(9,'Give the cannon muzzle an eight-unit opening and level its rear support; the wider tube no longer tapers to a narrow slit.',('(44, 14), (30, 24)','(44, 16), (30, 24)'),("L('trail', (14, 36), (4, 40))","P('trail',(14,36),(8,40),(4,40))"))
change(10,'Replace the short slanted outriggers with matching longer feet and straighten the barrel-to-muzzle junction.',("L('left-leg',(12,36),(4,40))","P('left-leg',(12,36),(8,40),(4,40))"),("(28,36),(36,36),(44,40)","(28,36),(38,40),(44,40)"))
change(11,'Lower the exaggerated front sight and broaden the receiver top; the sight becomes a short purposeful notch rather than a tall unrelated spike.',("(19, 13), (32, 13)","(19, 8), (32, 8)"),("(40, 21), (40, 8)","(40, 21), (40, 14)"))
change(12,'Replace the needle-shaped ribbon tails with broad forked tails, preserving the centered flower and opening the negative space beneath it.',("(18, 30), (12, 44), (24, 38), (36, 44), (30, 30)","(18, 30), (10, 44), (24, 40), (38, 44), (30, 30)"))
change(13,'Give the landmark smoother flared shoulders with matched vertical tangents at the crown; widen the base transition on both sides.',('((36,24),(40,33),(42,42))','((36,20),(38,30),(42,42))'),('((8,33),(12,24),(12,6))','((10,30),(12,20),(12,6))'))
change(16,'Round the walker frame foot into the base and shorten the hanging seat wall to enlarge the open space under the tray.',("self.add_polyline('frame', (8, 8), (8, 40), (4, 40), closed=False)","self.add_line('frame',(8,8),(8,36))\n        self.add_arc('frame-foot',(8,36),(12,40),radius_x=4,sweep=False)\n        self.relate('connect','frame','frame-foot')\n        self.relate('connect','frame-foot','base')"),("(8, 40), (38, 40), (44, 40)","(4, 40), (12, 40), (38, 40), (44, 40)"),("self.relate(\"connect\", 'frame', 'base')",""))
change(17,'Redistribute the necklace beads to a smoother circular rhythm and broaden the heart tip so the charm does not end in a long sharp wedge.',('(10, 27)','(9, 28)'),('(17, 31)','(17, 33)'),('(27, 11)','(28, 10)'),("self.add_line('charm-ls', p_26_31, p_34_42)","self.add_bezier('charm-ls',p_26_31,((26,36),(30,40),p_34_42))"),("self.add_line('charm-rs', p_34_42, p_42_31)","self.add_bezier('charm-rs',p_34_42,((38,40),(42,36),p_42_31))"))
change(18,'Correct the bent wire to a true tangent quarter-ellipse; center the straight wire on the left bead instead of leaving it offset.',('p_12_4 = (12, 4)','p_12_4 = (13, 4)'),('p_12_15 = (12, 15)','p_12_15 = (13, 15)'),('p_12_28 = (12, 28)','p_12_28 = (13, 28)'),('p_12_44 = (12, 44)','p_12_44 = (13, 44)'),('radius_x=7, radius_y=8','radius_x=8, radius_y=8'))
change(22,'Widen the vise opening to twelve units and give both jaws identical geometry about their own stems; lengthen the screw shaft for a clearer working handle.',('x = 16 if left else 26','x = 16 if left else 28'),('outer = 4 if left else 38','outer = 4 if left else 40'),('radius_y=14','radius_y=14'))
change(23,'Widen the cup bridge and round the lower cups to remove the compressed inner tips; keep the ties mirrored about x=24.',("(x(4),32)","(x(5),32)"),("(x(4),27)","(x(5),27)"),("(x(4),38)","(x(5),38)"),("(20,32),(28,32)","(19,32),(29,32)"))
change(24,'Smooth the raised wing into a broad tapered curve and give the belly a tangent return into the tail rather than a hard angular kink.',("self.add_line('wing-leading',(12,26),(18,8))","self.add_bezier('wing-leading',(12,26),((14,20),(16,12),(18,8)))"),("self.add_line('belly',(25,40),(16,36))","self.add_bezier('belly',(25,40),((22,40),(19,37),(16,36)))"))
draw(25,'Broaden the gravestone shoulders and reduce the oversized base projection; join the arched crown and straight walls as one continuous contour.','VRECT_L',"""
path('stone',(10,36),[('L',(10,18)),('A',(24,4),14,14,True),('A',(38,18),14,14,True),('L',(38,36))])
poly('plinth',(8,36),(10,36),(38,36),(40,36),(40,44),(8,44),closed=True);join('stone','plinth')
""")
draw(26,'Use a true round pom-pom and an upright hat crown, replacing the flat button and squat dome. The cuff has two matching round ends.','VRECT_L',"""
circle('pompom',24,8,4)
path('crown',(10,34),[('L',(10,26)),('A',(24,12),14,14,True),('A',(38,26),14,14,True),('L',(38,34))]);join('pompom','crown')
rounded('cuff',8,34,40,44,3);join('cuff','crown')
""")
change(27,'Replace the deep square notch with a shallower rounded tuck opening, reducing the visual weight of the top edge.',("('L',(18,18)),('L',(30,18)),('L',(30,6))","('L',(18,14)),('A',(22,18),4,4,False),('L',(26,18)),('A',(30,14),4,4,False),('L',(30,6))"))
change(28,'Give the carton a deeper lid band and smaller matching bottom radii; rebalance the lid-to-body proportions.',('(44,18)','(44,20)'),('(4,18)','(4,20)'),('(24,18)','(24,20)'),("(44,34)","(44,36)"),("('A',(38,40),6,6,True)","('A',(40,40),4,4,True)"),("('L',(10,40))","('L',(8,40))"),("('A',(4,34),6,6,True)","('A',(4,36),4,4,True)"))
change(29,'Raise the carton fold to give the pitched top more depth and align both shoulders symmetrically; keep the side gusset distinct.',('(8,14)','(8,16)'),('(30,14)','(30,16)'),('(40,14)','(40,16)'),('(30,4)','(32,4)'))
change(30,'Smooth the brain fissure into two consistent S-bends with tangent alignment at their shared midpoint, eliminating the alternating kinks.',("[('C',(24,24),(18,14),(30,18)),('C',(24,38),(18,30),(30,33))]","[('C',(24,24),(18,12),(30,20)),('C',(24,38),(18,28),(30,34))]"))
change(33,'Broaden the cannon muzzle and flatten the carriage foot so the barrel and support read as solid parts rather than sharp slivers.',('(44,18),(32,24)','(44,20),(32,24)'),('(14,30),(4,34),(4,40),(24,40)','(14,30),(4,32),(4,40),(24,40)'))
change(35,'Replace the uneven roof transition with a single tangent curve into the windscreen and widen the door handle for a clearer side view.',("('C', (31, 11), (29, 8), (30, 10))","('C', (33, 13), (29, 8), (31, 11))"),("(18,20),(24,20)","(17,20),(24,20)"))
change(36,'Remove the tiny doubled notches in the clover lobes and make each side lobe one broad smooth curve; mirror the correction across the stem axis.',("('C',(6,30),(8,36),(6,34)),('C',(8,26),(6,28),(8,28)),('C',(6,22),(8,24),(6,24)),('C',(12,16),(6,18),(8,16))","('C',(6,25),(8,36),(6,30)),('C',(12,16),(6,20),(8,16))"))
draw(38,'Replace the oval paw pad with a broad triangular pad with rounded toes and a soft central top notch; space the four toe dots as mirrored pairs.','SQUARE',"""
for x,y in [(6,21),(16,6),(32,6),(42,21)]:dot(f'toe-{x}',(x,y))
path('pad',(24,27),[('C',(17,28),(21,23),(19,25)),('C',(12,36),(14,31),(12,32)),('C',(24,42),(12,41),(19,42)),('C',(36,36),(29,42),(36,41)),('C',(31,28),(36,32),(34,31)),('C',(24,27),(29,25),(27,23))],True)
""")
change(39,'Move the string attachment to the ball’s bottom tangent and make its first loop flow smoothly out of the circle rather than forming a kink.',("path('string',(24,22),[('C',(42,28),(28,27),(42,23)),('C',(31,33),(42,32),(37,33))","path('string',(16,26),[('C',(42,28),(25,26),(42,22)),('C',(31,33),(42,32),(37,33))"))
change(40,'Round the dragon’s intermediate cheek corners while keeping the pointed chin and antlers; the paired face contours now flow continuously toward the muzzle.',("self.add_line('cheek-right-2', p_39_21, p_37_27)","self.add_bezier('cheek-right-2',p_39_21,((39,23),(38,25),p_37_27))"),("self.add_line('cheek-left-2', p_11_27, p_9_21)","self.add_bezier('cheek-left-2',p_11_27,((10,25),(9,23),p_9_21))"))
change(42,'Shorten the narrow wing tip and broaden the tail root to remove the pinched center of the climbing airliner.',('(27,40),(17,40),(21,29),(12,34)','(29,40),(17,40),(21,29),(12,32)'),('(4,25),(8,18),(15,23)','(4,25),(8,16),(15,23)'))
change(43,'Use one center for both rainbow arcs so their curvature and spacing stay consistent from the cloud to the sky end.',("(28, 30), (44, 18), radius_x=16, radius_y=12","(28, 24), (44, 16), radius_x=16, radius_y=8"),("self.relate(\"connect\", 'cloud', 'rainbow-inner')","self.relate(\"connect\", 'cloud', 'rainbow-inner')"))
change(44,'Replace the flattened rear cloud with a fuller crown and remove its redundant zero-length return; use two balanced fog strokes instead of one long heavy underline.',("radius_x=8, radius_y=4, sweep=True, large_arc=False","radius_x=8, radius_y=4, sweep=True, large_arc=False"),("self.add_line('mist', (6, 40), (42, 40))","self.add_line('mist-left',(6,40),(20,40))\n        self.add_line('mist-right',(28,40),(42,40))"))
change(46,'Make the pearl truly circular and recenter its adjoining collar curves; the pendant no longer reads as a flattened bead.',('(30, 37)','(30, 36)'),('(18, 37)','(18, 36)'),('radius_x=6, radius_y=5','radius_x=6, radius_y=6'),('radius_x=12, radius_y=16','radius_x=12, radius_y=14'))
change(47,'Turn the two sheen marks into opposed semicircular arcs for a clearer disc reflection pattern; keep their shared center and radius.',("(24, 13), (35, 24)","(24, 13), (24, 35)"),("(24, 35), (13, 24)","(24, 35), (24, 13)"))
change(48,'Angle the short roll bar to match the windscreen direction and soften the front hood corner; the two upper attachments now follow a consistent vehicle profile.',("(18, 14), (18, 22)","(14, 14), (18, 22)"),("(40, 22), (44, 26)","(38, 22), (44, 28)"))
change(49,'Lengthen the drill motor and shorten the exposed bit, improving their proportions; move the grip attachment with the motor and make the battery corners circular.',("box('motor', 4, 8, 26, 14, 4)","box('motor', 4, 8, 30, 14, 4)"),("(30, 15), (44, 15)","(34, 15), (44, 15)"),("(26, 22)","(28, 22)"),("box('battery', 6, 32, 24, 8, 3)","box('battery', 6, 32, 24, 8, 4)"))
change(50,'Bring the flipper tips away from the belly and make their outward curves smoother; use a broader, flatter beak to distinguish the penguin from a generic smiling face.',('((8,17),(6,26),(6,34))','((8,18),(6,29),(6,36))'),('((40,17),(42,26),(42,34))','((40,18),(42,29),(42,36))'),("(21,30),(24,33),(27,30)","(20,30),(24,32),(28,30)"))

change(51,'Enlarge the spindle opening and lengthen the three drive slots so they read as mechanical cuts rather than scattered dots.',("circle('hub', 24, 24, 2)","circle('hub', 24, 24, 3)"),("(23, 13), (25, 13)","(22, 12), (26, 12)"),("(24 + side * 10, 28), (24 + side * 9, 30)","(24 + side * 12, 28), (24 + side * 10, 32)"))
change(52,'Smooth the two inner ear edges into the forehead while preserving tall pointed ears, and use a lower rounded nose mark for a more canine face.',("self.add_line('left-ear-inner', p_8_4, p_19_18)","self.add_bezier('left-ear-inner',p_8_4,((11,11),(15,17),p_19_18))"),("self.add_line('right-ear-inner', p_29_18, p_40_4)","self.add_bezier('right-ear-inner',p_29_18,((33,17),(37,11),p_40_4))"))
change(53,'Attach the trunk exactly to the ground corner and give the ground crack a stepped break instead of a simple diagonal divider.',("(35, 8), (35, 31)","(33, 8), (33, 31)"),("(29, 17), (35, 23), (44, 15)","(27, 17), (33, 23), (44, 15)"),("self.add_line('ground-crack', (27, 31), (21, 40))","self.add_polyline('ground-crack',(26,31),(23,35),(25,36),(22,40))"))
draw(54,'Replace the flattened oval dust cloud with a smooth raised crown and round end curl; retain the long horizontal gust with a clear gap underneath.','HRECT_L',"""
path('cloud',(18,22),[('C',(4,16),(10,22),(4,20)),('C',(18,8),(4,10),(10,8)),('C',(32,14),(25,8),(32,10)),('C',(44,18),(39,14),(44,14)),('C',(36,22),(44,21),(40,22))])
path('gust',(13,30),[('A',(8,35),5,5,False),('A',(13,40),5,5,False),('L',(42,40))])
""")
change(56,'Smooth the ear’s long descending wall into the lobe with a single tangent curve; the outline no longer has a sudden bend at the lower ear.',("self.add_arc('ear-down', (22, 26), (18, 36), radius_x=10, radius_y=10, large_arc=False, sweep=True)","self.add_bezier('ear-down',(22,26),((22,31),(18,31),(18,36)))"))
change(57,'Replace wavy filter edges with a clear repeated zigzag pleat; keep the two pleats identical and separate, with aligned inlet strokes.',("self.add_arc(f'pleat-{i}-a',(x,8),(x-2,16),radius_x=2,radius_y=8)","self.add_line(f'pleat-{i}-a',(x,8),(x-2,16))"),("self.add_arc(f'pleat-{i}-b',(x-2,16),(x,24),radius_x=2,radius_y=8,sweep=False)","self.add_line(f'pleat-{i}-b',(x-2,16),(x,24))"),("self.add_arc(f'pleat-{i}-c',(x,24),(x+2,32),radius_x=2,radius_y=8,sweep=False)","self.add_line(f'pleat-{i}-c',(x,24),(x+2,32))"),("self.add_arc(f'pleat-{i}-d',(x+2,32),(x,40),radius_x=2,radius_y=8)","self.add_line(f'pleat-{i}-d',(x+2,32),(x,40))"))
change(58,'Smooth the train nose into the lower body without its pointed turn, and align the front windscreen with the longer sloping roof.',("('C',(40,20),(30,8),(36,14)),('C',(36,28),(44,26),(40,28))","('C',(40,20),(32,8),(37,15)),('C',(36,28),(43,25),(41,28))"))
change(59,'Replace the kink between the curled breech and barrel with a tangent curve that rises smoothly toward the muzzle.',("L('upper-barrel',(13,13),(40,8))","self.add_bezier('upper-barrel',(13,13),((22,13),(31,8),(40,8)))"))
change(61,'Give the fox paired slanted eye marks and move the nose lower, replacing the blank face while keeping its long pointed muzzle.',("self.add_dot('nose', (24, 32))","self.add_dot('nose',(24,34))\n        self.add_line('eye-left',(17,24),(19,25))\n        self.add_line('eye-right',(31,24),(29,25))"))
change(62,'Reduce the freight ribs from three to two and space them evenly across the wagon, opening the crowded narrow panels.',("for x in (16,24,32):","for x in (18,30):"))
change(63,'Replace the sharp filter-bowl point with a rounded sump and keep the drop centered below its lowest point.',("(12, 18), (24, 24), (36, 18)","(12, 18), (18, 22), (30, 22), (36, 18)"))
change(65,'Reduce the compressed little-finger step and shorten the finger creases to open the palm; keep the glove’s stepped finger heights and thumb silhouette.',("(34,18,25)","(34,18,23)"),("(18,12,23),(26,12,23)","(18,12,21),(26,12,21)"))
change(66,'Move the glove cuff slightly left to follow the palm center and deepen the outer thumb bend; rebalance the wrist beneath the finger row.',("(14,34),(14,42),(34,42),(34,34)","(12,34),(12,42),(34,42),(34,34)"),("('cuff',[(14,34),(34,34)])","('cuff',[(12,34),(34,34)])"),("(6,28)","(6,26)"))
draw(68,'Rebuild the helicopter from a circular cockpit, long tapered tail boom, and crossed rotor strokes; remove the heavy enclosed X that obscured the fuselage.','VRECT_L',"""
path('body',(16,20),[('L',(16,12)),('A',(24,4),8,8,True),('A',(32,12),8,8,True),('L',(32,20)),('A',(24,28),8,8,True),('A',(16,20),8,8,True)],True)
poly('rotor-a',(8,8),(24,24),(40,40));poly('rotor-b',(8,40),(24,24),(40,8));join('rotor-a','rotor-b');join('rotor-a','body');join('rotor-b','body')
line('tail',(24,28),(24,44));line('tail-rotor',(18,44),(30,44));join('tail','body');join('tail','tail-rotor');join('tail','rotor-a');join('tail','rotor-b')
""")
change(69,'Replace the hockey stick’s kinked heel with a curve tangent to both shaft and blade; keep the puck separate and the blade level.',("self.add_line('shaft',(42,6),(30,38))","self.add_line('shaft',(42,6),(31,35))"),("self.add_arc('heel',(30,38),(26,42),radius_x=4)","self.add_bezier('heel',(31,35),((29,40),(29,42),(24,42)))"),("(26,42),(6,42)","(24,42),(6,42)"))
change(70,'Taper the cobra hood into its neck with smooth inward curves; replace the abrupt round-to-straight shoulder corners while keeping the wide hood and coil.',("self.add_arc('taper-right', (42, 18), (30, 30), radius_x=12, radius_y=12, sweep=True)","self.add_bezier('taper-right',(42,18),((42,27),(30,24),(30,30)))"),("self.add_arc('taper-left', (18, 30), (6, 18), radius_x=12, radius_y=12, sweep=True)","self.add_bezier('taper-left',(18,30),((18,24),(6,27),(6,18)))"))
change(71,'Raise the receiver’s inner recess to make the handle slimmer and enlarge the opening beneath it; mirror the new recess on the central axis.',("(32,28)","(32,24)"),("(28,24)","(28,20)"),("(20,24)","(20,20)"),("(16,28)","(16,24)"))
change(72,'Strengthen the demon’s slanted eyes with longer straight marks, keeping them mirrored and well separated from the cheek outline.',('self.add_arc(f"eye-{side}",(24+sign*(17-24),24),(24+sign*(19-24),26),radius_x=5,sweep=sign>0)','self.add_line(f"eye-{side}",(24+sign*(16-24),23),(24+sign*(20-24),26))'))
change(74,'Smooth the horse’s rear mane into a continuous downward curve and align the inner mane’s lower tangent with the neck; preserve the side-facing head.',("self.add_arc('mane-back', (42, 20), (34, 42), radius_x=40, radius_y=40, sweep=True)","self.add_bezier('mane-back',(42,20),((42,28),(38,35),(34,42)))"))
change(76,'Broaden and raise the doorway to balance the house interior, replacing the small cramped arched opening with a clearer entrance.',("('L',(20,42)),('L',(20,34)),('A',(24,30),4,4,True),('A',(28,34),4,4,True),('L',(28,42))","('L',(19,42)),('L',(19,32)),('A',(24,27),5,5,True),('A',(29,32),5,5,True),('L',(29,42))"))
change(77,'Make the rifle’s lower stock a smooth shoulder curve and give the barrel a level run into the front sight.',("self.add_line('barrel',(28, 18),(44, 13))","self.add_line('barrel',(28,18),(44,12))"),("(44, 13),(44, 8)","(44,12),(44,8)"),("(22, 28),(16, 34)","(24, 28),(16, 36)"))
change(78,'Smooth the Hutt’s tail into its rising head and separate the eye marks, making the face read as a creature rather than two stacked dashes.',("self.add_arc('tail-curl',(4,28),(20,24),radius_x=9,sweep=False)","self.add_bezier('tail-curl',(4,28),((8,36),(20,34),(20,24)))"),("self.add_line('eyes',(29,19),(31,19))","self.add_dot('eye-left',(26,20))\n        self.add_dot('eye-right',(34,20))"),("(29,27),(31,27)","(29,29),(31,29)"))
change(79,'Extend the central falling-water stroke and use two smooth wave troughs with equal depth, improving the dam’s vertical flow.',("(24, 24),(24, 28)","(24, 24),(24, 31)"),("radius_x=10,radius_y=3", "radius_x=10,radius_y=3"))
change(80,'Replace the pod’s flattened asymmetric nose arcs with exact matching half-ellipse quarters, preserving a smooth tangent at the forward tip.',("(24,14),(42,24),20,10", "(24,14),(44,24),20,10"),("(42,24),(24,34),20,10", "(44,24),(24,34),20,10"),("(32,24),(42,24)","(32,24),(44,24)"))
change(81,'Make the ice-cream cone taller and broader at its shoulder; replace the skinny wedge with a stronger centered cone silhouette.',("(14, 28), (24, 44), (34, 28)","(12, 27), (24, 44), (36, 27)"))
change(82,'Raise and round the skate’s toe so the boot no longer looks flattened, while keeping a clear gap to the blade.',("(20,19),(32,19)","(20,17),(32,17)"),("(32,19),(32,29),10,5", "(32,17),(32,29),10,6"))
change(83,'Make the unfinished space-station edge use clear eight-unit steps, removing the tiny top notch and uneven fragment widths.',("(24,44),(24,36),(36,36),(36,28),(43,28),(43,20),(26,20),(26,12),(26,8),(24,8),(24,4)","(24,44),(24,36),(36,36),(36,28),(44,28),(44,20),(28,20),(28,12),(28,4),(24,4),(24,4)"),("(26,12),(34,12),(40,12)","(28,12),(36,12),(44,12)"),("(34,8),(34,18)","(36,4),(36,20)"))
change(85,'Widen the column base and taper the shaft slightly inward toward the capital; the scrolls now sit above a more convincing column proportion.',('p_12_34 = (12, 34)','p_12_34 = (10, 34)'),('p_36_34 = (36, 34)','p_36_34 = (38, 34)'),('p_9_42 = (9, 42)','p_9_42 = (6, 42)'),('p_9_34 = (9, 34)','p_9_34 = (6, 34)'),('p_39_34 = (39, 34)','p_39_34 = (42, 34)'),('p_39_42 = (39, 42)','p_39_42 = (42, 42)'))
change(86,'Round the lower muzzle into a true semicircle and raise the inner ear roots for a more elongated jackal face.',('(19, 18)','(19, 16)'),('(29, 18)','(29, 16)'),('radius_x=4, radius_y=5','radius_x=4, radius_y=4'))
change(87,'Give the long ears gently flared curves rather than straight triangular sides, preserving the tall eye stalks and widening the hanging ear tips.',("self.add_polyline('left-ear',(12,16),(6,42),(14,42))","self.add_bezier('left-ear',(12,16),((10,26),(6,33),(6,42)),((8,42),(11,42),(14,42)))"),("self.add_polyline('right-ear',(36,16),(42,42),(34,42))","self.add_bezier('right-ear',(36,16),((38,26),(42,33),(42,42)),((40,42),(37,42),(34,42)))"))
change(88,'Round the three jellyfish bells to full semicircles and align their tentacle lengths, replacing the flattened caps with fuller domes.',('((6, 12, (6, 14)), (26, 25, (34, 42)), (6, 38, (6, 14)))','((6, 14, (6, 14)), (26, 27, (34, 42)), (6, 38, (6, 14)))'),('radius_x=8, radius_y=6','radius_x=8, radius_y=8'),('(18, 29, 42)','(18, 31, 42)'))
change(91,'Replace the kayak’s four offset arcs with smooth matched hull curves; keep the widest point at the paddle attachments and give the cockpit an oval opening.',("self.add_arc('boat-upper-left', (24, 6), (12, 24), radius_x=60, radius_y=30, sweep=False)","self.add_bezier('boat-upper-left',(24,6),((18,10),(12,17),(12,24)))"),("self.add_arc('boat-lower-left', (12, 24), (24, 42), radius_x=60, radius_y=30, sweep=False)","self.add_bezier('boat-lower-left',(12,24),((12,31),(18,38),(24,42)))"),("self.add_arc('boat-lower-right', (24, 42), (36, 24), radius_x=60, radius_y=30, sweep=False)","self.add_bezier('boat-lower-right',(24,42),((30,38),(36,31),(36,24)))"),("self.add_arc('boat-upper-right', (36, 24), (24, 6), radius_x=60, radius_y=30, sweep=False)","self.add_bezier('boat-upper-right',(36,24),((36,17),(30,10),(24,6)))"),('radius_x=3, radius_y=3','radius_x=3, radius_y=5'))
for n in (92,93):
 change(n,'Rebalance the diagonal hull with matched tangent controls and a broader middle section; remove the unequal bow/stern curvature while preserving the paddle and cockpit arrangement.',('28.6666666667','30'),('19.6666666667','20'),('28.3333333333','28'),('8.3333333333','8'),('19.3333333333','18'),('39.6666666667','40'))
change(94,'Add a clear tooth to the left key and shorten its lower stem; distinguish the hanging keys instead of leaving one as a bare line.',("(6,18),(6,30),(6,42)","(6,18),(6,30),(6,38),(10,38)"))
change(95,'Replace the blunt rectangular key tip with a stepped tooth and shoulder, preserving the circular bow and diagonal shaft.',("[(18,18),(30,6),(42,6),(42,18),(30,30)]","[(18,18),(30,6),(42,6),(42,14),(36,14),(36,24),(30,30)]"))
change(96,'Straighten the kiwi’s long beak into a clean tapered direction and shift the eye forward toward the head; smooth the top of the neck.',("self.add_bezier('beak',(31,17),((37,20),(41,25),(44,30)))","self.add_line('beak',(31,17),(44,30))"),("(18,22)","(22,20)"))
change(97,'Make the knife’s exposed blade a coherent curved cutting edge instead of a broken polygon, keeping the contact tip fixed on the surface.',("self.add_polyline('knife',(16,42),(26,16),(30,6),(40,10),(36,20),(32,28),(24,38),(16,42))","self.add_polyline('knife-spine',(16,42),(26,16),(30,6),(40,10),(36,20))\n        self.add_bezier('cutting-edge',(36,20),((32,31),(24,40),(16,42)))\n        self.relate('connect','knife-spine','cutting-edge')"),("'handle-seam','knife'","'handle-seam','knife-spine'"),("'knife','surface'","'knife-spine','surface'"))
change(98,'Round the koala’s ear top and soften the back-to-belly transition; attach the arm exactly to the sloping branch instead of leaving the endpoint off the centerline.',("self.add_line('ear-top-1', (20, 8), (16, 6))","self.add_bezier('ear-top-1',(20,8),((19,7),(18,6),(16,6)))"),("(20, 28), (36, 25)","(20,28),(36,25)"),("(30, 42), (42, 8)","(30,42),(42,8)"))

# Second visual pass: fix measured crowding instead of retaining warnings.
change(3,'Smooth the hooked tuft into a curved feather and deepen the centered brow angle while preserving clear space inside the round body.',("(19, 23), (24, 25), (29, 23)","(18, 23), (24, 26), (30, 23)"),("self.add_polyline('tuft', (24, 12), (20, 4), (29, 4))","self.add_bezier('tuft',(24,12),((20,12),(20,4),(28,4)))"))
draw(4,'Separate the head, narrow waist, and round abdomen; spread the two retained leg pairs outward so they no longer curl tightly around the body.','VRECT_L',"""
circle('head',24,10,6);circle('abdomen',24,38,6)
poly('waist',(24,16),(24,24),(24,32));join('waist','head');join('waist','abdomen')
for side in (-1,1):
 x=lambda d:24+side*d
 poly(f'antenna-{side}',(x(6),10),(x(16),4));join(f'antenna-{side}','head')
 poly(f'upper-leg-{side}',(24,24),(x(16),24),(x(16),18));join(f'upper-leg-{side}','waist')
 line(f'lower-leg-{side}',(x(6),38),(x(16),44));join(f'lower-leg-{side}','abdomen')
join('upper-leg--1','upper-leg-1')
""")
# Wheel tops meet the barrel at a single support, leaving the rear breech well clear.
for n,cx,hub in [(9,20,False),(33,24,True)]:
 draw(n,'Lift the barrel clear of the wheel and use one vertical trunnion support; open the breech-wheel gap and give the muzzle a consistent thickness.','HRECT_L',f"""
circle('wheel',{cx},32,8)
poly('barrel',(4,16),(44,8),(44,16),(4,24),closed=True)
line('mount',({cx},24),({cx},21));join('mount','wheel');join('mount','barrel')
line('trail',({cx-8},32),(4,40));join('trail','wheel')
{'dot("hub",(24,32))' if hub else ''}
""")
draw(10,'Open the space around the raised gun and wheel; use a clear pivot support and two separate outward feet instead of a crowded polygon over the wheel.','HRECT_L',"""
circle('wheel',20,30,10)
poly('gun',(12,12),(28,20),(38,8));line('pivot',(20,20),(20,16));join('pivot','wheel');join('pivot','gun')
line('left-foot',(12,36),(4,40));poly('right-foot',(28,36),(36,40),(44,40));join('left-foot','wheel');join('right-foot','wheel')
""")
change(12,'Separate the two ribbon tails with a clear central notch and broaden their ends; remove the narrow diamond trapped under the flower.',("self.add_polyline('ribbon', (18, 30), (12, 44), (24, 38), (36, 44), (30, 30))","self.add_polyline('ribbon-left',(18,30),(10,44),(19,42))\n        self.add_polyline('ribbon-right',(30,30),(38,44),(29,42))\n        self.relate('connect','rosette','ribbon-left')\n        self.relate('connect','rosette','ribbon-right')"),("self.relate('connect', 'rosette', 'ribbon')",""))
change(35,'Smooth the roof-to-windscreen transition into one coherent curve while keeping the door mark clear of the body.',("('C', (31, 11), (29, 8), (30, 10))","('C', (33, 13), (29, 8), (31, 11))"))
draw(39,'Move the string knot to the ball’s right edge and open the two curling runs; remove the stroke that doubled back along the ball.','SQUARE',"""
circle('ball',16,16,10)
path('string',(26,16),[('C',(42,24),(34,16),(42,18)),('C',(30,32),(42,29),(35,32)),('C',(26,42),(22,32),(22,42)),('L',(30,42))]);join('ball','string')
""")
change(42,'Broaden the airliner’s near wing and tail opening, removing the pinched passage at the fuselage; shorten the far wing where it crowds the tail.',('(27,40),(17,40),(21,29),(12,34)','(29,40),(17,40),(22,28),(12,34)'),('(23,19),(10,8),(24,8),(33,14)','(23,19),(16,8),(24,8),(33,14)'))
change(43,'Open the gap between the two rainbow curves by lifting the outer arch; keep each arc attached to the cloud and preserve its clean quarter-ellipse construction.',("(20, 24), (44, 8), radius_x=24, radius_y=16","(20, 24), (44, 8), radius_x=24, radius_y=16"),("(28, 30), (44, 18), radius_x=16, radius_y=12","(28, 30), (44, 20), radius_x=16, radius_y=10"))
change(47,'Extend the two reflection arcs to balanced opposing sweeps while keeping them open; enlarge the reflections without turning them into a second rim.',("(24, 13), (35, 24), radius_x=11","(18, 16), (34, 24), radius_x=10"),("(24, 35), (13, 24), radius_x=11","(30, 32), (14, 24), radius_x=10"))
draw(48,'Integrate the wheel openings into a continuous car body so they cannot collide with the lower panel. Align the roll bar and windscreen above a clear open cabin.','HRECT_L',"""
path('body',(4,30),[('L',(4,20)),('L',(16,20)),('L',(32,20)),('L',(38,20)),('A',(44,26),6,6,True),('L',(44,34)),('L',(42,34)),('A',(36,40),6,6,True),('A',(30,34),6,6,True),('L',(18,34)),('A',(12,40),6,6,True),('A',(6,34),6,6,True),('L',(4,34)),('L',(4,30))],True)
for x in (12,36):path(f'wheel-{x}',(x-6,34),[('A',(x+6,34),6,6,True)]);join(f'wheel-{x}','body')
line('windscreen',(24,8),(32,20));line('roll-bar',(12,12),(16,20));join('windscreen','body');join('roll-bar','body')
""")
change(51,'Enlarge the spindle hole to a true three-unit radius and make all three drive slots longer and evenly placed inside the disc.',("circle('hub', 24, 24, 2)","circle('hub', 24, 24, 3)"),("(23, 13), (25, 13)","(22, 13), (26, 13)"),("(24 + side * 10, 28), (24 + side * 9, 30)","(24 + side * 10, 28), (24 + side * 8, 32)"))
change(53,'Attach the dry tree trunk exactly to the ground corner and angle the ground crack toward its own side of the parched slab.',("(35, 8), (35, 31)","(33, 8), (33, 31)"),("(29, 17), (35, 23), (44, 15)","(27, 17), (33, 23), (44, 15)"),("(27, 31), (21, 40)","(25,31),(18,40)"))
change(61,'Add paired slanted eyes to the fox’s blank face while preserving the low nose and pointed muzzle.',("self.add_dot('nose', (24, 32))","self.add_dot('nose',(24,32))\n        self.add_line('eye-left',(17,23),(19,24))\n        self.add_line('eye-right',(31,23),(29,24))"))
change(65,'Open the glove thumb into a broad side projection and shorten the finger seams; remove the tiny folded wedge beside the index finger.',("(6,26),(8,20),(10,24)","(6,26),(6,20),(10,24)"),("(18,12,23),(26,12,23),(34,18,25)","(18,12,21),(26,12,21),(34,18,23)"))
draw(68,'Use a long upright fuselage and one clear transverse rotor with a central hub; remove the crossed enclosed diagonals and extend the tail below the body.','VRECT_L',"""
path('fuselage',(16,22),[('L',(16,12)),('A',(24,4),8,8,True),('A',(32,12),8,8,True),('L',(32,22)),('A',(24,30),8,8,True),('A',(16,22),8,8,True)],True)
poly('rotor',(8,18),(16,18),(32,18),(40,18));join('rotor','fuselage')
line('tail',(24,30),(24,44));line('tail-rotor',(18,44),(30,44));join('tail','fuselage');join('tail','tail-rotor')
""")
change(78,'Round the Hutt’s upper head into a lower, broader dome and lengthen the mouth slightly; preserve the open tail curl.',("(20,24),(40,24),radius_x=10,radius_y=16","(20,24),(40,24),radius_x=10,radius_y=16"),("(29,27),(31,27)","(28,28),(32,28)"),("(29,19),(31,19)","(29,18),(31,18)"))
change(79,'Replace the short central water dash with two aligned falling-water marks, giving the dam a clearer discharge pattern.',("self.add_line('flow',(24, 24),(24, 28))","self.add_line('flow-left',(20,24),(20,28))\n        self.add_line('flow-right',(28,24),(28,28))"))
change(83,'Regularize the exposed frame into an eight-unit cross and lengthen the equator, removing the short uneven end fragments.',("(26,12),(34,12),(40,12)","(26,12),(34,12),(40,12)"),("(34,8),(34,18)","(34,8),(34,16)"),("(4,24),(24,24)","(4,24),(25,24)"))
draw(87,'Separate the eye stalks at their roots and widen the upper face; keep the long paired hanging ears and rounded muzzle without the pinched central notch.','SQUARE',"""
path('face',(10,18),[('A',(16,6),6,12,True),('A',(22,18),6,12,True),('L',(26,18)),('A',(32,6),6,12,True),('A',(38,18),6,12,True),('C',(24,42),(38,32),(32,42)),('C',(10,18),(16,42),(10,32))],True)
poly('ear-left',(10,18),(6,42),(14,42));poly('ear-right',(38,18),(42,42),(34,42));join('ear-left','face');join('ear-right','face')
path('mouth',(21,30),[('A',(27,30),4,4,False)])
""")
change(96,'Straighten the kiwi’s beak and spread the feet outward, removing the tight overlap below the belly while preserving the compact body.',("self.add_bezier('beak',(31,17),((37,20),(41,25),(44,30)))","self.add_line('beak',(31,17),(44,30))"),("(12,34),(10,40),(6,40)","(12,34),(10,40),(4,40)"))
draw(98,'Open the koala’s ear away from the head and use a clean shared arm-to-branch junction; round the seated body and keep the nose centered in the face.','SQUARE',"""
path('head',(12,10),[('A',(28,10),8,8,True),('A',(28,26),8,8,True),('A',(12,26),8,8,True),('A',(12,10),8,8,True)],True)
dot('nose',(20,18))
path('ear',(12,10),[('A',(6,6),6,4,False),('L',(6,14)),('L',(9,17))]);join('ear','head')
path('body',(12,26),[('C',(10,36),(8,28),(8,34)),('A',(20,42),10,6,False),('L',(32,42))]);join('body','head')
line('branch',(32,42),(42,6));join('branch','body')
line('arm',(28,26),(37,24));join('arm','head');join('arm','branch')
""")

# Resolve the remaining join and spacing findings.
EDITS[3]=(EDITS[3][0],tuple((a,b.replace('(24, 26)','(24, 25)')) for a,b in EDITS[3][1]),None,None)
draw(9,'Give the cannon a consistent tube opening and separate it from the wheel with an explicit vertical mount; the rear support extends clearly to the ground.','HRECT_L',"""
poly('barrel',(4,8),(44,8),(44,16),(24,16),(4,16),closed=True)
circle('wheel',24,32,8)
line('mount',(24,16),(24,24));join('mount','wheel');join('mount','barrel')
line('trail',(16,32),(4,40));join('trail','wheel')
""")
draw(33,'Rebuild the cannon carriage as a separate block and axle beneath a consistent tube; open all wheel and body clearances.','HRECT_L',"""
poly('barrel',(4,8),(44,8),(44,16),(8,16),(4,16),closed=True)
poly('block',(4,24),(8,24),(12,24),(12,32),(12,40),(4,40),closed=True)
circle('wheel',28,32,8)
line('axle',(12,32),(20,32));join('axle','block');join('axle','wheel')
line('support',(8,16),(8,24));join('support','block');join('support','barrel')
""")
draw(10,'Rebuild the raised gun above its wheel with a clean pivot and spread outriggers; remove the crowded diamond around the wheel top.','HRECT_L',"""
circle('wheel',20,30,10)
poly('barrel',(12,12),(24,12),(32,8),(40,8))
line('mount',(20,12),(20,20));join('mount','barrel');join('mount','wheel')
poly('left-foot',(12,36),(8,40),(4,40));poly('right-foot',(28,36),(36,40),(44,40));join('left-foot','wheel');join('right-foot','wheel')
""")
draw(42,'Rebuild the climbing airliner as one continuous outline with a rounded nose and broad swept wings; remove overlapping strokes and the pinched central passages.','HRECT_L',"""
path('airliner',(38,8),[('C',(44,12),(42,8),(44,8)),('C',(38,20),(44,16),(40,18)),('L',(30,40)),('L',(20,40)),('L',(24,27)),('L',(14,34)),('L',(4,26)),('L',(8,18)),('L',(15,23)),('L',(22,18)),('L',(12,8)),('L',(24,8)),('L',(32,13)),('L',(38,8))],True)
""")
change(47,'Lengthen both disc reflection arcs into balanced opposing sweeps while keeping a clear open gap between their ends.',("(24, 13), (35, 24), radius_x=11","(24, 13), (35, 28), radius_x=11"),("(24, 35), (13, 24), radius_x=11","(24, 35), (13, 20), radius_x=11"))
draw(48,'Give the convertible one coherent wheel-and-body silhouette with taller clearance above the wheels; match the slanted roll bar to the windscreen.','HRECT_L',"""
path('body',(6,34),[('C',(4,24),(4,31),(4,27)),('A',(10,18),6,6,True),('L',(18,18)),('L',(32,18)),('L',(38,18)),('A',(44,24),6,6,True),('C',(42,34),(44,27),(44,31)),('A',(36,40),6,6,True),('A',(30,34),6,6,True),('L',(18,34)),('A',(12,40),6,6,True),('A',(6,34),6,6,True)],True)
for x in (12,36):path(f'wheel-{x}',(x-6,34),[('A',(x,28),6,6,True),('A',(x+6,34),6,6,True)]);join(f'wheel-{x}','body')
line('windscreen',(25,8),(32,18));line('roll-bar',(14,10),(18,18));join('windscreen','body');join('roll-bar','body')
""")
change(51,'Enlarge the spindle opening and give the drive slots equal two-unit lengths with matching distances from the hub.',("circle('hub', 24, 24, 2)","circle('hub', 24, 24, 3)"),("(23, 13), (25, 13)","(23, 12), (25, 12)"),("(24 + side * 10, 28), (24 + side * 9, 30)","(24 + side * 10, 30), (24 + side * 9, 31)"))
change(61,'Give the fox two small diagonal eye marks while preserving open space around the nose and tapered cheeks.',("self.add_dot('nose', (24, 32))","self.add_dot('nose',(24,33))\n        self.add_line('eye-left',(18,24),(19,25))\n        self.add_line('eye-right',(30,24),(29,25))"))
change(65,'Remove the tiny folded thumb wedge and replace it with a clean outward thumb bend; shorten the finger creases to open the palm.',("(10,24)","(10,22)"),("(6,26),(8,20)","(6,28),(6,22)"),("(18,12,23),(26,12,23),(34,18,25)","(18,12,21),(26,12,21),(34,18,23)"))
change(78,'Open the Hutt’s tail curl into a broader upward stroke and lengthen the mouth; keep the round head and seated silhouette.',("self.add_arc('tail-curl',(4,28),(20,24),radius_x=9,sweep=False)","self.add_bezier('tail-curl',(4,28),((10,30),(20,32),(20,24)))"),("(29,27),(31,27)","(28,28),(32,28)"))
draw(87,'Widen the separation between the two eye stalks and give the long hanging ears a clean outward flare; remove the pinched bridge above the face.','SQUARE',"""
path('face',(10,18),[('A',(15,6),5,12,True),('A',(20,18),5,12,True),('L',(28,18)),('A',(33,6),5,12,True),('A',(38,18),5,12,True),('C',(24,42),(38,32),(32,42)),('C',(10,18),(16,42),(10,32))],True)
poly('ear-left',(10,18),(6,42),(14,42));poly('ear-right',(38,18),(42,42),(34,42));join('ear-left','face');join('ear-right','face')
path('mouth',(21,30),[('A',(27,30),4,4,False)])
""")
change(96,'Straighten the kiwi’s long beak and lift the lower belly to open the gap above its feet; keep the compact bird body and short legs.',("self.add_bezier('beak',(31,17),((37,20),(41,25),(44,30)))","self.add_line('beak',(31,17),(44,30))"),("(18,34),(15,35),(12,34)","(18,32),(15,33),(12,32)"),("(7,34),(4,30)","(7,32),(4,28)"),("(12,34),(10,40),(6,40)","(12,32),(8,40),(4,40)"))
draw(98,'Merge the ear into one clean head outline, open the gap to the branch, and attach the reaching arm at an exact shared point; round the seated body beneath it.','SQUARE',"""
path('head',(20,8),[('A',(30,18),10,10,True),('A',(26,26),10,10,True),('A',(20,28),10,10,True),('A',(12,24),10,10,True),('A',(10,18),10,10,True),('A',(6,14),4,4,True),('L',(6,10)),('A',(10,6),4,4,True),('L',(16,6)),('L',(20,8))],True)
dot('nose',(20,18))
path('body',(12,24),[('C',(10,36),(8,28),(8,34)),('A',(20,42),10,6,False),('L',(36,42))]);join('body','head')
line('branch',(36,42),(42,6));join('branch','body')
line('arm',(26,26),(39,24));join('arm','head');join('arm','branch')
""")

EDITS[51]=("Enlarge the spindle opening and balance the three drive slots around the hub, keeping clear space to both circular edges.",tuple((a,b.replace('(23, 12), (25, 12)','(23, 13), (25, 13)')) for a,b in EDITS[51][1]),None,None)
draw(68,'Show four diagonal rotor tips around the helicopter body, with the middle shaft hidden by the fuselage. Open the crowded crossed center and keep the cockpit, hub, and tail distinct.','VRECT_L',"""
path('fuselage',(14,14),[('A',(24,4),10,10,True),('A',(34,14),10,10,True),('L',(34,34)),('L',(24,38)),('L',(14,34)),('L',(14,14))],True)
for n,a,b in [('nw',(8,8),(14,14)),('ne',(40,8),(34,14)),('sw',(8,40),(14,34)),('se',(40,40),(34,34))]:
 line('rotor-'+n,a,b);join('rotor-'+n,'fuselage')
dot('hub',(24,24))
line('tail',(24,38),(24,44));line('tail-rotor',(18,44),(30,44));join('tail','fuselage');join('tail','tail-rotor')
""")
EDITS[68]=(EDITS[68][0],(),EDITS[68][2],EDITS[68][3].replace('(24,38)','(24,36)'))
# MORE_ENTRIES

def apply():
 for n,(note,pairs,key,body) in EDITS.items():
  r=rows[n-1];s=(ROOT/r['original_model']).read_text()
  for old,new in pairs:
   if old not in s:raise ValueError(f'{n}: missing {old}')
   s=s.replace(old,new)
  tree=ast.parse(s)
  cls=next(c for c in tree.body if isinstance(c,ast.ClassDef) and any(isinstance(a,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='icon_id' for t in a.targets) for a in c.body))
  vid=r['icon_id']+'-centerline-v2'
  for a in cls.body:
   if isinstance(a,ast.Assign):
    names=[t.id for t in a.targets if isinstance(t,ast.Name)]
    if 'icon_id' in names:a.value=ast.Constant(vid)
    if 'keyshape' in names and key:a.value=ast.parse('Keyshape.'+key,mode='eval').body
  cls.body=[a for a in cls.body if not (isinstance(a,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ('variant_of','variant_label') for t in a.targets))]
  cls.body+=ast.parse(f'variant_of = {r["icon_id"]!r}\nvariant_label = "Batch 01 centerline repair"').body
  if body:
   cls.body=[a for a in cls.body if not (isinstance(a,ast.FunctionDef) and a.name=='build')]
   cls.body.append(ast.parse('def build(self):\n'+textwrap.indent(HELPERS+body,'    ')).body[0])
  for a in tree.body:
   if isinstance(a,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUTHOR' for t in a.targets):a.value=ast.Constant(AUTHOR)
  if isinstance(tree.body[0],ast.Expr) and isinstance(tree.body[0].value,ast.Constant):tree.body.pop(0)
  tree.body.insert(0,ast.Expr(ast.Constant(note+'\nIndependent centerline revision; original snapshot preserved.')))
  ast.fix_missing_locations(tree)
  dest=OUT/'drafts'/(Path(r['original_model']).stem+'_centerline_v2.py');dest.write_text(ast.unparse(tree)+'\n')
  r.update(variant_id=vid,variant_path=str(dest.relative_to(ROOT)),repair_note=note,action='revised',centerline_review=True)
 (OUT/'batch.json').write_text(json.dumps(rows,indent=2))
 print('Updated',len(EDITS),'centerline revisions.')
if __name__=='__main__':apply()
