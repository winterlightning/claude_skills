"""Separate the cutting blade from the support and make its vertical cutting direction clear.
Plan: rounded housing with hand slot, central support, forward blade and base shoe.
HRECT_L centerline extremes (4,8)-(44,40).
Lucide: drill; geometric contour construction adapted to SOLO48.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dc02504c-1fd9-4220-bb74-2ff809f58aba'
SOURCE_PATH = 'pictographic-primitives/tools/power tools wood cutter_dc02504c-1fd9-4220-bb74-2ff809f58aba.svg'
AUTHOR = 'gpt-6'

class JigsawPowerTool(Solo48):
    icon_id = 'jigsaw-power-tool'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    categories = ('primitives', 'tools')
    aliases = ()
    keywords = ('jigsaw', 'saw', 'power tool', 'cutting', 'woodworking', 'blade', 'electric', 'tool')

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
        path('body', (14, 8), [('L', (30, 8)), ('A', (36, 14), 6, 6, True), ('L', (36, 26)), ('L', (8, 26)), ('L', (8, 14)), ('A', (14, 8), 6, 6, True)], True)
        line('handle-slot', (18, 17), (26, 17))
        line('blade', (10, 26), (10, 40))
        join('body', 'blade')
        line('support', (28, 26), (28, 40))
        join('support', 'shoe')
        join('support', 'body')
        line('shoe', (4, 40), (38, 40))
        join('blade', 'shoe')
        join('support', 'shoe')
        path('cord', (36, 18), [('L', (40, 18)), ('A', (44, 22), 4, 4, True)])
        join('cord', 'body')
