"""British Pound Invoice Document: user-requested grid-fitted 32px version of british-pound-invoice-document-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='d540aa9a-0088-4ba3-b31e-9f6965432001'
SOURCE_PATH='pictographic-primitives/other/pound bill_d540aa9a-0088-4ba3-b31e-9f6965432001.svg'
SOLO_SOURCE_ICON_ID='british-pound-invoice-document-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='british-pound-invoice-document-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'british pound invoice document')
    def build(self):
        self.add_line('outline-1', (4, 2), (19, 2))
        self.add_line('outline-2', (19, 2), (28, 10))
        self.add_line('outline-3', (28, 10), (28, 30))
        self.add_line('outline-4', (28, 30), (4, 30))
        self.add_line('outline-5', (4, 30), (4, 2))
        self.add_arc('hook', (20, 15), (14, 15), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('stem', (14, 15), (14, 23))
        self.add_line('foot', (12, 23), (20, 23))
        self.add_line('bar', (12, 17), (15, 17))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', closed=True)
        self.add_contour('currency', 'hook', 'stem', closed=False)
        self.relate('connect', 'currency', 'bar')
        self.relate('connect', 'currency', 'foot')
        self.add_anchor('center',(16, 16))
