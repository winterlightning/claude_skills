"""Independent 32px profile of arrow-dot-up.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '76c32561-c42c-4de0-b32b-c4e51a1e90ca'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow dot up_76c32561-c42c-4de0-b32b-c4e51a1e90ca.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('76c32561-c42c-4de0-b32b-c4e51a1e90ca', 'pictographic-primitives/arrows/arrow dot up_76c32561-c42c-4de0-b32b-c4e51a1e90ca.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-dot-up',)
SOLO_SOURCE_ICON_IDS = ('arrow-dot-up',)
REFERENCE_EXPORT_SHA256 = '855d61846e2d5c885491d365810de6e44c4b8b0ea59eec71c3c0fd14d712d05f'

class Drawing(Sub32):
    icon_id = 'arrow-dot-up-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'arrows'
    categories = ('arrows', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 13), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (27, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 13), (16, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 30), (16, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 22), (16, 19))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
