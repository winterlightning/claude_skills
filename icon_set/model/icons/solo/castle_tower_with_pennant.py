"""Rebuild the lower tower with equal stepped side walls and a rectangular central gate; simplify the pennant to a clean rectangle. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '033da33f-ea2d-58ce-a57c-5cffb7818dd9'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/historical building castle_033da33f-ea2d-58ce-a57c-5cffb7818dd9.svg'
AUTHOR = 'gpt-6'

class Landmark(Solo48):
    icon_id = 'castle-tower-with-pennant'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    aliases = ()
    keywords = ('castle', 'tower', 'turret', 'fortress', 'battlement', 'flag', 'pennant', 'medieval')

    def build(self):
        """Symbol plan: Rebuild the lower tower with equal stepped side walls and a rectangular central gate; simplify the pennant to a clean rectangle. Reference: Lucide castle: shared battlement widths and a clear gate."""

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
        poly('wall', (8, 44), (8, 20), (16, 20), (16, 28), (24, 28), (32, 28), (32, 20), (40, 20), (40, 44), (30, 44), (30, 36), (18, 36), (18, 44), closed=True)
        poly('pole', (24, 28), (24, 12), (24, 4))
        poly('flag', (24, 4), (40, 4), (40, 12), (24, 12))
        join('pole', 'wall')
        join('flag', 'pole')
