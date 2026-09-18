"""Message Bubble with Checkmark: user-requested grid-fitted 32px version of message-bubble-with-checkmark-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='227c70e4-6853-47f9-b089-9eba3fe99d97'
SOURCE_PATH='pictographic-primitives/symbol/messages bubble round check_227c70e4-6853-47f9-b089-9eba3fe99d97.svg'
SOLO_SOURCE_ICON_ID='message-bubble-with-checkmark-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='message-bubble-with-checkmark-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'message bubble with checkmark')
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
        self.add_line('check-1', (11, 13), (14, 17))
        self.add_line('check-2', (14, 17), (21, 11))
        self.add_contour('outline', 'top', 'tr', 'right', 'br', 'tail-1', 'tail-2', 'tail-3', 'tail-4', 'bl', 'left', 'tl', closed=True)
        self.add_contour('check', 'check-1', 'check-2', closed=False)
        self.add_anchor('center',(16, 16))
