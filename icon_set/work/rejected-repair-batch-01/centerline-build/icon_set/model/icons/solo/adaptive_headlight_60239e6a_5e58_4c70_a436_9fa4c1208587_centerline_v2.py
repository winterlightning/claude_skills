"""Recenter the lamp on y=24 with two coherent half-ellipse quarters; align the adaptive stroke to the tangent and give all three light beams equal lengths.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '60239e6a-5e58-4c70-a436-9fa4c1208587'
SOURCE_PATH = 'pictographic-primitives/transportation/adaptive light 1_60239e6a-5e58-4c70-a436-9fa4c1208587.svg'
AUTHOR = 'gpt-6'

class AdaptiveHeadlight(Solo48):
    icon_id = 'adaptive-headlight-centerline-v2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('headlight', 'adaptive', 'lamp', 'beam', 'car', 'dashboard', 'lighting', 'indicator')
    variant_of = 'adaptive-headlight'
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
        path('lamp', (32, 8), [('A', (44, 24), 12, 16, True), ('A', (32, 40), 12, 16, True), ('L', (32, 8))], True)
        for i, y in enumerate((12, 24, 36)):
            line(f'beam-{i}', (4, y + 4), (20, y - 4))
        line('adaptive', (44, 24), (44, 8))
        join('adaptive', 'lamp')
