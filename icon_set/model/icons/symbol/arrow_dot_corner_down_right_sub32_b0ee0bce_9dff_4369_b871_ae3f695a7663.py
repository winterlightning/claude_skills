"""Independent 32px profile of arrow-dot-corner-down-right.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b0ee0bce-9dff-4369-b871-ae3f695a7663'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow dot corner down right_b0ee0bce-9dff-4369-b871-ae3f695a7663.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b0ee0bce-9dff-4369-b871-ae3f695a7663', 'pictographic-primitives/arrows/arrow dot corner down right_b0ee0bce-9dff-4369-b871-ae3f695a7663.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-dot-corner-down-right',)
SOLO_SOURCE_ICON_IDS = ('arrow-dot-corner-down-right',)
REFERENCE_EXPORT_SHA256 = 'bdb0a6f5124f80dcfdaa5c47f68557a87b36ed24ad0bc275cc0b5acf68e8bc3d'

class Drawing(Sub32):
    icon_id = 'arrow-dot-corner-down-right-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'arrows'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (5, 5))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (10, 10), (13, 13))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (18, 18), (30, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 30), (30, 30))
        self.add_line('p4-r1-2', (30, 30), (30, 16))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
