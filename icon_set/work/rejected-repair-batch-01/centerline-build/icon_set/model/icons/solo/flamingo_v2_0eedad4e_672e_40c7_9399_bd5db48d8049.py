"""Curve the flamingo neck and turn down the beak; preserve the bent standing pose.
Plan: oval body, continuous curved neck and beak, one vertical and one bent leg.
VRECT_L centerline extremes (8,4)-(40,44).
Lucide: bird; geometric contour construction adapted to SOLO48.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0eedad4e-672e-40c7-9399-bd5db48d8049'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird flamingo_0eedad4e-672e-40c7-9399-bd5db48d8049.svg'
AUTHOR = 'gpt-6'

class FlamingoVariant2(Solo48):
    icon_id = 'flamingo-v2'
    variant_of = 'flamingo'
    variant_label = 'Batch 01: visual refinement'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('flamingo', 'standing', 'one leg', 'bird', 'pink', 'tropical', 'wading', 'beak')

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
        path('body', (8, 29), [('A', (19, 24), 11, 5, True), ('A', (30, 29), 11, 5, True), ('A', (19, 34), 11, 5, True), ('A', (8, 29), 11, 5, True)], True)
        path('neck', (30, 29), [('L', (30, 16)), ('C', (34, 4), (30, 10), (28, 4)), ('A', (40, 10), 6, 6, True), ('L', (40, 13))])
        join('body', 'neck')
        line('leg', (19, 34), (19, 44))
        poly('bent-leg', (19, 34), (8, 42))
        join('body', 'leg')
        join('body', 'bent-leg')
