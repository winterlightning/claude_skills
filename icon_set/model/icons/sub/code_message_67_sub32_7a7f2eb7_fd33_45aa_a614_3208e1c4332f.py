"""Code Chat Bubble: user-requested grid-fitted 32px version of code-message-67-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='7a7f2eb7-fd33-45aa-a614-3208e1c4332f'
SOURCE_PATH='pictographic-primitives/other/messages bubble square code_7a7f2eb7-fd33-45aa-a614-3208e1c4332f.svg'
SOLO_SOURCE_ICON_ID='code-message-67-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='code-message-67-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'code chat bubble')
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
        self.add_line('code-left-1', (13, 9), (9, 13))
        self.add_line('code-left-2', (9, 13), (13, 16))
        self.add_line('code-underscore', (19, 16), (23, 16))
        self.add_contour('outline', 'top', 'tr', 'right', 'br', 'tail-1', 'tail-2', 'tail-3', 'tail-4', 'bl', 'left', 'tl', closed=True)
        self.add_contour('code-left', 'code-left-1', 'code-left-2', closed=False)
        self.add_anchor('center',(16, 16))
