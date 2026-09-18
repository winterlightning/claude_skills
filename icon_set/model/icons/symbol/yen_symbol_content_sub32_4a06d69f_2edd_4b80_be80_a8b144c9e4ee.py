"""Independent 32px profile of yen-symbol-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4a06d69f-2edd-4b80-be80-a8b144c9e4ee'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/4a06d69f-2edd-4b80-be80-a8b144c9e4ee.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4a06d69f-2edd-4b80-be80-a8b144c9e4ee', 'icon_set/dist/gallery/combination-originals/4a06d69f-2edd-4b80-be80-a8b144c9e4ee.svg'),)
PROFILE_SOURCE_KEYS = ('solo/yen-symbol-content',)
SOLO_SOURCE_ICON_IDS = ('yen-symbol-content',)
REFERENCE_EXPORT_SHA256 = 'e96d1fa889bbb45aa38e0ba78e43f4afbf0f256de107ddc8d71da9320572be02'

class Drawing(Sub32):
    icon_id = 'yen-symbol-content-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 2), (16, 16))
        self.add_line('p1-r1-2', (16, 16), (27, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 16), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (8, 19), (16, 19))
        self.add_line('p3-r1-2', (16, 19), (24, 19))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
