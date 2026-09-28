"""Widen each pin neck to eight centerline units and stagger the center pin below the rear pair. Remove its crowded collar line while keeping the rear pair’s collars. Applied to the original icon identity."""
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
        """Symbol plan: Widen each pin neck to eight centerline units, stagger the larger center pin below the rear pair, and use level collars with clear enclosed gaps. Reference: inspected current parent; no useful exact Lucide match selected."""

        def path(n, start, commands, closed=False):
            here = start
            members = []
            for i, c in enumerate(commands):
                kind, end, *args = c
                name = f'{n}-{i}'
                if kind == 'L':
                    self.add_line(name, here, end)
                elif kind == 'A':
                    self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C':
                    self.add_bezier(name, here, (args[0], args[1], end))
                members.append(name)
                here = end
            self.add_contour(n, *members, closed=closed)

        def oval(n, x, y, rx, ry):
            path(n, (x - rx, y), [('A', (x + rx, y), rx, ry, True), ('A', (x - rx, y), rx, ry, True)], True)

        def box(n, l, t, r, b, rad=4):
            path(n, (l + rad, t), [('L', (r - rad, t)), ('A', (r, t + rad), rad, rad, True), ('L', (r, b - rad)), ('A', (r - rad, b), rad, rad, True), ('L', (l + rad, b)), ('A', (l, b - rad), rad, rad, True), ('L', (l, t + rad)), ('A', (l + rad, t), rad, rad, True)], True)
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        for n, cx in [('left', 8), ('right', 40)]:
            path(n, (cx - 4, 12), [('A', (cx + 4, 12), 4, 4, True), ('L', (cx + 4, 18)), ('L', (cx + 4, 24)), ('A', (cx - 4, 24), 4, 4, True), ('L', (cx - 4, 18)), ('L', (cx - 4, 12))], True)
            line(n + '-collar', (cx - 4, 18), (cx + 4, 18))
            join(n, n + '-collar')
        path('center', (20, 26), [('A', (28, 26), 4, 4, True), ('L', (28, 30)), ('C', (29, 36), (28, 32), (29, 34)), ('C', (24, 40), (29, 40), (27, 40)), ('C', (19, 36), (21, 40), (19, 40)), ('C', (20, 30), (19, 34), (20, 32)), ('L', (20, 26))], True)
