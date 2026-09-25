"""Square Plus Sign: user-requested grid-fitted 32px version of square-plus-sign-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='b427db74-943b-4338-aab0-19f2d54abf47'
SOURCE_PATH='pictographic-primitives/other/square add_b427db74-943b-4338-aab0-19f2d54abf47.svg'
SOLO_SOURCE_ICON_ID='square-plus-sign-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='square-plus-sign-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'square plus sign')
    def build(self):
        self.add_line('outline-0', (6, 2), (26, 2))
        self.add_arc('outline-1', (26, 2), (30, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('outline-2', (30, 6), (30, 26))
        self.add_arc('outline-3', (30, 26), (26, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('outline-4', (26, 30), (6, 30))
        self.add_arc('outline-5', (6, 30), (2, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('outline-6', (2, 26), (2, 6))
        self.add_arc('outline-7', (2, 6), (6, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('h-1', (9, 16), (16, 16))
        self.add_line('h-2', (16, 16), (23, 16))
        self.add_line('v-1', (16, 9), (16, 16))
        self.add_line('v-2', (16, 16), (16, 23))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
        self.add_contour('h', 'h-1', 'h-2', closed=False)
        self.add_contour('v', 'v-1', 'v-2', closed=False)
        self.relate('connect', 'h', 'v')
        self.add_anchor('center',(16, 16))
