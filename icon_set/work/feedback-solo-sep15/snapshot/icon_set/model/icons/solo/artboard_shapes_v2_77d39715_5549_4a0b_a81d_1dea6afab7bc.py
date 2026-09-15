"""Use a smaller rounded rectangle behind a larger bottom-right rounded rectangle. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '77d39715-5549-4a0b-a81d-1dea6afab7bc'
SOURCE_PATH = 'pictographic-primitives/design/artboard shapes_77d39715-5549-4a0b-a81d-1dea6afab7bc.svg'
AUTHOR = 'gpt-6'

class ArtboardShapesVariant2(Solo48):
    icon_id = 'artboard-shapes-v2'
    variant_of = 'artboard-shapes'
    variant_label = 'Use a smaller rounded rectangle behind a larger bottom-right rounded rectangle.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('artboard', 'shapes', 'design')

    def build(self):
        """Symbol plan: Use a smaller rounded rectangle behind a larger bottom-right rounded rectangle. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('back', (24, 16), [('L', (24, 10)), ('A', (20, 6), 4, 4, False), ('L', (10, 6)), ('A', (6, 10), 4, 4, False), ('L', (6, 26)), ('A', (10, 30), 4, 4, False), ('L', (16, 30))])
        path('front', (20, 16), [('L', (24, 16)), ('L', (38, 16)), ('A', (42, 20), 4, 4, True), ('L', (42, 38)), ('A', (38, 42), 4, 4, True), ('L', (20, 42)), ('A', (16, 38), 4, 4, True), ('L', (16, 30)), ('L', (16, 20)), ('A', (20, 16), 4, 4, True)], True)
        join('back', 'front')
