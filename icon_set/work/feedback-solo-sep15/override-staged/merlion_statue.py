"""Give the Merlion a rounded mane and projecting muzzle, a smoother fish body, and a curved spout that visibly leaves its mouth. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4d6b18c3-9c28-4f4a-8e22-8679e1c298f6'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/merlion statue_4d6b18c3-9c28-4f4a-8e22-8679e1c298f6.svg'
AUTHOR = 'gpt-6'

class MerlionStatue(Solo48):
    icon_id = 'merlion-statue'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('merlion', 'singapore', 'statue', 'lion', 'fish', 'landmark', 'monument', 'mascot')

    def build(self):
        """Symbol plan: Give the Merlion a rounded mane and projecting muzzle, a smoother fish body, and a curved spout that visibly leaves its mouth. Reference: Lucide cat and fish: rounded head mass and a coherent aquatic body; asymmetric statue profile."""

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
        path('lion-fish', (14, 16), [('L', (20, 16)), ('L', (20, 10)), ('A', (28, 6), 8, 4, True), ('C', (42, 20), (37, 6), (42, 12)), ('L', (42, 28)), ('C', (28, 42), (42, 36), (36, 42)), ('L', (14, 42)), ('L', (24, 32)), ('L', (24, 26)), ('L', (14, 26)), ('A', (14, 16), 5, 5, True)], True)
        dot('eye', (30, 17))
        path('water', (9, 21), [('C', (6, 36), (6, 25), (6, 31))])
        join('water', 'lion-fish')
