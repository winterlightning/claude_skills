"""Independent 32px profile of rod-shaped-bacterium-bb2d6fc6.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'bb2d6fc6-f43a-40b7-b206-3b9eb2889351'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/bacteria_bb2d6fc6-f43a-40b7-b206-3b9eb2889351.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bb2d6fc6-f43a-40b7-b206-3b9eb2889351', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/bacteria_bb2d6fc6-f43a-40b7-b206-3b9eb2889351.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rod-shaped-bacterium-bb2d6fc6',)
SOLO_SOURCE_ICON_IDS = ('rod-shaped-bacterium-bb2d6fc6',)
REFERENCE_EXPORT_SHA256 = '90cfb61375d9d2e68e70010aeacedb70da2c334091777e51409d30d4b38420fa'

class Drawing(Sub32):
    icon_id = 'rod-shaped-bacterium-bb2d6fc6-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'health'
    categories = ('health', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Rod at 45 degrees: parallel sides, rounded ends, two flagella per side and one at each end.
        self.add_line('p1-r1-1', (4, 18), (18, 4))
        self.add_arc('p1-r1-2', (18, 4), (26, 6), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (26, 6), (28, 14), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (28, 14), (14, 28))
        self.add_arc('p1-r1-5', (14, 28), (6, 26), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (6, 26), (4, 18), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=True)
        self.add_line('p2-r1-1', (8, 14), (5, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (14, 8), (11, 5))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (18, 24), (21, 27))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (24, 18), (27, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (26, 6), (30, 2))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (6, 26), (2, 30))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        for flag in ('p2-r1-1', 'p3-r1-1'):
            self.relate('connect', 'p1-r1-1', flag)
        for flag in ('p4-r1-1', 'p5-r1-1'):
            self.relate('connect', 'p1-r1-4', flag)
        self.relate('connect', 'p1-r1-2', 'p6-r1-1')
        self.relate('connect', 'p1-r1-3', 'p6-r1-1')
        self.relate('connect', 'p1-r1-5', 'p7-r1-1')
        self.relate('connect', 'p1-r1-6', 'p7-r1-1')
