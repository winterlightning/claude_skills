"""Simple Music Headphones: user-requested grid-fitted 32px version of simple-music-headphones-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='71ce4923-14d6-48ce-9ae4-686eac75200e'
SOURCE_PATH='pictographic-primitives/other/headphone_71ce4923-14d6-48ce-9ae4-686eac75200e.svg'
SOLO_SOURCE_ICON_ID='simple-music-headphones-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='simple-music-headphones-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'simple music headphones')
    def build(self):
        self.add_arc('band', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('left-pad-0', (6, 16), (6, 16))
        self.add_arc('left-pad-1', (6, 16), (10, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('left-pad-2', (10, 20), (10, 26))
        self.add_arc('left-pad-3', (10, 26), (6, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('left-pad-4', (6, 30), (6, 30))
        self.add_arc('left-pad-5', (6, 30), (2, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('left-pad-6', (2, 26), (2, 20))
        self.add_arc('left-pad-7', (2, 20), (6, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('right-pad-0', (26, 16), (26, 16))
        self.add_arc('right-pad-1', (26, 16), (30, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('right-pad-2', (30, 20), (30, 26))
        self.add_arc('right-pad-3', (30, 26), (26, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('right-pad-4', (26, 30), (26, 30))
        self.add_arc('right-pad-5', (26, 30), (22, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('right-pad-6', (22, 26), (22, 20))
        self.add_arc('right-pad-7', (22, 20), (26, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('left-pad', 'left-pad-0', 'left-pad-1', 'left-pad-2', 'left-pad-3', 'left-pad-4', 'left-pad-5', 'left-pad-6', 'left-pad-7', closed=True)
        self.add_contour('right-pad', 'right-pad-0', 'right-pad-1', 'right-pad-2', 'right-pad-3', 'right-pad-4', 'right-pad-5', 'right-pad-6', 'right-pad-7', closed=True)
        self.relate('connect', 'band', 'left-pad', 'right-pad')
        self.add_anchor('center',(16, 16))
