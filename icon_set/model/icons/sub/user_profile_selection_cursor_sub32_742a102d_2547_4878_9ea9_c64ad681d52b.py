"""User Profile Selection Cursor: user-requested grid-fitted 32px version of user-profile-selection-cursor-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='742a102d-2547-4878-9ea9-c64ad681d52b'
SOURCE_PATH='pictographic-primitives/other/cursor head_742a102d-2547-4878-9ea9-c64ad681d52b.svg'
SOLO_SOURCE_ICON_ID='user-profile-selection-cursor-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='user-profile-selection-cursor-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'user profile selection cursor')
    def build(self):
        self.add_arc('head-upper', (2, 12), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('head-lower', (12, 22), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('cursor-1', (18, 17), (30, 23))
        self.add_line('cursor-2', (30, 23), (25, 25))
        self.add_line('cursor-3', (25, 25), (22, 30))
        self.add_line('cursor-4', (22, 30), (18, 17))
        self.add_contour('head', 'head-lower', 'head-upper', closed=False)
        self.add_contour('cursor', 'cursor-1', 'cursor-2', 'cursor-3', 'cursor-4', closed=True)
        self.add_anchor('center',(16, 16))
