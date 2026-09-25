"""Round the raised index and show three folded knuckles above a rectangular wrist cuff. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '806acf8e-3fa3-5523-a16c-605e6d202d8b'
SOURCE_PATH = 'pictographic-primitives/work/task finger bandage_806acf8e-3fa3-5523-a16c-605e6d202d8b.svg'
AUTHOR = 'gpt-6'

class BandagedIndexFinger(Solo48):
    icon_id = 'bandaged-index-finger'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    aliases = ()
    keywords = ('hand', 'finger', 'bandage', 'injury', 'pointing', 'care')

    def build(self):
        """Symbol plan: Round the raised index and show three folded knuckles above a rectangular wrist cuff. Reference: Lucide hand: joined knuckle arcs and clear fingertip; shared human-reference.md for anatomy."""

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
        path('hand', (8, 8), [('A', (16, 8), 4, 4, True), ('L', (16, 24)), ('A', (24, 24), 4, 4, True), ('A', (32, 24), 4, 4, True), ('A', (40, 24), 4, 4, True), ('L', (40, 30)), ('A', (34, 36), 6, 6, True), ('L', (14, 36)), ('A', (8, 30), 6, 6, True), ('L', (8, 8))], True)
        for x in (24, 32):
            line(f'finger-{x}', (x, 24), (x, 28))
            join(f'finger-{x}', 'hand')
        poly('cuff', (14, 36), (14, 44), (34, 44), (34, 36))
        join('hand', 'cuff')
