"""Simplify the canyon to two stepped cliffs, distant mountain slopes, and one curved river. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '021a0b5f-bd2d-4f08-b36b-7afe509eb0fc'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/grand canyon usa 1_021a0b5f-bd2d-4f08-b36b-7afe509eb0fc.svg'
AUTHOR = 'gpt-6'

class GrandCanyonWithRiver(Solo48):
    icon_id = 'grand-canyon-with-river'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('grand canyon', 'canyon', 'usa', 'arizona', 'river', 'cliff', 'landscape', 'nature', 'landmark')

    def build(self):
        """Symbol plan: Simplify the canyon to two stepped cliffs, distant mountain slopes, and one curved river. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        poly('left-cliff', (6, 42), (6, 18), (16, 18), (16, 26))
        poly('right-cliff', (42, 42), (42, 18), (34, 18), (34, 26))
        poly('mountain', (6, 10), (16, 6), (25, 12), (34, 6), (42, 10))
        path('river', (25, 23), [('C', (23, 33), (25, 28), (23, 30)), ('C', (29, 42), (23, 37), (27, 40))])
