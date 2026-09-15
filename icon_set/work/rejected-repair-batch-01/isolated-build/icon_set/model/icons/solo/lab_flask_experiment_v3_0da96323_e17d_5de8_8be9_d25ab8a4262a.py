"""Rebuild the flask with exact mirrored neck and shoulder geometry; remove small curve mismatches.
Plan: mirrored flask shoulders, paired radius-6 base corners, level liquid surface.
VRECT_L centerline extremes (8,4)-(40,44).
Lucide: milk; geometric contour construction adapted to SOLO48.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0da96323-e17d-5de8-8be9-d25ab8a4262a'
SOURCE_PATH = 'pictographic-primitives/science/lab flask experiment_0da96323-e17d-5de8-8be9-d25ab8a4262a.svg'
AUTHOR = 'gpt-6'

class LabFlaskExperimentVariant3(Solo48):
    icon_id = 'lab-flask-experiment-v3'
    variant_of = 'lab-flask-experiment'
    variant_label = 'Batch 01: visual refinement'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('lab', 'flask', 'experiment', 'science')

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
        path('flask', (16, 4), [('L', (32, 4)), ('L', (30, 8)), ('L', (30, 18)), ('L', (36, 30)), ('L', (40, 38)), ('A', (34, 44), 6, 6, True), ('L', (14, 44)), ('A', (8, 38), 6, 6, True), ('L', (12, 30)), ('L', (18, 18)), ('L', (18, 8)), ('L', (16, 4))], True)
        line('liquid', (12, 30), (36, 30))
        join('liquid', 'flask')
