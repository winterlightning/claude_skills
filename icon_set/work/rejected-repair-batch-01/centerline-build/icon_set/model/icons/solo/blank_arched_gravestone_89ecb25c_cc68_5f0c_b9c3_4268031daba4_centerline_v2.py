"""Broaden the gravestone shoulders and reduce the oversized base projection; join the arched crown and straight walls as one continuous contour.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '89ecb25c-cc68-5f0c-b9c3-4268031daba4'
SOURCE_PATH = 'pictographic-primitives/war/death grave_89ecb25c-cc68-5f0c-b9c3-4268031daba4.svg'
AUTHOR = 'gpt-6'

class BlankArchedGravestone(Solo48):
    icon_id = 'blank-arched-gravestone-centerline-v2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('gravestone', 'grave', 'tombstone', 'memorial', 'cemetery', 'stone')
    variant_of = 'blank-arched-gravestone'
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
        path('stone', (10, 36), [('L', (10, 18)), ('A', (24, 4), 14, 14, True), ('A', (38, 18), 14, 14, True), ('L', (38, 36))])
        poly('plinth', (8, 36), (10, 36), (38, 36), (40, 36), (40, 44), (8, 44), closed=True)
        join('stone', 'plinth')
