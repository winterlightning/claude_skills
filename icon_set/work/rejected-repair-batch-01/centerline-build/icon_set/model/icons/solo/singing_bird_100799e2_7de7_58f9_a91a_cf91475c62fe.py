"""Remove the triangular crest and enlarge the smooth crown to retain the full icon height. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '100799e2-7de7-58f9-a91a-cf91475c62fe'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird sing_100799e2-7de7-58f9-a91a-cf91475c62fe.svg'
AUTHOR = 'gpt-6'

class SingingBird(Solo48):
    icon_id = 'singing-bird'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/birds'
    aliases = ()
    keywords = ('bird', 'singing', 'beak', 'open', 'song', 'chirp', 'head', 'wildlife')

    def build(self):
        """Symbol plan: Remove the triangular crest and enlarge the smooth crown to retain the full icon height. Reference: Lucide bird: rounded head with a simple open beak."""

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
        path('front', (8, 24), [('A', (24, 4), 16, 20, True), ('A', (34, 20), 10, 16, True), ('L', (40, 16)), ('L', (32, 28)), ('L', (40, 32)), ('L', (29, 40)), ('L', (30, 44))])
        path('back', (8, 24), [('C', (10, 39), (8, 31), (9, 36)), ('L', (8, 44))])
        join('front', 'back')
        dot('eye', (23, 19))
