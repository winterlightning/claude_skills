"""Circular Pause Button: user-requested grid-fitted 32px version of circular-pause-button-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='6dae9bf0-ff9d-4c48-a1b8-aba624cfab2b'
SOURCE_PATH='pictographic-primitives/other/circle pause_6dae9bf0-ff9d-4c48-a1b8-aba624cfab2b.svg'
SOLO_SOURCE_ICON_ID='circular-pause-button-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='circular-pause-button-sub32'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'circular pause button')
    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('pause-left', (12, 10), (12, 22))
        self.add_line('pause-right', (20, 10), (20, 22))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_anchor('center',(16, 16))
