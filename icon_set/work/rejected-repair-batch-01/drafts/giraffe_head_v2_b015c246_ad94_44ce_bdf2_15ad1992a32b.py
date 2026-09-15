"""Give the giraffe a clearer muzzle and eye while preserving its long neck and ear.
Plan: open neck, rounded muzzle and forehead, two ossicones and one ear.
SQUARE centerline extremes (6,6)-(42,42).
Lucide: No useful subject-specific match; supplied original guides the silhouette.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b015c246-ad94-44ce-bdf2-15ad1992a32b'
SOURCE_PATH = 'pictographic-primitives/animals/giraffe_b015c246-ad94-44ce-bdf2-15ad1992a32b.svg'
AUTHOR = 'gpt-6'

class GiraffeHeadVariant2(Solo48):
    icon_id = 'giraffe-head-v2'
    variant_of = 'giraffe-head'
    variant_label = 'Batch 01: visual refinement'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('giraffe', 'head', 'neck', 'ossicone', 'ear', 'profile', 'animal', 'safari')

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
        path('outline', (6, 42), [('L', (14, 18)), ('L', (18, 14)), ('L', (18, 6)), ('L', (26, 6)), ('L', (26, 14)), ('L', (34, 14)), ('L', (42, 26)), ('L', (42, 34)), ('L', (26, 34)), ('L', (18, 42))])
        poly('ear', (14, 18), (6, 10), (6, 6))
        join('ear', 'outline')
        dot('eye', (26, 24))
