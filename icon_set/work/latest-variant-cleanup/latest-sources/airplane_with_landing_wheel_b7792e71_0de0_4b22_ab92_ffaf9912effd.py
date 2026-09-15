"""Shorten and widen both wings around a horizontal fuselage; retain the landing wheel. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b7792e71-0de0-4b22-ab92-ffaf9912effd'
SOURCE_PATH = 'pictographic-primitives/travel/plane with wheel_b7792e71-0de0-4b22-ab92-ffaf9912effd.svg'
AUTHOR = 'gpt-6'

class AirplaneWithLandingWheel(Solo48):
    icon_id = 'airplane-with-landing-wheel'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/travel'
    aliases = ()
    keywords = ('airplane', 'landing-gear', 'wheel', 'flight', 'aircraft', 'plane', 'aviation', 'travel')

    def build(self):
        """Symbol plan: Shorten and widen both wings around a horizontal fuselage; retain the landing wheel. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('plane', (4, 12), [('L', (12, 16)), ('L', (16, 20)), ('L', (20, 20)), ('L', (16, 8)), ('L', (24, 8)), ('L', (32, 20)), ('L', (40, 20)), ('A', (40, 28), 4, 4, True), ('L', (32, 28)), ('L', (24, 36)), ('L', (16, 36)), ('L', (20, 28)), ('L', (12, 28)), ('L', (4, 12))], True)
        line('strut', (40, 28), (40, 34))
        join('strut', 'plane')
        oval('wheel', 40, 37, 3, 3)
        join('strut', 'wheel')
