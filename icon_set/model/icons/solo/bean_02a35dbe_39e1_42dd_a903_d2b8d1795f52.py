"""Widen the kidney bean and use four coherent rounded arcs. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '02a35dbe-39e1-42dd-a903-d2b8d1795f52'
SOURCE_PATH = 'pictographic-primitives/symbol/peanut_02a35dbe-39e1-42dd-a903-d2b8d1795f52.svg'
AUTHOR = 'gpt-6'

class Bean(Solo48):
    icon_id = 'bean'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('bean', 'peanut', 'legume', 'seed', 'food', 'vegan', 'nut', 'coffee')

    def build(self):
        """Symbol plan: Widen the kidney bean and use four coherent rounded arcs. Reference: Lucide bean: one notched outline and a curved inner seam."""

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
        path('bean', (24, 16), [('A', (44, 16), 10, 8, True), ('A', (12, 40), 32, 24, True), ('A', (12, 24), 8, 8, True), ('A', (24, 16), 12, 8, False)], True)
        path('seam', (24, 29), [('C', (34, 18), (27, 29), (32, 24))])
