"""Circular Close Icon: user-requested grid-fitted 32px version of circular-close-icon-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='8fece960-4425-489e-b4df-bb3dfe7ebe00'
SOURCE_PATH='pictographic-primitives/other/circle remove_8fece960-4425-489e-b4df-bb3dfe7ebe00.svg'
SOLO_SOURCE_ICON_ID='circular-close-icon-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='circular-close-icon-sub32'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'circular close icon')
    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('cross-a-1', (11, 11), (16, 16))
        self.add_line('cross-a-2', (16, 16), (21, 21))
        self.add_line('cross-b-1', (11, 21), (16, 16))
        self.add_line('cross-b-2', (16, 16), (21, 11))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('cross-a', 'cross-a-1', 'cross-a-2', closed=False)
        self.add_contour('cross-b', 'cross-b-1', 'cross-b-2', closed=False)
        self.relate('connect', 'cross-a', 'cross-b')
        self.add_anchor('center',(16, 16))
