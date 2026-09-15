"""Widen the cobra hood and taper the neck so it no longer reads as a skull.
Plan: cobra hood owns mirrored shoulders, narrow neck, paired eyes, and mouth.
VRECT_L centerline extremes (8,4)-(40,44).
Lucide: No useful subject-specific match; supplied original guides the silhouette.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/cobra_head_friendly.py'
AUTHOR = 'gpt-6'

class CobraHeadFriendlyVariant2(Solo48):
    icon_id = 'cobra-head-friendly-v2'
    variant_of = 'cobra-head-friendly'
    variant_label = 'Batch 01: visual refinement'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ('cobra-head',)
    keywords = ('cobra', 'snake', 'reptile', 'hood', 'head', 'friendly')

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
        path('hood', (24, 4), [('C', (40, 20), (36, 4), (40, 10)), ('C', (30, 34), (40, 28), (32, 30)), ('L', (30, 44)), ('L', (18, 44)), ('L', (18, 34)), ('C', (8, 20), (16, 30), (8, 28)), ('C', (24, 4), (8, 10), (12, 4))], True)
        dot('eye-left', (19, 16))
        dot('eye-right', (29, 16))
        poly('mouth', (21, 25), (24, 28), (27, 25))
