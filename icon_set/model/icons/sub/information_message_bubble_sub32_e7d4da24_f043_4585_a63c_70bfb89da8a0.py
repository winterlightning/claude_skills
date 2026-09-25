"""Information Message Bubble: user-requested grid-fitted 32px version of information-message-bubble-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='e7d4da24-f043-4585-a63c-70bfb89da8a0'
SOURCE_PATH='pictographic-primitives/messages/messages bubble square information_e7d4da24-f043-4585-a63c-70bfb89da8a0.svg'
SOLO_SOURCE_ICON_ID='information-message-bubble-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='information-message-bubble-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'messages'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'information message bubble')
    def build(self):
        self.add_line('top', (8, 2), (24, 2))
        self.add_arc('tr', (24, 2), (28, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('right', (28, 6), (28, 23))
        self.add_arc('br', (28, 23), (24, 27), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('bottom', (24, 27), (11, 27))
        self.add_line('tail', (11, 27), (4, 30))
        self.add_line('left', (4, 30), (4, 6))
        self.add_arc('tl', (4, 6), (8, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('dot', (16, 9), (16, 9))
        self.add_line('stem', (16, 15), (16, 19))
        self.add_line('foot', (12, 19), (20, 19))
        self.add_contour('outline', 'top', 'tr', 'right', 'br', 'bottom', 'tail', 'left', 'tl', closed=True)
        self.relate('connect', 'stem', 'foot')
        self.add_anchor('center',(16, 16))
