"""Turn the test tube diagonally to preserve a slender tube and a rounded closed end.
Plan: diagonal tube with two parallel sides and a radius-8 round base; straight rim.
SQUARE centerline extremes (6,6)-(42,42).
Lucide: No useful subject-specific match; supplied original guides the silhouette.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fb52e379-0f84-4c69-a8bd-3b7fd2c8c58e'
SOURCE_PATH = 'pictographic-primitives/science/lab tube experiment_fb52e379-0f84-4c69-a8bd-3b7fd2c8c58e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class LabTubeExperiment(Solo48):
    icon_id = 'lab-tube-experiment'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('lab', 'tube', 'experiment', 'science')

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
        path('tube', (28, 6), [('L', (8, 26)), ('A', (22, 40), 10, 10, False), ('L', (42, 20))])
        poly('rim', (26, 6), (28, 6), (42, 20), (42, 22))
        join('rim', 'tube')
        line('liquid', (20, 14), (34, 28))
        join('liquid', 'tube')
