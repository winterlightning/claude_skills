"""Circular Check Mark Symbol: user-requested grid-fitted 32px version of circular-check-mark-symbol-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e827e098-b2c1-4c9d-a347-ed197ce977ef'
SOURCE_PATH = 'pictographic-primitives/other/circle check 1_e827e098-b2c1-4c9d-a347-ed197ce977ef.svg'
SOLO_SOURCE_ICON_ID = 'circular-check-mark-symbol-solo'
AUTHOR = 'gpt-6'

class DrawingContainerSymbol(Sub32):
    icon_id = 'circular-check-mark-symbol-sub32-symbol'
    related_origin_icon_id = 'circular-check-mark-symbol-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/circular-check-mark-symbol-sub32'
    counterpart_icon_id = 'circular-check-mark-symbol-sub32'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'grid fitted', 'circular check mark symbol')

    def build(self):
        self.add_arc('open-circle', (30, 16), (16, 2), radius_x=14, radius_y=14, large_arc=True, sweep=True)
        self.add_line('check-1', (10, 15), (16, 21))
        self.add_line('check-2', (16, 21), (27, 9))
        self.add_contour('check', 'check-1', 'check-2', closed=False)
        self.add_anchor('center', (16, 16))
