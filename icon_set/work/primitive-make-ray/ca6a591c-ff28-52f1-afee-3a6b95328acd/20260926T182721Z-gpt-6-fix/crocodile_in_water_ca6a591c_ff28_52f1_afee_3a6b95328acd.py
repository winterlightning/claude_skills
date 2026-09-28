"""Simplify the crocodile snout to one horizontal stroke and keep a low toothed back above the water. Applied to the original icon identity."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ca6a591c-ff28-52f1-afee-3a6b95328acd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crocodile-in-water/20260926T182517Z-thuan-mac-1/reference/reptile crocodile water_ca6a591c-ff28-52f1-afee-3a6b95328acd.svg'
AUTHOR = "gpt-6"

class CrocodileInWater(Solo48):
    icon_id = 'crocodile-in-water'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('crocodile', 'alligator', 'water', 'swim', 'river', 'reptile', 'waves', 'submerged')

    def build(self):
        """Symbol plan: Simplify the crocodile snout to one horizontal stroke and keep a low toothed back above the water. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        poly('back', (4, 18), (8, 14), (12, 18), (18, 18))
        path('brow', (18, 18), [('A', (36, 18), 9, 10, True), ('L', (44, 18)), ('L', (38, 24))])
        join('back', 'brow')
        dot('eye', (27, 18))
        path('water', (4, 36), [('A', (18, 36), 7, 4, False), ('A', (30, 36), 6, 4, False), ('A', (44, 36), 7, 4, False)])
