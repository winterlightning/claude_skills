"""Use concentric faucet bends about (24,20), replacing the offset inner bend and short kink. Align the two water strokes beneath the outlet.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c6244934-fcab-4b97-a0d0-7bb5ba491549'
SOURCE_PATH = 'pictographic-primitives/wayfinding/water fountain jet_c6244934-fcab-4b97-a0d0-7bb5ba491549.svg'
AUTHOR = 'gpt-6'

class ArchedTapSprayingWater(Solo48):
    icon_id = 'arched-tap-spraying-water-centerline-v2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('tap', 'faucet', 'spray', 'water', 'plumbing', 'lever')
    variant_of = 'arched-tap-spraying-water'
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
        path('tap', (8, 44), [('L', (8, 20)), ('A', (24, 4), 16, 16, True), ('A', (40, 20), 16, 16, True), ('L', (30, 20)), ('A', (24, 14), 6, 6, False), ('A', (18, 20), 6, 6, False), ('L', (18, 44)), ('L', (8, 44))], True)
        for x in (30, 40):
            line(f'water-{x}', (x, 30), (x, 36))
