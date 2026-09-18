"""Euro Financial Document: user-requested grid-fitted 32px version of euro-financial-document-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='36b5ce8c-0ffe-4bbc-9abc-5d99e806b0d9'
SOURCE_PATH='pictographic-primitives/other/euro bill_36b5ce8c-0ffe-4bbc-9abc-5d99e806b0d9.svg'
SOLO_SOURCE_ICON_ID='euro-financial-document-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='euro-financial-document-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/finance'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'euro financial document')
    def build(self):
        self.add_line('outline-1', (4, 2), (19, 2))
        self.add_line('outline-2', (19, 2), (28, 10))
        self.add_line('outline-3', (28, 10), (28, 30))
        self.add_line('outline-4', (28, 30), (4, 30))
        self.add_line('outline-5', (4, 30), (4, 2))
        self.add_arc('currency-upper', (20, 12), (12, 17), radius_x=8, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('currency-lower', (12, 17), (20, 23), radius_x=8, radius_y=6, large_arc=False, sweep=False)
        self.add_line('bar', (12, 17), (18, 17))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', closed=True)
        self.add_contour('currency', 'currency-upper', 'currency-lower', closed=False)
        self.relate('connect', 'currency', 'bar')
        self.add_anchor('center',(16, 16))
