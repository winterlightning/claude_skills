"""Redraw the torii with a smooth upturned roof, two evenly placed posts, and a wider vertical opening between its two horizontal beams. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '32e3b1cc-fbf3-4478-858a-ce86e17b4058'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/shrine of itsukushima_32e3b1cc-fbf3-4478-858a-ce86e17b4058.svg'
AUTHOR = 'gpt-6'

class ItsukushimaToriiGate(Solo48):
    icon_id = 'itsukushima-torii-gate'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    categories = ('landmarks', 'primitives')
    aliases = ()
    keywords = ('itsukushima', 'torii', 'gate', 'shrine', 'japan', 'shinto', 'miyajima', 'landmark')

    def build(self):
        """Symbol plan: Redraw the torii with a smooth upturned roof, two evenly placed posts, and a wider vertical opening between its two horizontal beams. Reference: Lucide landmark: paired posts; deliberate upturned torii roof."""

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
        path('roof', (4, 8), [('C', (12, 12), (4, 11), (8, 12)), ('L', (36, 12)), ('C', (44, 8), (40, 12), (44, 11))])
        poly('beam', (4, 24), (12, 24), (36, 24), (44, 24))
        for side, x in [('left', 12), ('right', 36)]:
            poly(side, (x, 12), (x, 24), (x, 40))
            join(side, 'roof')
            join(side, 'beam')
