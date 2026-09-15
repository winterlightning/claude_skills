"""Rounded-tail takeoff alternative: soften the tail and wing corners while keeping the rising airplane. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1c7f6825-5aeb-4100-8e73-fd8c444b5b5c'
SOURCE_PATH = 'pictographic-primitives/travel/optimization plane_1c7f6825-5aeb-4100-8e73-fd8c444b5b5c.svg'
AUTHOR = 'gpt-6'

class AirplaneDepartingRunwayVariant2(Solo48):
    icon_id = 'airplane-departing-runway-v2'
    variant_of = 'airplane-departing-runway'
    variant_label = 'Rounded-tail takeoff alternative: soften the tail and wing corners while keeping the rising airplane.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/travel'
    aliases = ()
    keywords = ('airplane', 'departure', 'runway', 'takeoff', 'airport', 'flight', 'plane', 'travel')

    def build(self):
        """Symbol plan: Rounded-tail takeoff alternative: soften the tail and wing corners while keeping the rising airplane. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('plane', (12, 25), [('C', (6, 16), (9, 25), (7, 20)), ('A', (10, 12), 4, 4, True), ('L', (17, 16)), ('L', (30, 11)), ('L', (34, 8)), ('A', (40, 16), 5, 5, True), ('L', (18, 25)), ('C', (12, 25), (16, 25), (14, 25))], True)
        line('wing', (30, 11), (22, 6))
        join('wing', 'plane')
        poly('runway', (10, 34), (38, 34), (42, 42), (6, 42), closed=True)

