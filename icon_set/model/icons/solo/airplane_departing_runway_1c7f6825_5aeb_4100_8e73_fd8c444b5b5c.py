"""Side-view takeoff alternative: a larger tail, clear upper and lower wings, and one runway line. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1c7f6825-5aeb-4100-8e73-fd8c444b5b5c'
SOURCE_PATH = 'pictographic-primitives/travel/optimization plane_1c7f6825-5aeb-4100-8e73-fd8c444b5b5c.svg'
AUTHOR = 'gpt-6'

class AirplaneDepartingRunway(Solo48):
    icon_id = 'airplane-departing-runway'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/travel'
    aliases = ()
    keywords = ('airplane', 'departure', 'runway', 'takeoff', 'airport', 'flight', 'plane', 'travel')

    def build(self):
        """Symbol plan: Side-view takeoff alternative: a larger tail, clear upper and lower wings, and one runway line. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('plane', (6, 12), [('L', (14, 12)), ('L', (14, 18)), ('L', (26, 18)), ('L', (38, 18)), ('A', (42, 22), 4, 4, True), ('A', (38, 26), 4, 4, True), ('L', (26, 26)), ('L', (6, 26)), ('L', (6, 12))], True)
        line('upper-wing', (26, 18), (26, 6))
        line('lower-wing', (26, 26), (20, 32))
        join('upper-wing', 'plane')
        join('lower-wing', 'plane')
        line('runway', (6, 42), (42, 42))
