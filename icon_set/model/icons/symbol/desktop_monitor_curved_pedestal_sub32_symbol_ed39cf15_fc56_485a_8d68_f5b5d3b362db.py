"""Independent 32px profile of desktop-monitor-curved-pedestal.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'ed39cf15-fc56-485a-8d68-f5b5d3b362db'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/monitor_ed39cf15-fc56-485a-8d68-f5b5d3b362db.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ed39cf15-fc56-485a-8d68-f5b5d3b362db', 'pictographic-primitives/computers/batch-04/monitor_ed39cf15-fc56-485a-8d68-f5b5d3b362db.svg'),)
PROFILE_SOURCE_KEYS = ('solo/desktop-monitor-curved-pedestal',)
SOLO_SOURCE_ICON_IDS = ('desktop-monitor-curved-pedestal',)
REFERENCE_EXPORT_SHA256 = 'dec03f28ba3b705c3829c1eda97b7ba8035caa956709e70b9a141ecc0a8451ea'

class DrawingContainerSymbol(Sub32):
    icon_id = 'desktop-monitor-curved-pedestal-sub32-symbol'
    related_origin_icon_id = 'desktop-monitor-curved-pedestal-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/desktop-monitor-curved-pedestal-sub32'
    counterpart_icon_id = 'desktop-monitor-curved-pedestal-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'computers'
    categories = ('computers', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Screen with a straight stand and a flat base (the curved neck could not keep 4 units).
        self.add_line('p1-r1-1', (5, 4), (27, 4))
        self.add_arc('p1-r1-2', (27, 4), (30, 6), radius_x=3, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 6), (30, 18))
        self.add_arc('p1-r1-4', (30, 18), (27, 20), radius_x=3, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (27, 20), (16, 20))
        self.add_line('p1-r1-7', (16, 20), (5, 20))
        self.add_arc('p1-r1-8', (5, 20), (2, 18), radius_x=3, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (2, 18), (2, 6))
        self.add_arc('p1-r1-10', (2, 6), (5, 4), radius_x=3, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=True)
        self.add_line('p2-r1-1', (16, 20), (16, 28))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (8, 28), (16, 28))
        self.add_line('p3-r1-2', (16, 28), (24, 28))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
