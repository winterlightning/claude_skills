"""Independent 32px profile of cargo-ship.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1b1d9d6c-194c-5757-b0b8-4299a625eaaa'
SOURCE_PATH = 'pictographic-primitives/shipping/cargo boat_1b1d9d6c-194c-5757-b0b8-4299a625eaaa.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1b1d9d6c-194c-5757-b0b8-4299a625eaaa', 'pictographic-primitives/shipping/cargo boat_1b1d9d6c-194c-5757-b0b8-4299a625eaaa.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cargo-ship',)
SOLO_SOURCE_ICON_IDS = ('cargo-ship',)
REFERENCE_EXPORT_SHA256 = 'd5f58e07738e0d621e1ea16e28b9d357c769a39e443b5f5dc7293197bd7979d0'

class Drawing(Sub32):
    icon_id = 'cargo-ship-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/shipping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 19), (5, 19))
        self.add_line('p1-r1-2', (5, 19), (16, 19))
        self.add_line('p1-r1-3', (16, 19), (23, 19))
        self.add_line('p1-r1-4', (23, 19), (29, 19))
        self.add_line('p1-r1-5', (29, 19), (30, 19))
        self.add_line('p1-r1-6', (30, 19), (26, 27))
        self.add_line('p1-r1-7', (26, 27), (8, 27))
        self.add_line('p1-r1-8', (8, 27), (2, 19))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (5, 19), (5, 6))
        self.add_line('p2-r1-2', (5, 6), (16, 6))
        self.add_line('p2-r1-3', (16, 6), (16, 19))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (23, 19), (23, 12))
        self.add_line('p3-r1-2', (23, 12), (26, 12))
        self.add_line('p3-r1-3', (26, 12), (29, 12))
        self.add_line('p3-r1-4', (29, 12), (29, 19))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (26, 5), (26, 12))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-3')
        self.relate("connect", 'p1-r1-3', 'p2-r1-3')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-4')
        self.relate("connect", 'p1-r1-5', 'p3-r1-4')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-3', 'p4-r1-1')
