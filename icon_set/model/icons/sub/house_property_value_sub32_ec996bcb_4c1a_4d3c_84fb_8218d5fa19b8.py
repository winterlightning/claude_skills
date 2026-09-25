"""House Property Value: user-requested grid-fitted 32px version of house-property-value-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='ec996bcb-4c1a-4d3c-84fb-8218d5fa19b8'
SOURCE_PATH='pictographic-primitives/symbol/house dollar_ec996bcb-4c1a-4d3c-84fb-8218d5fa19b8.svg'
SOLO_SOURCE_ICON_ID='house-property-value-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='house-property-value-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'house property value')
    def build(self):
        self.add_line('outline-1', (2, 30), (2, 14))
        self.add_line('outline-2', (2, 14), (16, 2))
        self.add_line('outline-3', (16, 2), (30, 14))
        self.add_line('outline-4', (30, 14), (30, 30))
        self.add_line('currency-top', (21, 15), (16, 15))
        self.add_arc('currency-upper', (16, 15), (16, 21), radius_x=5, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('currency-lower', (16, 21), (16, 28), radius_x=5, radius_y=3, large_arc=False, sweep=True)
        self.add_line('currency-foot', (16, 28), (11, 28))
        self.add_line('stem-top', (16, 14), (16, 15))
        self.add_line('stem-bottom', (16, 28), (16, 28))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', closed=False)
        self.add_contour('currency', 'currency-top', 'currency-upper', 'currency-lower', 'currency-foot', closed=False)
        self.relate('connect', 'currency', 'stem-top')
        self.relate('connect', 'currency', 'stem-bottom')
        self.add_anchor('center',(16, 16))
