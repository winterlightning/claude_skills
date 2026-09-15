"""Keep the exact square envelope while replacing the abrupt elbow with a 6-unit tangent quarter-circle; both arms remain equal. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f974b62e-0d33-55cb-be2b-f88ed0faccf9'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow corner right_f974b62e-0d33-55cb-be2b-f88ed0faccf9.svg'
AUTHOR = 'gpt-6'

class ArrowCornerRight(Solo48):
    icon_id = 'arrow-corner-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'corner', 'right', 'arrows')

    def build(self):
        """Symbol plan: Keep the exact square envelope while replacing the abrupt elbow with a 6-unit tangent quarter-circle; both arms remain equal. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('corner', (42, 42), [('L', (42, 12)), ('A', (36, 6), 6, 6, False), ('L', (6, 6))])
