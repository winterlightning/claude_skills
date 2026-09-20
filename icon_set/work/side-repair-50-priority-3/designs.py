"""Individually authored centerlines, side repair batch 3."""
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/side-repair-50-priority-3/batch.json'
AUTHOR='gpt-6'
D={}
def plan(n,shape,parts,ref,body):D[n]=(shape,parts,ref,body)
plan(1,'VRECT_XL','Shield with central crown, two dipped shoulders, curved pointed base and horizontal divider.','shield','''
self.add_line('tip-l',(16,2),(10,6))
self.add_bezier('dip-l',(10,6),((8,7),(6,6),(4,5)))
self.add_line('left',(4,5),(4,15))
self.add_bezier('base-l',(4,15),((4,22),(9,27),(16,30)))
self.add_bezier('base-r',(16,30),((23,27),(28,22),(28,15)))
self.add_line('right',(28,15),(28,5))
self.add_bezier('dip-r',(28,5),((26,6),(24,7),(22,6)))
self.add_line('tip-r',(22,6),(16,2))
self.add_contour('shield','tip-l','dip-l','left','base-l','base-r','right','dip-r','tip-r',closed=True)
self.add_line('divider',(4,14),(28,14));self.relate('connect','divider','shield')
''')
for n,dots in [(3,False),(4,True)]:
 plan(n,'SQUARE','Open skull with domed cranium, two '+('dot' if dots else 'slanted')+' eyes, cheek transitions and three lower tooth strokes.','skull','''
self.add_line('jaw-l',(8,30),(8,27))
self.add_bezier('cheek-l',(8,27),((8,23),(2,25),(2,18)))
self.add_line('side-l',(2,18),(2,16))
self.add_arc('crown',(2,16),(30,16),radius_x=14)
self.add_line('side-r',(30,16),(30,18))
self.add_bezier('cheek-r',(30,18),((30,25),(24,23),(24,27)))
self.add_line('jaw-r',(24,27),(24,30))
self.add_contour('skull','jaw-l','cheek-l','side-l','crown','side-r','cheek-r','jaw-r')
self.add_line('tooth',(16,28),(16,30))
'''+("self.add_dot('eye-l',(11,15));self.add_dot('eye-r',(21,15))\n" if dots else "self.add_line('eye-l',(10,15),(12,16));self.add_line('eye-r',(22,15),(20,16))\n"))
plan(7,'HRECT_XL','Rounded rectangular panel with exactly three equally spaced dots.','none','''
box(self,'panel',2,4,30,28,3)
for i,x in enumerate((9,16,23)):self.add_dot(f'dot-{i}',(x,16))
''')
plan(8,'VRECT_XL','Tall crescent, smooth convex outer edge and concave inner edge meeting at both tips.','moon','''
self.add_bezier('outer-top',(28,2),((14,2),(4,8),(4,16)))
self.add_bezier('outer-bottom',(4,16),((4,24),(14,30),(28,30)))
self.add_bezier('inner-bottom',(28,30),((23,26),(21,21),(21,16)))
self.add_bezier('inner-top',(21,16),((21,11),(23,6),(28,2)))
self.add_contour('crescent','outer-top','outer-bottom','inner-bottom','inner-top',closed=True)
''')
plan(9,'HRECT_XL','Three left-aligned lines, progressively shorter from top to bottom.','none','''
for i,(y,end) in enumerate(((4,30),(16,23),(28,16))):self.add_line(f'line-{i}',(2,y),(end,y))
''')
plan(10,'VRECT_XL','Thumb-up silhouette with raised rounded thumb, concave web, slanted finger edge and short wrist.','thumbs-up','''
self.add_bezier('wrist-top',(4,16),((10,16),(11,12),(12,6)))
self.add_bezier('thumb-top',(12,6),((12,2),(14,2),(16,2)))
self.add_bezier('thumb-round',(16,2),((20,2),(22,4),(21,8)))
self.add_line('thumb-side',(21,8),(20,14))
self.add_line('finger-top',(20,14),(25,14))
self.add_bezier('finger-tip',(25,14),((28,14),(28,16),(28,17)))
self.add_line('finger-side',(28,17),(25,27))
self.add_bezier('palm',(25,27),((24,30),(22,30),(19,30)))
self.add_line('base',(19,30),(14,30))
self.add_bezier('wrist-bottom',(14,30),((10,30),(10,28),(7,28)))
self.add_polyline('wrist',(7,28),(4,28),(4,16))
self.add_contour('hand','wrist-top','thumb-top','thumb-round','thumb-side','finger-top','finger-tip','finger-side','palm','base','wrist-bottom','wrist',closed=True)
''')
plan(11,'HRECT_XL','Left-facing tilted CCTV housing, detached front marker and curved wall bracket.','cctv','''
self.add_polyline('housing',(8,10),(26,4),(30,17),(12,23),closed=True)
self.add_line('front',(2,14),(4,21))
self.add_line('bracket-stem',(22,20),(22,25))
self.add_arc('bracket-turn',(22,25),(25,28),radius_x=3,sweep=False)
self.add_line('bracket-end',(25,28),(30,28))
self.add_contour('bracket','bracket-stem','bracket-turn','bracket-end');self.relate('connect','housing','bracket')
''')
plan(12,'VRECT_XL','Tulip with two pointed upper petals, curved cup, straight stem and two curved leaves.','flower-2','''
self.add_polyline('petals',(7,2),(16,8),(25,2),(25,11))
self.add_arc('cup',(25,11),(7,11),radius_x=9)
self.add_line('left',(7,11),(7,2));self.add_contour('flower','petals','cup','left',closed=True)
self.add_line('stem',(16,20),(16,30));self.relate('connect','stem','flower')
for name,end,c1,c2 in [('leaf-l',(4,24),(14,26),(8,24)),('leaf-r',(28,24),(18,26),(24,24))]:
 self.add_bezier(name,(16,30),(c1,c2,end));self.relate('connect',name,'stem')
self.relate('connect','leaf-l','leaf-r')
''')
plan(13,'VRECT_XL','Three pointed upright leaves seated in a tapered flowerpot with a shared rim.','sprout','''
self.add_bezier('left-outer',(9,22),((5,18),(4,13),(4,8)))
self.add_bezier('left-inner',(4,8),((8,9),(10,12),(12,15)))
self.add_bezier('center-l',(12,15),((12,9),(14,4),(16,2)))
self.add_bezier('center-r',(16,2),((18,4),(20,9),(20,15)))
self.add_bezier('right-inner',(20,15),((22,12),(24,9),(28,8)))
self.add_bezier('right-outer',(28,8),((28,13),(27,18),(23,22)))
self.add_contour('plant','left-outer','left-inner','center-l','center-r','right-inner','right-outer')
self.add_polyline('pot',(8,22),(24,22),(22,30),(10,30),closed=True);self.relate('connect','plant','pot')
''')
plan(14,'HRECT_XL','Two outlined circular heads above overlapping rounded shoulder busts with a common baseline.','human_ref/user.svg','''
# Equal circular heads; own head bottom 12 and shoulder top 20: exact 4px ink gap.
for name,x in [('front',9),('back',23)]:circle(self,name+'-head',x,8,4)
self.add_line('front-l',(2,28),(2,27));self.add_arc('front-shoulders',(2,27),(16,27),radius_x=7)
self.add_line('front-r',(16,27),(16,28));self.add_line('baseline',(16,28),(2,28))
self.add_contour('front-body','front-l','front-shoulders','front-r','baseline',closed=True)
self.add_arc('back-shoulders',(16,27),(30,27),radius_x=7)
self.add_polyline('back-base',(30,27),(30,28),(16,28));self.add_contour('back-body','back-shoulders','back-base',closed=True)
self.relate('connect','front-body','back-body')
''')
plan(16,'SQUARE','Rounded warning triangle with a vertical exclamation stem and separate dot.','triangle-alert','''
self.add_line('left',(3,30),(15,3));self.add_bezier('top',(15,3),((16,1),(16,1),(17,3)))
self.add_line('right',(17,3),(30,29));self.add_arc('br',(30,29),(29,30),radius_x=1)
self.add_line('base',(29,30),(3,30));self.add_contour('triangle','left','top','right','br','base',closed=True)
self.add_line('stem',(16,16),(16,18));self.add_dot('dot',(16,24))
''')
plan(17,'VRECT_XL','Upward index-finger pointer with rounded finger, folded palm, thumb and open wrist.','hand','''
self.add_line('index-l',(13,17),(13,6));self.add_arc('index-top',(13,6),(21,6),radius_x=4)
self.add_line('index-r',(21,6),(21,14))
self.add_bezier('palm',(21,14),((26,14),(28,18),(28,22)))
self.add_line('wrist-r',(28,22),(28,30))
self.add_contour('right','index-l','index-top','index-r','palm','wrist-r')
self.add_line('thumb-inner',(13,17),(9,13))
self.add_bezier('thumb-top',(9,13),((6,10),(4,12),(4,15)))
self.add_bezier('thumb-lower',(4,15),((4,17),(5,18),(7,20)))
self.add_line('wrist-l',(7,20),(17,30))
self.add_contour('left','thumb-inner','thumb-top','thumb-lower','wrist-l');self.relate('connect','left','right')
''')
plan(18,'HRECT_XL','Rounded video-camera body with attached outward flared lens on the right.','video','''
box(self,'body',2,4,22,28,4)
self.add_polyline('lens',(22,12),(30,8),(30,24),(22,20));self.relate('connect','lens','body')
''')
plan(19,'HRECT_XL','Three separate horizontal wind waves with rising curled right ends.','wind','''
for i,y in enumerate((6,16,26)):
 self.add_bezier(f'a-{i}',(2,y),((8,y-4),(12,y),(16,y)))
 self.add_bezier(f'b-{i}',(16,y),((20,y+4),(30,y+2),(30,y-2)))
 self.add_contour(f'wave-{i}',f'a-{i}',f'b-{i}')
''')
plan(20,'HRECT_XL','Open laptop with rounded screen top, sloping base sides and single shared hinge.','laptop','''
self.add_line('left',(4,20),(4,7));self.add_arc('tl',(4,7),(7,4),radius_x=3)
self.add_line('top',(7,4),(25,4));self.add_arc('tr',(25,4),(28,7),radius_x=3)
self.add_line('right',(28,7),(28,20));self.add_line('hinge',(28,20),(4,20))
self.add_contour('screen','left','tl','top','tr','right','hinge',closed=True)
self.add_polyline('base',(4,20),(2,28),(30,28),(28,20));self.relate('connect','base','screen')
''')
plan(21,'SQUARE','Contactless wallet: two Wi-Fi arcs above an open folded wallet with its diagonal flap.','wallet','''
self.add_bezier('wifi-l',(2,6),((6,3),(11,2),(16,2)));self.add_bezier('wifi-r',(16,2),((21,2),(26,3),(30,6)));self.add_contour('wifi','wifi-l','wifi-r')
self.add_bezier('signal',(10,11),((14,8),(18,8),(22,11)))
self.add_line('top',(8,18),(24,18));self.add_arc('tr',(24,18),(27,21),radius_x=3)
self.add_line('back',(27,21),(27,27));self.add_contour('back-leaf','top','tr','back')
self.add_bezier('fold-top',(8,18),((5,18),(5,20),(5,22)))
self.add_line('fold-left',(5,22),(5,25));self.add_bezier('fold-base',(5,25),((5,27),(11,30),(14,30)))
self.add_bezier('fold-tip',(14,30),((17,30),(17,29),(17,27)))
self.add_line('fold-right',(17,27),(17,23));self.add_bezier('fold-diagonal',(17,23),((17,21),(11,19),(8,18)))
self.add_contour('fold','fold-top','fold-left','fold-base','fold-tip','fold-right','fold-diagonal',closed=True);self.relate('connect','fold','back-leaf')
''')
for n in (22,34):
 plan(n,'SQUARE' if n==22 else 'VRECT_XL','Rounded suitcase, raised rectangular handle and two short straight wheel stems.','luggage',f'''
box(self,'case',{2 if n==22 else 4},10,{30 if n==22 else 28},26,3)
self.add_polyline('handle',(11,10),(11,2),(21,2),(21,10));self.relate('connect','handle','case')
for i,x in enumerate((9,23)):
 self.add_line(f'wheel-{{i}}',(x,26),(x,30));self.relate('connect',f'wheel-{{i}}','case')
''')
plan(23,'SQUARE','Drafting compass with circular pivot, short top stem, two spreading legs and cross brace.','drafting-compass','''
circle(self,'pivot',23,9,5)
self.add_line('cap',(27,5),(30,2));self.relate('connect','cap','pivot')
self.add_line('left-leg',(19,12),(2,24));self.relate('connect','left-leg','pivot')
self.add_line('right-leg',(23,14),(18,30));self.relate('connect','right-leg','pivot')
self.add_line('brace',(12,17),(24,24));self.relate('connect','brace','left-leg');self.relate('connect','brace','right-leg')
''')
plan(24,'VRECT_XL','Circular rotation arrow with a break at upper right and curved diagonal internal sweep.','rotate-cw','''
self.add_bezier('outer-a',(16,4),((8,4),(4,9),(4,16)))
self.add_bezier('outer-b',(4,16),((4,24),(9,30),(16,30)))
self.add_bezier('outer-c',(16,30),((23,30),(28,24),(28,17)))
self.add_bezier('outer-d',(28,17),((28,13),(26,10),(24,8)))
self.add_contour('outer','outer-a','outer-b','outer-c','outer-d')
self.add_polyline('arrow',(12,2),(16,4),(12,8));self.relate('connect','arrow','outer')
self.add_bezier('sweep',(8,8),((10,17),(20,23),(27,23)));self.relate('connect','sweep','outer')
''')
plan(25,'SQUARE','T-shirt with round collar, curved shoulders, two sleeve hems, side slits and straight lower hem.','shirt','''
self.add_arc('collar',(10,2),(22,2),radius_x=6,sweep=False)
self.add_bezier('shoulder-r',(22,2),((27,2),(30,6),(30,10)))
self.add_polyline('right',(30,10),(30,18),(22,18),(22,30),(10,30),(10,18),(2,18),(2,10))
self.add_bezier('shoulder-l',(2,10),((2,6),(5,2),(10,2)))
self.add_contour('shirt','collar','shoulder-r','right','shoulder-l',closed=True)
for name,x in [('slit-l',10),('slit-r',22)]:
 self.add_line(name,(x,18),(x,14));self.relate('connect',name,'shirt')
''')
plan(26,'VRECT_XL','Trash can with separate-width lid, central lid stem, straight body sides and rounded lower corners.','trash','''
self.add_line('lid',(4,10),(28,10));self.add_line('handle',(16,2),(16,10));self.relate('connect','lid','handle')
self.add_line('right',(26,10),(26,26));self.add_arc('br',(26,26),(22,30),radius_x=4)
self.add_line('base',(22,30),(10,30));self.add_arc('bl',(10,30),(6,26),radius_x=4)
self.add_line('left',(6,26),(6,10));self.add_contour('body','right','br','base','bl','left');self.relate('connect','lid','body')
''')
plan(28,'VRECT_XL','Open padlock with rounded body and circular shackle open at the right.','lock-open','''
box(self,'body',4,16,28,30,3)
self.add_line('shackle-l',(9,16),(9,9));self.add_arc('shackle-top',(9,9),(23,9),radius_x=7)
self.add_contour('shackle','shackle-l','shackle-top');self.relate('connect','body','shackle')
''')
plan(29,'SQUARE','Rounded microchip body with exactly two straight pins on each of its four sides.','cpu','''
box(self,'body',6,6,26,26,3)
for i,v in enumerate((11,21)):
 for side,a,b in [('top',(v,2),(v,6)),('bottom',(v,26),(v,30)),('left',(2,v),(6,v)),('right',(26,v),(30,v))]:
  name=f'{side}-{i}';self.add_line(name,a,b);self.relate('connect',name,'body')
''')
plan(30,'CIRCLE','Enclosing circle and two upward diverging curved arrows sharing a bottom origin.','split','''
circle(self,'frame',16,16,14)
for name,end,c1,c2,pts in [('left',(11,11),(16,18),(14,14),((11,15),(11,11),(15,11))),('right',(21,11),(16,18),(18,14),((17,11),(21,11),(21,15)))]:
 self.add_bezier(name,(16,24),(c1,c2,end));self.add_polyline(name+'-head',*pts);self.relate('connect',name,name+'-head')
self.relate('connect','left','right')
''')
# Facial-scan source is the same complete construction reviewed in batch 2.
import runpy
prior=runpy.run_path(str(__import__('pathlib').Path(__file__).resolve().parent.parent/'side-repair-50-priority-2/designs.py'))['D']
D[31]=prior[11]
plan(42,'VRECT_XL','Vertical paperclip formed by an outer upper arch, lower return and inner hook.','paperclip','''
self.add_arc('outer-top',(4,14),(28,14),radius_x=12)
self.add_line('outer-r',(28,14),(28,22));self.add_arc('bottom',(28,22),(12,22),radius_x=8)
self.add_line('inner-l',(12,22),(12,16));self.add_arc('hook',(12,16),(20,16),radius_x=4)
self.add_line('end',(20,16),(20,22))
self.add_contour('clip','outer-top','outer-r','bottom','inner-l','hook','end')
''')
plan(45,'VRECT_XL','Rounded document with two left-aligned lines, the lower line shorter.','file','''
box(self,'page',4,2,28,30,3)
self.add_line('line-1',(12,12),(20,12));self.add_line('line-2',(12,21),(15,21))
''')
plan(48,'SQUARE','Three circular toes around a triangular paw pad.','paw-print','''
for name,x,y in [('top',16,6),('left',6,16),('right',26,16)]:circle(self,name,x,y,4)
self.add_polyline('pad',(8,30),(16,23),(24,30),closed=True)
''')
plan(50,'HRECT_XL','Downward diagonal pointing hand with extended finger, curved back, folded thumb and open wrist.','hand','''
self.add_bezier('back',(30,4),((26,7),(22,7),(20,7)))
self.add_bezier('upper',(20,7),((15,7),(7,12),(3,16)))
self.add_bezier('thumb-round',(3,16),((2,17),(2,19),(4,19)))
self.add_line('thumb-inner',(4,19),(12,16))
self.add_line('finger-left',(12,16),(7,25))
self.add_bezier('tip',(7,25),((6,27),(7,28),(9,28)))
self.add_line('finger-base',(9,28),(15,28));self.add_line('finger-right',(15,28),(30,10))
self.add_contour('hand','back','upper','thumb-round','thumb-inner','finger-left','tip','finger-base','finger-right')
''')
# Repair contour membership explicitly; polylines own their member contour.
def change(n,old,new):
 shape,parts,ref,body=D[n];assert old in body,(n,old);D[n]=(shape,parts,ref,body.replace(old,new))
change(10,"self.add_polyline('wrist',(7,28),(4,28),(4,16))","self.add_line('wrist-a',(7,28),(4,28));self.add_line('wrist-b',(4,28),(4,16))")
change(10,"'wrist',closed=True","'wrist-a','wrist-b',closed=True")
change(12,"self.add_polyline('petals',(7,2),(16,8),(25,2),(25,11))","self.add_line('petal-l',(7,2),(16,8));self.add_line('petal-r',(16,8),(25,2));self.add_line('petal-side',(25,2),(25,11))")
change(12,"'petals','cup'","'petal-l','petal-r','petal-side','cup'")
change(14,"self.add_polyline('back-base',(30,27),(30,28),(16,28));self.add_contour('back-body','back-shoulders','back-base',closed=True)","self.add_line('back-r',(30,27),(30,28));self.add_line('back-base',(30,28),(16,28));self.add_line('back-l',(16,28),(16,27));self.add_contour('back-body','back-shoulders','back-r','back-base','back-l',closed=True)")
change(25,"self.add_polyline('right',(30,10),(30,18),(22,18),(22,30),(10,30),(10,18),(2,18),(2,10))","pts=((30,10),(30,18),(22,18),(22,30),(10,30),(10,18),(2,18),(2,10))\nfor i,(a,b) in enumerate(zip(pts,pts[1:])):self.add_line(f'edge-{i}',a,b)")
change(25,"'right','shoulder-l'","*[f'edge-{i}' for i in range(7)],'shoulder-l'")
# Wave extrema are owned by horizontal tangent joints, avoiding an overshoot.
plan(19,'HRECT_XL','Three separate horizontal wind waves with rising curled right ends.','wind','''
for i,y in enumerate((4,14,24)):
 self.add_bezier(f'a-{i}',(2,y+2),((5,y),(7,y),(9,y)))
 self.add_bezier(f'b-{i}',(9,y),((14,y),(15,y+4),(22,y+4)))
 self.add_bezier(f'c-{i}',(22,y+4),((27,y+4),(30,y+4),(30,y)))
 self.add_contour(f'wave-{i}',f'a-{i}',f'b-{i}',f'c-{i}')
''')
plan(16,'SQUARE','Warning triangle with a vertical exclamation stem and separate dot.','triangle-alert','''
self.add_polyline('triangle',(16,2),(30,30),(2,30),closed=True)
self.add_line('stem',(16,15),(16,17));self.add_dot('dot',(16,23))
''')
change(17,"(7,20),(17,30)","(7,20),(15,30)")
change(24,"((10,17),(20,23),(27,23))","((10,17),(20,23),(27,23))")
# Shorter arrowhead avoids trapping a tiny enclosed wedge at the attachment.
change(24,"(12,2),(16,4),(12,8)","(12,2),(18,4),(14,8)")
change(24,"'outer-a',(16,4)","'outer-a',(18,4)")
change(30,"(16,24)","(16,23)")
# Keep both circular wheels open and make the truck body stop at their edges.
for n in (2,37):
 plan(n,'HRECT_XL','Delivery truck with rectangular cargo body, sloped cab, vertical divider and two open circular wheels.','truck','''
for name,x in [('rear',6),('front',26)]:circle(self,name,x,24,4)
self.add_line('left',(2,24),(2,6));self.add_arc('tl',(2,6),(4,4),radius_x=2)
self.add_line('top',(4,4),(16,4));self.add_line('divider',(16,4),(16,24))
self.add_line('floor',(10,24),(22,24))
self.add_polyline('cab',(16,10),(24,10),(30,18),(30,24))
self.add_contour('cargo','left','tl','top','divider')
for a,b in [('rear','cargo'),('rear','floor'),('front','cab'),('front','floor'),('cargo','floor'),('cargo','cab')]:self.relate('connect',a,b)
''')
plan(15,'SQUARE','Thermometer with rounded stem, bulb, interior mercury line, bulb dot and two right-side scale ticks.','thermometer','''
self.add_arc('top',(4,10),(20,10),radius_x=8)
self.add_line('right',(20,10),(20,19));self.add_bezier('bulb-r',(20,19),((24,23),(22,30),(12,30)))
self.add_bezier('bulb-l',(12,30),((2,30),(0,23),(4,19)))
self.add_line('left',(4,19),(4,10));self.add_contour('thermometer','top','right','bulb-r','bulb-l','left',closed=True)
self.add_line('mercury',(12,13),(12,17));self.add_dot('bulb-dot',(12,24))
self.add_line('tick-1',(28,6),(30,6));self.add_line('tick-2',(28,14),(30,14))
''')
plan(35,'SQUARE','Pig face with two rounded ears, broad curved cheeks, two short eyes and open oval snout.','none','''
self.add_bezier('ear-l-top',(9,6),((7,2),(3,2),(2,2)))
self.add_bezier('ear-l-side',(2,2),((2,9),(3,10),(5,11)))
self.add_bezier('cheek-l',(5,11),((1,23),(5,30),(16,30)))
self.add_bezier('cheek-r',(16,30),((27,30),(31,23),(27,11)))
self.add_bezier('ear-r-side',(27,11),((29,10),(30,9),(30,2)))
self.add_bezier('ear-r-top',(30,2),((29,2),(25,2),(23,6)))
self.add_bezier('forehead',(23,6),((19,4),(13,4),(9,6)))
self.add_contour('face','ear-l-top','ear-l-side','cheek-l','cheek-r','ear-r-side','ear-r-top','forehead',closed=True)
self.add_arc('snout-top',(11,22),(21,22),radius_x=5,radius_y=4)
self.add_arc('snout-bottom',(21,22),(11,22),radius_x=5,radius_y=4)
self.add_contour('snout','snout-top','snout-bottom',closed=True)
self.add_dot('eye-l',(10,13));self.add_dot('eye-r',(22,13))
''')
from text_designs import TEXT
for n,t in TEXT.items():
 plan(n,'SQUARE','Shared typeface '+', '.join(t['glyphs'])+'; natural proportions, 32-unit ink height and grid-fitted layout.','icon_set/typeface/glyphs.json',t['body'])
plan(15,'SQUARE','Thermometer with rounded stem, bulb, interior mercury line, bulb dot and two right-side scale ticks.','thermometer','''
self.add_arc('top',(4,10),(20,10),radius_x=8)
self.add_line('right',(20,10),(20,19));self.add_bezier('bulb-r',(20,19),((22,21),(22,23),(22,24)))
self.add_arc('bulb-bottom',(22,24),(2,24),radius_x=10,radius_y=6)
self.add_bezier('bulb-l',(2,24),((2,23),(2,21),(4,19)))
self.add_line('left',(4,19),(4,10));self.add_contour('thermometer','top','right','bulb-r','bulb-bottom','bulb-l','left',closed=True)
self.add_line('mercury',(12,13),(12,16));self.add_dot('bulb-dot',(12,23))
self.add_line('tick-1',(28,6),(30,6));self.add_line('tick-2',(28,14),(30,14))
''')
change(16,"(16,15),(16,17)","(16,16),(16,17)")
change(30,"(11,11),(16,18),(14,14),((11,15),(11,11),(15,11))","(10,12),(16,18),(13,15),((10,16),(10,12),(13,12))")
change(30,"(21,11),(16,18),(18,14),((17,11),(21,11),(21,15))","(22,12),(16,18),(19,15),((19,12),(22,12),(22,16))")
change(48,"(8,30),(16,23),(24,30)","(6,30),(16,21),(26,30)")
change(35,"(11,22),(21,22),radius_x=5,radius_y=4","(11,20),(21,20),radius_x=5,radius_y=3")
change(35,"(21,22),(11,22),radius_x=5,radius_y=4","(21,20),(11,20),radius_x=5,radius_y=3")
change(35,"(10,13)","(11,11)");change(35,"(22,13)","(21,11)")
plan(50,'HRECT_XL','Downward diagonal pointing hand with extended finger, curved back, folded thumb and open wrist.','hand','''
self.add_bezier('back',(30,4),((26,7),(22,7),(20,7)))
self.add_bezier('upper',(20,7),((13,7),(2,12),(2,15)))
self.add_bezier('thumb-round',(2,15),((2,18),(3,19),(5,19)))
self.add_line('thumb-inner',(5,19),(13,16))
self.add_line('finger-left',(13,16),(7,25))
self.add_bezier('tip',(7,25),((6,27),(7,28),(9,28)))
self.add_line('finger-base',(9,28),(15,28));self.add_line('finger-right',(15,28),(30,10))
self.add_contour('hand','back','upper','thumb-round','thumb-inner','finger-left','tip','finger-base','finger-right')
''')
# Shared dollar paths genuinely cross at the stem; declare that scoped contact.
shape,parts,ref,body=D[32];D[32]=(shape,parts,ref,body+"\nself.relate('connect','path-1-1','path-2-1')\n")
change(35,"(9,6)","(9,5)");change(35,"(23,6)","(23,5)")
plan(41,'SQUARE','Two staggered falling bombs, each with an elongated rounded body and complete notched chevron tail.','none','''
for name,x,y in [('left',2,2),('right',22,8)]:
 box(self,name+'-body',x,y+10,x+8,y+22,4)
 self.add_polyline(name+'-tail',(x,y),(x+4,y+3),(x+8,y),(x+8,y+8),(x+4,y+10),(x,y+8),closed=True)
 self.relate('connect',name+'-tail',name+'-body')
''')
change(35,"(5,11)","(4,11)");change(35,"(27,11)","(28,11)")
change(14,"for name,x in [('front',9),('back',23)]:circle(self,name+'-head',x,8,4)","circle(self,'front-head',9,8,4)\ncircle(self,'back-head',23,9,3)")
# Shared integer attachment nodes on the housing edge and both compass legs.
change(11,"(30,17),(12,23)","(30,16),(12,22)")
change(11,"(22,20),(22,25)","(21,19),(21,25)")
change(11,"(22,25),(25,28)","(21,25),(24,28)")
change(11,"(25,28),(30,28)","(24,28),(30,28)")
plan(23,'SQUARE','Drafting compass with circular pivot, short top stem, two spreading legs and cross brace.','drafting-compass','''
circle(self,'pivot',22,9,5)
# (25,5) and (18,12) are exact 3-4-5 points on the circular pivot.
self.add_line('cap',(25,5),(30,2));self.relate('connect','cap','pivot')
self.add_line('left-leg',(18,12),(2,24));self.relate('connect','left-leg','pivot')
self.add_line('right-leg',(22,14),(18,30));self.relate('connect','right-leg','pivot')
# Brace begins on the left leg at (10,18), crosses the right at (20,22).
self.add_line('brace',(10,18),(25,24));self.relate('connect','brace','left-leg');self.relate('connect','brace','right-leg')
''')
plan(24,'VRECT_XL','Circular rotation arrow with a break at upper right and curved diagonal internal sweep.','rotate-cw','''
self.add_bezier('outer-a',(18,4),((13,4),(9,6),(7,9)))
self.add_bezier('outer-upper-left',(7,9),((5,12),(4,14),(4,17)))
self.add_bezier('outer-b',(4,17),((4,24),(9,30),(16,30)))
self.add_bezier('outer-c',(16,30),((21,30),(25,27),(27,23)))
self.add_bezier('outer-lower-right',(27,23),((28,21),(28,19),(28,17)))
self.add_bezier('outer-d',(28,17),((28,13),(26,10),(24,8)))
self.add_contour('outer','outer-a','outer-upper-left','outer-b','outer-c','outer-lower-right','outer-d')
self.add_polyline('arrow',(12,2),(18,4),(14,8));self.relate('connect','arrow','outer')
self.add_bezier('sweep',(7,9),((10,17),(20,23),(27,23)));self.relate('connect','sweep','outer')
''')
