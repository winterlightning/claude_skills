"""Mobile and Tablet Devices: user-requested grid-fitted 32px version of mobile-and-tablet-devices-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='5eacd8f1-eba2-4a29-9ba9-bed6d733e5d3'
SOURCE_PATH='pictographic-primitives/state/responsive_5eacd8f1-eba2-4a29-9ba9-bed6d733e5d3.svg'
SOLO_SOURCE_ICON_ID='mobile-and-tablet-devices-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='mobile-and-tablet-devices-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'mobile and tablet devices')
    def build(self):
        self.add_line('phone-0', (4, 14), (11, 14))
        self.add_arc('phone-1', (11, 14), (13, 17), radius_x=2, radius_y=3, large_arc=False, sweep=True)
        self.add_line('phone-2', (13, 17), (13, 28))
        self.add_arc('phone-3', (13, 28), (11, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('phone-4', (11, 30), (4, 30))
        self.add_arc('phone-5', (4, 30), (2, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('phone-6', (2, 28), (2, 17))
        self.add_arc('phone-7', (2, 17), (4, 14), radius_x=2, radius_y=3, large_arc=False, sweep=True)
        self.add_line('tablet-1', (9, 7), (9, 2))
        self.add_line('tablet-2', (9, 2), (30, 2))
        self.add_line('tablet-3', (30, 2), (30, 22))
        self.add_line('tablet-4', (30, 22), (20, 22))
        self.add_line('phone-rule', (2, 22), (13, 22))
        self.add_contour('phone', 'phone-0', 'phone-1', 'phone-2', 'phone-3', 'phone-4', 'phone-5', 'phone-6', 'phone-7', closed=True)
        self.add_contour('tablet', 'tablet-1', 'tablet-2', 'tablet-3', 'tablet-4', closed=False)
        self.relate('connect', 'phone', 'phone-rule')
        self.add_anchor('center',(16, 16))
