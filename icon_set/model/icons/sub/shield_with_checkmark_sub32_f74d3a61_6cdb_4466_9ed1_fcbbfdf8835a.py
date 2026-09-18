"""Shield with Checkmark: user-requested grid-fitted 32px version of shield-with-checkmark-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='f74d3a61-6cdb-4466-9ed1-fcbbfdf8835a'
SOURCE_PATH='pictographic-primitives/protection/protection shield_f74d3a61-6cdb-4466-9ed1-fcbbfdf8835a.svg'
SOLO_SOURCE_ICON_ID='shield-with-checkmark-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='shield-with-checkmark-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'shield with checkmark')
    def build(self):
        self.add_bezier('shield', (16, 2), ((12, 4), (8, 6), (4, 6)), ((4, 17), (4, 24), (16, 30)), ((28, 24), (28, 17), (28, 6)), ((24, 6), (20, 4), (16, 2)))
        self.add_line('check-1', (11, 15), (15, 20))
        self.add_line('check-2', (15, 20), (21, 12))
        self.add_contour('outline', 'shield', closed=True)
        self.add_contour('check', 'check-1', 'check-2', closed=False)
        self.add_anchor('center',(16, 16))
