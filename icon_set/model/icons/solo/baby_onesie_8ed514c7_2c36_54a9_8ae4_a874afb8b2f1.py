"""Replace both tapered sleeves with mirrored horizontal rectangles. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8ed514c7-2c36-54a9-8ae4-a874afb8b2f1'
SOURCE_PATH = 'pictographic-primitives/babies/baby care clothes_8ed514c7-2c36-54a9-8ae4-a874afb8b2f1.svg'
AUTHOR = 'gpt-6'

class BabyOnesie(Solo48):
    icon_id = 'baby-onesie'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    aliases = ()
    keywords = ('onesie', 'bodysuit', 'baby', 'clothes', 'romper', 'garment', 'infant', 'laundry')

    def build(self):
        """Symbol plan: Replace both tapered sleeves with mirrored horizontal rectangles. Reference: Lucide shirt: mirrored rectangular sleeves."""

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
        path('suit', (16, 6), [('L', (6, 6)), ('L', (6, 18)), ('L', (14, 18)), ('L', (14, 30)), ('A', (20, 36), 6, 6, True), ('L', (20, 42)), ('L', (28, 42)), ('L', (28, 36)), ('A', (34, 30), 6, 6, True), ('L', (34, 18)), ('L', (42, 18)), ('L', (42, 6)), ('L', (32, 6)), ('A', (16, 6), 8, 8, True)], True)
