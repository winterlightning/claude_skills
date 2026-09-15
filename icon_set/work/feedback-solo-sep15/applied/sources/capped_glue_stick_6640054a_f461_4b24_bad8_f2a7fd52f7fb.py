"""Rebuild the glue stick as a narrow upright tube with a wider cap and a simple base seam. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6640054a-f461-4b24-bad8-f2a7fd52f7fb'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/paper glue_6640054a-f461-4b24-bad8-f2a7fd52f7fb.svg'
AUTHOR = 'gpt-6'

class CappedGlueStick(Solo48):
    icon_id = 'capped-glue-stick'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('glue', 'stick', 'adhesive', 'paper', 'craft', 'stationery', 'cap')

    def build(self):
        """Symbol plan: Rebuild the glue stick as a narrow upright tube with a wider cap and a simple base seam. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        poly('cap', (8, 4), (40, 4), (40, 14), (32, 14), (16, 14), (8, 14), closed=True)
        path('tube', (16, 14), [('L', (16, 36)), ('L', (16, 40)), ('A', (20, 44), 4, 4, False), ('L', (28, 44)), ('A', (32, 40), 4, 4, False), ('L', (32, 36)), ('L', (32, 14))])
        join('tube', 'cap')
        line('base', (16, 36), (32, 36))
        join('base', 'tube')
