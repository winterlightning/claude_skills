"""Round the raised wing and simplify the flying bird into a swept wing, small head, projecting bill and curved belly. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '00732191-23f0-53ae-84da-b288489181c6'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird fly_00732191-23f0-53ae-84da-b288489181c6.svg'
AUTHOR = 'gpt-6'

class FlyingBird(Solo48):
    icon_id = 'flying-bird'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('bird', 'flying', 'wings', 'dove', 'flight', 'sky', 'freedom', 'soar')

    def build(self):
        """Symbol plan: Round the raised wing and simplify the flying bird into a swept wing, small head, projecting bill and curved belly. Reference: Lucide bird: distinguish the bill and head from the larger wing and belly."""

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
        path('bird', (6, 30), [('L', (6, 6)), ('C', (24, 18), (14, 8), (20, 12)), ('L', (26, 24)), ('C', (30, 20), (29, 26), (30, 24)), ('A', (38, 20), 4, 6, True), ('L', (42, 24)), ('L', (38, 27)), ('C', (24, 42), (38, 36), (33, 42)), ('C', (6, 30), (14, 42), (6, 38))], True)
