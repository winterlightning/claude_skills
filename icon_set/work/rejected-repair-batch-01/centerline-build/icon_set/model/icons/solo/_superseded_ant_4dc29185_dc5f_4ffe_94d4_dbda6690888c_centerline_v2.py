"""Separate the head, narrow waist, and round abdomen; spread the two retained leg pairs outward so they no longer curl tightly around the body.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4dc29185-dc5f-4ffe-94d4-dbda6690888c'
SOURCE_PATH = 'pictographic-primitives/animals/insect ant_4dc29185-dc5f-4ffe-94d4-dbda6690888c.svg'
AUTHOR = 'gpt-6'

class Ant(Solo48):
    icon_id = 'ant-centerline-v2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('ant', 'insect', 'worker', 'bug', 'colony', 'antennae', 'legs', 'nature')
    variant_of = 'ant'
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
        circle('head', 24, 10, 6)
        circle('abdomen', 24, 38, 6)
        poly('waist', (24, 16), (24, 24), (24, 32))
        join('waist', 'head')
        join('waist', 'abdomen')
        for side in (-1, 1):
            x = lambda d: 24 + side * d
            poly(f'antenna-{side}', (x(6), 10), (x(16), 4))
            join(f'antenna-{side}', 'head')
            poly(f'upper-leg-{side}', (24, 24), (x(16), 24), (x(16), 18))
            join(f'upper-leg-{side}', 'waist')
            line(f'lower-leg-{side}', (x(6), 38), (x(16), 44))
            join(f'lower-leg-{side}', 'abdomen')
        join('upper-leg--1', 'upper-leg-1')
