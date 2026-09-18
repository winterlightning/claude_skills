"""Female User Profile Icon: user-requested grid-fitted 32px version of female-user-profile-icon-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='7e7928dc-c2b2-4979-be45-5ca674afd12d'
SOURCE_PATH='pictographic-primitives/other/full body women_7e7928dc-c2b2-4979-be45-5ca674afd12d.svg'
SOLO_SOURCE_ICON_ID='female-user-profile-icon-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='female-user-profile-icon-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'female user profile icon')
    def build(self):
        self.add_arc('head-top', (12, 6), (20, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (20, 6), (12, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('dress-1', (12, 16), (8, 16))
        self.add_line('dress-2', (8, 16), (4, 24))
        self.add_line('dress-3', (4, 24), (11, 24))
        self.add_line('dress-4', (11, 24), (12, 30))
        self.add_line('dress-5', (12, 30), (20, 30))
        self.add_line('dress-6', (20, 30), (21, 24))
        self.add_line('dress-7', (21, 24), (28, 24))
        self.add_line('dress-8', (28, 24), (24, 16))
        self.add_line('dress-9', (24, 16), (20, 16))
        self.add_line('dress-10', (20, 16), (12, 16))
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_contour('dress', 'dress-1', 'dress-2', 'dress-3', 'dress-4', 'dress-5', 'dress-6', 'dress-7', 'dress-8', 'dress-9', 'dress-10', closed=True)
        self.add_anchor('center',(16, 16))
