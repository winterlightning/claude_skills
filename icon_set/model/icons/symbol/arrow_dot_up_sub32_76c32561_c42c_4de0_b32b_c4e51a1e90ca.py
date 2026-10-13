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
        # Arrow pointing up with a dotted tail: the arrow, then two dots, every gap 4 units.
        self.add_dot('dot-1', (16, 30))
        self.add_dot('dot-2', (16, 22))
        self.add_line('stem', (16, 14), (16, 2))
        self.add_polyline('head', (4, 14), (16, 2), (28, 14))
        self.relate('connect', 'stem', 'head')
