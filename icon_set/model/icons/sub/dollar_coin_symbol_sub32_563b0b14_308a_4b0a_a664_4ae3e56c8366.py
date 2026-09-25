"""Dollar Coin Symbol: user-requested grid-fitted 32px version of dollar-coin-symbol-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='563b0b14-308a-4b0a-a664-4ae3e56c8366'
SOURCE_PATH='pictographic-primitives/other/circle dollar_563b0b14-308a-4b0a-a664-4ae3e56c8366.svg'
SOLO_SOURCE_ICON_ID='dollar-coin-symbol-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='dollar-coin-symbol-sub32'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'dollar coin symbol')
    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('currency-top', (20, 10), (16, 10))
        self.add_arc('currency-upper', (16, 10), (16, 16), radius_x=4, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('currency-lower', (16, 16), (16, 22), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('currency-bottom', (16, 22), (12, 22))
        self.add_line('stem-top', (16, 9), (16, 10))
        self.add_line('stem-bottom', (16, 22), (16, 23))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('currency', 'currency-top', 'currency-upper', 'currency-lower', 'currency-bottom', closed=False)
        self.relate('connect', 'currency', 'stem-top')
        self.relate('connect', 'currency', 'stem-bottom')
        self.add_anchor('center',(16, 16))
