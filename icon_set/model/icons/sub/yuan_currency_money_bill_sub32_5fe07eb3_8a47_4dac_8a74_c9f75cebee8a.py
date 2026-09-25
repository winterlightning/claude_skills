"""Yuan Currency Money Bill: user-requested grid-fitted 32px version of yuan-currency-money-bill-solo.
Plan: retain source primitive/contour topology and fit HRECT_XL ink (0, 2, 32, 30).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='5fe07eb3-8a47-4dac-8a74-c9f75cebee8a'
SOURCE_PATH='pictographic-primitives/other/money bill yuan_5fe07eb3-8a47-4dac-8a74-c9f75cebee8a.svg'
SOLO_SOURCE_ICON_ID='yuan-currency-money-bill-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='yuan-currency-money-bill-sub32'
    keyshape=Keyshape.HRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    categories = ('other', 'state', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'yuan currency money bill')
    def build(self):
        self.add_line('outline-0', (5, 4), (27, 4))
        self.add_arc('outline-1', (27, 4), (30, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('outline-2', (30, 7), (30, 25))
        self.add_arc('outline-3', (30, 25), (27, 28), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('outline-4', (27, 28), (5, 28))
        self.add_arc('outline-5', (5, 28), (2, 25), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('outline-6', (2, 25), (2, 7))
        self.add_arc('outline-7', (2, 7), (5, 4), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('currency-fork-1', (12, 12), (16, 16))
        self.add_line('currency-fork-2', (16, 16), (20, 12))
        self.add_line('currency-stem-1', (16, 16), (16, 18))
        self.add_line('currency-stem-2', (16, 18), (16, 20))
        self.add_line('currency-bar-1', (13, 18), (16, 18))
        self.add_line('currency-bar-2', (16, 18), (19, 18))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
        self.add_contour('currency-fork', 'currency-fork-1', 'currency-fork-2', closed=False)
        self.add_contour('currency-stem', 'currency-stem-1', 'currency-stem-2', closed=False)
        self.add_contour('currency-bar', 'currency-bar-1', 'currency-bar-2', closed=False)
        self.relate('connect', 'currency-fork', 'currency-stem')
        self.relate('connect', 'currency-stem', 'currency-bar')
        self.add_anchor('center',(16, 16))
