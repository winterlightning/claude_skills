"""Square Horizontal Exchange Arrows: user-requested grid-fitted 32px version of square-horizontal-exchange-arrows-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='78aaab68-fc23-4751-a93d-0e4f746ad065'
SOURCE_PATH='pictographic-primitives/other/square arrow opposite_78aaab68-fc23-4751-a93d-0e4f746ad065.svg'
SOLO_SOURCE_ICON_ID='square-horizontal-exchange-arrows-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='square-horizontal-exchange-arrows-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'square horizontal exchange arrows')
    def build(self):
        self.add_line('outline-0', (6, 2), (26, 2))
        self.add_arc('outline-1', (26, 2), (30, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('outline-2', (30, 6), (30, 26))
        self.add_arc('outline-3', (30, 26), (26, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('outline-4', (26, 30), (6, 30))
        self.add_arc('outline-5', (6, 30), (2, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('outline-6', (2, 26), (2, 6))
        self.add_arc('outline-7', (2, 6), (6, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('top-1', (22, 12), (10, 12))
        self.add_line('top-2', (10, 12), (13, 9))
        self.add_line('bottom-1', (10, 20), (22, 20))
        self.add_line('bottom-2', (22, 20), (19, 23))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
        self.add_contour('top', 'top-1', 'top-2', closed=False)
        self.add_contour('bottom', 'bottom-1', 'bottom-2', closed=False)
        self.add_anchor('center',(16, 16))
