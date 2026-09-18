"""Mobile Wireless Pound Payment: user-requested grid-fitted 32px version of mobile-wireless-pound-payment-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='3ebbbe60-66ff-4346-a1c8-9367527d9ea9'
SOURCE_PATH='pictographic-primitives/other/mobile phone pound sign wireless_3ebbbe60-66ff-4346-a1c8-9367527d9ea9.svg'
SOLO_SOURCE_ICON_ID='mobile-wireless-pound-payment-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='mobile-wireless-pound-payment-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/finance'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'mobile wireless pound payment')
    def build(self):
        self.add_bezier('signal', (4, 6), ((8, 3), (12, 2), (16, 2)), ((20, 2), (24, 3), (28, 6)))
        self.add_line('left', (4, 12), (4, 26))
        self.add_arc('bl', (4, 26), (8, 30), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('bottom', (8, 30), (24, 30))
        self.add_arc('br', (24, 30), (28, 26), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('right', (28, 26), (28, 12))
        self.add_arc('currency-hook', (20, 16), (14, 16), radius_x=3, radius_y=2, large_arc=False, sweep=False)
        self.add_line('currency-stem-upper', (14, 16), (14, 18))
        self.add_line('currency-stem-lower', (14, 18), (14, 24))
        self.add_line('currency-foot', (14, 24), (18, 24))
        self.add_line('currency-bar-1', (13, 18), (14, 18))
        self.add_line('currency-bar-2', (14, 18), (17, 18))
        self.add_contour('phone', 'left', 'bl', 'bottom', 'br', 'right', closed=False)
        self.add_contour('currency', 'currency-hook', 'currency-stem-upper', 'currency-stem-lower', 'currency-foot', closed=False)
        self.add_contour('currency-bar', 'currency-bar-1', 'currency-bar-2', closed=False)
        self.relate('connect', 'currency', 'currency-bar')
        self.add_anchor('center',(16, 16))
