"""Independent 32px profile of three-bars.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '33ef65ff-2528-4211-8fb6-5f9788166e2b'
SOURCE_PATH = 'pictographic-primitives/other/three bars_33ef65ff-2528-4211-8fb6-5f9788166e2b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('33ef65ff-2528-4211-8fb6-5f9788166e2b', 'pictographic-primitives/other/three bars_33ef65ff-2528-4211-8fb6-5f9788166e2b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-bars',)
SOLO_SOURCE_ICON_IDS = ('three-bars',)
REFERENCE_EXPORT_SHA256 = '29a5106dab583ea4eb10ad236f5dca473faab7eed68e455b70a2443ee96bce4b'

class Drawing(Sub32):
    icon_id = 'three-bars-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (16, 30), (16, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (30, 2), (30, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
