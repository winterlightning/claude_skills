"""Smiling Face with Closed Eyes on SYMBOL32.

Plan: Circular face with equal horizontal closed eyes and an elliptical smile. Lucide face-slightly-smiling informs spacing; source closed-eye direction is preserved.
Centerline extremes use the CIRCLE contract; all coordinates are authored at 32px.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = 'd4bfde85-9d9b-43bf-842d-9d3bc926de17'
SOURCE_PATH = 'published/gallery/combination-originals/d4bfde85-9d9b-43bf-842d-9d3bc926de17.svg'
AUTHOR = 'gpt-6'


class Drawing(Symbol32):
    icon_id = 'closed-eye-smiling-face-symbol32'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ('Smiling Face with Closed Eyes',)
    keywords = ('symbol', 'container content')

    def build(self):

        axis, radius = 16, 14
        self.add_arc('face-top', (axis-radius, axis), (axis+radius, axis), radius_x=radius)
        self.add_arc('face-bottom', (axis+radius, axis), (axis-radius, axis), radius_x=radius)
        self.add_contour('face', 'face-top', 'face-bottom', closed=True)
        for side in (-1, 1):
            x = axis + side * 5
            self.add_line(f'eye-{side}', (x-1, 11), (x+1, 11))
        self.add_arc('smile', (10, 19), (22, 19), radius_x=6, radius_y=4, sweep=False)
