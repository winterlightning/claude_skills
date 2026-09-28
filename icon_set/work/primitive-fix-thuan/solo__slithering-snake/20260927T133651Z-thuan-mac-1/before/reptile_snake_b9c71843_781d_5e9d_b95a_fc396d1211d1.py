"""Rebuild the snake with a larger round head, a short forked tongue and two generous S-bends with tangent straight runs. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b9c71843-781d-5e9d-b95a-fc396d1211d1'
SOURCE_PATH = 'pictographic-primitives/animals/reptile snake_b9c71843-781d-5e9d-b95a-fc396d1211d1.svg'
AUTHOR = 'gpt-6'

class SlitheringSnake(Solo48):
    icon_id = 'slithering-snake'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('snake', 'slither', 'serpent', 'reptile', 'zigzag', 'coil', 'python', 'wild')

    def build(self):
        """Symbol plan: Rebuild the snake with a larger round head, a short forked tongue and two generous S-bends with tangent straight runs. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        oval('head', 30, 12, 6, 6)
        path('body', (24, 12), [('L', (14, 12)), ('A', (14, 26), 8, 7, False), ('L', (28, 26)), ('A', (28, 42), 8, 8, True), ('L', (12, 42))])
        join('head', 'body')
        line('tongue', (36, 12), (38, 12))
        poly('fork', (42, 8), (38, 12), (42, 16))
        join('head', 'tongue')
        join('tongue', 'fork')
