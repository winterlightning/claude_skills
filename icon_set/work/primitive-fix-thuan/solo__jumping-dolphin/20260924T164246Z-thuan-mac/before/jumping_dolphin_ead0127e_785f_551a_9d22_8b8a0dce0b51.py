"""Smooth the dolphin’s back and belly and define its beak, dorsal fin, and tail.
Plan: one arched swimming profile; intrinsic dorsal and pectoral fins share the outline.
SQUARE centerline extremes (6,6)-(42,42).
Lucide: fish; geometric contour construction adapted to SOLO48.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ead0127e-785f-551a-9d22-8b8a0dce0b51'
SOURCE_PATH = 'pictographic-primitives/animals/dolphin_ead0127e-785f-551a-9d22-8b8a0dce0b51.svg'
AUTHOR = 'gpt-6'

class JumpingDolphin(Solo48):
    icon_id = 'jumping-dolphin'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('dolphin', 'jump', 'sea', 'ocean', 'marine', 'mammal', 'arc', 'swim')

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
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        path('dolphin', (6, 22), [('C', (22, 10), (9, 13), (14, 10)), ('L', (29, 6)), ('L', (28, 14)), ('C', (38, 30), (35, 18), (37, 24)), ('C', (42, 42), (39, 35), (42, 36)), ('L', (33, 38)), ('L', (25, 42)), ('L', (31, 34)), ('C', (22, 22), (28, 30), (25, 25)), ('L', (18, 36)), ('L', (14, 24)), ('L', (6, 27)), ('L', (6, 22))], True)
