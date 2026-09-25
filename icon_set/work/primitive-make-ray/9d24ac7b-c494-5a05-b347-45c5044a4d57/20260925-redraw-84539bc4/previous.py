"""Widen and straighten the ATV upper body while keeping both wheels and handlebar. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9d24ac7b-c494-5a05-b347-45c5044a4d57'
SOURCE_PATH = 'pictographic-primitives/transportation/car_9d24ac7b-c494-5a05-b347-45c5044a4d57.svg'
SOURCE_REFERENCES = (('9d24ac7b-c494-5a05-b347-45c5044a4d57', 'pictographic-primitives/transportation/car_9d24ac7b-c494-5a05-b347-45c5044a4d57.svg'),)
AUTHOR = 'gpt-6'

class AtvSideView(Solo48):
    icon_id = 'atv-side-view'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('atv', 'quad', 'quad bike', 'off-road', 'vehicle', 'four wheeler', 'offroad', 'side view')

    def build(self):
        """Symbol plan: Widen and straighten the ATV upper body while keeping both wheels and handlebar. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('body', (4, 17), [('L', (28, 17)), ('L', (44, 17))])
        line('handlebar', (28, 17), (24, 8))
        join('handlebar', 'body')
        for n, x in [('rear', 11), ('front', 37)]:
            oval(n, x, 33, 7, 7)
            line(n + '-support', (x, 17), (x, 26))
            join(n + '-support', 'body')
            join(n + '-support', n)
        line('chassis', (18, 33), (30, 33))
        join('chassis', 'rear')
        join('chassis', 'front')
