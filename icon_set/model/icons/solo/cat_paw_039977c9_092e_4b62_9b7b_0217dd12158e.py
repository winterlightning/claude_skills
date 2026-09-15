"""Make the toe pads read as a paw instead of a two-eyed face.
Plan: three rounded toes and a broad paw pad; preserve the open leg sides.
VRECT_L centerline extremes (8,4)-(40,44).
Lucide: paw-print; geometric contour construction adapted to SOLO48.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '039977c9-092e-4b62-9b7b-0217dd12158e'
SOURCE_PATH = 'pictographic-primitives/animals/cat pawn_039977c9-092e-4b62-9b7b-0217dd12158e.svg'
AUTHOR = 'gpt-6'

class CatPaw(Solo48):
    icon_id = 'cat-paw'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/animals'
    aliases = ()
    keywords = ('cat', 'paw', 'print', 'pad', 'toe', 'pet', 'animal', 'foot')

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
        path('outline', (8, 44), [('L', (8, 18)), ('A', (16, 10), 8, 8, True), ('A', (24, 4), 8, 6, True), ('A', (32, 10), 8, 6, True), ('A', (40, 18), 8, 8, True), ('L', (40, 44))])
        for x, y in [(17, 21), (24, 15), (31, 21)]:
            dot(f'toe-{x}', (x, y))
        path('pad', (17, 37), [('A', (24, 31), 7, 6, True), ('A', (31, 37), 7, 6, True), ('A', (24, 41), 7, 4, True), ('A', (17, 37), 7, 4, True)], True)
