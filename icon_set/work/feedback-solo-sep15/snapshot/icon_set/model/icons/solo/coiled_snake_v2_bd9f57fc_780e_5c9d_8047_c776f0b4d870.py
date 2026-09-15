"""Rebuild the snake as a clear open coil with a broad rounded head. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bd9f57fc-780e-5c9d-8047-c776f0b4d870'
SOURCE_PATH = 'pictographic-primitives/animals/reptile snake_bd9f57fc-780e-5c9d-8047-c776f0b4d870.svg'
AUTHOR = 'gpt-6'

class CoiledSnakeVariant2(Solo48):
    icon_id = 'coiled-snake-v2'
    variant_of = 'coiled-snake'
    variant_label = 'Rebuild the snake as a clear open coil with a broad rounded head.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('snake', 'coil', 'spiral', 'serpent', 'reptile', 'curl', 'python', 'wild')

    def build(self):
        """Symbol plan: Rebuild the snake as a clear open coil with a broad rounded head. Reference: Lucide shell: coherent spiral strokes."""

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
        path('coil', (18, 36), [('A', (6, 24), 12, 12, True), ('A', (24, 6), 18, 18, True), ('A', (42, 24), 18, 18, True), ('L', (42, 34)), ('A', (34, 42), 8, 8, True), ('A', (26, 34), 8, 8, True), ('L', (26, 25))])
        path('head', (26, 25), [('A', (34, 17), 8, 8, True), ('L', (39, 17))])
        join('head', 'coil')
