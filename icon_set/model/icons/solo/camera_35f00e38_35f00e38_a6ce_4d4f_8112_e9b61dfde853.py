"""Add the missing lens and replace segmented corners with four matching arcs.
Plan: symmetric camera outline with raised prism, radius-4 corners, centered lens.
HRECT_L centerline extremes (4,8)-(44,40).
Lucide: camera; geometric contour construction adapted to SOLO48.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '35f00e38-a6ce-4d4f-8112-e9b61dfde853'
SOURCE_PATH = 'pictographic-primitives/video/camera_35f00e38-a6ce-4d4f-8112-e9b61dfde853.svg'
AUTHOR = 'gpt-6'

class Camera35f00e38(Solo48):
    icon_id = 'camera-35f00e38'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('camera', 'video')

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
        path('camera', (18, 8), [('L', (30, 8)), ('L', (34, 14)), ('L', (40, 14)), ('A', (44, 18), 4, 4, True), ('L', (44, 36)), ('A', (40, 40), 4, 4, True), ('L', (8, 40)), ('A', (4, 36), 4, 4, True), ('L', (4, 18)), ('A', (8, 14), 4, 4, True), ('L', (14, 14)), ('L', (18, 8))], True)
        circle('lens', 24, 26, 5)
