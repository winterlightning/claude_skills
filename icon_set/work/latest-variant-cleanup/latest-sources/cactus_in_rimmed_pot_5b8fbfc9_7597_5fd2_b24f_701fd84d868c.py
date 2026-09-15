"""Open the pot rim and simplify the cactus to a tall center stem with larger mirrored branches. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5b8fbfc9-7597-5fd2-b24f-701fd84d868c'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_5b8fbfc9-7597-5fd2-b24f-701fd84d868c.svg'
AUTHOR = 'gpt-6'

class CactusInRimmedPot(Solo48):
    icon_id = 'cactus-in-rimmed-pot'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/plants'
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self):
        """Symbol plan: Open the pot rim and simplify the cactus to a tall center stem with larger mirrored branches. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        poly('rim', (8, 28), (24, 28), (40, 28), (40, 38), (8, 38), closed=True)
        poly('pot', (13, 38), (16, 44), (32, 44), (35, 38))
        join('pot', 'rim')
        poly('stem', (24, 4), (24, 18), (24, 28))
        join('stem', 'rim')
        path('left-arm', (8, 8), [('L', (8, 12)), ('A', (14, 18), 6, 6, False), ('L', (24, 18))])
        path('right-arm', (40, 8), [('L', (40, 12)), ('A', (34, 18), 6, 6, True), ('L', (24, 18))])
        join('left-arm', 'stem')
        join('right-arm', 'stem')
        join('left-arm', 'right-arm')
