"""Use exact paired quarter-ellipses for the opposing claws, broaden the upper body curve, and give each leg a shared side attachment. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '41bb3775-67e6-5a7f-bc03-6922fe35a73f'
SOURCE_PATH = 'pictographic-primitives/animals/shellfish crab_41bb3775-67e6-5a7f-bc03-6922fe35a73f.svg'
AUTHOR = 'gpt-6'

class Crab(Solo48):
    icon_id = 'crab'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('crab', 'claws', 'shellfish', 'sea', 'beach', 'seafood', 'cancer', 'marine')

    def build(self):
        """Symbol plan: Use exact paired quarter-ellipses for the opposing claws, broaden the upper body curve, and give each leg a shared side attachment. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('body', (12, 33), [('A', (36, 33), 12, 7, True), ('A', (12, 33), 12, 7, True)], True)
        for side in [-1, 1]:
            x = lambda d: 24 + side * d
            path(f'claw-{side}', (x(18), 6), [('A', (x(12), 16), 6, 10, side == 1), ('A', (x(6), 6), 6, 10, side == 1)])
            line(f'arm-{side}', (x(12), 33), (x(12), 16))
            join(f'arm-{side}', 'body')
            join(f'arm-{side}', f'claw-{side}')
            poly(f'leg-{side}', (x(12), 33), (x(18), 40), (x(18), 42))
            join(f'leg-{side}', 'body')
            join(f'leg-{side}', f'arm-{side}')
