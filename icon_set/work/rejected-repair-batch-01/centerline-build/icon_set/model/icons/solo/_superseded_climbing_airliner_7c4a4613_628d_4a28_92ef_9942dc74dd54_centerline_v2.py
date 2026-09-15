"""Rebuild the climbing airliner as one continuous outline with a rounded nose and broad swept wings; remove overlapping strokes and the pinched central passages.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7c4a4613-628d-4a28-92ef-9942dc74dd54'
SOURCE_PATH = 'pictographic-primitives/travel/plane 1_7c4a4613-628d-4a28-92ef-9942dc74dd54.svg'
AUTHOR = 'gpt-6'

class ClimbingAirliner(Solo48):
    icon_id = 'climbing-airliner-centerline-v2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/travel'
    aliases = ()
    keywords = ('airplane', 'plane', 'takeoff', 'flight', 'climbing', 'aviation', 'departure', 'travel')
    variant_of = 'climbing-airliner'
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
        path('airliner', (38, 8), [('C', (44, 12), (42, 8), (44, 8)), ('C', (38, 20), (44, 16), (40, 18)), ('L', (30, 40)), ('L', (20, 40)), ('L', (24, 27)), ('L', (14, 34)), ('L', (4, 26)), ('L', (8, 18)), ('L', (15, 23)), ('L', (22, 18)), ('L', (12, 8)), ('L', (24, 8)), ('L', (32, 13)), ('L', (38, 8))], True)
