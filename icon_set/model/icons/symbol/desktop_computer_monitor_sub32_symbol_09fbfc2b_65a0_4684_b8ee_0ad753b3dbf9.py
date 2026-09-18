"""Desktop Computer Monitor: user-requested grid-fitted 32px version of desktop-computer-monitor-solo.
Plan: retain source primitive/contour topology and fit HRECT_XL ink (0, 2, 32, 30).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '09fbfc2b-65a0-4684-b8ee-0ad753b3dbf9'
SOURCE_PATH = 'pictographic-primitives/computers/batch-02/monitor_09fbfc2b-65a0-4684-b8ee-0ad753b3dbf9.svg'
SOLO_SOURCE_ICON_ID = 'desktop-computer-monitor-solo'
AUTHOR = 'gpt-6'

class DrawingContainerSymbol(Sub32):
    icon_id = 'desktop-computer-monitor-sub32-symbol'
    related_origin_icon_id = 'desktop-computer-monitor-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/desktop-computer-monitor-sub32'
    counterpart_icon_id = 'desktop-computer-monitor-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'grid fitted', 'desktop computer monitor')

    def build(self):
        self.add_line('screen-0', (5, 4), (27, 4))
        self.add_arc('screen-1', (27, 4), (30, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('screen-2', (30, 7), (30, 18))
        self.add_arc('screen-3', (30, 18), (27, 20), radius_x=3, radius_y=2, large_arc=False, sweep=True)
        self.add_line('screen-4', (27, 20), (5, 20))
        self.add_arc('screen-5', (5, 20), (2, 18), radius_x=3, radius_y=2, large_arc=False, sweep=True)
        self.add_line('screen-6', (2, 18), (2, 7))
        self.add_arc('screen-7', (2, 7), (5, 4), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('divider', (2, 12), (30, 12))
        self.add_line('stand-1', (13, 20), (12, 28))
        self.add_line('stand-2', (12, 28), (20, 28))
        self.add_line('stand-3', (20, 28), (19, 20))
        self.add_contour('screen', 'screen-0', 'screen-1', 'screen-2', 'screen-3', 'screen-4', 'screen-5', 'screen-6', 'screen-7', closed=True)
        self.add_contour('stand', 'stand-1', 'stand-2', 'stand-3', closed=False)
        self.relate('connect', 'screen', 'divider')
        self.relate('connect', 'screen', 'stand')
        self.add_anchor('center', (16, 16))
