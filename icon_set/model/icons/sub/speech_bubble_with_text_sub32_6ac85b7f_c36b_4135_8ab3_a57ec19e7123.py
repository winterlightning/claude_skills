"""Speech Bubble with Text: user-requested grid-fitted 32px version of speech-bubble-with-text-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='6ac85b7f-c36b-4135-8ab3-a57ec19e7123'
SOURCE_PATH='pictographic-primitives/other/comment_6ac85b7f-c36b-4135-8ab3-a57ec19e7123.svg'
SOLO_SOURCE_ICON_ID='speech-bubble-with-text-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='speech-bubble-with-text-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'speech bubble with text')
    def build(self):
        self.add_line('top', (7, 2), (25, 2))
        self.add_arc('tr', (25, 2), (30, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('right', (30, 7), (30, 19))
        self.add_arc('br', (30, 19), (25, 26), radius_x=5, radius_y=7, large_arc=False, sweep=True)
        self.add_line('tail-1', (25, 26), (16, 26))
        self.add_line('tail-2', (16, 26), (8, 30))
        self.add_line('tail-3', (8, 30), (8, 26))
        self.add_line('tail-4', (8, 26), (7, 26))
        self.add_arc('bl', (7, 26), (2, 19), radius_x=5, radius_y=7, large_arc=False, sweep=True)
        self.add_line('left', (2, 19), (2, 7))
        self.add_arc('tl', (2, 7), (7, 2), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('text-top', (9, 10), (23, 10))
        self.add_line('text-bottom', (9, 18), (18, 18))
        self.add_contour('outline', 'top', 'tr', 'right', 'br', 'tail-1', 'tail-2', 'tail-3', 'tail-4', 'bl', 'left', 'tl', closed=True)
        self.add_anchor('center',(16, 16))
