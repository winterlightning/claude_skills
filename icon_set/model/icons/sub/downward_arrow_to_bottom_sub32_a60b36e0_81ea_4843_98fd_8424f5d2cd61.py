"""Downward Arrow To Bottom: user-requested grid-fitted 32px version of downward-arrow-to-bottom-solo.
Plan: retain source primitive/contour topology and fit HRECT_XL ink (0, 2, 32, 30).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='a60b36e0-81ea-4843-98fd-8424f5d2cd61'
SOURCE_PATH='pictographic-primitives/other/move bottom_a60b36e0-81ea-4843-98fd-8424f5d2cd61.svg'
SOLO_SOURCE_ICON_ID='downward-arrow-to-bottom-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='downward-arrow-to-bottom-sub32'
    keyshape=Keyshape.HRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'downward arrow to bottom')
    def build(self):
        self.add_line('bar', (2, 28), (30, 28))
        self.add_line('shaft', (16, 4), (16, 21))
        self.add_line('head-1', (9, 14), (16, 21))
        self.add_line('head-2', (16, 21), (23, 14))
        self.add_contour('head', 'head-1', 'head-2', closed=False)
        self.relate('connect', 'shaft', 'head')
        self.add_anchor('center',(16, 16))
