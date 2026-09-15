"""Recompose the bendable phone as a broad horizontal rectangle with smoothly bowed long edges. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd5e38ad3-3442-57ac-9e2b-af7bbe8cc090'
SOURCE_PATH = 'pictographic-primitives/technology/bendable phone_d5e38ad3-3442-57ac-9e2b-af7bbe8cc090.svg'
AUTHOR = 'gpt-6'

class BendablePhoneVariant2(Solo48):
    icon_id = 'bendable-phone-v2'
    variant_of = 'bendable-phone'
    variant_label = 'Recompose the bendable phone as a broad horizontal rectangle with smoothly bowed long edges.'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('phone', 'bendable', 'flexible', 'smartphone', 'mobile', 'device', 'foldable')

    def build(self):
        """Symbol plan: Recompose the bendable phone as a broad horizontal rectangle with smoothly bowed long edges. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('body', (8, 8), [('C', (40, 8), (17, 16), (31, 16)), ('A', (44, 12), 4, 4, True), ('L', (44, 36)), ('A', (40, 40), 4, 4, True), ('C', (8, 40), (31, 32), (17, 32)), ('A', (4, 36), 4, 4, True), ('L', (4, 12)), ('A', (8, 8), 4, 4, True)], True)
        line('slot', (33, 22), (33, 26))
