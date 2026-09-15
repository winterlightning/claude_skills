"""Replace the oval paw pad with a broad triangular pad with rounded toes and a soft central top notch; space the four toe dots as mirrored pairs.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/cat_paw_print.py'
AUTHOR = 'gpt-6'

class CatPawPrint(Solo48):
    icon_id = 'cat-paw-print-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ('feline paw print',)
    keywords = ('cat', 'paw', 'pet', 'kitten', 'footprint', 'animal')
    variant_of = 'cat-paw-print'
    variant_label = 'Batch 01 centerline repair'

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

        def rounded(n, x0, y0, x1, y1, r):
            path(n, (x0 + r, y0), [('L', (x1 - r, y0)), ('A', (x1, y0 + r), r, r, True), ('L', (x1, y1 - r)), ('A', (x1 - r, y1), r, r, True), ('L', (x0 + r, y1)), ('A', (x0, y1 - r), r, r, True), ('L', (x0, y0 + r)), ('A', (x0 + r, y0), r, r, True)], True)
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        for x, y in [(6, 21), (16, 6), (32, 6), (42, 21)]:
            dot(f'toe-{x}', (x, y))
        path('pad', (24, 27), [('C', (17, 28), (21, 23), (19, 25)), ('C', (12, 36), (14, 31), (12, 32)), ('C', (24, 42), (12, 41), (19, 42)), ('C', (36, 36), (29, 42), (36, 41)), ('C', (31, 28), (36, 32), (34, 31)), ('C', (24, 27), (29, 25), (27, 23))], True)
