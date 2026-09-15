"""Reduce the spillway to two falling streams above a single smooth water stroke. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6e9836ef-b3e3-41e7-819a-f79c721f25ec'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/renewable energy water dam_6e9836ef-b3e3-41e7-819a-f79c721f25ec.svg'
AUTHOR = 'gpt-6'

class DamSpillwayWater(Solo48):
    icon_id = 'dam-spillway-water'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('dam', 'spillway', 'water', 'hydro', 'energy', 'flow', 'waterfall', 'renewable', 'power')

    def build(self):
        """Symbol plan: Reduce the spillway to two falling streams above a single smooth water stroke. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        for i, x in enumerate((10, 32)):
            path(f'stream-{i}', (x, 8), [('L', (x, 23)), ('A', (x + 6, 29), 6, 6, False)])
        path('water', (4, 38), [('C', (24, 40), (10, 38), (18, 40)), ('C', (44, 38), (30, 40), (38, 38))])
