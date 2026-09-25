"""Bird Footprint Symbol: user-requested grid-fitted 32px version of bird-footprint-symbol-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='ac9f5eb0-9ca6-4ae8-b650-3216bba2d023'
SOURCE_PATH='pictographic-primitives/other/bird print_ac9f5eb0-9ca6-4ae8-b650-3216bba2d023.svg'
SOLO_SOURCE_ICON_ID='bird-footprint-symbol-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='bird-footprint-symbol-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'bird footprint symbol')
    def build(self):
        self.add_line('stem-1', (16, 2), (16, 17))
        self.add_line('stem-2', (16, 17), (16, 30))
        self.add_line('toes-1', (4, 9), (16, 17))
        self.add_line('toes-2', (16, 17), (28, 9))
        self.add_contour('stem', 'stem-1', 'stem-2', closed=False)
        self.add_contour('toes', 'toes-1', 'toes-2', closed=False)
        self.relate('connect', 'stem', 'toes')
        self.add_anchor('center',(16, 16))
