# Executes the preceding reconstruction before applying the final visual refinements.
from refine import *
body(3,{"self.add_bezier('tail',(9,27),((8,28),(6,28),(5,26)))":"self.add_bezier('tail-start',(9,27),((8,28),(8,28),(7,28)))\nself.add_bezier('tail',(7,28),((6,28),(6,27),(5,26)))","'fuselage','tail','tail-end'":"'fuselage','tail-start','tail','tail-end'"})
body(14,{'(18,16)':'(18,17)'})
body(20,{"(7,25),((10,24)":"(7,27),((10,26)","(16,21),((16,25),(15,28),(13,30))":"(16,22),((16,25),(15,28),(13,30))"})
body(30,{
"self.add_arc('lower-end',(4,22),(10,28),radius_x=5,sweep=False)":"self.add_bezier('lower-end-a',(4,22),((2,24),(2,26),(4,28)))\nself.add_bezier('lower-end-b',(4,28),((6,30),(8,30),(10,28)))",
"'lower-left','lower-end','lower-right'":"'lower-left','lower-end-a','lower-end-b','lower-right'",
"self.add_arc('upper-end',(23,4),(29,10),radius_x=5)":"self.add_bezier('upper-end-a',(23,4),((25,2),(27,2),(29,4)))\nself.add_bezier('upper-end-b',(29,4),((30,5),(30,6),(30,7)))\nself.add_bezier('upper-end-c',(30,7),((30,8),(30,9),(29,10)))",
"'upper-left','upper-end','upper-right'":"'upper-left','upper-end-a','upper-end-b','upper-end-c','upper-right'"})
# Keyshape here must be genuinely reached: bottom link is rounded through y30.
body(30,{"self.add_bezier('lower-end-b',(4,28),((6,30),(8,30),(10,28)))":"self.add_bezier('lower-end-b',(4,28),((5,29),(6,30),(7,30)))\nself.add_bezier('lower-end-c',(7,30),((8,30),(9,29),(10,28)))","'lower-end-b','lower-right'":"'lower-end-b','lower-end-c','lower-right'"})
body(31,{
"self.add_arc('head',(7,12),(25,12),radius_x=9,radius_y=8)":"self.add_bezier('head-left',(7,12),((7,9),(8,6),(11,5)))\nself.add_bezier('head-top-left',(11,5),((12,4),(14,4),(16,4)))\nself.add_bezier('head-top-right',(16,4),((18,4),(20,4),(21,5)))\nself.add_bezier('head-right',(21,5),((24,6),(25,9),(25,12)))",
"'head','head-base'":"'head-left','head-top-left','head-top-right','head-right','head-base'",
"(25,12),(25,23)":"(25,12),(25,28)","(25,23),(7,23),radius_x=9,radius_y=7":"(25,28),(7,28),radius_x=9,radius_y=2","(7,23),(7,12)":"(7,28),(7,12)",
"(12,20,27)":"(12,20,28)","start=(x,y if j<2 else 23)":"start=(x,y)","y+3 if j==2":"y+2 if j==2"})
# Move eyes inward to give the muzzle/outer head genuine margin.
PATCHES[43][2].update({'(10, 13)':'(11, 13)','(22, 13)':'(21, 13)'})
body(45,{"(11,20),(21,20),radius_x=5":"(12,20),(20,20),radius_x=4"})
body(47,{'(8,y),(10,y+2),(14,y-2)':'(9,y),(11,y+2),(15,y-2)','(21,y+1),(24,y+1)':'(22,y+1),(23,y+1)'})
DESIGNS[19]=('HRECT_XL','Bicycle with two equal wheels, triangular frame, saddle and raised handlebar.','none','''
for x in (6,26):circle(self,f'wheel-{x}',x,24,4)
self.add_polyline('frame',(6,24),(12,12),(20,12),(16,24),(6,24))
self.add_line('crank',(12,12),(16,24))
self.add_polyline('fork',(26,24),(22,4),(19,4))
self.add_line('seatpost',(12,12),(12,6))
self.add_line('seat',(9,6),(15,6))
self.relate('connect','frame','crank');self.relate('connect','frame','seatpost')
self.relate('connect','seatpost','seat');self.relate('connect','frame','fork')
self.relate('connect','frame','wheel-6');self.relate('connect','fork','wheel-26')
''')
# Complete references with too many details get real candidate checks, never simplified replacements.
DESIGNS[10]=('SQUARE','Balaclava outline and two crossing loop eye opening; all source parts retained.','none','''
self.add_bezier('top-left',(2,17),((2,8),(7,2),(16,2)))
self.add_bezier('top-right',(16,2),((25,2),(30,8),(30,17)))
self.add_bezier('right',(30,17),((30,23),(27,25),(26,26)))
self.add_polyline('hem-right',(26,26),(28,30),(4,30),(6,26))
self.add_bezier('left',(6,26),((5,25),(2,23),(2,17)))
self.add_contour('top','top-left','top-right','right')
self.relate('connect','top','hem-right');self.relate('connect','left','hem-right');self.relate('connect','left','top')
self.add_bezier('eye-a',(16,16),((10,7),(6,11),(8,17)))
self.add_bezier('eye-b',(8,17),((10,22),(13,19),(16,16)))
self.add_bezier('eye-c',(16,16),((22,7),(26,11),(24,17)))
self.add_bezier('eye-d',(24,17),((22,22),(19,19),(16,16)))
self.add_contour('eyes','eye-a','eye-b','eye-c','eye-d',closed=True)
''')
main()
