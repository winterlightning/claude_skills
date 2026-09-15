"""Replace the flattened head with a true vertical oval, mirror both oval ears, and attach a simple curled trunk below the face. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '448ae7e7-230e-5858-9857-5a4d7a93f188'
SOURCE_PATH = 'pictographic-primitives/animals/elephant head_448ae7e7-230e-5858-9857-5a4d7a93f188.svg'
AUTHOR = 'gpt-6'

class ElephantHead(Solo48):
    icon_id = 'elephant-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('elephant', 'head', 'face', 'trunk', 'tusks', 'ears', 'animal', 'wildlife')

    def build(self):
        """Symbol plan: Replace the flattened head with a true vertical oval, mirror both oval ears, and attach a simple curled trunk below the face. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        oval('face', 24, 18, 10, 12)
        for n, x in [('left', 10), ('right', 38)]:
            oval('ear-' + n, x, 18, 4, 12)
            join('ear-' + n, 'face')
        path('trunk', (24, 30), [('L', (24, 36)), ('A', (30, 42), 6, 6, False), ('A', (36, 36), 6, 6, False)])
        join('trunk', 'face')
