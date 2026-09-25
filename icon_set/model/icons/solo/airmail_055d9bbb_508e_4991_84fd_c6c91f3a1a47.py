"""Round all four envelope corners with equal-radius arcs; retain the folded flap. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '055d9bbb-508e-4991-84fd-c6c91f3a1a47'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/airmail_055d9bbb-508e-4991-84fd-c6c91f3a1a47.svg'
AUTHOR = 'gpt-6'

class Airmail(Solo48):
    icon_id = 'airmail'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('airmail', '_uncategorized_01')

    def build(self):
        """Symbol plan: Round all four envelope corners with equal-radius arcs; retain the folded flap. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('envelope', (8, 8), [('L', (40, 8)), ('A', (44, 12), 4, 4, True), ('L', (44, 36)), ('A', (40, 40), 4, 4, True), ('L', (8, 40)), ('A', (4, 36), 4, 4, True), ('L', (4, 12)), ('A', (8, 8), 4, 4, True)], True)
        path('flap', (4, 12), [('L', (21, 26)), ('A', (27, 26), 5, 5, False), ('L', (44, 12))])
        join('envelope', 'flap')
