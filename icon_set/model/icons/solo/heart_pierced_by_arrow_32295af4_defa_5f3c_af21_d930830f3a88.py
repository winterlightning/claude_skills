"""A Cupid arrow pierces a heart diagonally; one fletching chevron replaces tiny feathers.

Construction references: Lucide heart, hand-heart, sprout and balloon as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '32295af4-defa-5f3c-af21-d930830f3a88'
SOURCE_PATH = 'pictographic-primitives/romance/love heart arrow_32295af4-defa-5f3c-af21-d930830f3a88.svg'
AUTHOR = 'gpt-6'

class HeartPiercedByArrow(Solo48):
    icon_id = 'heart-pierced-by-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/romance'
    aliases = ()
    keywords = ('heart', 'arrow', 'cupid', 'love', 'romance', 'pierced')

    def build(self):
        # Plan: Move the complete heart away from the arrowhead; show the shaft entering and leaving its outline, with the middle naturally hidden behind the heart.

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
        path('heart',(20,18), [('A',(8,18),6,6,False),('A',(10,22),5,5,False),('L',(18,30)),('L',(24,36)),('L',(28,30)),('L',(30,22)),('A',(32,18),5,5,False),('A',(20,18),6,6,False)],True)
        line('arrow-front',(32,18),(42,6));line('arrowhead',(42,6),(42,16));join('arrow-front','heart');join('arrow-front','arrowhead')
        line('arrow-back',(6,42),(18,30));poly('fletching',(6,34),(6,42),(14,42));join('arrow-back','heart');join('arrow-back','fletching')
