"""Rebuild the aircraft around one diagonal fuselage with mirrored swept wings and tailplanes, replacing the uneven zigzag silhouette."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7c4a4613-628d-4a28-92ef-9942dc74dd54'
SOURCE_PATH = 'pictographic-primitives/travel/plane 1_7c4a4613-628d-4a28-92ef-9942dc74dd54.svg'
AUTHOR = 'gpt-6'

class ClimbingAirliner(Solo48):
    icon_id = 'climbing-airliner-redraw-v3'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/travel'
    aliases = ()
    keywords = ('airplane', 'plane', 'takeoff', 'flight', 'climbing', 'aviation', 'departure', 'travel')
    variant_of = 'climbing-airliner'
    variant_label = 'Batch 01: user feedback redraw'

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

        def rounded(n, x0, y0, x1, y1, r):
            path(n, (x0 + r, y0), [('L', (x1 - r, y0)), ('A', (x1, y0 + r), r, r, True), ('L', (x1, y1 - r)), ('A', (x1 - r, y1), r, r, True), ('L', (x0 + r, y1)), ('A', (x0, y1 - r), r, r, True), ('L', (x0, y0 + r)), ('A', (x0 + r, y0), r, r, True)], True)
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        path('plane', (36, 6), [('C', (42, 12), (40, 6), (42, 8)), ('L', (32, 22)), ('L', (32, 38)), ('L', (24, 42)), ('L', (22, 30)), ('L', (16, 36)), ('L', (16, 42)), ('L', (6, 42)), ('L', (6, 32)), ('L', (12, 32)), ('L', (18, 26)), ('L', (6, 24)), ('L', (10, 16)), ('L', (26, 16)), ('L', (36, 6))], True)
