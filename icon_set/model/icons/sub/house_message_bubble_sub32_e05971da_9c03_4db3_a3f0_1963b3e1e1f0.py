"""House Message Bubble: user-requested grid-fitted 32px version of house-message-bubble-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='e05971da-9c03-4db3-a3f0-1963b3e1e1f0'
SOURCE_PATH='pictographic-primitives/symbol/massage bubble with house_e05971da-9c03-4db3-a3f0-1963b3e1e1f0.svg'
SOLO_SOURCE_ICON_ID='house-message-bubble-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='house-message-bubble-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'symbol'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'house message bubble')
    def build(self):
        self.add_line('top', (7, 2), (25, 2))
        self.add_arc('tr', (25, 2), (30, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('right', (30, 7), (30, 19))
        self.add_arc('br', (30, 19), (25, 24), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('tail-1', (25, 24), (16, 24))
        self.add_line('tail-2', (16, 24), (8, 30))
        self.add_line('tail-3', (8, 30), (8, 24))
        self.add_line('tail-4', (8, 24), (7, 24))
        self.add_arc('bl', (7, 24), (2, 19), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('left', (2, 19), (2, 7))
        self.add_arc('tl', (2, 7), (7, 2), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('house-1', (10, 14), (16, 9))
        self.add_line('house-2', (16, 9), (22, 14))
        self.add_line('house-3', (22, 14), (22, 16))
        self.add_line('house-4', (22, 16), (10, 16))
        self.add_line('house-5', (10, 16), (10, 14))
        self.add_contour('outline', 'top', 'tr', 'right', 'br', 'tail-1', 'tail-2', 'tail-3', 'tail-4', 'bl', 'left', 'tl', closed=True)
        self.add_contour('house', 'house-1', 'house-2', 'house-3', 'house-4', 'house-5', closed=True)
        self.add_anchor('center',(16, 16))
