"""Smooth the brain fissure into two consistent S-bends with tangent alignment at their shared midpoint, eliminating the alternating kinks.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2039321a-3302-40c2-86c4-0a7e4c5ef8fb'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/brain 1_2039321a-3302-40c2-86c4-0a7e4c5ef8fb.svg'
AUTHOR = 'gpt-6'

class Brain1(Solo48):
    icon_id = 'brain-1-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('brain', 'artificial-intelligence', 'solo-ai-next50')

    def build(self):

        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f'{name}-{index}'
                kind, end, *args = command
                if kind == 'L':
                    self.add_line(ident, here, end)
                elif kind == 'A':
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == 'C':
                    c1, c2 = args
                    self.add_bezier(ident, here, (c1, c2, end))
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)

        def circle(name, cx, cy, r):
            path(name, (cx - r, cy), [('A', (cx + r, cy), r, r, True), ('A', (cx - r, cy), r, r, True)], True)

        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0 + r, y0), [('L', (x1 - r, y0)), ('A', (x1, y0 + r), r, r, True), ('L', (x1, y1 - r)), ('A', (x1 - r, y1), r, r, True), ('L', (x0 + r, y1)), ('A', (x0, y1 - r), r, r, True), ('L', (x0, y0 + r)), ('A', (x0 + r, y0), r, r, True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a, b: self.relate('connect', a, b)
        left = [('C', (14, 6), (22, 6), (18, 6)), ('C', (8, 16), (8, 6), (8, 12)), ('C', (6, 24), (8, 18), (6, 20)), ('C', (10, 32), (6, 28), (6, 32)), ('C', (16, 42), (8, 38), (10, 42)), ('C', (24, 38), (21, 42), (23, 40))]
        segments = []
        start = (24, 8)
        for kind, end, c1, c2 in left:
            segments.append((start, end, c1, c2))
            start = end
        mirror = lambda p: (48 - p[0], p[1])
        commands = left + [('C', mirror(a), mirror(c2), mirror(c1)) for a, b, c1, c2 in reversed(segments)]
        path('brain', (24, 8), commands, True)
        path('fissure', (24, 8), [('C', (24, 24), (18, 12), (30, 20)), ('C', (24, 38), (18, 28), (30, 34))])
        join('fissure', 'brain')
    variant_of = 'brain-1'
    variant_label = 'Batch 01 centerline repair'
