"""Wireless Mobile Yuan Payment: user-requested grid-fitted 32px version of wireless-mobile-yuan-payment-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='54325bec-9e76-47f3-ae84-9ced16fe0a3a'
SOURCE_PATH='pictographic-primitives/other/mobile phone yuan sign wireless_54325bec-9e76-47f3-ae84-9ced16fe0a3a.svg'
SOLO_SOURCE_ICON_ID='wireless-mobile-yuan-payment-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='wireless-mobile-yuan-payment-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'wireless mobile yuan payment')
    def build(self):
        self.add_bezier('signal', (4, 6), ((8, 3), (12, 2), (16, 2)), ((20, 2), (24, 3), (28, 6)))
        self.add_line('left', (4, 13), (4, 26))
        self.add_arc('bl', (4, 26), (9, 30), radius_x=5, radius_y=4, large_arc=False, sweep=False)
        self.add_line('bottom', (9, 30), (23, 30))
        self.add_arc('br', (23, 30), (28, 26), radius_x=5, radius_y=4, large_arc=False, sweep=False)
        self.add_line('right', (28, 26), (28, 13))
        self.add_line('currency-fork-1', (12, 15), (16, 19))
        self.add_line('currency-fork-2', (16, 19), (20, 15))
        self.add_line('currency-stem-1', (16, 19), (16, 20))
        self.add_line('currency-stem-2', (16, 20), (16, 23))
        self.add_line('currency-bar-1', (13, 20), (16, 20))
        self.add_line('currency-bar-2', (16, 20), (19, 20))
        self.add_contour('phone', 'left', 'bl', 'bottom', 'br', 'right', closed=False)
        self.add_contour('currency-fork', 'currency-fork-1', 'currency-fork-2', closed=False)
        self.add_contour('currency-stem', 'currency-stem-1', 'currency-stem-2', closed=False)
        self.add_contour('currency-bar', 'currency-bar-1', 'currency-bar-2', closed=False)
        self.relate('connect', 'currency-fork', 'currency-stem')
        self.relate('connect', 'currency-stem', 'currency-bar')
        self.add_anchor('center',(16, 16))
