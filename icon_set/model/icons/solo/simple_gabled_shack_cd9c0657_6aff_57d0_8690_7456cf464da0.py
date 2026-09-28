"""Redraw the roof as two clean slopes and widen the hut body with matching lower corners; make the doorway one longer centered vertical stroke. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cd9c0657-6aff-57d0-8690-7456cf464da0'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/shanty house_cd9c0657-6aff-57d0-8690-7456cf464da0.svg'
AUTHOR = 'gpt-6'

class SimpleGabledShack(Solo48):
    icon_id = 'simple-gabled-shack'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    categories = ('landmarks', 'state')
    aliases = ()
    keywords = ('shack', 'house', 'home', 'shanty', 'hut', 'dwelling', 'shelter', 'gable')

    def build(self):
        """Symbol plan: Redraw the roof as two clean slopes and widen the hut body with matching lower corners; make the doorway one longer centered vertical stroke. Reference: Lucide house: straight roof slopes and a centered entrance."""

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
        poly('roof', (6, 20), (10, 17), (24, 6), (38, 17), (42, 20))
        path('walls', (10, 17), [('L', (10, 38)), ('A', (14, 42), 4, 4, False), ('L', (24, 42)), ('L', (34, 42)), ('A', (38, 38), 4, 4, False), ('L', (38, 17))])
        line('door', (24, 42), (24, 28))
        join('walls', 'roof')
        join('door', 'walls')
