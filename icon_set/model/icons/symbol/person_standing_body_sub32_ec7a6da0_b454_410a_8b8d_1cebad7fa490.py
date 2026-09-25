"""Independent 32px profile of person-standing-body.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'ec7a6da0-b454-410a-8b8d-1cebad7fa490'
SOURCE_PATH = 'pictographic-primitives/symbol/person body 1_ec7a6da0-b454-410a-8b8d-1cebad7fa490.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ec7a6da0-b454-410a-8b8d-1cebad7fa490', 'pictographic-primitives/symbol/person body 1_ec7a6da0-b454-410a-8b8d-1cebad7fa490.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person-standing-body',)
SOLO_SOURCE_ICON_IDS = ('person-standing-body',)
REFERENCE_EXPORT_SHA256 = 'd47d4a873592aaff7cc90b19e6d2bd889804b8f551ec0ebdd3e3a0e903697bf3'

class Drawing(Sub32):
    icon_id = 'person-standing-body-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (11, 7), (21, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (21, 7), (11, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (10, 30), (10, 24))
        self.add_line('p2-r1-2', (10, 24), (5, 24))
        self.add_arc('p2-r1-3', (5, 24), (10, 19), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (10, 19), (22, 19))
        self.add_arc('p2-r1-5', (22, 19), (27, 24), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-6', (27, 24), (22, 24))
        self.add_line('p2-r1-7', (22, 24), (22, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
