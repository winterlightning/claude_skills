"""Three bowling pins with the central pin lower and wider. No useful local Lucide bowling match; shared heads and smoothly bulging bellies preserve all three pins. Source overlaps separated for clearance.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '012843f4-1e2d-4bd4-8797-27a0f5f0fd46'
SOURCE_PATH = 'pictographic-primitives/symbol/three bowlings_012843f4-1e2d-4bd4-8797-27a0f5f0fd46.svg'
AUTHOR = 'gpt-6'

class BowlingPinsThree(Solo48):
    icon_id = 'bowling-pins-three'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('bowling', 'pins', 'skittles', 'sport', 'game', 'alley', 'strike', 'leisure')

    def oval(self, n, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(n + '-top', (cx - rx, cy), (cx + rx, cy), radius_x=rx, radius_y=ry)
        self.add_arc(n + '-bottom', (cx + rx, cy), (cx - rx, cy), radius_x=rx, radius_y=ry)
        self.add_contour(n, n + '-top', n + '-bottom', closed=True)

    def raw(self, n, points):
        for j, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(n + '-' + str(j), a, b)

    def path(self, n, points, closed=False):
        self.add_polyline(n, *points, closed=closed)

    def build(self):
        # Plan: Three repeated bowling pins: small circular heads, clear narrow necks and smooth broader bodies; preserve the row and circular head exception.

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
        for j,x in enumerate((8,24,40)):
         path(f'head-{j}',(x,8), [('A',(x,14),3,3,True),('A',(x,8),3,3,True)],True)
         path(f'body-{j}',(x,22), [('A',(x,40),4,9,True),('A',(x,22),4,9,True)],True)
         line(f'neck-{j}',(x,14),(x,22));join(f'neck-{j}',f'head-{j}');join(f'neck-{j}',f'body-{j}')
