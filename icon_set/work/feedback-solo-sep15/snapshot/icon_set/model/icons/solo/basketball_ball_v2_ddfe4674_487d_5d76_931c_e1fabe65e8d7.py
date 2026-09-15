"""Replace the nearly straight side seams with visibly curved, mirrored arcs; retain equal clear spaces around the central cross. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ddfe4674-487d-5d76-931c-e1fabe65e8d7'
SOURCE_PATH = 'pictographic-primitives/sports/basketball ball_ddfe4674-487d-5d76-931c-e1fabe65e8d7.svg'
AUTHOR = 'gpt-6'

class BasketballBallVariant2(Solo48):
    icon_id = 'basketball-ball-v2'
    variant_of = 'basketball-ball'
    variant_label = 'Replace the nearly straight side seams with visibly curved, mirrored arcs; retain equal clear spaces around the central cross.'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('basketball', 'ball', 'sports', 'solo-ai-first50')

    def build(self):
        """Symbol plan: Replace the nearly straight side seams with visibly curved, mirrored arcs; retain equal clear spaces around the central cross. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('outline', (24, 4), [('A', (36, 8), 20, 20, True), ('A', (44, 24), 20, 20, True), ('A', (36, 40), 20, 20, True), ('A', (24, 44), 20, 20, True), ('A', (12, 40), 20, 20, True), ('A', (4, 24), 20, 20, True), ('A', (12, 8), 20, 20, True), ('A', (24, 4), 20, 20, True)], True)
        poly('vertical', (24, 4), (24, 24), (24, 44))
        poly('horizontal', (4, 24), (14, 24), (24, 24), (34, 24), (44, 24))
        for side in (-1, 1):
            x = lambda d: 24 + side * d
            path(f'curve-{side}', (x(12), 8), [('C', (x(10), 24), (x(8), 12), (x(10), 18)), ('C', (x(12), 40), (x(10), 30), (x(8), 36))])
            join(f'curve-{side}', 'horizontal')
            join(f'curve-{side}', 'outline')
        join('vertical', 'horizontal')
        join('vertical', 'outline')
        join('horizontal', 'outline')
