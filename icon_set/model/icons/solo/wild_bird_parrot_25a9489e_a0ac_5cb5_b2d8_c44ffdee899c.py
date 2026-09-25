"""Raise the open wing curve into the body and keep it clear of the tail; widen the body to preserve room for the eye. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '25a9489e-a0ac-5cb5-b2d8-c44ffdee899c'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird parrot_25a9489e-a0ac-5cb5-b2d8-c44ffdee899c.svg'
AUTHOR = 'gpt-6'

class Toucan(Solo48):
    icon_id = 'toucan'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('toucan', 'bird', 'beak', 'tropical', 'rainforest', 'perch', 'parrot', 'exotic')

    def build(self):
        """Symbol plan: Raise the open wing curve into the body and keep it clear of the tail; widen the body to preserve room for the eye. Reference: Lucide bird: a coherent body outline with one open wing curve."""

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
        path('outline', (6, 20), [('A', (20, 6), 14, 14, True), ('C', (42, 18), (32, 6), (42, 10)), ('L', (28, 18)), ('L', (30, 26)), ('A', (20, 38), 10, 12, True), ('L', (6, 42)), ('L', (6, 28)), ('L', (6, 20))], True)
        line('bill-root', (20, 6), (28, 18))
        join('bill-root', 'outline')
        dot('eye', (16, 18))
        path('wing', (6, 28), [('C', (18, 26), (6, 30), (18, 31))])
        join('wing', 'outline')
