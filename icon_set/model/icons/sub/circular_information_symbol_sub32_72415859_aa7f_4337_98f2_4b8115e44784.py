"""Circular Information Symbol: user-requested grid-fitted 32px version of circular-information-symbol-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='72415859-aa7f-4337-98f2-4b8115e44784'
SOURCE_PATH='pictographic-primitives/other/circle information_72415859-aa7f-4337-98f2-4b8115e44784.svg'
SOLO_SOURCE_ICON_ID='circular-information-symbol-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='circular-information-symbol-sub32'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'circular information symbol')
    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('dot', (16, 10), (16, 10))
        self.add_line('stem', (16, 16), (16, 22))
        self.add_line('foot', (12, 22), (20, 22))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.relate('connect', 'stem', 'foot')
        self.add_anchor('center',(16, 16))
