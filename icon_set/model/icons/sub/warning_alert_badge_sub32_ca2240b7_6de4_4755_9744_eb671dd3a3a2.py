"""Warning Alert Badge: user-requested grid-fitted 32px version of warning-alert-badge-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='ca2240b7-6de4-4755-9744-eb671dd3a3a2'
SOURCE_PATH='pictographic-primitives/state/badge exclamation mark_ca2240b7-6de4-4755-9744-eb671dd3a3a2.svg'
SOLO_SOURCE_ICON_ID='warning-alert-badge-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='warning-alert-badge-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'state'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'warning alert badge')
    def build(self):
        self.add_line('outline-1', (16, 2), (21, 7))
        self.add_line('outline-2', (21, 7), (25, 7))
        self.add_line('outline-3', (25, 7), (25, 11))
        self.add_line('outline-4', (25, 11), (30, 16))
        self.add_line('outline-5', (30, 16), (25, 21))
        self.add_line('outline-6', (25, 21), (25, 25))
        self.add_line('outline-7', (25, 25), (21, 25))
        self.add_line('outline-8', (21, 25), (16, 30))
        self.add_line('outline-9', (16, 30), (11, 25))
        self.add_line('outline-10', (11, 25), (7, 25))
        self.add_line('outline-11', (7, 25), (7, 21))
        self.add_line('outline-12', (7, 21), (2, 16))
        self.add_line('outline-13', (2, 16), (7, 11))
        self.add_line('outline-14', (7, 11), (7, 7))
        self.add_line('outline-15', (7, 7), (11, 7))
        self.add_line('outline-16', (11, 7), (16, 2))
        self.add_line('stem', (16, 11), (16, 14))
        self.add_line('dot', (16, 21), (16, 21))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', 'outline-8', 'outline-9', 'outline-10', 'outline-11', 'outline-12', 'outline-13', 'outline-14', 'outline-15', 'outline-16', closed=True)
        self.add_anchor('center',(16, 16))
