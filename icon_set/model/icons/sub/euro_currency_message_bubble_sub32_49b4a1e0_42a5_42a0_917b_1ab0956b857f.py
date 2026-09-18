"""Euro Currency Message Bubble: user-requested grid-fitted 32px version of euro-currency-message-bubble-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='49b4a1e0-42a5-42a0-917b-1ab0956b857f'
SOURCE_PATH='pictographic-primitives/other/message euro sign lines_49b4a1e0-42a5-42a0-917b-1ab0956b857f.svg'
SOLO_SOURCE_ICON_ID='euro-currency-message-bubble-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='euro-currency-message-bubble-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/finance'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'euro currency message bubble')
    def build(self):
        self.add_line('top', (8, 2), (24, 2))
        self.add_arc('tr', (24, 2), (28, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('right', (28, 6), (28, 23))
        self.add_arc('br', (28, 23), (24, 27), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('bottom', (24, 27), (11, 27))
        self.add_line('tail', (11, 27), (4, 30))
        self.add_line('left', (4, 30), (4, 6))
        self.add_arc('tl', (4, 6), (8, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('currency-upper', (21, 9), (11, 14), radius_x=10, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('currency-lower', (11, 14), (21, 19), radius_x=10, radius_y=5, large_arc=False, sweep=False)
        self.add_line('bar', (11, 14), (18, 14))
        self.add_contour('outline', 'top', 'tr', 'right', 'br', 'bottom', 'tail', 'left', 'tl', closed=True)
        self.add_contour('currency', 'currency-upper', 'currency-lower', closed=False)
        self.relate('connect', 'currency', 'bar')
        self.add_anchor('center',(16, 16))
