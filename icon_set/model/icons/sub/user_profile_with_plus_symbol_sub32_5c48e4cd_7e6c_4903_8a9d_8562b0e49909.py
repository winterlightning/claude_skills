"""User Profile with Plus Symbol: user-requested grid-fitted 32px version of user-profile-with-plus-symbol-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='5c48e4cd-7e6c-4903-8a9d-8562b0e49909'
SOURCE_PATH='pictographic-primitives/other/doctor_5c48e4cd-7e6c-4903-8a9d-8562b0e49909.svg'
SOLO_SOURCE_ICON_ID='user-profile-with-plus-symbol-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='user-profile-with-plus-symbol-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'user profile with plus symbol')
    human_construction='bust'
    def build(self):
        self.add_arc('head-top', (10, 8), (22, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (22, 8), (10, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('body', (2, 30), (30, 30), radius_x=14, radius_y=12, large_arc=False, sweep=True)
        self.add_line('h-1', (11, 27), (16, 27))
        self.add_line('h-2', (16, 27), (21, 27))
        self.add_line('v-1', (16, 25), (16, 27))
        self.add_line('v-2', (16, 27), (16, 30))
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_contour('h', 'h-1', 'h-2', closed=False)
        self.add_contour('v', 'v-1', 'v-2', closed=False)
        self.relate('connect', 'head', 'body')
        self.relate('connect', 'h', 'v')
        self.add_anchor('center',(16, 16))
