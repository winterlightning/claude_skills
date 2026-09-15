"""Remove the tiny doubled notches in the clover lobes and make each side lobe one broad smooth curve; mirror the correction across the stem axis.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '940923da-19e4-4b49-811d-53f2118f022d'
SOURCE_PATH = 'pictographic-primitives/entertainment/casino clover_940923da-19e4-4b49-811d-53f2118f022d.svg'
AUTHOR = 'gpt-6'

class CasinoClover(Solo48):
    icon_id = 'casino-clover-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('solo-ai-clover-curve', 'solo-ai-next100', 'casino-clover')

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
        left = [('C', (11, 36), (20, 29), (15, 36)), ('C', (6, 25), (8, 36), (6, 30)), ('C', (12, 16), (6, 20), (8, 16)), ('C', (16, 18), (14, 16), (17, 19)), ('C', (14, 12), (15, 17), (14, 15)), ('C', (19, 6), (14, 8), (16, 6)), ('C', (24, 9), (22, 6), (22, 9))]
        commands = list(left)
        starts = [(24, 29)] + [c[1] for c in left[:-1]]
        mirror = lambda p: (48 - p[0], p[1])
        for start, (kind, end, c1, c2) in reversed(list(zip(starts, left))):
            commands.append(('C', mirror(start), mirror(c2), mirror(c1)))
        path('leaves', (24, 29), commands, True)
        path('stem', (24, 29), [('C', (30, 42), (21, 37), (24, 42))])
        join('stem', 'leaves')
    variant_of = 'casino-clover'
    variant_label = 'Batch 01 centerline repair'
