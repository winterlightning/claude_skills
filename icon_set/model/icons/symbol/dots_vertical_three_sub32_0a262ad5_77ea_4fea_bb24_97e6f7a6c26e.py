"""Independent 32px profile of dots-vertical-three.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '0a262ad5-77ea-4fea-bb24-97e6f7a6c26e'
SOURCE_PATH = 'pictographic-primitives/symbol/three dots_0a262ad5-77ea-4fea-bb24-97e6f7a6c26e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0a262ad5-77ea-4fea-bb24-97e6f7a6c26e', 'pictographic-primitives/symbol/three dots_0a262ad5-77ea-4fea-bb24-97e6f7a6c26e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/dots-vertical-three',)
SOLO_SOURCE_ICON_IDS = ('dots-vertical-three',)
REFERENCE_EXPORT_SHA256 = 'e02a2b10158d646de3f2b8e90c5b5d000c823e9e7bf2453dc5a7a69c394d2f77'

class Drawing(Sub32):
    icon_id = 'dots-vertical-three-sub32'
    keyshape = Keyshape.VRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (16, 16), (16, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 30), (16, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
