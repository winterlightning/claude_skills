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
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('enclosing circle', 'two rounded B bowls', 'middle bar', 'two upper and two lower stem tips')
REPAIR_PLAN = {'concept': 'bitcoin cryptocurrency symbol', 'core_parts': ('enclosing circle', 'two rounded B bowls', 'middle bar', 'two upper and two lower stem tips'), 'flexible_parts': 'Only minor curves and spacing may be simplified for 32px clearance', 'ladder': 'Rebalance and redraw on the strict SUB32 canvas'}

class DrawingVariant2(Sub32):
    icon_id='bitcoin-cryptocurrency-symbol-sub32-v2'
    variant_of = 'bitcoin-cryptocurrency-symbol-sub32'
    variant_label = "Strict 32x32 repair draft"
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/finance'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'bitcoin cryptocurrency symbol')
    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('coin-top', (12, 10), (18, 10))
        self.add_arc('upper', (18, 10), (18, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('lower', (18, 16), (18, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('coin-bottom', (18, 22), (12, 22))
        self.add_line('spine', (12, 22), (12, 10))
        self.add_line('middle', (12, 16), (18, 16))
        self.add_line('tick--6--1', (12, 10), (12, 9))
        self.add_line('tick--6-1', (12, 22), (12, 23))
        self.add_line('tick-2--1', (18, 10), (18, 9))
        self.add_line('tick-2-1', (18, 22), (18, 23))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('currency', 'coin-top', 'upper', 'lower', 'coin-bottom', 'spine', closed=True)
        self.relate('connect', 'currency', 'middle')
        self.relate('connect', 'currency', 'tick--6--1')
        self.relate('connect', 'currency', 'tick--6-1')
        self.relate('connect', 'currency', 'tick-2--1')
        self.relate('connect', 'currency', 'tick-2-1')
        self.add_anchor('center',(16, 16))
