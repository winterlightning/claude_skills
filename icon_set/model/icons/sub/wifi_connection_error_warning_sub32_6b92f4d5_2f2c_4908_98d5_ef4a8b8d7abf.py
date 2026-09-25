"""Wifi Connection Error Warning: user-requested grid-fitted 32px version of wifi-connection-error-warning-solo.
Plan: retain source primitive/contour topology and fit HRECT_XL ink (0, 2, 32, 30).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='6b92f4d5-2f2c-4908-98d5-ef4a8b8d7abf'
SOURCE_PATH='pictographic-primitives/state/wifi exclamation_6b92f4d5-2f2c-4908-98d5-ef4a8b8d7abf.svg'
SOLO_SOURCE_ICON_ID='wifi-connection-error-warning-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='wifi-connection-error-warning-sub32'
    keyshape=Keyshape.HRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'state'
    categories = ('state',)
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'wifi connection error warning')
    def build(self):
        self.add_bezier('left-outer', (2, 9), ((5, 6), (8, 5), (10, 4)))
        self.add_bezier('right-outer', (22, 4), ((24, 5), (27, 6), (30, 9)))
        self.add_line('left-inner', (6, 17), (10, 14))
        self.add_line('right-inner', (22, 14), (26, 17))
        self.add_line('stem', (16, 6), (16, 20))
        self.add_line('dot', (16, 28), (16, 28))
        self.add_anchor('center',(16, 16))
