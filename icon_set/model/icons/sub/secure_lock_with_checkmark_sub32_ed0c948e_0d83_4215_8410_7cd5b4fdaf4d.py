"""Secure Lock with Checkmark: user-requested grid-fitted 32px version of secure-lock-with-checkmark-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='ed0c948e-0d83-4215-8410-7cd5b4fdaf4d'
SOURCE_PATH='pictographic-primitives/other/check lock_ed0c948e-0d83-4215-8410-7cd5b4fdaf4d.svg'
SOLO_SOURCE_ICON_ID='secure-lock-with-checkmark-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='secure-lock-with-checkmark-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'secure lock with checkmark')
    def build(self):
        self.add_line('body-0', (7, 13), (25, 13))
        self.add_arc('body-1', (25, 13), (28, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('body-2', (28, 16), (28, 27))
        self.add_arc('body-3', (28, 27), (25, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('body-4', (25, 30), (7, 30))
        self.add_arc('body-5', (7, 30), (4, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('body-6', (4, 27), (4, 16))
        self.add_arc('body-7', (4, 16), (7, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('shackle-left', (9, 13), (9, 8))
        self.add_arc('shackle-top', (9, 8), (23, 8), radius_x=7, radius_y=6, large_arc=False, sweep=True)
        self.add_line('shackle-right', (23, 8), (23, 13))
        self.add_line('check-1', (11, 21), (15, 23))
        self.add_line('check-2', (15, 23), (20, 20))
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', closed=True)
        self.add_contour('shackle', 'shackle-left', 'shackle-top', 'shackle-right', closed=False)
        self.add_contour('check', 'check-1', 'check-2', closed=False)
        self.relate('connect', 'body', 'shackle')
        self.add_anchor('center',(16, 16))
