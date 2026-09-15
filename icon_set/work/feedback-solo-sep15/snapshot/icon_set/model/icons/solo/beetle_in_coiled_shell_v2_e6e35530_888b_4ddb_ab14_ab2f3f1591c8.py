"""Replace the rectangular insect with a curved beetle body and distinct legs.
Plan: open shell spiral enclosing one oval beetle with three paired leg rows.
SQUARE centerline extremes (6,6)-(42,42).
Lucide: bug; geometric contour construction adapted to SOLO48.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e6e35530-888b-4ddb-ab14-ab2f3f1591c8'
SOURCE_PATH = 'pictographic-primitives/animals/insect earth_e6e35530-888b-4ddb-ab14-ab2f3f1591c8.svg'
AUTHOR = 'gpt-6'

class BeetleInCoiledShellVariant2(Solo48):
    icon_id = 'beetle-in-coiled-shell-v2'
    variant_of = 'beetle-in-coiled-shell'
    variant_label = 'Batch 01: visual refinement'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('insect', 'beetle', 'shell', 'coil', 'spiral', 'cocoon', 'bug', 'nest')

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
        path('shell', (24, 6), [('A', (42, 24), 18, 18, True), ('A', (24, 42), 18, 18, True), ('A', (6, 24), 18, 18, True)])
        path('beetle', (20, 18), [('A', (28, 18), 4, 4, True), ('L', (28, 28)), ('A', (20, 28), 4, 4, True), ('L', (20, 18))], True)
        for side, x, ex in [('left', 20, 14), ('right', 28, 32)]:
            for y in (18, 28):
                line(f'{side}-leg-{y}', (x, y), (ex, y))
                join(f'{side}-leg-{y}', 'beetle')
        line('antenna-left', (20, 18), (17, 12))
        line('antenna-right', (28, 18), (28, 16))
        join('antenna-left', 'beetle')
        join('antenna-right', 'beetle')
