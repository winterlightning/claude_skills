"""Add visible blade teeth and a center hub so the tool reads as a circular saw.
Plan: circular upper guard with shared shoe nodes, handle, toothed exposed lower blade.
SQUARE centerline extremes (6,6)-(42,42).
Lucide: No useful subject-specific match; supplied original guides the silhouette.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6d7f07b0-c4a7-5343-80d4-cc97519098e9'
SOURCE_PATH = 'pictographic-primitives/tools/power tools electric saw_6d7f07b0-c4a7-5343-80d4-cc97519098e9.svg'
AUTHOR = 'gpt-6'

class HandheldCircularSaw(Solo48):
    icon_id = 'handheld-circular-saw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    aliases = ()
    keywords = ('circular saw', 'saw', 'power tool', 'blade', 'cutting', 'woodworking', 'handheld', 'construction')

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
        path('guard', (10, 26), [('A', (26, 10), 16, 16, True), ('A', (42, 26), 16, 16, True)])
        poly('shoe', (6, 26), (10, 26), (14, 26), (26, 26), (38, 26), (42, 26))
        join('guard', 'shoe')
        poly('handle', (10, 26), (6, 18), (6, 6), (26, 6), (26, 10))
        join('handle', 'guard')
        join('handle', 'shoe')
        poly('blade', (38, 26), (38, 34), (34, 34), (34, 39), (28, 37), (26, 42), (22, 38), (16, 38), (16, 34), (14, 34), (14, 26))
        join('blade', 'shoe')
