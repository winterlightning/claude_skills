"""Rebuild the mirrored wings and join the abdomen to exact shared nodes on their inner edges, eliminating the offset body endpoints. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0cfadabd-8efa-4aaa-ba5a-9f400bfecce1'
SOURCE_PATH = 'pictographic-primitives/animals/fantasy pit locust_0cfadabd-8efa-4aaa-ba5a-9f400bfecce1.svg'
AUTHOR = 'gpt-6'

class WingedInsect(Solo48):
    icon_id = 'winged-insect'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('winged', 'insect')

    def build(self):
        """Symbol plan: Rebuild the mirrored wings and join the abdomen to exact shared nodes on their inner edges, eliminating the offset body endpoints. Reference: Lucide bug: body and mirrored limbs meet at shared construction nodes."""

        def path(n, start, commands, closed=False):
            here = start
            members = []
            for i, c in enumerate(commands):
                kind, end, *args = c
                name = f'{n}-{i}'
                if kind == 'L':
                    self.add_line(name, here, end)
                elif kind == 'A':
                    self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C':
                    self.add_bezier(name, here, (args[0], args[1], end))
                members.append(name)
                here = end
            self.add_contour(n, *members, closed=closed)

        def oval(n, x, y, rx, ry):
            path(n, (x - rx, y), [('A', (x + rx, y), rx, ry, True), ('A', (x - rx, y), rx, ry, True)], True)

        def box(n, l, t, r, b, rad=4):
            path(n, (l + rad, t), [('L', (r - rad, t)), ('A', (r, t + rad), rad, rad, True), ('L', (r, b - rad)), ('A', (r - rad, b), rad, rad, True), ('L', (l + rad, b)), ('A', (l, b - rad), rad, rad, True), ('L', (l, t + rad)), ('A', (l + rad, t), rad, rad, True)], True)
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        poly('thorax', (18, 12), (30, 12), (30, 20), (18, 20), closed=True)
        line('antenna-left', (18, 12), (14, 6))
        line('antenna-right', (30, 12), (34, 6))
        join('thorax', 'antenna-left')
        join('thorax', 'antenna-right')
        for side in [-1, 1]:
            x = lambda d: 24 + side * d
            path(f'wing-{side}', (x(6), 20), [('C', (x(18), 36), (x(14), 24), (x(18), 31)), ('L', (x(10), 40)), ('L', (x(8), 30)), ('L', (x(6), 20))], True)
            join(f'wing-{side}', 'thorax')
        path('abdomen', (16, 30), [('A', (32, 30), 8, 12, False)])
        join('abdomen', 'wing--1')
        join('abdomen', 'wing-1')
