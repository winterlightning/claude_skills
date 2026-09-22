"""Simple Smiling Face on SYMBOL32.

Plan: Circular face, mirrored short upright eyes, one shallow smile. Lucide face-slightly-smiling informs separated facial marks; no body is present.
Centerline extremes use the CIRCLE contract; all coordinates are authored at 32px.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '89fbe59a-21d5-4c1c-b815-db67a6781259'
SOURCE_PATH = 'published/gallery/combination-originals/89fbe59a-21d5-4c1c-b815-db67a6781259.svg'
AUTHOR = 'gpt-6'


class Drawing(Symbol32):
    icon_id = 'simple-smiling-face-symbol32'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ('Simple Smiling Face',)
    keywords = ('symbol', 'container content')

    def build(self):

        axis, radius = 16, 14
        self.add_arc('face-top', (axis-radius, axis), (axis+radius, axis), radius_x=radius)
        self.add_arc('face-bottom', (axis+radius, axis), (axis-radius, axis), radius_x=radius)
        self.add_contour('face', 'face-top', 'face-bottom', closed=True)
        for side in (-1, 1):
            x = axis + side * 5
            self.add_line(f'eye-{side}', (x, 11), (x, 12))
        self.add_arc('smile', (10, 20), (22, 20), radius_x=6, radius_y=3, sweep=False)
