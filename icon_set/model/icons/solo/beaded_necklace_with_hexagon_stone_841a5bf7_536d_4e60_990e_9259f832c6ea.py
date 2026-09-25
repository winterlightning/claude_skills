"""Simplify the necklace to three dot beads, paired curved chain sections, and one hexagonal pendant. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '841a5bf7-536d-4e60-990e-9259f832c6ea'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/necklace stone_841a5bf7-536d-4e60-990e-9259f832c6ea.svg'
AUTHOR = 'gpt-6'

class BeadedNecklaceWithHexagonStone(Solo48):
    icon_id = 'beaded-necklace-with-hexagon-stone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('necklace', 'bead', 'stone', 'hexagon', 'gem', 'jewellery', 'jewelry', 'pendant', 'accessory')

    def build(self):
        """Symbol plan: Simplify the necklace to three dot beads, paired curved chain sections, and one hexagonal pendant. Reference: Lucide gem: minimal faceted perimeter."""

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
        for x in (6, 24, 42):
            dot(f'bead-{x}', (x, 6))
        path('chain-left', (6, 16), [('A', (16, 30), 10, 14, False)])
        path('chain-right', (42, 16), [('A', (32, 30), 10, 14, True)])
        poly('stone', (24, 26), (32, 30), (32, 38), (24, 42), (16, 38), (16, 30), closed=True)
        join('chain-left', 'stone')
        join('chain-right', 'stone')
