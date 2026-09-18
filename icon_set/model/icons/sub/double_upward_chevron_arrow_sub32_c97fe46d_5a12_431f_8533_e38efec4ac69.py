"""Double Upward Chevron Arrow: user-requested grid-fitted 32px version of double-upward-chevron-arrow-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='c97fe46d-5a12-431f-8533-e38efec4ac69'
SOURCE_PATH='pictographic-primitives/other/double arrow up_c97fe46d-5a12-431f-8533-e38efec4ac69.svg'
SOLO_SOURCE_ICON_ID='double-upward-chevron-arrow-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='double-upward-chevron-arrow-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'double upward chevron arrow')
    def build(self):
        self.add_line('outline-1', (2, 11), (16, 2))
        self.add_line('outline-2', (16, 2), (30, 11))
        self.add_line('outline-3', (30, 11), (30, 30))
        self.add_line('outline-4', (30, 30), (16, 21))
        self.add_line('outline-5', (16, 21), (2, 30))
        self.add_line('outline-6', (2, 30), (2, 11))
        self.add_line('divider-1', (2, 21), (16, 11))
        self.add_line('divider-2', (16, 11), (30, 21))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', closed=True)
        self.add_contour('divider', 'divider-1', 'divider-2', closed=False)
        self.relate('connect', 'outline', 'divider')
        self.add_anchor('center',(16, 16))
