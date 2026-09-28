"""A rounded rocket points diagonally upper-right with two angular fins. Two clear diagonal exhaust streaks trail toward the lower left.

SQUARE visible bounds (4,4)-(44,44). The porthole and rear nozzle seam were omitted because their spacing is too tight at 48 pixels. Lucide rocket informed the pointed silhouette.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '683c4fec-fa63-5a3e-ac51-16a0e58b788c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__flying-rocket-exhaust-streaks/20260927T034714Z-thuan-mac-1/reference/rocket flying_683c4fec-fa63-5a3e-ac51-16a0e58b788c.svg'
AUTHOR = "gpt-6"

class FlyingRocketExhaustStreaks(Solo48):
    icon_id = 'flying-rocket-exhaust-streaks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    categories = ("science", "primitives")
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
        # Two visible diagonal streaks replace the rejected dot-like exhaust.
        line('exhaust-left',(6,38),(10,34))
        line('exhaust-right',(14,42),(18,38))
