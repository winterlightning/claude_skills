"""Rebuild the fan blade as an exact circle with a diagonal handle at a shared circle point. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7be3733e-dd31-5735-a409-964d8f89d37b'
SOURCE_PATH = 'pictographic-primitives/animals/ray_7be3733e-dd31-5735-a409-964d8f89d37b.svg'
AUTHOR = 'gpt-6'

class RoundHandFan(Solo48):
    icon_id = 'round-hand-fan'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('fan', 'hand fan', 'uchiwa', 'handle', 'cooling', 'japanese', 'round', 'paddle')

    def build(self):
        """Symbol plan: Rebuild the fan blade as an exact circle with a diagonal handle at a shared circle point. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('blade', (17, 32), [('A', (14, 23), 15, 15, True), ('A', (29, 8), 15, 15, True), ('A', (44, 23), 15, 15, True), ('A', (29, 38), 15, 15, True), ('A', (17, 32), 15, 15, True)], True)
        line('handle', (4, 40), (17, 32))
        join('handle', 'blade')
