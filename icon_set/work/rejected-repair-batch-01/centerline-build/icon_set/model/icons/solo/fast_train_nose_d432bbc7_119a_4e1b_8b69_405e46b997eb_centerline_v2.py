"""Smooth the train nose into the lower body without its pointed turn, and align the front windscreen with the longer sloping roof.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd432bbc7-119a-4e1b-8b69-405e46b997eb'
SOURCE_PATH = 'pictographic-primitives/transportation/railroad fast train_d432bbc7-119a-4e1b-8b69-405e46b997eb.svg'
AUTHOR = 'gpt-6'

class FastTrainNose(Solo48):
    icon_id = 'fast-train-nose-centerline-v2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('fast train', 'high speed rail', 'bullet train', 'train', 'railway', 'rail', 'express', 'transport')

    def build(self):

        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L':
                    self.add_line(name, here, end)
                elif k == 'A':
                    self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C':
                    self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)

        def circle(n, x, y, r):
            path(n, (x - r, y), [('A', (x + r, y), r, r, True), ('A', (x - r, y), r, r, True)], True)

        def box(n, l, t, r, b, rad=4):
            path(n, (l + rad, t), [('L', (r - rad, t)), ('A', (r, t + rad), rad, rad, True), ('L', (r, b - rad)), ('A', (r - rad, b), rad, rad, True), ('L', (l + rad, b)), ('A', (l, b - rad), rad, rad, True), ('L', (l, t + rad)), ('A', (l + rad, t), rad, rad, True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a, b: self.relate('connect', a, b)
        path('body', (4, 8), [('L', (16, 8)), ('L', (24, 8)), ('C', (40, 20), (32, 8), (37, 15)), ('C', (36, 28), (43, 25), (41, 28)), ('L', (12, 28)), ('L', (4, 28))])
        poly('windscreen', (16, 8), (22, 20), (40, 20))
        join('windscreen', 'body')
        path('wheel', (12, 28), [('A', (12, 40), 6, 6, True), ('A', (12, 28), 6, 6, True)], True)
        join('wheel', 'body')
        poly('rail', (4, 40), (12, 40), (44, 40))
        join('rail', 'wheel')
    variant_of = 'fast-train-nose'
    variant_label = 'Batch 01 centerline repair'
