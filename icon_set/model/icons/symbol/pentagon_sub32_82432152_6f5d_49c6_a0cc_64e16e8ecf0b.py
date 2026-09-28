"""Independent 32px profile of pentagon-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '82432152-6f5d-49c6-a0cc-64e16e8ecf0b'
SOURCE_PATH = 'pictographic-primitives/symbol/pentagon_82432152-6f5d-49c6-a0cc-64e16e8ecf0b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('82432152-6f5d-49c6-a0cc-64e16e8ecf0b', 'pictographic-primitives/symbol/pentagon_82432152-6f5d-49c6-a0cc-64e16e8ecf0b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pentagon-solo',)
SOLO_SOURCE_ICON_IDS = ('pentagon-solo',)
REFERENCE_EXPORT_SHA256 = 'ead77a365668a900cdeb9466af033062c248e50515fba7611cdfff870096eb4d'

class Drawing(Sub32):
    icon_id = 'pentagon-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (30, 13))
        self.add_line('p1-r1-2', (30, 13), (25, 30))
        self.add_line('p1-r1-3', (25, 30), (7, 30))
        self.add_line('p1-r1-4', (7, 30), (2, 13))
        self.add_line('p1-r1-5', (2, 13), (16, 2))
        self.add_line('p1-r1-6', (16, 2), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
