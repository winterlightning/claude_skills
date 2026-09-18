"""Heart Speech Bubble: user-requested grid-fitted 32px version of heart-message-22-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='2a3f04f0-a404-41db-90b7-a6ee5813413b'
SOURCE_PATH='pictographic-primitives/symbol/messages bubble round heart_2a3f04f0-a404-41db-90b7-a6ee5813413b.svg'
SOLO_SOURCE_ICON_ID='heart-message-22-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='heart-message-22-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'heart speech bubble')
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
        self.add_bezier('heart', (16, 17), ((13, 14), (9, 14), (9, 11)), ((9, 9), (14, 8), (16, 11)), ((18, 8), (23, 9), (23, 11)), ((23, 14), (19, 14), (16, 17)))
        self.add_contour('outline', 'top', 'tr', 'right', 'br', 'tail-1', 'tail-2', 'tail-3', 'tail-4', 'bl', 'left', 'tl', closed=True)
        self.add_contour('heart-shape', 'heart', closed=True)
        self.add_anchor('center',(16, 16))
