"""Bitcoin Cryptocurrency Symbol: user-requested grid-fitted 32px version of bitcoin-cryptocurrency-symbol-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='056563c8-a6c4-4201-b355-6ff5f08795ea'
SOURCE_PATH='pictographic-primitives/other/circle bitcoin_056563c8-a6c4-4201-b355-6ff5f08795ea.svg'
SOLO_SOURCE_ICON_ID='bitcoin-cryptocurrency-symbol-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='bitcoin-cryptocurrency-symbol-sub32'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/finance'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'bitcoin cryptocurrency symbol')
    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('coin-top', (10, 8), (18, 8))
        self.add_arc('upper', (18, 8), (18, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('lower', (18, 16), (18, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('coin-bottom', (18, 24), (10, 24))
        self.add_line('spine', (10, 24), (10, 8))
        self.add_line('middle', (10, 16), (18, 16))
        self.add_line('tick--6--1', (10, 8), (10, 7))
        self.add_line('tick--6-1', (10, 24), (10, 25))
        self.add_line('tick-2--1', (18, 8), (18, 7))
        self.add_line('tick-2-1', (18, 24), (18, 25))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('currency', 'coin-top', 'upper', 'lower', 'coin-bottom', 'spine', closed=True)
        self.relate('connect', 'currency', 'middle')
        self.relate('connect', 'currency', 'tick--6--1')
        self.relate('connect', 'currency', 'tick--6-1')
        self.relate('connect', 'currency', 'tick-2--1')
        self.relate('connect', 'currency', 'tick-2-1')
        self.add_anchor('center',(16, 16))
