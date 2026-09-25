"""Spread the amphitheater into a broad horseshoe, with flatter concentric elliptical rows and longer vertical ends. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2baf247e-0126-4274-99c5-a0211405791f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/amfitheater in delphi top_2baf247e-0126-4274-99c5-a0211405791f.svg'
AUTHOR = 'gpt-6'

class AmfitheaterInDelphiTop(Solo48):
    icon_id = 'amfitheater-in-delphi-top'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('amfitheater', 'in', 'delphi', 'top', '_uncategorized_03', 'solo-ai-first50')

    def build(self):
        """Symbol plan: Spread the amphitheater into a broad horseshoe, with flatter concentric elliptical rows and longer vertical ends. Reference: Lucide landmark: centered architectural geometry; deliberate horizontal ellipse."""

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
        path('seats', (4, 40), [('L', (4, 24)), ('A', (44, 24), 20, 16, True), ('L', (44, 40)), ('L', (35, 40)), ('L', (35, 24)), ('A', (13, 24), 11, 7, False), ('L', (13, 40)), ('L', (4, 40))], True)
