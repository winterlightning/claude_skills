"""Three heart blooms on uneven branches grow from a square pot; tiny leaf twists omitted.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e88fb37a-e605-4d7e-a557-9e046dcb12ba'
SOURCE_PATH = 'pictographic-primitives/romance/love plant_e88fb37a-e605-4d7e-a557-9e046dcb12ba.svg'
AUTHOR = 'gpt-6'

class ThreeHeartPlantInSquarePot(Solo48):
    icon_id = 'three-heart-plant-in-square-pot'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    categories = ('primitives', 'romance')
    aliases = ()
    keywords = ('heart', 'plant', 'pot', 'branch', 'flower', 'romance')

    def build(self):
        # Plan: Three equal smooth heart leaves use the radial envelope to keep their spacing; a square pot owns three separated stem attachments.

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
        def heart(n,x,y):
         path(n,(x,y), [('C',(x-5,y+1),(x-1,y-2),(x-5,y-3)),('C',(x,y+8),(x-5,y+4),(x-2,y+6)),('C',(x+5,y+1),(x+2,y+6),(x+5,y+4)),('C',(x,y),(x+5,y-3),(x+1,y-2))],True)
        heart('centre',24,8);heart('left',10,20);heart('right',38,20)
        line('stem',(24,16),(24,35));line('branch-left',(10,28),(18,35));line('branch-right',(38,28),(30,35))
        poly('pot',(18,35),(24,35),(30,35),(30,43),(18,43),closed=True)
        for leaf,stem in [('centre','stem'),('left','branch-left'),('right','branch-right')]:join(leaf,stem);join(stem,'pot')
