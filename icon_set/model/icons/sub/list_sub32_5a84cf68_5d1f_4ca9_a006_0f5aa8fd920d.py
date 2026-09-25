"""Independent 32px profile of list.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '5a84cf68-5d1f-4ca9-a006-0f5aa8fd920d'
SOURCE_PATH = 'pictographic-primitives/content/list_5a84cf68-5d1f-4ca9-a006-0f5aa8fd920d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5a84cf68-5d1f-4ca9-a006-0f5aa8fd920d', 'pictographic-primitives/content/list_5a84cf68-5d1f-4ca9-a006-0f5aa8fd920d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/list',)
SOLO_SOURCE_ICON_IDS = ('list',)
REFERENCE_EXPORT_SHA256 = '1863e4d4a061b2f5ddd6123a7997498c233b900f1b2546d78a74c0150bce541b'

class Drawing(Sub32):
    icon_id = 'list-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'content'
    categories = ('primitives', 'content')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 5), (6, 13))
        self.add_line('p1-r1-2', (6, 13), (2, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (19, 11), (30, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (13, 19), (6, 27))
        self.add_line('p3-r1-2', (6, 27), (2, 24))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (19, 25), (30, 25))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
