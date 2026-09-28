"""Upright test tube with a straight rim, level liquid, and rounded closed end.
Plan: a symmetric tube silhouette with a radius-12 round base.
VRECT_M centerline extremes (10,4)-(38,44).
Lucide: No useful subject-specific match; supplied original guides the silhouette.
Independent variant; original preserved."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fb52e379-0f84-4c69-a8bd-3b7fd2c8c58e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__lab-tube-experiment/20260927T133723Z-thuan-mac-1/reference/lab tube experiment_fb52e379-0f84-4c69-a8bd-3b7fd2c8c58e.svg'
AUTHOR = "gpt-6"
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class LabTubeExperiment(Solo48):
    icon_id = 'lab-tube-experiment'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    categories = ('science', 'primitives')
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
        # Upright rim and rounded bottom follow the supplied test-tube reference.
        line('rim',(10,4),(38,4))
        path('tube',(12,4),[('L',(12,32)),('A',(36,32),12,12,False),('L',(36,4))])
        join('rim','tube')
        line('liquid',(12,23),(36,23))
        join('liquid','tube')
