from refine_final import *
# The supplied beetle has FOUR lateral legs, not the six invented by its parent.
DESIGNS[31]=('SQUARE','Restore original four lateral legs, two antennae, domed head and rounded body.','bug','''
self.add_bezier('head-left',(7,12),((7,9),(8,8),(11,5)))
self.add_bezier('head-top-left',(11,5),((12,4),(14,4),(16,4)))
self.add_bezier('head-top-right',(16,4),((18,4),(20,4),(21,5)))
self.add_bezier('head-right',(21,5),((24,8),(25,9),(25,12)))
self.add_line('head-base',(25,12),(7,12))
self.add_contour('head','head-left','head-top-left','head-top-right','head-right','head-base',closed=True)
self.add_line('right',(25,12),(25,21))
self.add_arc('bottom',(25,21),(7,21),radius_x=9)
self.add_line('left',(7,21),(7,12))
self.add_contour('body','right','bottom','left')
self.relate('connect','head','body')
for side in (-1,1):
    x=16+9*side;outer=16+14*side
    self.add_polyline(f'upper-leg-{side}',(x,14),(outer-2*side,14),(outer,10))
    self.add_polyline(f'lower-leg-{side}',(x,21),(outer-2*side,24),(outer,28))
    self.relate('connect','body',f'upper-leg-{side}')
    self.relate('connect','body',f'lower-leg-{side}')
    self.add_line(f'antenna-{side}',(16+5*side,5),(16+9*side,2))
    self.relate('connect','head',f'antenna-{side}')
''')
body(20,{"(16,22),((16,25),(15,28),(13,30))":"(15,22),((15,25),(14,28),(12,30))"})
PATCHES[43][2].update({'(11, 13)':'(11, 14)','(21, 13)':'(21, 14)'})
# Corresponding pupil and mouth clearances need room in the same parent layout.
PATCHES[43][2].update({'(10, 20)':'(10, 21)','(16, 20)':'(16, 21)','(22, 20)':'(22, 21)'})
body(39,{"(7,13),(11,6)":"(7,13),(10,7)","self.add_arc('roof-left',(11,6),(14,4),radius_x=4)":"self.add_bezier('roof-left',(10,7),((11,5),(12,4),(14,4)))","self.add_arc('roof-right',(18,4),(21,6),radius_x=4)":"self.add_bezier('roof-right',(18,4),((20,4),(21,5),(22,7)))","(21,6),(25,13)":"(22,7),(25,13)"})
body(36,{"self.add_polyline('top',(5,10),(8,10),(12,4),(20,4),(24,10),(27,10))":"self.add_line('top-left',(5,10),(8,10))\nself.add_bezier('housing-left',(8,10),((10,10),(10,4),(12,4)))\nself.add_line('housing-top',(12,4),(20,4))\nself.add_bezier('housing-right',(20,4),((22,4),(22,10),(24,10)))\nself.add_line('top-right',(24,10),(27,10))\nself.add_contour('top','top-left','housing-left','housing-top','housing-right','top-right')"})
PATCHES[50][2].pop('(29, 12)')
PATCHES[50][2].update({'((28, 14), (28, 15), (28, 16))':'((27, 14), (28, 15), (28, 16))',"self.add_bezier('p1-r1-2', (7, 17), ((13, 17), (17, 14), (22, 12)))\n        self.add_bezier('p1-r1-3', (22, 12), ((23, 11), (24, 10), (25, 10)))":"self.add_bezier('p1-r1-2', (7, 17), ((15, 17), (21, 10), (25, 10)))","'p1-r1-2', 'p1-r1-3', 'p1-r1-4'":"'p1-r1-2', 'p1-r1-4'"})
# Broader beak is required to preserve the diamond hole; keep the failure if it crowds the eyes.
body(48,{'(16,22),(20,26),(16,30),(12,26)':'(16,18),(22,24),(16,30),(10,24)'})
# Fix the bicycle's real fork/frame attachment before assessing residual spacing.
body(19,{'(12,12),(20,12),(16,24)':'(12,12),(22,12),(13,24)','(12,12),(16,24)':'(12,12),(13,24)','(26,24),(22,4),(19,4)':'(26,24),(22,12),(20,4),(17,4)','(12,12),(12,6)':'(12,12),(12,4)','(9,6),(15,6)':'(9,4),(15,4)'})
main()
