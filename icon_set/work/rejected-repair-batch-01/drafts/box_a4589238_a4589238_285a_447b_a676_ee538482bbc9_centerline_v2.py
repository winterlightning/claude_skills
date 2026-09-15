"""Raise the carton fold to give the pitched top more depth and align both shoulders symmetrically; keep the side gusset distinct.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a4589238-285a-447b-a676-ee538482bbc9'
SOURCE_PATH = 'pictographic-primitives/shipping/box_a4589238-285a-447b-a676-ee538482bbc9.svg'
AUTHOR = 'gpt-6'

class BoxA4589238(Solo48):
    icon_id = 'box-a4589238-centerline-v2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('box', 'shipping', 'solo-ai-next50')

    def build(self):

        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f'{name}-{index}'
                kind, end, *args = command
                if kind == 'L':
                    self.add_line(ident, here, end)
                elif kind == 'A':
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == 'C':
                    c1, c2 = args
                    self.add_bezier(ident, here, (c1, c2, end))
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)

        def circle(name, cx, cy, r):
            path(name, (cx - r, cy), [('A', (cx + r, cy), r, r, True), ('A', (cx - r, cy), r, r, True)], True)

        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0 + r, y0), [('L', (x1 - r, y0)), ('A', (x1, y0 + r), r, r, True), ('L', (x1, y1 - r)), ('A', (x1 - r, y1), r, r, True), ('L', (x0 + r, y1)), ('A', (x0, y1 - r), r, r, True), ('L', (x0, y0 + r)), ('A', (x0 + r, y0), r, r, True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a, b: self.relate('connect', a, b)
        poly('carton', (8, 16), (16, 4), (32, 4), (40, 16), (40, 44), (30, 44), (8, 44), closed=True)
        poly('fold', (8, 16), (30, 16), (40, 16))
        line('side', (30, 16), (30, 44))
        join('fold', 'carton')
        join('side', 'carton')
        join('side', 'fold')
    variant_of = 'box-a4589238'
    variant_label = 'Batch 01 centerline repair'
