"""Open the Hutt’s tail curl into a broader upward stroke and lengthen the mouth; keep the round head and seated silhouette.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8d9dbd78-bcd2-586d-9f37-3e76d77e8447'
SOURCE_PATH = 'pictographic-primitives/science/hutt_8d9dbd78-bcd2-586d-9f37-3e76d77e8447.svg'
AUTHOR = 'gpt-6'

class HuttCreature(Solo48):
    icon_id = 'hutt-creature-centerline-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/science'
    aliases = ()
    keywords = ('hutt', 'alien', 'slug', 'creature', 'tail', 'fiction')

    def segments(self, name, *points):
        for i, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f'{name}-{i}', a, b)

    def circle(self, name, x, y, r):
        points = [(x - r, y), (x, y - r), (x + r, y), (x, y + r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i + 1) % 4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('head', (20, 24), (40, 24), radius_x=10, radius_y=16)
        self.add_arc('back', (40, 24), (44, 32), radius_x=4, radius_y=8)
        self.add_arc('belly-corner', (44, 32), (36, 40), radius_x=8)
        self.add_line('belly', (36, 40), (12, 40))
        self.add_arc('tail-bottom', (12, 40), (4, 32), radius_x=8)
        self.add_line('tail-tip', (4, 32), (4, 28))
        self.add_bezier('tail-curl', (4, 28), ((10, 30), (20, 32), (20, 24)))
        self.add_contour('body', 'head', 'back', 'belly-corner', 'belly', 'tail-bottom', 'tail-tip', 'tail-curl', closed=True)
        self.add_line('eyes', (29, 19), (31, 19))
        self.add_line('mouth', (28, 28), (32, 28))
    variant_of = 'hutt-creature'
    variant_label = 'Batch 01 centerline repair'
