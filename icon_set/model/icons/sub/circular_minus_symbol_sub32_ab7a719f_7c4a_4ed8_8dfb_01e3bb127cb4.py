"""Circular Minus Symbol: user-requested grid-fitted 32px version of circular-minus-symbol-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='ab7a719f-7c4a-4ed8-8dfb-01e3bb127cb4'
SOURCE_PATH='pictographic-primitives/other/circle minus_ab7a719f-7c4a-4ed8-8dfb-01e3bb127cb4.svg'
SOLO_SOURCE_ICON_ID='circular-minus-symbol-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='circular-minus-symbol-sub32'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'circular minus symbol')
    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('minus', (9, 16), (23, 16))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_anchor('center',(16, 16))
