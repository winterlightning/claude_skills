"""Two Falling Bombs: user-requested grid-fitted 32px version of two-falling-bombs-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='a92b9733-23c6-4903-9f3a-c893edb5e9f4'
SOURCE_PATH='pictographic-primitives/state/bombs_a92b9733-23c6-4903-9f3a-c893edb5e9f4.svg'
SOLO_SOURCE_ICON_ID='two-falling-bombs-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='two-falling-bombs-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'two falling bombs')
    def build(self):
        self.add_line('bomb-left-0', (7, 11), (8, 11))
        self.add_arc('bomb-left-1', (8, 11), (12, 15), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('bomb-left-2', (12, 15), (12, 17))
        self.add_arc('bomb-left-3', (12, 17), (8, 21), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('bomb-left-4', (8, 21), (7, 21))
        self.add_arc('bomb-left-5', (7, 21), (2, 17), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_line('bomb-left-6', (2, 17), (2, 15))
        self.add_arc('bomb-left-7', (2, 15), (7, 11), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_line('fins-left-1', (3, 11), (3, 2))
        self.add_line('fins-left-2', (3, 2), (7, 5))
        self.add_line('fins-left-3', (7, 5), (12, 2))
        self.add_line('fins-left-4', (12, 2), (12, 11))
        self.add_line('bomb-right-0', (24, 19), (25, 19))
        self.add_arc('bomb-right-1', (25, 19), (30, 24), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('bomb-right-2', (30, 24), (30, 25))
        self.add_arc('bomb-right-3', (30, 25), (25, 30), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('bomb-right-4', (25, 30), (24, 30))
        self.add_arc('bomb-right-5', (24, 30), (20, 25), radius_x=4, radius_y=5, large_arc=False, sweep=True)
        self.add_line('bomb-right-6', (20, 25), (20, 24))
        self.add_arc('bomb-right-7', (20, 24), (24, 19), radius_x=4, radius_y=5, large_arc=False, sweep=True)
        self.add_line('fins-right-1', (20, 19), (20, 11))
        self.add_line('fins-right-2', (20, 11), (25, 14))
        self.add_line('fins-right-3', (25, 14), (29, 11))
        self.add_line('fins-right-4', (29, 11), (29, 19))
        self.add_contour('bomb-left', 'bomb-left-0', 'bomb-left-1', 'bomb-left-2', 'bomb-left-3', 'bomb-left-4', 'bomb-left-5', 'bomb-left-6', 'bomb-left-7', closed=True)
        self.add_contour('fins-left', 'fins-left-1', 'fins-left-2', 'fins-left-3', 'fins-left-4', closed=False)
        self.add_contour('bomb-right', 'bomb-right-0', 'bomb-right-1', 'bomb-right-2', 'bomb-right-3', 'bomb-right-4', 'bomb-right-5', 'bomb-right-6', 'bomb-right-7', closed=True)
        self.add_contour('fins-right', 'fins-right-1', 'fins-right-2', 'fins-right-3', 'fins-right-4', closed=False)
        self.relate('connect', 'bomb-left', 'fins-left')
        self.relate('connect', 'bomb-right', 'fins-right')
        self.add_anchor('center',(16, 16))
