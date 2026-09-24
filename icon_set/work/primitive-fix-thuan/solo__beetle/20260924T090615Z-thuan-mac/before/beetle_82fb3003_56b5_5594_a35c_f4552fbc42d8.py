"""Replace the segmented shell with one true oval, give it a centered seam, and attach matching leg fans to its sides. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '82fb3003-56b5-5594-a35c-f4552fbc42d8'
SOURCE_PATH = 'pictographic-primitives/animals/insect_82fb3003-56b5-5594-a35c-f4552fbc42d8.svg'
AUTHOR = 'gpt-6'

class Beetle(Solo48):
    icon_id = 'beetle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('beetle', 'bug', 'insect', 'shell', 'antennae', 'legs', 'nature', 'wildlife')

    def build(self):
        """Symbol plan: Replace the segmented shell with one true oval, give it a centered seam, and attach matching leg fans to its sides. Reference: Lucide bug: one shell, a center seam and repeated mirrored legs."""

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
            path(n, (x - rx, y), [('A', (x, y - ry), rx, ry, True), ('A', (x + rx, y), rx, ry, True), ('A', (x, y + ry), rx, ry, True), ('A', (x - rx, y), rx, ry, True)], True)

        def box(n, l, t, r, b, rad=4):
            path(n, (l + rad, t), [('L', (r - rad, t)), ('A', (r, t + rad), rad, rad, True), ('L', (r, b - rad)), ('A', (r - rad, b), rad, rad, True), ('L', (l + rad, b)), ('A', (l, b - rad), rad, rad, True), ('L', (l, t + rad)), ('A', (l + rad, t), rad, rad, True)], True)
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        oval('head', 24, 10, 6, 6)
        oval('shell', 24, 30, 10, 14)
        join('head', 'shell')
        line('seam', (24, 16), (24, 44))
        join('seam', 'shell')
        join('seam', 'head')
        for side in [-1, 1]:
            for j, y in enumerate([20, 30, 40]):
                n = f'leg-{side}-{j}'
                line(n, (24 + side * 10, 30), (24 + side * 16, y))
                join(n, 'shell')
            for a, b in [(0, 1), (0, 2), (1, 2)]:
                join(f'leg-{side}-{a}', f'leg-{side}-{b}')
