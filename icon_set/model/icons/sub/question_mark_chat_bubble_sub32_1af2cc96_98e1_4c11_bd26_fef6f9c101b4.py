"""Question Mark Chat Bubble: user-requested grid-fitted 32px version of question-mark-chat-bubble-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='1af2cc96-98e1-4c11-bd26-fef6f9c101b4'
SOURCE_PATH='pictographic-primitives/symbol/question mark in chat bubble_1af2cc96-98e1-4c11-bd26-fef6f9c101b4.svg'
SOLO_SOURCE_ICON_ID='question-mark-chat-bubble-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='question-mark-chat-bubble-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'symbol'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'question mark chat bubble')
    def build(self):
        self.add_line('top', (8, 2), (24, 2))
        self.add_arc('tr', (24, 2), (28, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('right', (28, 6), (28, 23))
        self.add_arc('br', (28, 23), (24, 28), radius_x=4, radius_y=5, large_arc=False, sweep=True)
        self.add_line('bottom', (24, 28), (11, 28))
        self.add_line('tail', (11, 28), (4, 30))
        self.add_line('left', (4, 30), (4, 6))
        self.add_arc('tl', (4, 6), (8, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('hook', (12, 12), (20, 12), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('turn', (20, 12), ((20, 14), (16, 14), (16, 14)))
        self.add_line('dot', (16, 21), (16, 21))
        self.add_contour('outline', 'top', 'tr', 'right', 'br', 'bottom', 'tail', 'left', 'tl', closed=True)
        self.add_contour('question', 'hook', 'turn', closed=False)
        self.add_anchor('center',(16, 16))
