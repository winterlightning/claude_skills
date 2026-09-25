"""Yen Currency Message Bubble: user-requested grid-fitted 32px version of yen-currency-message-bubble-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='16791ce0-2910-4e3b-82ee-8dcb1834e398'
SOURCE_PATH='pictographic-primitives/other/message yuan sign lines_16791ce0-2910-4e3b-82ee-8dcb1834e398.svg'
SOLO_SOURCE_ICON_ID='yen-currency-message-bubble-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='yen-currency-message-bubble-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'yen currency message bubble')
    def build(self):
        self.add_line('top', (9, 2), (23, 2))
        self.add_arc('tr', (23, 2), (28, 6), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_line('right', (28, 6), (28, 23))
        self.add_arc('br', (28, 23), (23, 27), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_line('bottom', (23, 27), (12, 27))
        self.add_line('tail', (12, 27), (4, 30))
        self.add_line('left', (4, 30), (4, 6))
        self.add_arc('tl', (4, 6), (9, 2), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_line('fork-1', (12, 9), (16, 14))
        self.add_line('fork-2', (16, 14), (20, 9))
        self.add_line('stem', (16, 14), (16, 19))
        self.add_line('bar', (12, 14), (20, 14))
        self.add_contour('outline', 'top', 'tr', 'right', 'br', 'bottom', 'tail', 'left', 'tl', closed=True)
        self.add_contour('fork', 'fork-1', 'fork-2', closed=False)
        self.relate('connect', 'fork', 'stem', 'bar')
        self.add_anchor('center',(16, 16))
