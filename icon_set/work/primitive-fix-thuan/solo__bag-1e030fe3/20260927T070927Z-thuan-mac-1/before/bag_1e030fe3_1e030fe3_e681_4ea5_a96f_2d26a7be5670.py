"""Make the handle a broader shallow half-ellipse, center it within a taller body opening, and give the two lower bag corners matching radii. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1e030fe3-e681-4ea5-a96f-2d26a7be5670'
SOURCE_PATH = 'pictographic-primitives/shopping/bag_1e030fe3-e681-4ea5-a96f-2d26a7be5670.svg'
AUTHOR = 'gpt-6'

class Bag1e030fe3(Solo48):
    icon_id = 'bag-1e030fe3'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('solo-ai-refine', 'solo-ai-first50', 'bag-1e030fe3')

    def build(self):
        """Symbol plan: Make the handle a broader shallow half-ellipse, center it within a taller body opening, and give the two lower bag corners matching radii. Reference: Lucide shopping-bag: centered curved handle and coherent bag corners."""

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
        path('body', (8, 14), [('L', (16, 4)), ('L', (32, 4)), ('L', (40, 14)), ('L', (40, 40)), ('A', (36, 44), 4, 4, True), ('L', (12, 44)), ('A', (8, 40), 4, 4, True), ('L', (8, 14))], True)
        line('fold', (8, 14), (40, 14))
        join('fold', 'body')
        path('handle', (17, 25), [('A', (31, 25), 7, 5, False)])
