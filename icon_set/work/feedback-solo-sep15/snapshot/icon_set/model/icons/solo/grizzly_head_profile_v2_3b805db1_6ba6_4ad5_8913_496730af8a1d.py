"""Connect the open jaw to the muzzle through a smooth throat return, closing the broken head contour without a detached line. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3b805db1-6ba6-4ad5-8913-496730af8a1d'
SOURCE_PATH = 'pictographic-primitives/animals/grizzly head side_3b805db1-6ba6-4ad5-8913-496730af8a1d.svg'
AUTHOR = 'gpt-6'

class GrizzlyHeadProfileVariant2(Solo48):
    icon_id = 'grizzly-head-profile-v2'
    variant_of = 'grizzly-head-profile'
    variant_label = 'Connect the open jaw to the muzzle through a smooth throat return, closing the broken head contour without a detached line.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('bear', 'grizzly', 'head', 'profile', 'roar', 'snout', 'wildlife', 'animal')

    def build(self):
        """Symbol plan: Connect the open jaw to the muzzle through a smooth throat return, closing the broken head contour without a detached line. Reference: Lucide dog: one connected head outline with a clearly projecting muzzle."""

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
        path('head', (6, 17), [('L', (10, 13)), ('L', (8, 9)), ('C', (12, 6), (8, 7), (10, 6)), ('C', (18, 11), (15, 6), (17, 8)), ('L', (23, 11)), ('A', (35, 17), 13, 13, True), ('L', (42, 22)), ('L', (42, 26)), ('C', (31, 30), (42, 30), (36, 30))])
        path('jaw', (31, 39), [('C', (15, 42), (23, 36), (20, 40))])
        path('neck', (6, 17), [('L', (6, 29)), ('C', (15, 42), (6, 36), (10, 40))])
        join('neck', 'head')
        join('neck', 'jaw')
        self.add_dot('eye', (28, 21))
        path('throat', (31, 30), [('C', (31, 39), (27, 30), (27, 37))])
        join('throat', 'head')
        join('throat', 'jaw')
