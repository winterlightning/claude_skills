"""Rebuild the ant with a continuous head, thorax and rounded abdomen, six paired legs, and short antennae; remove the stick-figure proportions."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4dc29185-dc5f-4ffe-94d4-dbda6690888c'
SOURCE_PATH = 'pictographic-primitives/animals/insect ant_4dc29185-dc5f-4ffe-94d4-dbda6690888c.svg'
AUTHOR = 'gpt-6'

class Ant(Solo48):
    icon_id = 'ant-redraw-v3'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('ant', 'insect', 'worker', 'bug', 'colony', 'antennae', 'legs', 'nature')
    variant_of = 'ant'
    variant_label = 'Batch 01: user feedback redraw'

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
        path('body', (20, 8), [('A', (24, 4), 4, 4, True), ('A', (28, 8), 4, 4, True), ('L', (28, 12)), ('C', (32, 20), (28, 16), (32, 16)), ('L', (32, 28)), ('L', (32, 36)), ('A', (24, 44), 8, 8, True), ('A', (16, 36), 8, 8, True), ('L', (16, 28)), ('L', (16, 20)), ('C', (20, 12), (16, 16), (20, 16)), ('L', (20, 8))], True)
        line('abdomen-joint', (16, 28), (32, 28))
        join('abdomen-joint', 'body')
        for side in (-1, 1):
            x = lambda d: 24 + side * d
            for k, y, tip_y in [('front', 20, 12), ('middle', 28, 28), ('rear', 36, 44)]:
                line(f'{k}-leg-{side}', (x(8), y), (x(16), tip_y))
                join(f'{k}-leg-{side}', 'body')
            line(f'antenna-{side}', (x(4), 8), (x(10), 4))
            join(f'antenna-{side}', 'body')
