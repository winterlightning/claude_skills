"""Wave-bottom dam alternative: add three equal wave sections along the base. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f9f457f4-66e4-4c02-af5b-93edb4742bbd'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/water dam_f9f457f4-66e4-4c02-af5b-93edb4742bbd.svg'
AUTHOR = 'gpt-6'

class CurvedDamWall(Solo48):
    icon_id = 'curved-dam-wall'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    aliases = ()
    keywords = ('dam', 'wall', 'water', 'reservoir', 'barrier', 'spillway', 'infrastructure', 'river')

    def build(self):
        """Symbol plan: Wave-bottom dam alternative: add three equal wave sections along the base. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        poly('wall', (4, 34), (4, 8), (14, 8), (14, 16), (34, 16), (34, 8), (44, 8), (44, 34))
        path('water', (44, 34), [('A', (30, 34), 7, 6, True), ('A', (18, 34), 6, 6, True), ('A', (4, 34), 7, 6, True)])
        join('wall', 'water')
