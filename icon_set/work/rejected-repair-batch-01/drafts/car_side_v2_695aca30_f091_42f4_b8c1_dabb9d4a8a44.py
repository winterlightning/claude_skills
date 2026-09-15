"""Replace the front-facing windshield with a recognizable asymmetric side profile.
Plan: side-facing roof and hood, two equal wheels sharing the body baseline.
HRECT_L centerline extremes (4,8)-(44,40).
Lucide: car; geometric contour construction adapted to SOLO48.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '695aca30-f091-42f4-b8c1-dabb9d4a8a44'
SOURCE_PATH = 'pictographic-primitives/symbol/car side_695aca30-f091-42f4-b8c1-dabb9d4a8a44.svg'
AUTHOR = 'gpt-6'

class CarSideVariant2(Solo48):
    icon_id = 'car-side-v2'
    variant_of = 'car-side'
    variant_label = 'Batch 01: visual refinement'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('solo-ai-cars-refine', 'solo-ai-next100', 'car-side')

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
        path('body', (12, 28), [('L', (4, 28)), ('L', (4, 20)), ('L', (12, 8)), ('L', (24, 8)), ('L', (32, 20)), ('L', (40, 20)), ('A', (44, 24), 4, 4, True), ('L', (44, 28)), ('L', (36, 28))])
        circle('rear-wheel', 12, 34, 6)
        circle('front-wheel', 36, 34, 6)
        line('sill', (18, 34), (30, 34))
        join('sill', 'rear-wheel')
        join('sill', 'front-wheel')
        join('body', 'rear-wheel')
        join('body', 'front-wheel')
        line('window-base', (4, 20), (32, 20))
        join('window-base', 'body')
