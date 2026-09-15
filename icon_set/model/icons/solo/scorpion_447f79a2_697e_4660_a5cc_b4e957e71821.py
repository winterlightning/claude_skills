"""Shorten the four legs and replace the angular claws with opposing curves. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '447f79a2-697e-4660-a5cc-b4e957e71821'
SOURCE_PATH = 'pictographic-primitives/animals/insect scorpion_447f79a2-697e-4660-a5cc-b4e957e71821.svg'
AUTHOR = 'gpt-6'

class Scorpion(Solo48):
    icon_id = 'scorpion'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('scorpion', 'sting', 'claws', 'arachnid', 'tail', 'desert', 'venom', 'zodiac')

    def build(self):
        """Symbol plan: Shorten the four legs and replace the angular claws with opposing curves. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('body',(18,24), [('A',(24,18),6,6,True),('A',(30,24),6,6,True),('L',(30,32)),('A',(24,36),6,4,True),('A',(18,32),6,4,True),('L',(18,24))],True)
        for side in (-1, 1):
            x = lambda d: 24 + side * d
            line(f'upper-leg-{side}', (x(6), 24), (x(12), 24))
            join(f'upper-leg-{side}', 'body')
            line(f'lower-leg-{side}', (x(6), 32), (x(14), 34))
            join(f'lower-leg-{side}', 'body')
            path(f'arm-{side}', (24, 18), [('L', (x(12), 12))])
            join(f'arm-{side}', 'body')
            path(f'claw-{side}', (x(18), 6), [('A', (x(12), 12), 6, 6, side == 1), ('A', (x(6), 6), 6, 6, side == 1)])
            join(f'arm-{side}', f'claw-{side}')
        join('arm--1', 'arm-1')
        path('tail',(24,36),[('C',(14,42),(24,42),(18,42)),('L',(6,42))])
        join('tail', 'body')

