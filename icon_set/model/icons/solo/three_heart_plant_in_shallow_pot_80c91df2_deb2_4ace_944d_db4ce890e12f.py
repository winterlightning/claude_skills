"""Three heart blooms rise from a shallow planter. Small feet and double rim are omitted.

Construction references: Lucide heart, hand-heart, sprout and balloon as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '80c91df2-deb2-4ace-944d-db4ce890e12f'
SOURCE_PATH = 'pictographic-primitives/romance/lgbt love plant_80c91df2-deb2-4ace-944d-db4ce890e12f.svg'
AUTHOR = 'gpt-6'

class ThreeHeartPlantInShallowPot(Solo48):
    icon_id = 'three-heart-plant-in-shallow-pot'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    categories = ('primitives', 'romance')
    aliases = ()
    keywords = ('heart', 'plant', 'pot', 'flower', 'romance', 'growth')

    def build(self):
        # Plan: A rounded three-leaf cluster fits the circle envelope, reaching radius twenty at the bowl base. Smaller smooth leaves, separated stems and a broad bowl preserve all three hearts.

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
        line('stem',(24,16),(24,35));line('branch-left',(10,28),(19,35));line('branch-right',(38,28),(29,35))
        path('pot',(19,35), [('L',(24,35)),('L',(29,35)),('A',(33,39),4,4,True),('A',(29,43),4,4,True),('L',(19,43)),('A',(15,39),4,4,True),('A',(19,35),4,4,True)],True)
        for leaf,stem in [('centre','stem'),('left','branch-left'),('right','branch-right')]:join(leaf,stem);join(stem,'pot')
