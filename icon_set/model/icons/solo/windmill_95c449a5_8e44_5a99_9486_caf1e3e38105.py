"""Spread the windmill supports across a broad tapered building, center its entrance, and align the four sails around one hub. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '95c449a5-8e44-5a99-9486-caf1e3e38105'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/netherlands windmill_95c449a5-8e44-5a99-9486-caf1e3e38105.svg'
AUTHOR = 'gpt-6'

class Windmill(Solo48):
    icon_id = 'windmill'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    aliases = ()
    keywords = ('windmill', 'netherlands', 'dutch', 'mill', 'sails', 'landmark', 'countryside', 'energy')

    def build(self):
        """Symbol plan: Spread the windmill supports across a broad tapered building, center its entrance, and align the four sails around one hub. Reference: Lucide landmark: clean separated supports; no exact windmill reference."""

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
        poly('sail-a', (8, 4), (24, 12), (40, 20))
        poly('sail-b', (8, 20), (24, 12), (40, 4))
        join('sail-a', 'sail-b')
        poly('building', (16, 28), (32, 28), (36, 44), (24, 44), (12, 44), closed=True)
        line('door', (24, 36), (24, 44))
        join('door', 'building')
