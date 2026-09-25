"""Clipboard with checkmark: user-requested grid-fitted 32px version of clipboard-with-checkmark-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='c6e3c13b-a55a-4543-8d6f-5f9c7b2ff0e3'
SOURCE_PATH='pictographic-primitives/symbol/clipboard check_c6e3c13b-a55a-4543-8d6f-5f9c7b2ff0e3.svg'
SOLO_SOURCE_ICON_ID='clipboard-with-checkmark-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='clipboard-with-checkmark-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'clipboard with checkmark')
    def build(self):
        self.add_line('board-1', (12, 5), (4, 5))
        self.add_line('board-2', (4, 5), (4, 30))
        self.add_line('board-3', (4, 30), (28, 30))
        self.add_line('board-4', (28, 30), (28, 5))
        self.add_line('board-5', (28, 5), (20, 5))
        self.add_line('clip-0', (13, 2), (19, 2))
        self.add_arc('clip-1', (19, 2), (20, 5), radius_x=1, radius_y=3, large_arc=False, sweep=True)
        self.add_line('clip-2', (20, 5), (20, 6))
        self.add_arc('clip-3', (20, 6), (19, 10), radius_x=1, radius_y=4, large_arc=False, sweep=True)
        self.add_line('clip-4', (19, 10), (13, 10))
        self.add_arc('clip-5', (13, 10), (12, 6), radius_x=1, radius_y=4, large_arc=False, sweep=True)
        self.add_line('clip-6', (12, 6), (12, 5))
        self.add_arc('clip-7', (12, 5), (13, 2), radius_x=1, radius_y=3, large_arc=False, sweep=True)
        self.add_line('check-1', (12, 20), (14, 22))
        self.add_line('check-2', (14, 22), (20, 17))
        self.add_contour('board', 'board-1', 'board-2', 'board-3', 'board-4', 'board-5', closed=False)
        self.add_contour('clip', 'clip-0', 'clip-1', 'clip-2', 'clip-3', 'clip-4', 'clip-5', 'clip-6', 'clip-7', closed=True)
        self.add_contour('check', 'check-1', 'check-2', closed=False)
        self.relate('connect', 'clip', 'board')
        self.add_anchor('center',(16, 16))
