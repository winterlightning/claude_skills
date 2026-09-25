"""Medical Consultation Chat Bubble: user-requested grid-fitted 32px version of medical-message-54-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='b1da8322-82a2-455f-9885-2883a9e3199a'
SOURCE_PATH='pictographic-primitives/other/chat medical cross 1_b1da8322-82a2-455f-9885-2883a9e3199a.svg'
SOLO_SOURCE_ICON_ID='medical-message-54-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='medical-message-54-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    categories = ('other', 'state', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'medical consultation chat bubble')
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
        self.add_line('cross-h-1', (11, 13), (16, 13))
        self.add_line('cross-h-2', (16, 13), (21, 13))
        self.add_line('cross-v-1', (16, 9), (16, 13))
        self.add_line('cross-v-2', (16, 13), (16, 17))
        self.add_contour('outline', 'top', 'tr', 'right', 'br', 'tail-1', 'tail-2', 'tail-3', 'tail-4', 'bl', 'left', 'tl', closed=True)
        self.add_contour('cross-h', 'cross-h-1', 'cross-h-2', closed=False)
        self.add_contour('cross-v', 'cross-v-1', 'cross-v-2', closed=False)
        self.relate('connect', 'cross-h', 'cross-v')
        self.add_anchor('center',(16, 16))
