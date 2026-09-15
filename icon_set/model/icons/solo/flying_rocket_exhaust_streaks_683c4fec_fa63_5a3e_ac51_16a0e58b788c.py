"""A rounded rocket points diagonally upper-right with a circular porthole, two angular fins, and a short rear nozzle. Three separate diagonal exhaust streaks trail behind it toward the lower left.

SQUARE visible bounds (4,4)-(44,44); diagonal rocket, angular fins, porthole and three separated exhaust streaks. Porthole reduced to dot and rear nozzle seam omitted. Lucide rocket informed the pointed silhouette. Upper-right flight direction retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '683c4fec-fa63-5a3e-ac51-16a0e58b788c'
SOURCE_PATH = 'pictographic-primitives/science/rocket flying_683c4fec-fa63-5a3e-ac51-16a0e58b788c.svg'
AUTHOR = 'gpt-6'

class FlyingRocketExhaustStreaks(Solo48):
    icon_id = 'flying-rocket-exhaust-streaks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('rocket', 'flight', 'exhaust', 'porthole', 'fin', 'space')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        # Plan: Smooth nose curves share broad fin roots; retain the diagonal launch and two well-separated exhaust streaks, omitting the cramped porthole.

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
        path('hull',(16,26), [('C',(22,16),(16,22),(19,19)),('C',(42,6),(28,10),(36,6)),('C',(30,26),(42,14),(36,22)),('L',(24,32)),('L',(16,26))],True)
        poly('fin-left',(22,16),(12,14),(6,24),(16,26));join('fin-left','hull')
        poly('fin-right',(30,26),(40,30),(30,42),(24,32));join('fin-right','hull')
        line('exhaust-left',(6,36),(8,34));line('exhaust-right',(14,42),(16,40))
