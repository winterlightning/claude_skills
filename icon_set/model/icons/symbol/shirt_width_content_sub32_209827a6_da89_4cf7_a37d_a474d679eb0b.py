"""Independent 32px profile of shirt-width-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '209827a6-da89-4cf7-a37d-a474d679eb0b'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/209827a6-da89-4cf7-a37d-a474d679eb0b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('209827a6-da89-4cf7-a37d-a474d679eb0b', 'icon_set/dist/gallery/combination-originals/209827a6-da89-4cf7-a37d-a474d679eb0b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shirt-width-content',)
SOLO_SOURCE_ICON_IDS = ('shirt-width-content',)
REFERENCE_EXPORT_SHA256 = '55fd29a7b450e76b61bb1194566c81abd5f8e09a44e64ea6286dd52f5354803e'

class Drawing(Sub32):
    icon_id = 'shirt-width-content-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Shirt width: a T-shirt above a double-headed arrow showing its width.
        self.add_polyline('shirt', (12, 4), (14, 4), (16, 6), (18, 4), (20, 4), (20, 14), (12, 14), closed=True)
        self.add_line('sleeve-l', (12, 4), (6, 9))
        self.add_line('sleeve-r', (20, 4), (26, 9))
        self.relate('connect', 'shirt', 'sleeve-l')
        self.relate('connect', 'shirt', 'sleeve-r')
        self.add_line('arrow', (2, 24), (30, 24))
        self.add_polyline('head-l', (6, 20), (2, 24), (6, 28))
        self.add_polyline('head-r', (26, 20), (30, 24), (26, 28))
        self.relate('connect', 'arrow', 'head-l')
        self.relate('connect', 'arrow', 'head-r')
