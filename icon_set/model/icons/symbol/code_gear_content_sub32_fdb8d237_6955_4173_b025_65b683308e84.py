"""Independent 32px profile of code-gear-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'fdb8d237-6955-4173-b025-65b683308e84'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/fdb8d237-6955-4173-b025-65b683308e84.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fdb8d237-6955-4173-b025-65b683308e84', 'icon_set/dist/gallery/combination-originals/fdb8d237-6955-4173-b025-65b683308e84.svg'),)
PROFILE_SOURCE_KEYS = ('solo/code-gear-content',)
SOLO_SOURCE_ICON_IDS = ('code-gear-content',)
REFERENCE_EXPORT_SHA256 = 'b0b55ee24401989dd47ec8cb1bd27d40c8122fdcbbd457810a7a82f944cf290f'

class Drawing(Sub32):
    icon_id = 'code-gear-content-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 5), (19, 5))
        self.add_line('p1-r1-2', (19, 5), (19, 10))
        self.add_line('p1-r1-3', (19, 10), (23, 13))
        self.add_line('p1-r1-4', (23, 13), (23, 20))
        self.add_line('p1-r1-5', (23, 20), (19, 22))
        self.add_line('p1-r1-6', (19, 22), (19, 27))
        self.add_line('p1-r1-7', (19, 27), (13, 27))
        self.add_line('p1-r1-8', (13, 27), (13, 22))
        self.add_line('p1-r1-9', (13, 22), (9, 20))
        self.add_line('p1-r1-10', (9, 20), (9, 13))
        self.add_line('p1-r1-11', (9, 13), (13, 10))
        self.add_line('p1-r1-12', (13, 10), (13, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (3, 12), (2, 16))
        self.add_line('p2-r1-2', (2, 16), (3, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (29, 12), (30, 16))
        self.add_line('p3-r1-2', (30, 16), (29, 20))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
