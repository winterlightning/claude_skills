"""Round the roof, windscreen slope and lower body corners consistently. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '67545933-613d-5320-bb66-9887235b5423'
SOURCE_PATH = 'pictographic-primitives/recreation/camping rv_67545933-613d-5320-bb66-9887235b5423.svg'
AUTHOR = 'gpt-6'

class CamperVan(Solo48):
    icon_id = 'camper-van'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/recreation'
    aliases = ()
    keywords = ('camper', 'van')

    def build(self):
        """Symbol plan: Round the roof, windscreen slope and lower body corners consistently. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('body', (9, 35), [('L', (8, 35)), ('A', (4, 31), 4, 4, True), ('L', (4, 12)), ('A', (8, 8), 4, 4, True), ('L', (28, 8)), ('C', (34, 11), (31, 8), (33, 9)), ('L', (42, 21)), ('C', (44, 27), (43, 23), (44, 25)), ('L', (44, 31)), ('A', (40, 35), 4, 4, True), ('L', (39, 35))])
        for n, x in [('rear', 14), ('front', 34)]:
            oval(n, x, 35, 5, 5)
            join('body', n)
        line('sill', (19, 35), (29, 35))
        join('sill', 'rear')
        join('sill', 'front')
        line('window', (13, 20), (23, 20))
