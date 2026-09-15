"""Move the string knot to the ball’s right edge and open the two curling runs; remove the stroke that doubled back along the ball.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6be7fb94-82a9-5934-b611-1bdbeceda224'
SOURCE_PATH = 'pictographic-primitives/pets/cat toy_6be7fb94-82a9-5934-b611-1bdbeceda224.svg'
AUTHOR = 'gpt-6'

class CatToy(Solo48):
    icon_id = 'cat-toy-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('cat', 'toy', 'pets', 'solo-ai-next100')
    variant_of = 'cat-toy'
    variant_label = 'Batch 01 centerline repair'

    def build(self):

        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, (kind, end, *args) in enumerate(commands):
                name = f'{n}-{j}'
                if kind == 'L':
                    self.add_line(name, here, end)
                elif kind == 'A':
                    self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C':
                    self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)

        def circle(n, x, y, r):
            path(n, (x - r, y), [('A', (x, y - r), r, r, True), ('A', (x + r, y), r, r, True), ('A', (x, y + r), r, r, True), ('A', (x - r, y), r, r, True)], True)

        def rounded(n, x0, y0, x1, y1, r):
            path(n, (x0 + r, y0), [('L', (x1 - r, y0)), ('A', (x1, y0 + r), r, r, True), ('L', (x1, y1 - r)), ('A', (x1 - r, y1), r, r, True), ('L', (x0 + r, y1)), ('A', (x0, y1 - r), r, r, True), ('L', (x0, y0 + r)), ('A', (x0 + r, y0), r, r, True)], True)
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        circle('ball', 16, 16, 10)
        path('string', (26, 16), [('C', (42, 24), (34, 16), (42, 18)), ('C', (30, 32), (42, 29), (35, 32)), ('C', (26, 42), (22, 32), (22, 42)), ('L', (30, 42))])
        join('ball', 'string')
