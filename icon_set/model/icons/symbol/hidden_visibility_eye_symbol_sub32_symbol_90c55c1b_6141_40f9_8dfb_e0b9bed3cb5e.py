"""Hidden Visibility Eye Symbol: user-requested grid-fitted 32px version of hidden-visibility-eye-symbol-solo.
Plan: retain source primitive/contour topology and fit HRECT_XL ink (0, 2, 32, 30).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '90c55c1b-6141-40f9-8dfb-e0b9bed3cb5e'
SOURCE_PATH = 'pictographic-primitives/other/eye slash_90c55c1b-6141-40f9-8dfb-e0b9bed3cb5e.svg'
SOLO_SOURCE_ICON_ID = 'hidden-visibility-eye-symbol-solo'
AUTHOR = 'gpt-6'

class DrawingContainerSymbol(Sub32):
    icon_id = 'hidden-visibility-eye-symbol-sub32-symbol'
    related_origin_icon_id = 'hidden-visibility-eye-symbol-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/hidden-visibility-eye-symbol-sub32'
    counterpart_icon_id = 'hidden-visibility-eye-symbol-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    tags = ('sub icon',)
    keywords = ('sub icon', 'grid fitted', 'hidden visibility eye symbol')

    def build(self):
        self.add_bezier('upper', (2, 16), ((9, 0), (23, 0), (30, 16)))
        self.add_bezier('lower', (30, 16), ((23, 32), (9, 32), (2, 16)))
        self.add_line('slash', (6, 28), (26, 4))
        self.add_contour('eye', 'upper', 'lower', closed=True)
        self.relate('connect', 'eye', 'slash')
        self.add_anchor('center', (16, 16))
