"""Upward Pointing Chevron: user-requested grid-fitted 32px version of upward-pointing-chevron-solo.
Plan: retain source primitive/contour topology and fit HRECT_XL ink (0, 2, 32, 30).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='93e589ef-a49d-4782-8494-d3c593234d3c'
SOURCE_PATH='pictographic-primitives/other/double arrow up 1_93e589ef-a49d-4782-8494-d3c593234d3c.svg'
SOLO_SOURCE_ICON_ID='upward-pointing-chevron-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='upward-pointing-chevron-sub32'
    keyshape=Keyshape.HRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'upward pointing chevron')
    def build(self):
        self.add_line('chevron-1', (2, 16), (16, 4))
        self.add_line('chevron-2', (16, 4), (30, 16))
        self.add_line('chevron-3', (30, 16), (30, 28))
        self.add_line('chevron-4', (30, 28), (16, 16))
        self.add_line('chevron-5', (16, 16), (2, 28))
        self.add_line('chevron-6', (2, 28), (2, 16))
        self.add_contour('chevron', 'chevron-1', 'chevron-2', 'chevron-3', 'chevron-4', 'chevron-5', 'chevron-6', closed=True)
        self.add_anchor('center',(16, 16))
