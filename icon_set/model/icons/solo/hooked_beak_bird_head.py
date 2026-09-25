"""Replace the zero-length eye line with a centered dot and rebuild the crown and hooked beak using fewer smooth curves. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '79a4190f-e22e-5e6a-b9b2-2509c13da3ff'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird head_79a4190f-e22e-5e6a-b9b2-2509c13da3ff.svg'
AUTHOR = 'gpt-6'

class HookedBeakBirdHead(Solo48):
    icon_id = 'hooked-beak-bird-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('bird', 'head', 'beak', 'hooked', 'parrot', 'falcon', 'profile', 'raptor')

    def build(self):
        """Symbol plan: Replace the zero-length eye line with a centered dot and rebuild the crown and hooked beak using fewer smooth curves. Reference: Lucide bird: a dot eye inside a coherent round head."""

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
        path('head', (6, 42), [('L', (6, 24)), ('C', (24, 6), (6, 14), (14, 6)), ('C', (36, 14), (30, 6), (34, 9)), ('C', (28, 28), (36, 22), (32, 26)), ('L', (28, 30)), ('L', (28, 42))])
        path('beak', (36, 14), [('C', (42, 30), (42, 16), (42, 24)), ('L', (28, 30))])
        join('head', 'beak')
        dot('eye', (23, 17))
