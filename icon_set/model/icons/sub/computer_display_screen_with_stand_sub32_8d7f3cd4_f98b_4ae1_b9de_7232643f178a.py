"""Computer Display Screen with Stand: user-requested grid-fitted 32px version of computer-display-screen-with-stand-solo.
Plan: retain source primitive/contour topology and fit HRECT_XL ink (0, 2, 32, 30).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='8d7f3cd4-f98b-4ae1-b9de-7232643f178a'
SOURCE_PATH='pictographic-primitives/computers/batch-02/monitor_8d7f3cd4-f98b-4ae1-b9de-7232643f178a.svg'
SOLO_SOURCE_ICON_ID='computer-display-screen-with-stand-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='computer-display-screen-with-stand-sub32'
    keyshape=Keyshape.HRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'computers'
    categories = ('computers', 'primitives')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'computer display screen with stand')
    def build(self):
        self.add_line('screen-0', (5, 4), (27, 4))
        self.add_arc('screen-1', (27, 4), (30, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('screen-2', (30, 7), (30, 18))
        self.add_arc('screen-3', (30, 18), (27, 20), radius_x=3, radius_y=2, large_arc=False, sweep=True)
        self.add_line('screen-4', (27, 20), (5, 20))
        self.add_arc('screen-5', (5, 20), (2, 18), radius_x=3, radius_y=2, large_arc=False, sweep=True)
        self.add_line('screen-6', (2, 18), (2, 7))
        self.add_arc('screen-7', (2, 7), (5, 4), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('stem', (16, 20), (16, 28))
        self.add_line('foot', (10, 28), (22, 28))
        self.add_contour('screen', 'screen-0', 'screen-1', 'screen-2', 'screen-3', 'screen-4', 'screen-5', 'screen-6', 'screen-7', closed=True)
        self.relate('connect', 'screen', 'stem')
        self.relate('connect', 'stem', 'foot')
        self.add_anchor('center',(16, 16))
