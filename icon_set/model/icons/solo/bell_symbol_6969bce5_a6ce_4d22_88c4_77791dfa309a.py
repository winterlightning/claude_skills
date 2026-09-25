"""Add the missing top finial and give the bell a balanced upright silhouette.
Plan: symmetric dome with continuous sides, top finial and shared rim endpoints.
VRECT_L centerline extremes (8,4)-(40,44).
Lucide: bell; geometric contour construction adapted to SOLO48.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6969bce5-a6ce-4d22-88c4-77791dfa309a'
SOURCE_PATH = 'pictographic-primitives/symbol/bell_6969bce5-a6ce-4d22-88c4-77791dfa309a.svg'
AUTHOR = 'gpt-6'

class BellSymbol(Solo48):
    icon_id = 'bell-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('bell', 'symbol', 'solo-ai-first50')

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
        path('dome', (8, 44), [('L', (8, 28)), ('A', (24, 12), 16, 16, True), ('A', (40, 28), 16, 16, True), ('L', (40, 44))])
        line('rim', (8, 44), (40, 44))
        join('rim', 'dome')
        line('finial', (24, 4), (24, 12))
        join('finial', 'dome')
