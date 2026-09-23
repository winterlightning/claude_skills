"""Bitcoin Cryptocurrency Symbol: user-requested grid-fitted 32px version of bitcoin-cryptocurrency-symbol-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ._tall_base import SourceFaithfulSideSub
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '056563c8-a6c4-4201-b355-6ff5f08795ea'
SOURCE_PATH = 'pictographic-primitives/other/circle bitcoin_056563c8-a6c4-4201-b355-6ff5f08795ea.svg'
SOLO_SOURCE_ICON_ID = 'bitcoin-cryptocurrency-symbol-solo'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('enclosing circle', 'two rounded B bowls', 'middle bar', 'two upper and two lower stem tips')

class DrawingVariant2(SourceFaithfulSideSub):
    canvas_width = 60
    canvas_height = 60
    icon_id = 'bitcoin-cryptocurrency-symbol-sub32-v2'
    variant_of = 'bitcoin-cryptocurrency-symbol-sub32'
    variant_label = 'Complete source on a proportionate canvas'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/finance'
    tags = ('sub icon',)
    keywords = ('sub icon', 'grid fitted', 'bitcoin cryptocurrency symbol')

    def build(self):
        self.add_arc('outline-top', (2, 30), (58, 30), radius_x=28, radius_y=28, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (58, 30), (2, 30), radius_x=28, radius_y=28, large_arc=False, sweep=True)
        self.add_line('coin-top', (18, 14), (34, 14))
        self.add_arc('upper', (34, 14), (34, 30), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('lower', (34, 30), (34, 46), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('coin-bottom', (34, 46), (18, 46))
        self.add_line('spine', (18, 46), (18, 14))
        self.add_line('middle', (18, 30), (34, 30))
        self.add_line('tick--6--1', (18, 14), (18, 12))
        self.add_line('tick--6-1', (18, 46), (18, 48))
        self.add_line('tick-2--1', (34, 14), (34, 12))
        self.add_line('tick-2-1', (34, 46), (34, 48))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('currency', 'coin-top', 'upper', 'lower', 'coin-bottom', 'spine', closed=True)
        self.relate('connect', 'currency', 'middle')
        self.relate('connect', 'currency', 'tick--6--1')
        self.relate('connect', 'currency', 'tick--6-1')
        self.relate('connect', 'currency', 'tick-2--1')
        self.relate('connect', 'currency', 'tick-2-1')
        self.add_anchor('center', (30, 30))
