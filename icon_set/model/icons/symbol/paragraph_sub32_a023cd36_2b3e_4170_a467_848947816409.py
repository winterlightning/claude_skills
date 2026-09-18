"""Independent 32px profile of paragraph.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'a023cd36-2b3e-4170-a467-848947816409'
SOURCE_PATH = 'pictographic-primitives/interface-essential/paragraph_a023cd36-2b3e-4170-a467-848947816409.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a023cd36-2b3e-4170-a467-848947816409', 'pictographic-primitives/interface-essential/paragraph_a023cd36-2b3e-4170-a467-848947816409.svg'),)
PROFILE_SOURCE_KEYS = ('solo/paragraph',)
SOLO_SOURCE_ICON_IDS = ('paragraph',)
REFERENCE_EXPORT_SHA256 = '1f82192580aeac697c18abb7ee8d9becf7f5a79990c4cd58ebb6d02bb0c321cc'

class Drawing(Sub32):
    icon_id = 'paragraph-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (30, 5))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 27), (30, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
