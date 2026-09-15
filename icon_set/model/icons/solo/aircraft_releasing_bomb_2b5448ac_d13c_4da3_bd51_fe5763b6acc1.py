"""Give the aircraft a closed top-side silhouette with a rounded nose, swept wing and separate falling bomb. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2b5448ac-d13c-4da3-bd51-fe5763b6acc1'
SOURCE_PATH = 'pictographic-primitives/war/military drone attack_2b5448ac-d13c-4da3-bd51-fe5763b6acc1.svg'
AUTHOR = 'gpt-6'

class AircraftReleasingBomb(Solo48):
    icon_id = 'aircraft-releasing-bomb'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('aircraft', 'bomb', 'flight', 'military', 'wing', 'release')

    def build(self):
        """Symbol plan: Give the aircraft a closed top-side silhouette with a rounded nose, swept wing and separate falling bomb. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('plane', (6, 12), [('L', (14, 16)), ('L', (18, 16)), ('L', (24, 6)), ('L', (33, 6)), ('L', (28, 18)), ('L', (38, 18)), ('A', (42, 22), 4, 4, True), ('A', (38, 26), 4, 4, True), ('L', (12, 26)), ('L', (6, 12))], True)
        path('bomb', (14, 34), [('L', (24, 34)), ('L', (24, 38)), ('L', (24, 42)), ('L', (14, 42)), ('A', (14, 34), 4, 4, True)], True)
        poly('tail', (32, 34), (24, 38), (32, 42))
        join('tail', 'bomb')
