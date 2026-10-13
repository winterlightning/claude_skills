"""Independent 32px profile of backspace-key-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'f52af45c-34ba-4c0c-a151-62677a3ff4ab'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/f52af45c-34ba-4c0c-a151-62677a3ff4ab.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f52af45c-34ba-4c0c-a151-62677a3ff4ab', 'icon_set/dist/gallery/combination-originals/f52af45c-34ba-4c0c-a151-62677a3ff4ab.svg'),)
PROFILE_SOURCE_KEYS = ('solo/backspace-key-content',)
SOLO_SOURCE_ICON_IDS = ('backspace-key-content',)
REFERENCE_EXPORT_SHA256 = '7c4a05af2fac6b6eddb166d87f8fee1157d03d507d10a79cce3e95cf04b0510c'

class Drawing(Sub32):
    icon_id = 'backspace-key-content-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 6), (30, 6))
        self.add_line('p1-r1-2', (30, 6), (30, 26))
        self.add_line('p1-r1-3', (30, 26), (10, 26))
        self.add_line('p1-r1-4', (10, 26), (2, 16))
        self.add_line('p1-r1-5', (2, 16), (10, 6))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (16, 13), (20, 16))
        self.add_line('p2-r1-2', (20, 16), (23, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 20), (20, 16))
        self.add_line('p3-r1-2', (20, 16), (23, 12))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
