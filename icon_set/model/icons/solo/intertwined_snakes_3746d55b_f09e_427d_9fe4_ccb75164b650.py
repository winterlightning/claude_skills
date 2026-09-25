"""Give the intertwined snakes distinct head tips and smoother, balanced opposing curves.
Plan: two opposed S curves crossing at a real shared center, tapered head ends.
SQUARE centerline extremes (6,6)-(42,42).
Lucide: No useful subject-specific match; supplied original guides the silhouette.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3746d55b-f09e-427d-9fe4-ccb75164b650'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/snakes_3746d55b-f09e-427d-9fe4-ccb75164b650.svg'
AUTHOR = 'gpt-6'

class IntertwinedSnakes(Solo48):
    icon_id = 'intertwined-snakes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('snake', 'serpent', 'intertwined', 'caduceus', 'mythology', 'coil', 'reptile', 'symbol')

    def build(self):

        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, (kind, end, *args) in enumerate(commands):
                name = f'{n}-{j}'
                if kind == 'L':
                    self.add_line(name, here, end)
                elif kind == 'A':
                    self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C':
                    self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)

        def circle(n, x, y, r):
            path(n, (x - r, y), [('A', (x, y - r), r, r, True), ('A', (x + r, y), r, r, True), ('A', (x, y + r), r, r, True), ('A', (x - r, y), r, r, True)], True)
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        path('snake-a', (22, 12), [('L', (18, 6)), ('L', (16, 6)), ('A', (6, 14), 10, 8, False), ('C', (24, 24), (6, 20), (16, 22)), ('C', (42, 34), (32, 26), (42, 28)), ('A', (32, 42), 10, 8, True)])
        path('snake-b', (32, 6), [('A', (42, 14), 10, 8, True), ('C', (24, 24), (42, 20), (32, 22)), ('C', (6, 34), (16, 26), (6, 28)), ('A', (16, 42), 10, 8, False), ('L', (18, 42)), ('L', (22, 36))])
        join('snake-a', 'snake-b')
