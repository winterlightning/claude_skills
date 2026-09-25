"""Replace the diaper curve and tapered body with one rounded rectangular torso. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8e4bd3c6-f290-4652-9dfa-4a17d82dca3d'
SOURCE_PATH = 'pictographic-primitives/babies/family baby_8e4bd3c6-f290-4652-9dfa-4a17d82dca3d.svg'
AUTHOR = 'gpt-6'

class BabyFigure(Solo48):
    icon_id = 'baby-figure'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    aliases = ()
    keywords = ('baby', 'figure', 'infant', 'nursery')

    def build(self):
        """Symbol plan: Replace the diaper curve and tapered body with one rounded rectangular torso. Reference: Shared full_body_ref.png: circular head; head bottom16 to torso top24 gives exactly 4 ink units."""

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
        oval('head', 24, 10, 6, 6)
        path('torso', (24, 24), [('L', (28, 24)), ('A', (32, 28), 4, 4, True), ('L', (32, 36)), ('A', (28, 40), 4, 4, True), ('L', (20, 40)), ('A', (16, 36), 4, 4, True), ('L', (16, 28)), ('A', (20, 24), 4, 4, True), ('L', (24, 24))], True)
        line('arm-left', (16, 28), (8, 34))
        line('arm-right', (32, 28), (40, 34))
        join('arm-left', 'torso')
        join('arm-right', 'torso')
        line('leg-left', (20, 40), (16, 44))
        line('leg-right', (28, 40), (32, 44))
        join('leg-left', 'torso')
        join('leg-right', 'torso')
