"""Independent 32px profile of paragraph-normal.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '302ba70a-58d6-4bc5-8483-4e9e8b75df49'
SOURCE_PATH = 'pictographic-primitives/interface-essential/paragraph normal_302ba70a-58d6-4bc5-8483-4e9e8b75df49.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('302ba70a-58d6-4bc5-8483-4e9e8b75df49', 'pictographic-primitives/interface-essential/paragraph normal_302ba70a-58d6-4bc5-8483-4e9e8b75df49.svg'),)
PROFILE_SOURCE_KEYS = ('solo/paragraph-normal',)
SOLO_SOURCE_ICON_IDS = ('paragraph-normal',)
REFERENCE_EXPORT_SHA256 = 'ee82b2dae09f6cd3df5a4cb40a602db3153bf723d02d5b6c3e3c6ee83d4b0044'

class Drawing(Sub32):
    icon_id = 'paragraph-normal-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (30, 5))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 16), (30, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 27), (19, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
