"""Replace tall pointed ears with smaller rounded Bengal-style ear tips. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7702e4e2-e41d-5abb-87f2-54692461fd5d'
SOURCE_PATH = 'pictographic-primitives/pets/bengal_7702e4e2-e41d-5abb-87f2-54692461fd5d.svg'
AUTHOR = 'gpt-6'

class BengalCatFace(Solo48):
    icon_id = 'bengal-cat-face'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/pets'
    aliases = ()
    keywords = ('cat', 'bengal', 'face', 'breed', 'feline', 'pet', 'ears')

    def build(self):
        """Symbol plan: Replace tall pointed ears with smaller rounded Bengal-style ear tips. Reference: Lucide cat: mirrored ears and rounded jaw."""

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
        path('head', (6, 24), [('L', (6, 10)), ('C', (12, 6), (6, 6), (9, 6)), ('L', (18, 14)), ('L', (30, 14)), ('L', (36, 6)), ('C', (42, 10), (39, 6), (42, 6)), ('L', (42, 24)), ('A', (24, 42), 18, 18, True), ('A', (6, 24), 18, 18, True)], True)
        poly('nose', (21, 29), (24, 32), (27, 29))
