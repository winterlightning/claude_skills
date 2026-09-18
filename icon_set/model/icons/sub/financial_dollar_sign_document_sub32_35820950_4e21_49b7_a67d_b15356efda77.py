"""Financial Dollar Sign Document: user-requested grid-fitted 32px version of financial-dollar-sign-document-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='35820950-4e21-49b7-a67d-b15356efda77'
SOURCE_PATH='pictographic-primitives/other/dollar bill_35820950-4e21-49b7-a67d-b15356efda77.svg'
SOLO_SOURCE_ICON_ID='financial-dollar-sign-document-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='financial-dollar-sign-document-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/finance'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'financial dollar sign document')
    def build(self):
        self.add_line('outline-1', (4, 2), (19, 2))
        self.add_line('outline-2', (19, 2), (28, 10))
        self.add_line('outline-3', (28, 10), (28, 30))
        self.add_line('outline-4', (28, 30), (4, 30))
        self.add_line('outline-5', (4, 30), (4, 2))
        self.add_line('currency-top', (20, 13), (16, 13))
        self.add_arc('currency-upper', (16, 13), (16, 17), radius_x=4, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('currency-lower', (16, 17), (16, 21), radius_x=4, radius_y=2, large_arc=False, sweep=True)
        self.add_line('currency-bottom', (16, 21), (12, 21))
        self.add_line('stem-top', (16, 10), (16, 13))
        self.add_line('stem-bottom', (16, 21), (16, 24))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', closed=True)
        self.add_contour('currency', 'currency-top', 'currency-upper', 'currency-lower', 'currency-bottom', closed=False)
        self.relate('connect', 'currency', 'stem-top')
        self.relate('connect', 'currency', 'stem-bottom')
        self.add_anchor('center',(16, 16))
