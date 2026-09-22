"""Simple Heart Love Symbol on SYMBOL32.

Plan: Paired circular lobes join tangent circular shoulders, then converge at a shared tip. Lucide heart informs smooth lobe-to-side flow.
Centerline extremes use the HRECT_XL contract; all coordinates are authored at 32px.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '0104273d-3559-4788-a337-c2575e324bb8'
SOURCE_PATH = 'published/gallery/combination-originals/0104273d-3559-4788-a337-c2575e324bb8.svg'
AUTHOR = 'gpt-6'


class Drawing(Symbol32):
    icon_id = 'simple-heart-symbol32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ('Simple Heart Love Symbol',)
    keywords = ('symbol', 'container content')

    def build(self):

        axis, lobe_radius, shoulder_radius = 16, 7, 10
        self.add_arc('left-lobe', (axis, 11), (2, 11), radius_x=lobe_radius, sweep=False)
        self.add_arc('left-shoulder', (2, 11), (6, 19), radius_x=shoulder_radius, sweep=False)
        self.add_line('left-tip', (6, 19), (axis, 28))
        self.add_line('right-tip', (axis, 28), (2 * axis - 6, 19))
        self.add_arc('right-shoulder', (26, 19), (30, 11), radius_x=shoulder_radius, sweep=False)
        self.add_arc('right-lobe', (30, 11), (axis, 11), radius_x=lobe_radius, sweep=False)
        self.add_contour('heart', 'left-lobe', 'left-shoulder', 'left-tip', 'right-tip', 'right-shoulder', 'right-lobe', closed=True)
