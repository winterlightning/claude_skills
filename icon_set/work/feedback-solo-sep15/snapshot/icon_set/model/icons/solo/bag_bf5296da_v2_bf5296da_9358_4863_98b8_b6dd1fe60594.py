"""Shorten the carry handle and raise the bag top to create a taller body. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bf5296da-9358-4863-98b8-b6dd1fe60594'
SOURCE_PATH = 'pictographic-primitives/photography/bag_bf5296da-9358-4863-98b8-b6dd1fe60594.svg'
AUTHOR = 'gpt-6'

class BagBf5296daVariant2(Solo48):
    icon_id = 'bag-bf5296da-v2'
    variant_of = 'bag-bf5296da'
    variant_label = 'Shorten the carry handle and raise the bag top to create a taller body.'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('solo-ai-refine', 'solo-ai-first50', 'bag-bf5296da')

    def build(self):
        """Symbol plan: Shorten the carry handle and raise the bag top to create a taller body. Reference: inspected current parent; no useful exact Lucide match selected."""

        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f'{name}-{index}'
                kind, end, *args = command
                if kind == 'L':
                    self.add_line(ident, here, end)
                elif kind == 'A':
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == 'C':
                    c1, c2 = args
                    self.add_bezier(ident, here, (c1, c2, end))
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)

        def circle(name, cx, cy, r):
            path(name, (cx - r, cy), [('A', (cx + r, cy), r, r, True), ('A', (cx - r, cy), r, r, True)], True)

        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0 + r, y0), [('L', (x1 - r, y0)), ('A', (x1, y0 + r), r, r, True), ('L', (x1, y1 - r)), ('A', (x1 - r, y1), r, r, True), ('L', (x0 + r, y1)), ('A', (x0, y1 - r), r, r, True), ('L', (x0, y0 + r)), ('A', (x0 + r, y0), r, r, True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a, b: self.relate('connect', a, b)
        path('handle', (18, 16), [('L', (18, 10)), ('A', (30, 10), 6, 6, True), ('L', (30, 16))])
        poly('body', (12, 16), (18, 16), (30, 16), (36, 16), (40, 44), (8, 44), closed=True)
        join('body', 'handle')
