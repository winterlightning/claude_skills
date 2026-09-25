"""Replace the arrow-like valve with a rounded scallop fan and radiating ribs.
Plan: fan-shaped clam, wide curved crown, narrow hinge, paired radiating ribs.
SQUARE centerline extremes (6,6)-(42,42).
Lucide: No useful subject-specific match; supplied original guides the silhouette.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a23c6ef9-fd90-57c7-ae12-5006686062cd'
SOURCE_PATH = 'pictographic-primitives/animals/shell_a23c6ef9-fd90-57c7-ae12-5006686062cd.svg'
AUTHOR = 'gpt-6'

class ClamShell(Solo48):
    icon_id = 'clam-shell'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('shell', 'clam', 'mussel', 'oyster', 'sea', 'beach', 'bivalve', 'marine')

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
        path('shell', (18, 42), [('L', (8, 26)), ('C', (6, 18), (6, 23), (6, 21)), ('C', (24, 6), (6, 10), (15, 6)), ('C', (42, 18), (33, 6), (42, 10)), ('C', (40, 26), (42, 21), (42, 23)), ('L', (30, 42)), ('L', (18, 42))], True)
        poly('rib-left', (16, 18), (24, 32), (32, 18))
