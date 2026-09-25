"""Mouse Pointer Arrow: user-requested grid-fitted 32px version of mouse-pointer-arrow-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='9eb9abed-c76d-498f-b14a-fe878165b5e6'
SOURCE_PATH='pictographic-primitives/other/cursor left_9eb9abed-c76d-498f-b14a-fe878165b5e6.svg'
SOLO_SOURCE_ICON_ID='mouse-pointer-arrow-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='mouse-pointer-arrow-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'mouse pointer arrow')
    def build(self):
        self.add_line('pointer-1', (4, 2), (28, 18))
        self.add_line('pointer-2', (28, 18), (16, 21))
        self.add_line('pointer-3', (16, 21), (10, 30))
        self.add_line('pointer-4', (10, 30), (4, 2))
        self.add_contour('pointer', 'pointer-1', 'pointer-2', 'pointer-3', 'pointer-4', closed=True)
        self.add_anchor('center',(16, 16))
