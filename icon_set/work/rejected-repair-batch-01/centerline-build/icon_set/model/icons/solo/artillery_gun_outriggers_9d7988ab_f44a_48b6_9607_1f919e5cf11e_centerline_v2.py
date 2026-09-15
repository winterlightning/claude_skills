"""Rebuild the raised gun above its wheel with a clean pivot and spread outriggers; remove the crowded diamond around the wheel top.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9d7988ab-f44a-48b6-9607-1f919e5cf11e'
SOURCE_PATH = 'pictographic-primitives/war/tank machine gun_9d7988ab-f44a-48b6-9607-1f919e5cf11e.svg'
AUTHOR = 'gpt-6'

class ArtilleryGunOutriggers(Solo48):
    icon_id = 'artillery-gun-outriggers-centerline-v2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('artillery', 'gun', 'barrel', 'wheel', 'outrigger', 'military')
    variant_of = 'artillery-gun-outriggers'
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
        circle('wheel', 20, 30, 10)
        poly('barrel', (12, 12), (24, 12), (32, 8), (40, 8))
        line('mount', (20, 12), (20, 20))
        join('mount', 'barrel')
        join('mount', 'wheel')
        poly('left-foot', (12, 36), (8, 40), (4, 40))
        poly('right-foot', (28, 36), (36, 40), (44, 40))
        join('left-foot', 'wheel')
        join('right-foot', 'wheel')
