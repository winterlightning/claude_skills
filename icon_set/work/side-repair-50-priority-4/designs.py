"""Source-faithful centerlines, repair batch 4."""
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/side-repair-50-priority-4/batch.json'
AUTHOR='gpt-6'
D={}
def plan(n,shape,parts,ref,body):D[n]=(shape,parts,ref,body)
plan(2,'SQUARE','Rounded headphone arch and two open rectangular ear cups.','headphones','''
self.add_arc('arch',(2,16),(30,16),radius_x=14)
for side,x in [('left',2),('right',30)]:
 self.add_line(side,(x,16),(x,22));self.relate('connect',side,'arch')
box(self,'cup-l',2,22,10,30,2);box(self,'cup-r',22,22,30,30,2)
self.relate('connect','cup-l','left');self.relate('connect','cup-r','right')
''')
plan(3,'VRECT_XL','Right-facing horse head with pointed ear, projecting muzzle, curved neck and flat base.','none','''
self.add_bezier('back',(4,30),((4,12),(6,6),(16,5)))
self.add_line('ear-a',(16,5),(18,2));self.add_line('ear-b',(18,2),(19,7))
self.add_line('face',(19,7),(28,13));self.add_line('nose',(28,13),(26,18))
self.add_bezier('muzzle',(26,18),((24,20),(21,17),(17,16)))
self.add_bezier('neck',(17,16),((16,21),(19,27),(22,30)))
self.add_line('base',(22,30),(4,30))
self.add_contour('horse','back','ear-a','ear-b','face','nose','muzzle','neck','base',closed=True)
''')
plan(6,'SQUARE','Two broken diagonal chain ends and three separate upper-left break rays.','link-2-off','''
self.add_line('ur-a',(21,3),(23,2));self.add_bezier('ur-b',(23,2),((27,2),(30,5),(30,9)))
self.add_line('ur-c',(30,9),(23,16));self.add_contour('upper-link','ur-a','ur-b','ur-c')
self.add_line('ll-a',(9,16),(2,23));self.add_bezier('ll-b',(2,23),((2,27),(5,30),(9,30)))
self.add_line('ll-c',(9,30),(16,23));self.add_contour('lower-link','ll-a','ll-b','ll-c')
self.add_line('ray-top',(12,2),(12,6));self.add_line('ray-diagonal',(3,3),(6,6));self.add_line('ray-left',(2,12),(6,12))
''')
plan(8,'SQUARE','Circular search lens with lower-right handle and connected activity pulse.','search-activity (local reference unavailable)','''
circle(self,'lens',15,15,13)
self.add_line('handle',(24,24),(30,30));self.relate('connect','handle','lens')
self.add_polyline('pulse',(2,15),(8,15),(10,19),(14,9),(18,21),(20,13),(21,13));self.relate('connect','pulse','lens')
''')
plan(10,'VRECT_XL','Menstrual cup with closed thick rim, tapered curved cup and rounded lower stem.','none','''
box(self,'rim',4,2,28,10,3)
self.add_bezier('left',(7,10),((7,17),(9,20),(12,23)))
self.add_line('stem-l',(12,23),(12,26));self.add_arc('stem-base',(12,26),(20,26),radius_x=4,sweep=False)
self.add_line('stem-r',(20,26),(20,23));self.add_bezier('right',(20,23),((23,20),(25,17),(25,10)))
self.add_contour('cup','left','stem-l','stem-base','stem-r','right');self.relate('connect','cup','rim')
''')
plan(11,'VRECT_XL','Rounded smartphone with separate horizontal home bar.','smartphone','''
box(self,'phone',4,2,28,30,4)
self.add_line('home',(14,22),(18,22))
''')
plan(12,'HRECT_S','Wide closed rounded rectangular minus outline.','minus','''
box(self,'minus',2,10,30,22,3)
''')
plan(14,'VRECT_XL','Rounded smartphone with two pause bars and complete footer divider.','smartphone','''
box(self,'phone',4,2,28,30,3)
self.add_line('footer',(4,22),(28,22));self.relate('connect','phone','footer')
for i,x in enumerate((12,20)):self.add_line(f'pause-{i}',(x,10),(x,14))
''')
plan(18,'SQUARE','Hexagonal nanobot body, open circular center and two attached lower claws.','bot','''
self.add_polyline('body',(16,2),(28,9),(28,21),(16,28),(4,21),(4,9),closed=True)
circle(self,'opening',16,14,4)
for name,a,c1,c2,b in [('left',(4,21),(1,25),(1,27),(4,30)),('right',(28,21),(31,25),(31,27),(28,30))]:
 self.add_bezier(name,a,(c1,c2,b));self.relate('connect',name,'body')
''')
plan(20,'HRECT_XL','Horizontal oval frame and separate rising check mark.','circle-check','''
self.add_arc('top',(2,16),(30,16),radius_x=14,radius_y=12)
self.add_arc('bottom',(30,16),(2,16),radius_x=14,radius_y=12)
self.add_contour('oval','top','bottom',closed=True)
self.add_polyline('check',(10,16),(14,20),(21,12))
''')
plan(21,'SQUARE','Paper plane with pointed upper-right nose, lower folded tail and internal fold ending inside.','send','''
self.add_polyline('plane',(2,15),(30,2),(23,28),(15,23),(11,30),(10,20),closed=True)
self.add_line('fold',(10,20),(18,15));self.relate('connect','fold','plane')
''')
plan(24,'VRECT_XL','Upright religious cross with short horizontal arms and longer lower stem.','cross','''
self.add_polyline('cross',(12,2),(20,2),(20,10),(28,10),(28,18),(20,18),(20,30),(12,30),(12,18),(4,18),(4,10),(12,10),closed=True)
''')
plan(25,'HRECT_XL','Tilted retro controller with diagonal curved body, plus pad and two separate round buttons.','gamepad-2','''
self.add_bezier('a',(22,4),((26,4),(30,7),(30,12)))
self.add_bezier('b',(30,12),((30,19),(27,24),(22,25)))
self.add_bezier('c',(22,25),((17,26),(15,28),(10,28)))
self.add_bezier('d',(10,28),((5,28),(2,25),(2,20)))
self.add_bezier('e',(2,20),((2,15),(5,12),(10,10)))
self.add_bezier('f',(10,10),((15,8),(17,4),(22,4)))
self.add_contour('body','a','b','c','d','e','f',closed=True)
self.add_line('pad-h',(8,19),(14,19));self.add_line('pad-v',(11,16),(11,22));self.relate('connect','pad-h','pad-v')
self.add_dot('button-a',(22,11));self.add_dot('button-b',(22,18))
''')
plan(27,'SQUARE','Rounded microchip body with exactly two pins on each of four sides.','cpu','''
box(self,'body',6,6,26,26,3)
for i,v in enumerate((11,21)):
 for side,a,b in [('top',(v,2),(v,6)),('bottom',(v,26),(v,30)),('left',(2,v),(6,v)),('right',(26,v),(30,v))]:
  name=f'{side}-{i}';self.add_line(name,a,b);self.relate('connect',name,'body')
''')
plan(30,'HRECT_XL','Open triangular sand mound with three separate dots inside.','mountain','''
self.add_polyline('mound',(2,28),(16,4),(30,28))
for i,p in enumerate(((11,26),(21,26),(16,18))):self.add_dot(f'grain-{i}',p)
''')
plan(31,'HRECT_XL','Seated electric scooter with two open wheels, seat and stem, low chassis and tall steering handle.','bike','''
for name,x in [('rear',6),('front',26)]:circle(self,name,x,24,4)
self.add_polyline('steering',(20,4),(24,4),(26,24));self.relate('connect','steering','front')
self.add_line('chassis',(6,24),(18,24));self.add_bezier('rise',(18,24),((22,24),(23,18),(25,14)))
self.add_contour('frame','chassis','rise');self.relate('connect','frame','rear');self.relate('connect','frame','steering')
self.add_line('seat',(12,14),(18,14));self.add_line('post',(16,14),(16,24));self.relate('connect','seat','post');self.relate('connect','post','frame')
''')
plan(32,'SQUARE','Shopping cart with left handle, closed basket, lower hook and two round wheels.','shopping-cart','''
self.add_polyline('handle',(2,2),(6,2),(10,18))
self.add_line('top',(8,10),(30,10));self.add_bezier('basket-r',(30,10),((30,16),(29,18),(26,18)))
self.add_line('base',(26,18),(10,18));self.add_contour('basket','top','basket-r','base');self.relate('connect','basket','handle')
self.add_bezier('hook',(10,18),((8,20),(8,22),(10,24)));self.relate('connect','hook','basket');self.relate('connect','hook','handle')
self.add_dot('wheel-l',(12,30));self.add_dot('wheel-r',(26,30))
''')
plan(34,'CIRCLE','Circle containing three separated curved fragments of an inner ring.','none','''
circle(self,'outer',16,16,14)
self.add_bezier('inner-a',(9,12),((10,10),(12,9),(15,9)))
self.add_bezier('inner-b',(22,12),((24,14),(24,18),(22,20)))
self.add_bezier('inner-c',(15,23),((12,23),(10,22),(9,19)))
''')
plan(35,'HRECT_XL','Three nested open Wi-Fi arches without a dot.','wifi','''
for n,left,top,right,y in [('outer',2,4,30,12),('middle',8,14,24,20),('inner',12,24,20,28)]:
 self.add_bezier(n+'-l',(left,y),((left+3,top+2),(13,top),(16,top)))
 self.add_bezier(n+'-r',(16,top),((19,top),(right-3,top+2),(right,y)))
 self.add_contour(n,n+'-l',n+'-r')
''')
plan(36,'HRECT_XL','Cylindrical soap bar with complete open elliptical top, vertical sides and curved lower edge.','cylinder','''
self.add_arc('top-a',(2,10),(30,10),radius_x=14,radius_y=6)
self.add_arc('top-b',(30,10),(2,10),radius_x=14,radius_y=6)
self.add_contour('top','top-a','top-b',closed=True)
self.add_line('left',(2,10),(2,22));self.add_arc('base',(2,22),(30,22),radius_x=14,radius_y=6,sweep=False)
self.add_line('right',(30,22),(30,10));self.add_contour('body','left','base','right');self.relate('connect','body','top')
''')
plan(38,'CIRCLE','Circle with two centered equal-length horizontal equality bars.','equal','''
circle(self,'circle',16,16,14)
self.add_line('upper',(10,12),(22,12));self.add_line('lower',(10,20),(22,20))
''')
plan(40,'SQUARE','T-shirt with angled sleeves, round neck, upright torso and flat hem.','shirt','''
points=((11,2),(2,8),(6,16),(10,14),(10,30),(22,30),(22,14),(26,16),(30,8),(21,2))
for i,(a,b) in enumerate(zip(points,points[1:])):self.add_line(f'edge-{i}',a,b)
self.add_arc('neck',(21,2),(11,2),radius_x=5)
self.add_contour('shirt',*[f'edge-{i}' for i in range(9)],'neck',closed=True)
''')
plan(47,'SQUARE','Three acupuncture needles with open circular heads and distinct upward, horizontal and downward directions.','syringe','''
for name,x,y,a,b in [('top',19,5,(13,10),(17,7)),('middle',27,16,(2,16),(24,16)),('bottom',19,27,(2,24),(16,27))]:
 circle(self,name+'-head',x,y,3);self.add_line(name+'-stem',a,b);self.relate('connect',name+'-head',name+'-stem')
''')
plan(48,'SQUARE','Three downward arrows, center arrow lower than the two matching outer arrows.','arrow-down','''
for name,x,y in [('left',6,2),('right',26,2),('middle',16,14)]:
 self.add_line(name+'-stem',(x,y),(x,y+16));self.add_polyline(name+'-head',(x-4,y+12),(x,y+16),(x+4,y+12));self.relate('connect',name+'-head',name+'-stem')
''')
plan(49,'HRECT_XL','Three separate matching vertical lightning zigzags.','zap','''
for i,x in enumerate((2,13,25)):self.add_polyline(f'bolt-{i}',(x+5,4),(x,16),(x+5,16),(x,28))
''')
plan(50,'VRECT_XL','Three-petal bud with pointed center leaf, two side petals, visible internal boundaries and short stem.','flower-2','''
self.add_bezier('center-l-top',(16,2),((13,5),(11,8),(11,12)))
self.add_bezier('center-l-base',(11,12),((11,18),(13,22),(16,25)))
self.add_bezier('center-r-base',(16,25),((19,22),(21,18),(21,12)))
self.add_bezier('center-r-top',(21,12),((21,8),(19,5),(16,2)))
self.add_contour('center','center-l-top','center-l-base','center-r-base','center-r-top',closed=True)
for name,a,c1,c2,b,c3,c4 in [('left',(4,6),(4,15),(6,21),(16,25),(7,8),(9,10)),('right',(28,6),(28,15),(26,21),(16,25),(25,8),(23,10))]:
 self.add_bezier(name+'-outer',a,(c1,c2,b))
 self.add_bezier(name+'-upper',a,(c3,c4,(11 if name=='left' else 21,12)))
 self.relate('connect',name+'-outer',name+'-upper');self.relate('connect',name+'-outer','center');self.relate('connect',name+'-upper','center')
self.relate('connect','left-outer','right-outer')
self.add_line('stem',(16,25),(16,30));self.relate('connect','stem','center');self.relate('connect','stem','left-outer');self.relate('connect','stem','right-outer')
''')
from text_designs import TEXT
for n,t in TEXT.items():plan(n,'SQUARE','Shared typeface '+', '.join(t['glyphs'])+'; natural proportions, 32-unit ink height and integer fitted layout.','icon_set/typeface/glyphs.json',t['body'])
def change(n,old,new):
 shape,parts,ref,body=D[n];assert old in body,(n,old);D[n]=(shape,parts,ref,body.replace(old,new))
change(2,"2,22,10,30","2,20,10,30");change(2,"22,22,30,30","22,20,30,30")
change(10,"((7,17),(9,20),(12,23))","((7,17),(12,20),(12,24))")
change(10,"(12,23),(12,26)","(12,24),(12,26)")
change(10,"(20,26),(20,23)","(20,26),(20,24)")
change(10,"'right',(20,23),((23,20),(25,17),(25,10))","'right',(20,24),((20,20),(25,17),(25,10))")
plan(6,'SQUARE','Two open diagonal chain ends and three separate upper-left break rays.','link-2-off','''
self.add_line('upper-a',(16,9),(21,4))
self.add_bezier('upper-b',(21,4),((23,2),(24,2),(25,2)))
self.add_bezier('upper-c',(25,2),((28,2),(30,4),(30,7)))
self.add_bezier('upper-d',(30,7),((30,9),(29,10),(27,12)))
self.add_line('upper-e',(27,12),(23,16));self.add_contour('upper','upper-a','upper-b','upper-c','upper-d','upper-e')
self.add_line('lower-a',(9,16),(4,21))
self.add_bezier('lower-b',(4,21),((2,23),(2,24),(2,25)))
self.add_bezier('lower-c',(2,25),((2,28),(4,30),(7,30)))
self.add_bezier('lower-d',(7,30),((9,30),(10,29),(12,27)))
self.add_line('lower-e',(12,27),(16,23));self.add_contour('lower','lower-a','lower-b','lower-c','lower-d','lower-e')
self.add_line('ray-top',(12,2),(12,4));self.add_line('ray-diagonal',(3,3),(5,5));self.add_line('ray-left',(2,12),(4,12))
''')
plan(18,'SQUARE','Hexagonal nanobot body, open circular center and two attached lower claws.','bot','''
self.add_polyline('body',(16,2),(28,9),(28,21),(16,28),(4,21),(4,9),closed=True)
circle(self,'opening',16,14,4)
self.add_bezier('claw-l-a',(4,21),((3,23),(2,24),(2,26)))
self.add_bezier('claw-l-b',(2,26),((2,28),(3,29),(4,30)))
self.add_bezier('claw-r-a',(28,21),((29,23),(30,24),(30,26)))
self.add_bezier('claw-r-b',(30,26),((30,28),(29,29),(28,30)))
for side in ('l','r'):
 self.add_contour('claw-'+side,'claw-'+side+'-a','claw-'+side+'-b');self.relate('connect','claw-'+side,'body')
''')
change(25,"(11,16),(11,22)","(11,17),(11,22)")
plan(31,'HRECT_XL','Seated electric scooter with two open wheels, seat and stem, low chassis and tall steering handle.','bike','''
for name,x in [('rear',6),('front',26)]:circle(self,name,x,24,4)
self.add_polyline('steering',(20,4),(24,4),(26,20));self.relate('connect','steering','front')
self.add_line('chassis',(10,24),(17,24))
self.add_bezier('rise',(17,24),((21,24),(22,16),(25,12)))
self.add_contour('frame','chassis','rise');self.relate('connect','frame','rear');self.relate('connect','frame','steering')
self.add_line('seat',(12,14),(18,14));self.add_line('post',(16,14),(16,24));self.relate('connect','seat','post');self.relate('connect','post','frame')
''')
change(34,"(9,12),((10,10),(12,9),(15,9))","(10,12),((11,10),(13,9),(15,9))")
change(34,"(22,12),((24,14),(24,18),(22,20))","(22,13),((24,15),(24,17),(22,19))")
change(34,"(15,23),((12,23),(10,22),(9,19))","(15,23),((12,23),(11,22),(10,19))")
plan(35,'HRECT_XL','Three nested open Wi-Fi arches without a dot.','wifi','''
for n,left,right,y,rx,ry in [('outer',2,30,12,14,8),('middle',8,24,20,8,6),('inner',12,20,28,4,4)]:
 self.add_arc(n,(left,y),(right,y),radius_x=rx,radius_y=ry)
''')
plan(37,'SQUARE','Spiraling tornado with a continuous upper coil and two separate narrowing lower curves.','tornado','''
self.add_bezier('a',(22,2),((11,2),(2,5),(2,10)))
self.add_bezier('b',(2,10),((2,14),(8,16),(16,16)))
self.add_bezier('c',(16,16),((24,16),(30,14),(30,11)))
self.add_bezier('d',(30,11),((30,8),(22,8),(19,8)))
self.add_bezier('e',(19,8),((15,8),(12,9),(12,10)))
self.add_contour('coil','a','b','c','d','e')
self.add_bezier('middle',(8,22),((12,24),(20,24),(24,22)))
self.add_bezier('bottom-l',(12,29),((13,30),(14,30),(16,30)))
self.add_bezier('bottom-r',(16,30),((18,30),(19,30),(20,29)))
self.add_contour('bottom','bottom-l','bottom-r')
''')
change(25,"(8,19),(14,19)","(9,19),(14,19)")
change(47,"(13,10),(17,7)","(10,10),(16,5)")
change(37,"((12,24),(20,24),(24,22))","((12,23),(20,23),(24,22))")
change(37,"(12,9),(12,10)","(13,9),(13,10)")
change(25,"(9,19),(14,19)","(9,19),(13,19)")
change(25,"(11,17),(11,22)","(11,17),(11,21)")
change(37,"((30,8),(22,8),(19,8))","((30,9),(22,9),(19,9))")
change(37,"'e',(19,8),((15,8),(13,9),(13,10))","'e',(19,9),((16,9),(14,10),(14,11))")
