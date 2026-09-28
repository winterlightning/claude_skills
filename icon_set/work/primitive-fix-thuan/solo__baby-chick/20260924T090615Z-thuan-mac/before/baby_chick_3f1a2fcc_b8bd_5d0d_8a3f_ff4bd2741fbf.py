"""Restore a clear beak and eye; smooth the head, belly, and raised tail.
Plan: one chick silhouette with shared head/beak node, one eye and one wing.
SQUARE centerline extremes (6,6)-(42,42).
Lucide: bird; geometric contour construction adapted to SOLO48.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3f1a2fcc-b8bd-5d0d-8a3f-ff4bd2741fbf'
SOURCE_PATH = 'pictographic-primitives/animals/chick_3f1a2fcc-b8bd-5d0d-8a3f-ff4bd2741fbf.svg'
AUTHOR = 'gpt-6'

class BabyChick(Solo48):
    icon_id = 'baby-chick'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/animals'
    aliases = ()
    keywords = ('chick', 'chicken', 'bird', 'baby', 'hatch', 'farm', 'easter', 'poultry')

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
        path('chick', (6, 22), [('L', (12, 16)), ('A', (24, 6), 12, 10, True), ('A', (36, 18), 12, 12, True), ('L', (42, 18)), ('L', (42, 26)), ('A', (26, 42), 16, 16, True), ('L', (22, 42)), ('A', (6, 26), 16, 16, True), ('L', (6, 22))], True)
        dot('eye', (23, 17))
        path('wing', (22, 28), [('A', (29, 32), 7, 4, False)])
