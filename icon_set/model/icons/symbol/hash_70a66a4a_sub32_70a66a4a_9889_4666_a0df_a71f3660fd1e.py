"""Independent 32px profile of hash-70a66a4a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '70a66a4a-9889-4666-a0df-a71f3660fd1e'
SOURCE_PATH = 'pictographic-primitives/interface-essential/hash_70a66a4a-9889-4666-a0df-a71f3660fd1e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('70a66a4a-9889-4666-a0df-a71f3660fd1e', 'pictographic-primitives/interface-essential/hash_70a66a4a-9889-4666-a0df-a71f3660fd1e.svg'), ('fb5ba9f3-ed34-4ad9-a6c7-13d0b23d03d1', 'pictographic-primitives/interface-essential/hash_fb5ba9f3-ed34-4ad9-a6c7-13d0b23d03d1.svg'))
PROFILE_SOURCE_KEYS = ('solo/hash-70a66a4a', 'solo/hash-fb5ba9f3')
SOLO_SOURCE_ICON_IDS = ('hash-70a66a4a', 'hash-fb5ba9f3')
REFERENCE_EXPORT_SHA256 = 'd04eefc3c87654e600ca300555403eb94040350f892ba9516257a60b085b331e'

class Drawing(Sub32):
    icon_id = 'hash-70a66a4a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 11), (2, 11))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (21, 30), (21, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (30, 21), (2, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (11, 2), (11, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
