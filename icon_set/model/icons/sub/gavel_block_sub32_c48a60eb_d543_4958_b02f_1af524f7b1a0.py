"""Independent 32px profile of gavel-block.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c48a60eb-d543-4958-b02f-1af524f7b1a0'
SOURCE_PATH = 'pictographic-primitives/state/gavel block_c48a60eb-d543-4958-b02f-1af524f7b1a0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c48a60eb-d543-4958-b02f-1af524f7b1a0', 'pictographic-primitives/state/gavel block_c48a60eb-d543-4958-b02f-1af524f7b1a0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/gavel-block',)
SOLO_SOURCE_ICON_IDS = ('gavel-block',)
REFERENCE_EXPORT_SHA256 = '0851de1ce8150de5219a856397da403d2043c3417ce49fc05e222e3f7950695b'

class Drawing(Sub32):
    icon_id = 'gavel-block-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (30, 5))
        self.add_line('p1-r1-2', (30, 5), (30, 27))
        self.add_line('p1-r1-3', (30, 27), (2, 27))
        self.add_line('p1-r1-4', (2, 27), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
