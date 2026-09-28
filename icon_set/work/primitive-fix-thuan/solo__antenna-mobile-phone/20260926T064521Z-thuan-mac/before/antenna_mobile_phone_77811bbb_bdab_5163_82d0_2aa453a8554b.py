"""Recompose the antenna phone horizontally with a landscape body and clear screen division. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '77811bbb-bdab-5163-82d0-2aa453a8554b'
SOURCE_PATH = 'pictographic-primitives/phones/mobile phone blackberry_77811bbb-bdab-5163-82d0-2aa453a8554b.svg'
AUTHOR = 'gpt-6'

class AntennaMobilePhone(Solo48):
    icon_id = 'antenna-mobile-phone'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    categories = ('phones', 'primitives')
    aliases = ()
    keywords = ('phone', 'mobile', 'antenna', 'handset', 'screen', 'device')

    def build(self):
        """Symbol plan: Recompose the antenna phone horizontally with a landscape body and clear screen division. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('body', (8, 18), [('L', (18, 18)), ('L', (40, 18)), ('A', (44, 22), 4, 4, True), ('L', (44, 36)), ('A', (40, 40), 4, 4, True), ('L', (18, 40)), ('L', (8, 40)), ('A', (4, 36), 4, 4, True), ('L', (4, 22)), ('A', (8, 18), 4, 4, True)], True)
        line('antenna', (8, 8), (8, 18))
        join('antenna', 'body')
        line('screen-edge', (18, 18), (18, 40))
        join('screen-edge', 'body')
