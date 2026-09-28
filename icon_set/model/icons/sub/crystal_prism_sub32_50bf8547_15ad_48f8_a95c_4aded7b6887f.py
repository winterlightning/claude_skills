"""Independent 32px profile of crystal-prism.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '50bf8547-15ad-48f8-a95c-4aded7b6887f'
SOURCE_PATH = 'pictographic-primitives/symbol/crystal_50bf8547-15ad-48f8-a95c-4aded7b6887f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('50bf8547-15ad-48f8-a95c-4aded7b6887f', 'pictographic-primitives/symbol/crystal_50bf8547-15ad-48f8-a95c-4aded7b6887f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/crystal-prism',)
SOLO_SOURCE_ICON_IDS = ('crystal-prism',)
REFERENCE_EXPORT_SHA256 = '08dc4de9ea75b9d80f0980293b0eda1ffeaf8383a9701e91ac7c4df19ac91c44'

class Drawing(Sub32):
    icon_id = 'crystal-prism-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (27, 9))
        self.add_line('p1-r1-2', (27, 9), (27, 23))
        self.add_line('p1-r1-3', (27, 23), (16, 30))
        self.add_line('p1-r1-4', (16, 30), (5, 23))
        self.add_line('p1-r1-5', (5, 23), (5, 9))
        self.add_line('p1-r1-6', (5, 9), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (5, 9), (16, 13))
        self.add_line('p2-r1-2', (16, 13), (27, 9))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (5, 23), (16, 19))
        self.add_line('p3-r1-2', (16, 19), (27, 23))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (16, 13), (16, 19))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')
        self.relate("connect", 'p1-r1-2', 'p3-r1-2')
        self.relate("connect", 'p1-r1-3', 'p3-r1-2')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p3-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
