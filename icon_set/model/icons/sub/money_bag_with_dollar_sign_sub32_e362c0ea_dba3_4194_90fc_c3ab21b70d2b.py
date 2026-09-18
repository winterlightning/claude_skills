"""Money Bag with Dollar Sign: user-requested grid-fitted 32px version of money-bag-with-dollar-sign-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='e362c0ea-dba3-4194-90fc-c3ab21b70d2b'
SOURCE_PATH='pictographic-primitives/other/pouch dollar_e362c0ea-dba3-4194-90fc-c3ab21b70d2b.svg'
SOLO_SOURCE_ICON_ID='money-bag-with-dollar-sign-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='money-bag-with-dollar-sign-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/finance'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'money bag with dollar sign')
    def build(self):
        self.add_line('neck-a', (9, 6), (7, 2))
        self.add_line('neck-b', (7, 2), (25, 2))
        self.add_line('neck-c', (25, 2), (23, 6))
        self.add_bezier('bag', (23, 6), ((28, 11), (28, 13), (28, 24)), ((28, 30), (22, 30), (16, 30)), ((10, 30), (4, 30), (4, 24)), ((4, 13), (4, 11), (9, 6)))
        self.add_line('currency-top', (20, 13), (16, 13))
        self.add_arc('currency-upper', (16, 13), (16, 17), radius_x=4, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('currency-lower', (16, 17), (16, 21), radius_x=4, radius_y=2, large_arc=False, sweep=True)
        self.add_line('currency-foot', (16, 21), (12, 21))
        self.add_line('stem-top', (16, 11), (16, 13))
        self.add_line('stem-bottom', (16, 21), (16, 23))
        self.add_contour('outline', 'neck-a', 'neck-b', 'neck-c', 'bag', closed=True)
        self.add_contour('currency', 'currency-top', 'currency-upper', 'currency-lower', 'currency-foot', closed=False)
        self.relate('connect', 'currency', 'stem-top')
        self.relate('connect', 'currency', 'stem-bottom')
        self.add_anchor('center',(16, 16))
