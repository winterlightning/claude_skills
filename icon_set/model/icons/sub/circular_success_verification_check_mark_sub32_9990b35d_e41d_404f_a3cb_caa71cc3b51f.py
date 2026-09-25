"""Circular Success Verification Check Mark: user-requested grid-fitted 32px version of circular-success-verification-check-mark-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='9990b35d-e41d-404f-a3cb-caa71cc3b51f'
SOURCE_PATH='pictographic-primitives/other/circle check_9990b35d-e41d-404f-a3cb-caa71cc3b51f.svg'
SOLO_SOURCE_ICON_ID='circular-success-verification-check-mark-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='circular-success-verification-check-mark-sub32'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'circular success verification check mark')
    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('check-1', (10, 16), (14, 20))
        self.add_line('check-2', (14, 20), (22, 12))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('check', 'check-1', 'check-2', closed=False)
        self.add_anchor('center',(16, 16))
