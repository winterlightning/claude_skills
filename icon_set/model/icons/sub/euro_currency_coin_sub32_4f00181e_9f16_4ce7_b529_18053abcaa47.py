"""Euro Currency Coin: user-requested grid-fitted 32px version of euro-currency-coin-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='4f00181e-9f16-4ce7-b529-18053abcaa47'
SOURCE_PATH='pictographic-primitives/other/circle euro_4f00181e-9f16-4ce7-b529-18053abcaa47.svg'
SOLO_SOURCE_ICON_ID='euro-currency-coin-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='euro-currency-coin-sub32'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'euro currency coin')
    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('currency-upper', (20, 10), (12, 16), radius_x=8, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('currency-lower', (12, 16), (20, 22), radius_x=8, radius_y=6, large_arc=False, sweep=False)
        self.add_line('bar', (12, 16), (18, 16))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('currency', 'currency-upper', 'currency-lower', closed=False)
        self.relate('connect', 'currency', 'bar')
        self.add_anchor('center',(16, 16))
