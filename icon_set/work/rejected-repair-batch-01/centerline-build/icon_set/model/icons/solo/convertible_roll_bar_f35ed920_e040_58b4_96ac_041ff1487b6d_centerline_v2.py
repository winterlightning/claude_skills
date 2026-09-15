"""Give the convertible one coherent wheel-and-body silhouette with taller clearance above the wheels; match the slanted roll bar to the windscreen.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f35ed920-e040-58b4-96ac-041ff1487b6d'
SOURCE_PATH = 'pictographic-primitives/transportation/convertible_f35ed920-e040-58b4-96ac-041ff1487b6d.svg'
AUTHOR = 'gpt-6'

class ConvertibleRollBar(Solo48):
    icon_id = 'convertible-roll-bar-centerline-v2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('convertible', 'sports car', 'roadster', 'cabriolet', 'car', 'open top', 'vehicle', 'side view')
    variant_of = 'convertible-roll-bar'
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
        path('body', (6, 34), [('C', (4, 24), (4, 31), (4, 27)), ('A', (10, 18), 6, 6, True), ('L', (18, 18)), ('L', (32, 18)), ('L', (38, 18)), ('A', (44, 24), 6, 6, True), ('C', (42, 34), (44, 27), (44, 31)), ('A', (36, 40), 6, 6, True), ('A', (30, 34), 6, 6, True), ('L', (18, 34)), ('A', (12, 40), 6, 6, True), ('A', (6, 34), 6, 6, True)], True)
        for x in (12, 36):
            path(f'wheel-{x}', (x - 6, 34), [('A', (x, 28), 6, 6, True), ('A', (x + 6, 34), 6, 6, True)])
            join(f'wheel-{x}', 'body')
        line('windscreen', (25, 8), (32, 18))
        line('roll-bar', (14, 10), (18, 18))
        join('windscreen', 'body')
        join('roll-bar', 'body')
