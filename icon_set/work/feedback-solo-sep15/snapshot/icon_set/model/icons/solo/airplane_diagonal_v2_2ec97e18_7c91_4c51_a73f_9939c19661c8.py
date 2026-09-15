"""Round all four wing and tail tips with explicit smooth turns. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2ec97e18-7c91-4c51-a73f-9939c19661c8'
SOURCE_PATH = 'pictographic-primitives/symbol/airplane_2ec97e18-7c91-4c51-a73f-9939c19661c8.svg'
AUTHOR = 'gpt-6'

class AirplaneDiagonalVariant2(Solo48):
    icon_id = 'airplane-diagonal-v2'
    variant_of = 'airplane-diagonal'
    variant_label = 'Round all four wing and tail tips with explicit smooth turns.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbols/standalone'
    aliases = ()
    keywords = ('airplane', 'plane', 'flight', 'travel', 'aircraft', 'airport', 'trip', 'aviation')

    def build(self):
        """Symbol plan: Round all four wing and tail tips with explicit smooth turns. Reference: Lucide plane: smooth nose and coherent joined wing outline."""

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
        path('plane', (34, 6), [('A', (42, 14), 8, 8, True), ('L', (34, 24)), ('L', (40, 32)), ('C', (40, 36), (42, 34), (42, 34)), ('L', (36, 40)), ('C', (32, 39), (34, 42), (34, 42)), ('L', (26, 30)), ('L', (20, 36)), ('L', (21, 39)), ('C', (18, 42), (22, 42), (22, 42)), ('L', (15, 42)), ('A', (12, 39), 3, 3, True), ('L', (12, 36)), ('L', (8, 35)), ('C', (6, 32), (6, 34), (6, 34)), ('L', (6, 27)), ('C', (9, 25), (6, 24), (6, 24)), ('L', (14, 26)), ('L', (20, 20)), ('L', (9, 14)), ('C', (8, 10), (6, 12), (6, 12)), ('L', (10, 8)), ('C', (14, 7), (12, 6), (12, 6)), ('L', (26, 14)), ('L', (34, 6))], True)
