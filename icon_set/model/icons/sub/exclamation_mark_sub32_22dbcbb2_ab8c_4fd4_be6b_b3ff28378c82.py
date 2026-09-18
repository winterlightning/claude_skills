"""Independent 32px profile of exclamation-mark.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '22dbcbb2-ab8c-4fd4-be6b-b3ff28378c82'
SOURCE_PATH = 'pictographic-primitives/symbol/exclamation_22dbcbb2-ab8c-4fd4-be6b-b3ff28378c82.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('22dbcbb2-ab8c-4fd4-be6b-b3ff28378c82', 'pictographic-primitives/symbol/exclamation_22dbcbb2-ab8c-4fd4-be6b-b3ff28378c82.svg'),)
PROFILE_SOURCE_KEYS = ('solo/exclamation-mark',)
SOLO_SOURCE_ICON_IDS = ('exclamation-mark',)
REFERENCE_EXPORT_SHA256 = '97be2e8abe54201805ba47220d2275090d7606e360a1d183e52da6ff48c4d666'

class Drawing(Sub32):
    icon_id = 'exclamation-mark-sub32'
    keyshape = Keyshape.VRECT_S
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (16, 21))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (16, 30), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
