"""Enlarge both ant eyes from radius three to four and rebalance the head between them. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cabf46f7-0aba-55d5-a29f-651d4429c74f'
SOURCE_PATH = 'pictographic-primitives/animals/insect head_cabf46f7-0aba-55d5-a29f-651d4429c74f.svg'
AUTHOR = 'gpt-6'

class AntHead(Solo48):
    icon_id = 'ant-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('ant', 'insect', 'head', 'face', 'antennae', 'eyes', 'bug', 'mandible')

    def build(self):
        """Symbol plan: Enlarge both ant eyes from radius three to four and rebalance the head between them. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('head', (16, 27), [('A', (20, 18), 4, 9, True), ('L', (28, 18)), ('A', (32, 27), 4, 9, True), ('L', (32, 34)), ('A', (28, 38), 4, 4, True), ('L', (28, 44)), ('L', (20, 44)), ('L', (20, 38)), ('A', (16, 34), 4, 4, True), ('L', (16, 27))], True)
        for n, x in [('left', 12), ('right', 36)]:
            oval(n, x, 27, 4, 4)
            join(n, 'head')
        poly('antenna-left', (20, 18), (20, 8), (14, 4))
        poly('antenna-right', (28, 18), (28, 8), (34, 4))
        join('antenna-left', 'head')
        join('antenna-right', 'head')
