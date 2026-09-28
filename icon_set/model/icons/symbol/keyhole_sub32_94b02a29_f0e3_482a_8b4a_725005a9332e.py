"""Independent 32px profile of keyhole.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '94b02a29-f0e3-482a-8b4a-725005a9332e'
SOURCE_PATH = 'pictographic-primitives/symbol/keyhole_94b02a29-f0e3-482a-8b4a-725005a9332e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('94b02a29-f0e3-482a-8b4a-725005a9332e', 'pictographic-primitives/symbol/keyhole_94b02a29-f0e3-482a-8b4a-725005a9332e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/keyhole',)
SOLO_SOURCE_ICON_IDS = ('keyhole',)
REFERENCE_EXPORT_SHA256 = '744b136204cd38f77d4e16b03f7263102efebe9e032adbefeb9af9924225410d'

class Drawing(Sub32):
    icon_id = 'keyhole-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (22, 16), (27, 10), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('p1-r1-2', (27, 10), (24, 4), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('p1-r1-3', (24, 4), (17, 2), radius_x=15, radius_y=15, large_arc=False, sweep=False)
        self.add_line('p1-r1-4', (17, 2), (13, 2))
        self.add_arc('p1-r1-5', (13, 2), (5, 10), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_arc('p1-r1-6', (5, 10), (10, 16), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('p1-r1-7', (10, 16), (6, 30))
        self.add_line('p1-r1-8', (6, 30), (26, 30))
        self.add_line('p1-r1-9', (26, 30), (22, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
