"""Use a rounded carry handle above the existing rounded rectangular camera bag. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1342f536-c927-4566-8887-d52e83745630'
SOURCE_PATH = 'pictographic-primitives/photography/bag_1342f536-c927-4566-8887-d52e83745630.svg'
AUTHOR = 'gpt-6'

class BagPhotography(Solo48):
    icon_id = 'bag-photography'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('solo-ai-refine', 'solo-ai-first50', 'bag-photography')

    def build(self):
        """Symbol plan: Use a rounded carry handle above the existing rounded rectangular camera bag. Reference: inspected current parent; no useful exact Lucide match selected."""

        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f'{name}-{index}'
                kind, end, *args = command
                if kind == 'L':
                    self.add_line(ident, here, end)
                elif kind == 'A':
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == 'C':
                    c1, c2 = args
                    self.add_bezier(ident, here, (c1, c2, end))
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)

        def circle(name, cx, cy, r):
            path(name, (cx - r, cy), [('A', (cx + r, cy), r, r, True), ('A', (cx - r, cy), r, r, True)], True)

        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0 + r, y0), [('L', (x1 - r, y0)), ('A', (x1, y0 + r), r, r, True), ('L', (x1, y1 - r)), ('A', (x1 - r, y1), r, r, True), ('L', (x0 + r, y1)), ('A', (x0, y1 - r), r, r, True), ('L', (x0, y0 + r)), ('A', (x0 + r, y0), r, r, True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a, b: self.relate('connect', a, b)
        path('handle', (16, 16), [('A', (32, 16), 8, 8, True)])
        path('body', (8, 16), [('L', (16, 16)), ('L', (32, 16)), ('L', (40, 16)), ('A', (44, 20), 4, 4, True), ('L', (44, 24)), ('L', (44, 36)), ('A', (40, 40), 4, 4, True), ('L', (8, 40)), ('A', (4, 36), 4, 4, True), ('L', (4, 24)), ('L', (4, 20)), ('A', (8, 16), 4, 4, True)], True)
        path('flap', (4, 24), [('C', (24, 30), (10, 28), (17, 30)), ('C', (44, 24), (31, 30), (38, 28))])
        join('handle', 'body')
        join('flap', 'body')
