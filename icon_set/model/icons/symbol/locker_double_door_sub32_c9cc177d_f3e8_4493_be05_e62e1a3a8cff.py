"""Independent 32px profile of locker-double-door.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c9cc177d-f3e8-4493-be05-e62e1a3a8cff'
SOURCE_PATH = 'pictographic-primitives/symbol/locker_c9cc177d-f3e8-4493-be05-e62e1a3a8cff.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c9cc177d-f3e8-4493-be05-e62e1a3a8cff', 'pictographic-primitives/symbol/locker_c9cc177d-f3e8-4493-be05-e62e1a3a8cff.svg'),)
PROFILE_SOURCE_KEYS = ('solo/locker-double-door',)
SOLO_SOURCE_ICON_IDS = ('locker-double-door',)
REFERENCE_EXPORT_SHA256 = '2ef0e9aaec1d5ada11a44e2856b81ec1578cf1f88d07c6c7d7ecd47fe9d7c11c'

class Drawing(Sub32):
    icon_id = 'locker-double-door-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (30, 2))
        self.add_line('p1-r1-3', (30, 2), (30, 30))
        self.add_line('p1-r1-4', (30, 30), (16, 30))
        self.add_line('p1-r1-5', (16, 30), (2, 30))
        self.add_line('p1-r1-6', (2, 30), (2, 2))
        self.add_line('p1-r1-7', (2, 2), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (9, 16), (9, 19))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (23, 16), (23, 19))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
