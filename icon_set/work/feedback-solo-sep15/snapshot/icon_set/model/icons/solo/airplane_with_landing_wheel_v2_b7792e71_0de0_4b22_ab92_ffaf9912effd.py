"""Shorten and widen both wings; give the landing wheel clear space below the broad horizontal fuselage. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b7792e71-0de0-4b22-ab92-ffaf9912effd'
SOURCE_PATH = 'pictographic-primitives/travel/plane with wheel_b7792e71-0de0-4b22-ab92-ffaf9912effd.svg'
AUTHOR = 'gpt-6'

class AirplaneWithLandingWheelVariant2(Solo48):
    icon_id = 'airplane-with-landing-wheel-v2'
    variant_of = 'airplane-with-landing-wheel'
    variant_label = 'Shorten and widen both wings around a horizontal fuselage; retain the landing wheel.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/travel'
    aliases = ()
    keywords = ('airplane', 'landing-gear', 'wheel', 'flight', 'aircraft', 'plane', 'aviation', 'travel')

    def build(self):
        """Symbol plan: Shorten and widen both wings; give the landing wheel clear space below the broad horizontal fuselage. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('plane', (6, 14), [('L', (14, 16)), ('L', (18, 16)), ('L', (14, 6)), ('L', (24, 6)), ('L', (32, 16)), ('L', (38, 16)), ('A', (38, 24), 4, 4, True), ('L', (32, 24)), ('L', (24, 32)), ('L', (14, 32)), ('L', (18, 24)), ('L', (14, 24)), ('L', (6, 26)), ('L', (10, 20)), ('L', (6, 14))], True)
        line('strut', (38, 24), (39, 36))
        join('strut', 'plane')
        oval('wheel', 39, 39, 3, 3)
        join('wheel', 'strut')
