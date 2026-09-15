"""Rebuild the cannon carriage as a separate block and axle beneath a consistent tube; open all wheel and body clearances.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '63675998-808b-5a45-8289-50d26d3668d5'
SOURCE_PATH = 'pictographic-primitives/war/modern weapon cannon_63675998-808b-5a45-8289-50d26d3668d5.svg'
AUTHOR = 'gpt-6'

class CannonBlockCarriage(Solo48):
    icon_id = 'cannon-block-carriage-centerline-v2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('cannon', 'barrel', 'artillery', 'carriage', 'wheel', 'weapon')
    variant_of = 'cannon-block-carriage'
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
        poly('barrel', (4, 8), (44, 8), (44, 16), (8, 16), (4, 16), closed=True)
        poly('block', (4, 24), (8, 24), (12, 24), (12, 32), (12, 40), (4, 40), closed=True)
        circle('wheel', 28, 32, 8)
        line('axle', (12, 32), (20, 32))
        join('axle', 'block')
        join('axle', 'wheel')
        line('support', (8, 16), (8, 24))
        join('support', 'block')
        join('support', 'barrel')
