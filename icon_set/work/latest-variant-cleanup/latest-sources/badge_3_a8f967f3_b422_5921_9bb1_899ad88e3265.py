"""Widen the central shield symmetrically while retaining its side wings. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a8f967f3-b422-5921-9bb1-899ad88e3265'
SOURCE_PATH = 'pictographic-primitives/protection/badge 3_a8f967f3-b422-5921-9bb1-899ad88e3265.svg'
AUTHOR = 'gpt-6'

class Badge3(Solo48):
    icon_id = 'badge-3'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('badge', 'protection')

    def build(self):
        """Symbol plan: Widen the central shield symmetrically while retaining its side wings. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('shield', (24, 8), [('L', (36, 14)), ('L', (36, 20)), ('L', (36, 26)), ('A', (24, 40), 12, 14, True), ('A', (12, 26), 12, 14, True), ('L', (12, 20)), ('L', (12, 14)), ('L', (24, 8))], True)
        path('wing-left', (12, 20), [('L', (4, 20)), ('A', (12, 28), 8, 8, False)])
        path('wing-right', (36, 20), [('L', (44, 20)), ('A', (36, 28), 8, 8, True)])
        join('shield', 'wing-left')
        join('shield', 'wing-right')
