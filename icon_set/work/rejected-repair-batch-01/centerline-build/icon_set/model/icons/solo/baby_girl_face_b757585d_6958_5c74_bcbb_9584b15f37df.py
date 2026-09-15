"""Use a round baby face with curved ears and a small hair curl; remove the large angular bow. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b757585d-6958-5c74-bcbb-9584b15f37df'
SOURCE_PATH = 'pictographic-primitives/babies/baby girl_b757585d-6958-5c74-bcbb-9584b15f37df.svg'
AUTHOR = 'gpt-6'

class BabyGirlFace(Solo48):
    icon_id = 'baby-girl-face'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('baby', 'girl', 'face', 'infant', 'nursery')

    def build(self):
        """Symbol plan: Use a round baby face with curved ears and a small hair curl; remove the large angular bow. Reference: Lucide baby and shared human reference: round cheeks, curved ears, paired eyes."""

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
        path('face', (10, 24), [('A', (24, 6), 14, 18, True), ('A', (38, 24), 14, 18, True), ('A', (42, 28), 4, 4, True), ('A', (38, 32), 4, 4, True), ('A', (24, 42), 14, 10, True), ('A', (10, 32), 14, 10, True), ('A', (6, 28), 4, 4, True), ('A', (10, 24), 4, 4, True)], True)
        dot('eye-left', (19, 24))
        dot('eye-right', (29, 24))
