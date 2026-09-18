"""Money Message Bubble: user-requested grid-fitted 32px version of money-message-bubble-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='93c99818-8211-47c5-bf92-9fa83e3cab72'
SOURCE_PATH='pictographic-primitives/other/message dollar sign lines_93c99818-8211-47c5-bf92-9fa83e3cab72.svg'
SOLO_SOURCE_ICON_ID='money-message-bubble-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='money-message-bubble-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/finance'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'money message bubble')
    def build(self):
        self.add_line('top', (9, 2), (23, 2))
        self.add_arc('tr', (23, 2), (28, 6), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_line('right', (28, 6), (28, 21))
        self.add_arc('br', (28, 21), (23, 27), radius_x=5, radius_y=6, large_arc=False, sweep=True)
        self.add_line('bottom', (23, 27), (12, 27))
        self.add_line('tail', (12, 27), (4, 30))
        self.add_line('left', (4, 30), (4, 6))
        self.add_arc('tl', (4, 6), (9, 2), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_line('currency-top', (20, 11), (16, 11))
        self.add_arc('currency-upper', (16, 11), (16, 15), radius_x=4, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('currency-lower', (16, 15), (16, 19), radius_x=4, radius_y=2, large_arc=False, sweep=True)
        self.add_line('currency-foot', (16, 19), (12, 19))
        self.add_line('stem-top', (16, 9), (16, 11))
        self.add_line('stem-bottom', (16, 19), (16, 21))
        self.add_contour('outline', 'top', 'tr', 'right', 'br', 'bottom', 'tail', 'left', 'tl', closed=True)
        self.add_contour('currency', 'currency-top', 'currency-upper', 'currency-lower', 'currency-foot', closed=False)
        self.relate('connect', 'currency', 'stem-top')
        self.relate('connect', 'currency', 'stem-bottom')
        self.add_anchor('center',(16, 16))
