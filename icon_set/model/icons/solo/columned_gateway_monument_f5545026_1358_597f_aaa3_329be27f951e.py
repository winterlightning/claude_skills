"""Rebalance the monument vertically: enlarge the cross-to-attic gap and use matching ten-unit openings below it. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f5545026-1358-597f-aaa3-329be27f951e'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/brandenburg gate berlin_f5545026-1358-597f-aaa3-329be27f951e.svg'
AUTHOR = 'gpt-6'

class Landmark(Solo48):
    icon_id = 'columned-gateway-monument'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    aliases = ()
    keywords = ('gate', 'gateway', 'monument', 'brandenburg', 'berlin', 'landmark', 'arch', 'columns', 'architecture')

    def build(self):
        """Symbol plan: Rebalance the monument vertically: enlarge the cross-to-attic gap and use matching ten-unit openings below it. Reference: Lucide landmark: shared architectural axis and even bays."""

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
        poly('gateway', (8, 26), (16, 26), (32, 26), (40, 26), (40, 44), (32, 44), (32, 34), (16, 34), (16, 44), (8, 44), closed=True)
        poly('attic', (16, 26), (16, 16), (24, 16), (32, 16), (32, 26))
        join('attic', 'gateway')
        poly('mast', (24, 4), (24, 6), (24, 16))
        poly('cross', (20, 6), (24, 6), (28, 6))
        join('mast', 'cross')
        join('mast', 'attic')
