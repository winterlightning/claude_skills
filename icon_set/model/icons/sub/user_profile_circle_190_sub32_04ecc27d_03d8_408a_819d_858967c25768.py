"""User Profile in Circle: user-requested grid-fitted 32px version of user-profile-circle-190-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='04ecc27d-03d8-408a-819d-858967c25768'
SOURCE_PATH='pictographic-primitives/other/person_04ecc27d-03d8-408a-819d-858967c25768.svg'
SOLO_SOURCE_ICON_ID='user-profile-circle-190-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='user-profile-circle-190-sub32'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'user profile in circle')
    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('head-top', (13, 12), (19, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (19, 12), (13, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('shoulders', (11, 22), (21, 22), radius_x=5, radius_y=1, large_arc=False, sweep=True)
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_anchor('center',(16, 16))
