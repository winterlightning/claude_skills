"""Mobile Contactless Euro Payment: user-requested grid-fitted 32px version of mobile-contactless-euro-payment-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='70f23b14-d195-42bb-8255-807a7adba23b'
SOURCE_PATH='pictographic-primitives/other/mobile phone euro sign wireless_70f23b14-d195-42bb-8255-807a7adba23b.svg'
SOLO_SOURCE_ICON_ID='mobile-contactless-euro-payment-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='mobile-contactless-euro-payment-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/finance'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'mobile contactless euro payment')
    def build(self):
        self.add_bezier('signal', (4, 6), ((8, 3), (12, 2), (16, 2)), ((20, 2), (24, 3), (28, 6)))
        self.add_line('left', (4, 13), (4, 26))
        self.add_arc('bl', (4, 26), (9, 30), radius_x=5, radius_y=4, large_arc=False, sweep=False)
        self.add_line('bottom', (9, 30), (23, 30))
        self.add_arc('br', (23, 30), (28, 26), radius_x=5, radius_y=4, large_arc=False, sweep=False)
        self.add_line('right', (28, 26), (28, 13))
        self.add_arc('currency-upper', (18, 15), (13, 19), radius_x=5, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('currency-lower', (13, 19), (18, 23), radius_x=5, radius_y=4, large_arc=False, sweep=False)
        self.add_line('currency-bar', (13, 19), (17, 19))
        self.add_contour('phone', 'left', 'bl', 'bottom', 'br', 'right', closed=False)
        self.add_contour('currency', 'currency-upper', 'currency-lower', closed=False)
        self.relate('connect', 'currency', 'currency-bar')
        self.add_anchor('center',(16, 16))
