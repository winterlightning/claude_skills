"""Reduce the flock from five birds to three larger paired curves; use one repeated wing definition and generous air between the birds. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b7c1e75f-5c89-447a-8fb6-cc3765f450b1'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird flock_b7c1e75f-5c89-447a-8fb6-cc3765f450b1.svg'
AUTHOR = 'gpt-6'

class BirdFlock(Solo48):
    icon_id = 'bird-flock'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('birds', 'flock', 'flying', 'group', 'five', 'migration', 'sky', 'flight')

    def build(self):
        """Symbol plan: Reduce the flock from five birds to three larger paired curves; use one repeated wing definition and generous air between the birds. Reference: Lucide bird: minimal coherent wing silhouettes."""

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
        for n, cx, y in [('left', 12, 6), ('right', 36, 6), ('low', 24, 34)]:
            path(n, (cx - 6, y), [('C', (cx, y + 8), (cx - 4, y), (cx, y + 3)), ('C', (cx + 6, y), (cx, y + 3), (cx + 4, y))])
