"""Clarify the tail connection with a broad straight rear fuselage and one centered tail fin. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0e73af01-7338-412e-b76b-79b5b693ad46'
SOURCE_PATH = 'pictographic-primitives/symbol/plane horizontal_0e73af01-7338-412e-b76b-79b5b693ad46.svg'
AUTHOR = 'gpt-6'

class AirplaneHorizontalVariant2(Solo48):
    icon_id = 'airplane-horizontal-v2'
    variant_of = 'airplane-horizontal'
    variant_label = 'Clarify the tail connection with a broad straight rear fuselage and one centered tail fin.'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('airplane', 'plane', 'flight', 'travel', 'aircraft', 'airport', 'trip', 'aviation')

    def build(self):
        """Symbol plan: Clarify the tail connection with a broad straight rear fuselage and one centered tail fin. Reference: inspected current parent; no useful exact Lucide match selected."""

        def path(n, start, commands, closed=False):
            here = start
            members = []
            for i, c in enumerate(commands):
                kind, end, *args = c
                name = f'{n}-{i}'
                if kind == 'L':
                    self.add_line(name, here, end)
                elif kind == 'A':
                    self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C':
                    self.add_bezier(name, here, (args[0], args[1], end))
                members.append(name)
                here = end
            self.add_contour(n, *members, closed=closed)

        def oval(n, x, y, rx, ry):
            path(n, (x - rx, y), [('A', (x + rx, y), rx, ry, True), ('A', (x - rx, y), rx, ry, True)], True)

        def box(n, l, t, r, b, rad=4):
            path(n, (l + rad, t), [('L', (r - rad, t)), ('A', (r, t + rad), rad, rad, True), ('L', (r, b - rad)), ('A', (r - rad, b), rad, rad, True), ('L', (l + rad, b)), ('A', (l, b - rad), rad, rad, True), ('L', (l, t + rad)), ('A', (l + rad, t), rad, rad, True)], True)
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        path('airframe', (4, 16), [('L', (12, 18)), ('L', (18, 18)), ('L', (14, 8)), ('L', (22, 8)), ('L', (32, 18)), ('L', (38, 18)), ('A', (38, 30), 6, 6, True), ('L', (32, 30)), ('L', (22, 40)), ('L', (14, 40)), ('L', (18, 30)), ('L', (12, 30)), ('L', (4, 32)), ('L', (8, 24)), ('L', (4, 16))], True)
        line('tail-center', (8, 24), (16, 24))
        join('tail-center', 'airframe')
