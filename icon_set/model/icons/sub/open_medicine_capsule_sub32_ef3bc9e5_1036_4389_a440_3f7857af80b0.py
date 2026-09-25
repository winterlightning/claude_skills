"""Open Medicine Capsule: user-requested grid-fitted 32px version of open-medicine-capsule-solo.
Plan: retain source primitive/contour topology and fit HRECT_L ink (0, 4, 32, 28).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='ef3bc9e5-1036-4389-a440-3f7857af80b0'
SOURCE_PATH='pictographic-primitives/other/pill open_ef3bc9e5-1036-4389-a440-3f7857af80b0.svg'
SOLO_SOURCE_ICON_ID='open-medicine-capsule-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='open-medicine-capsule-sub32'
    keyshape=Keyshape.HRECT_L
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'open medicine capsule')
    def build(self):
        self.add_arc('left', (10, 6), (10, 26), radius_x=8, radius_y=10, large_arc=False, sweep=False)
        self.add_line('left-opening-1', (10, 26), (12, 23))
        self.add_line('left-opening-2', (12, 23), (12, 9))
        self.add_line('left-opening-3', (12, 9), (10, 6))
        self.add_arc('right', (22, 26), (22, 6), radius_x=8, radius_y=10, large_arc=False, sweep=False)
        self.add_line('right-opening-1', (22, 6), (20, 9))
        self.add_line('right-opening-2', (20, 9), (20, 23))
        self.add_line('right-opening-3', (20, 23), (22, 26))
        self.add_contour('left-half', 'left', 'left-opening-1', 'left-opening-2', 'left-opening-3', closed=False)
        self.add_contour('right-half', 'right', 'right-opening-1', 'right-opening-2', 'right-opening-3', closed=False)
        self.add_anchor('center',(16, 16))
