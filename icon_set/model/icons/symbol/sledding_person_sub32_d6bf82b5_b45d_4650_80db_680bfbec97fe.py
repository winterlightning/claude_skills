"""Independent 32px profile of sledding-person.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'd6bf82b5-b45d-4650-80db-680bfbec97fe'
SOURCE_PATH = 'pictographic-primitives/symbol/snow slide_d6bf82b5-b45d-4650-80db-680bfbec97fe.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d6bf82b5-b45d-4650-80db-680bfbec97fe', 'pictographic-primitives/symbol/snow slide_d6bf82b5-b45d-4650-80db-680bfbec97fe.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sledding-person',)
SOLO_SOURCE_ICON_IDS = ('sledding-person',)
REFERENCE_EXPORT_SHA256 = 'db1e356bee0953ac51aa88cfbad72e59043dacadc82812cc260bbcd3adde6505'

class Drawing(Sub32):
    icon_id = 'sledding-person-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Sledding: person sitting with legs forward and arms up, above the curved sled runner.
        self.add_arc('head-1', (5, 4), (9, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-2', (9, 4), (5, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('torso', (9, 14), (10, 22))
        self.add_line('arm', (9, 14), (18, 12))
        self.add_line('legs', (10, 22), (20, 22))
        self.add_line('runner', (2, 30), (24, 30))
        self.add_arc('tip', (24, 30), (30, 24), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_contour('sled', 'runner', 'tip')
        self.relate('connect', 'torso', 'arm')
        self.relate('connect', 'torso', 'legs')
