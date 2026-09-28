"""Enlarge and round the whale forehead, then flow its back into the raised tail with matching tangents and a broad smooth belly. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2977768a-df8d-5260-854a-5df367e6906c'
SOURCE_PATH = 'pictographic-primitives/animals/whale body_2977768a-df8d-5260-854a-5df367e6906c.svg'
AUTHOR = 'gpt-6'

class WhaleWithSpout(Solo48):
    icon_id = 'whale-with-spout'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('whale', 'spout', 'water', 'sea', 'ocean', 'marine', 'tail', 'mammal')

    def build(self):
        """Symbol plan: Enlarge and round the whale forehead, then flow its back into the raised tail with matching tangents and a broad smooth belly. Reference: Lucide fish: one smooth body contour with a distinct tail."""

        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L':
                    self.add_line(name, here, end)
                elif k == 'A':
                    self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C':
                    self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)

        def circle(n, x, y, r):
            path(n, (x - r, y), [('A', (x + r, y), r, r, True), ('A', (x - r, y), r, r, True)], True)

        def box(n, l, t, r, b, rad=4):
            path(n, (l + rad, t), [('L', (r - rad, t)), ('A', (r, t + rad), rad, rad, True), ('L', (r, b - rad)), ('A', (r - rad, b), rad, rad, True), ('L', (l + rad, b)), ('A', (l, b - rad), rad, rad, True), ('L', (l, t + rad)), ('A', (l + rad, t), rad, rad, True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a, b: self.relate('connect', a, b)
        path('whale', (6, 30), [('C', (18, 18), (6, 23), (11, 18)), ('C', (32, 24), (25, 18), (32, 30)), ('L', (32, 16)), ('A', (34, 6), 12, 12, True), ('L', (40, 11)), ('L', (42, 6)), ('L', (42, 19)), ('C', (24, 42), (42, 33), (34, 42)), ('C', (6, 30), (14, 42), (6, 38))], True)
        self.add_dot('eye', (15, 30))
        path('spout', (8, 6), [('C', (16, 10), (12, 6), (14, 7)), ('C', (24, 6), (18, 7), (20, 6))])
