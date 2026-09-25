"""Yen Currency Document: user-requested grid-fitted 32px version of yen-currency-document-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='b3374daa-5cf7-4d59-b44f-d2f472d4ca67'
SOURCE_PATH='pictographic-primitives/other/yuan bill_b3374daa-5cf7-4d59-b44f-d2f472d4ca67.svg'
SOLO_SOURCE_ICON_ID='yen-currency-document-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='yen-currency-document-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'yen currency document')
    def build(self):
        self.add_line('outline-1', (4, 2), (19, 2))
        self.add_line('outline-2', (19, 2), (28, 10))
        self.add_line('outline-3', (28, 10), (28, 30))
        self.add_line('outline-4', (28, 30), (4, 30))
        self.add_line('outline-5', (4, 30), (4, 2))
        self.add_line('fork-1', (12, 12), (16, 17))
        self.add_line('fork-2', (16, 17), (20, 12))
        self.add_line('stem', (16, 17), (16, 23))
        self.add_line('bar', (12, 17), (20, 17))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', closed=True)
        self.add_contour('fork', 'fork-1', 'fork-2', closed=False)
        self.relate('connect', 'fork', 'stem', 'bar')
        self.add_anchor('center',(16, 16))
