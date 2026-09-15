"""Make the cockatoo crest distinct and extend its hooked beak; round the crown and neck while keeping a single dot eye. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9442c76e-74c3-56b2-8dda-349c7fd38db5'
SOURCE_PATH = 'pictographic-primitives/animals/parrot_9442c76e-74c3-56b2-8dda-349c7fd38db5.svg'
AUTHOR = 'gpt-6'

class Cockatoo(Solo48):
    icon_id = 'cockatoo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('cockatoo',)

    def build(self):
        """Symbol plan: Make the cockatoo crest distinct and extend its hooked beak; round the crown and neck while keeping a single dot eye. Reference: Lucide bird: coherent head contour and dot eye; preserve the cockatoo crest and hook."""

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
        path('head', (8, 44), [('L', (8, 4)), ('C', (28, 12), (22, 4), (26, 8)), ('A', (34, 24), 8, 12, True), ('C', (40, 28), (40, 24), (40, 26)), ('L', (40, 36)), ('C', (32, 34), (36, 36), (34, 35)), ('A', (22, 44), 10, 10, True)])
        dot('eye', (23, 23))
