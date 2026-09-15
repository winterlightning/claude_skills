"""Give the eagle a centered, recognizable hooked beak and cleaner feather tips.
Plan: symmetrical eagle head, paired angular brow runs, and a separate hooked beak.
SQUARE centerline extremes (6,6)-(42,42).
Lucide: bird; geometric contour construction adapted to SOLO48.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3e22df15-b9ec-486b-ae4d-8ed0445ebba1'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird eagle head_3e22df15-b9ec-486b-ae4d-8ed0445ebba1.svg'
AUTHOR = 'gpt-6'

class EagleHeadFrontVariant2(Solo48):
    icon_id = 'eagle-head-front-v2'
    variant_of = 'eagle-head-front'
    variant_label = 'Batch 01: visual refinement'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('eagle', 'head', 'front', 'beak', 'feathers', 'raptor', 'bird', 'wildlife')

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
        path('head', (6, 24), [('A', (24, 6), 18, 18, True), ('A', (42, 24), 18, 18, True), ('L', (42, 38)), ('L', (32, 36)), ('L', (24, 42)), ('L', (16, 36)), ('L', (6, 38)), ('L', (6, 24))], True)
        poly('brow-left', (15, 20), (24, 24), (33, 20))
        path('beak', (24, 24), [('L', (27, 28)), ('A', (24, 31), 3, 3, True)])
        join('brow-left', 'beak')
