"""Replace the short stem mark with a pointed curved leaf and rebalance the fruit below it. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5fa35e01-b249-40d5-bda3-cb10017713e9'
SOURCE_PATH = 'pictographic-primitives/logos/ios logo 2_5fa35e01-b249-40d5-bda3-cb10017713e9.svg'
AUTHOR = 'gpt-6'

class AppleLogoVariant2(Solo48):
    icon_id = 'apple-logo-v2'
    variant_of = 'apple-logo'
    variant_label = 'Replace the short stem mark with a pointed curved leaf and rebalance the fruit below it.'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('apple', 'ios', 'mac', 'fruit', 'logo', 'brand', 'technology')

    def build(self):
        """Symbol plan: Replace the short stem mark with a pointed curved leaf and rebalance the fruit below it. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('leaf', (14, 12), [('C', (34, 4), (14, 4), (24, 4)), ('C', (14, 12), (34, 12), (24, 12))], True)
        path('fruit', (40, 24), [('C', (24, 22), (34, 18), (29, 24)), ('C', (8, 28), (16, 18), (8, 21)), ('C', (18, 44), (8, 36), (13, 44)), ('C', (24, 42), (21, 44), (22, 42)), ('C', (30, 44), (26, 42), (28, 44)), ('C', (40, 34), (36, 44), (39, 38)), ('C', (40, 24), (30, 32), (31, 26))], True)
