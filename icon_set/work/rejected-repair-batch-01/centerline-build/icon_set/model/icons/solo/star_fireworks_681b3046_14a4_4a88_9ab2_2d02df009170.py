"""Three five-point stars burst above a straight central trail and mirrored curved side trails.

Construction references: Lucide shirt and star as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '681b3046-14a4-4a88-9ab2-2d02df009170'
SOURCE_PATH = 'pictographic-primitives/romance/wedding fireworks_681b3046-14a4-4a88-9ab2-2d02df009170.svg'
AUTHOR = 'gpt-6'


class StarFireworks(Solo48):
    icon_id = 'star-fireworks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/romance"
    aliases = ()
    keywords = ('fireworks', 'star', 'burst', 'celebration', 'wedding', 'festival')

    def build(self):
        # Plan: Three symmetric open starbursts replace tiny filled star outlines; genuine shared ray centres own the trails.

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
        from itertools import combinations
        for j,(x,y) in enumerate(((24,14),(10,30),(38,30))):
         centre=(x,y);ends=[(x-6,y-4),(x+6,y-4),(x-6,y+4),(x+6,y+4),(x,y-6)]
         names=[]
         for k,end in enumerate(ends):
          n=f'burst-{j}-{k}';line(n,centre,end);names.append(n)
         trail=f'trail-{j}';line(trail,centre,(x,40));names.append(trail)
         for a,b in combinations(names,2):join(a,b)
