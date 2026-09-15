"""Simplify the portrait to a dot head and shoulder curve; separate both oval locket halves at one clean hinge. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '57afb5e4-7b86-4ac6-adf1-571db810e527'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/locket_57afb5e4-7b86-4ac6-adf1-571db810e527.svg'
AUTHOR = 'gpt-6'

class OpenLocketWithPortrait(Solo48):
    icon_id = 'open-locket-with-portrait'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('open', 'locket', 'with', 'portrait')

    def build(self):
        """Symbol plan: Simplify the portrait to a dot head and shoulder curve; separate both oval locket halves at one clean hinge. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        oval('back', 11, 24, 7, 16)
        oval('front', 31, 24, 13, 16)
        join('back', 'front')
        dot('portrait-head', (31, 17))
        path('portrait-shoulders', (27, 28), [('A', (35, 28), 4, 2, True)])
