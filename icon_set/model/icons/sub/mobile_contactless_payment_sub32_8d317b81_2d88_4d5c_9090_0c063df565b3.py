"""Mobile Contactless Payment: user-requested grid-fitted 32px version of mobile-contactless-payment-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='8d317b81-2d88-4d5c-9090-0c063df565b3'
SOURCE_PATH='pictographic-primitives/other/mobile phone dollar sign wireless_8d317b81-2d88-4d5c-9090-0c063df565b3.svg'
SOLO_SOURCE_ICON_ID='mobile-contactless-payment-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='mobile-contactless-payment-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/finance'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'mobile contactless payment')
    def build(self):
        self.add_bezier('signal', (4, 6), ((8, 3), (12, 2), (16, 2)), ((20, 2), (24, 3), (28, 6)))
        self.add_line('left', (4, 13), (4, 26))
        self.add_arc('bl', (4, 26), (9, 30), radius_x=5, radius_y=4, large_arc=False, sweep=False)
        self.add_line('bottom', (9, 30), (23, 30))
        self.add_arc('br', (23, 30), (28, 26), radius_x=5, radius_y=4, large_arc=False, sweep=False)
        self.add_line('right', (28, 26), (28, 13))
        self.add_line('currency-top', (20, 13), (16, 13))
        self.add_arc('currency-upper', (16, 13), (16, 17), radius_x=4, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('currency-lower', (16, 17), (16, 21), radius_x=4, radius_y=2, large_arc=False, sweep=True)
        self.add_line('currency-foot', (16, 21), (12, 21))
        self.add_line('stem-top', (16, 11), (16, 13))
        self.add_line('stem-bottom', (16, 21), (16, 23))
        self.add_contour('phone', 'left', 'bl', 'bottom', 'br', 'right', closed=False)
        self.add_contour('currency', 'currency-top', 'currency-upper', 'currency-lower', 'currency-foot', closed=False)
        self.relate('connect', 'currency', 'stem-top')
        self.relate('connect', 'currency', 'stem-bottom')
        self.add_anchor('center',(16, 16))
