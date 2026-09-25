"""Upward Arrow Pointing To Top Bar: user-requested grid-fitted 32px version of upward-arrow-pointing-to-top-bar-solo.
Plan: retain source primitive/contour topology and fit HRECT_XL ink (0, 2, 32, 30).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='c6533072-e1ca-4ce5-9d50-b5bc08763683'
SOURCE_PATH='pictographic-primitives/other/move top_c6533072-e1ca-4ce5-9d50-b5bc08763683.svg'
SOLO_SOURCE_ICON_ID='upward-arrow-pointing-to-top-bar-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='upward-arrow-pointing-to-top-bar-sub32'
    keyshape=Keyshape.HRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'upward arrow pointing to top bar')
    def build(self):
        self.add_line('bar', (2, 4), (30, 4))
        self.add_line('shaft', (16, 28), (16, 11))
        self.add_line('head-1', (9, 18), (16, 11))
        self.add_line('head-2', (16, 11), (23, 18))
        self.add_contour('head', 'head-1', 'head-2', closed=False)
        self.relate('connect', 'shaft', 'head')
        self.add_anchor('center',(16, 16))
