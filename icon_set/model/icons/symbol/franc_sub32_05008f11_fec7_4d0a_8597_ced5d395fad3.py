"""Independent 32px profile of franc.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '05008f11-fec7-4d0a-8597-ced5d395fad3'
SOURCE_PATH = 'pictographic-primitives/money/franc_05008f11-fec7-4d0a-8597-ced5d395fad3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('05008f11-fec7-4d0a-8597-ced5d395fad3', 'pictographic-primitives/money/franc_05008f11-fec7-4d0a-8597-ced5d395fad3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/franc',)
SOLO_SOURCE_ICON_IDS = ('franc',)
REFERENCE_EXPORT_SHA256 = 'a738ff10b28eff7b5cdaad2a3bb4758335964a031e95c65e807764e29353adce'

class Drawing(Sub32):
    icon_id = 'franc-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'money'
    categories = ('primitives', 'money')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (27, 2), (10, 2))
        self.add_line('p1-r1-2', (10, 2), (10, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (5, 17), (23, 17))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
