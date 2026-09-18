"""Circular Alert Warning Icon: user-requested grid-fitted 32px version of circular-alert-warning-icon-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '0b7e0cf7-560e-4993-8784-f72f371c1d27'
SOURCE_PATH = 'pictographic-primitives/state/circle with exclamation mark_0b7e0cf7-560e-4993-8784-f72f371c1d27.svg'
SOLO_SOURCE_ICON_ID = 'circular-alert-warning-icon-solo'
AUTHOR = 'gpt-6'

class DrawingContainerSymbol(Sub32):
    icon_id = 'circular-alert-warning-icon-sub32-symbol'
    related_origin_icon_id = 'circular-alert-warning-icon-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/circular-alert-warning-icon-sub32'
    counterpart_icon_id = 'circular-alert-warning-icon-sub32'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'grid fitted', 'circular alert warning icon')

    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('stem', (16, 9), (16, 17))
        self.add_line('dot', (16, 23), (16, 23))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_anchor('center', (16, 16))
