"""Independent 32px profile of hand-down-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ce80faa0-dd47-4d1a-9ecb-fb349333dde8'
SOURCE_PATH = 'pictographic-primitives/state/hand down 1_ce80faa0-dd47-4d1a-9ecb-fb349333dde8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ce80faa0-dd47-4d1a-9ecb-fb349333dde8', 'pictographic-primitives/state/hand down 1_ce80faa0-dd47-4d1a-9ecb-fb349333dde8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hand-down-1',)
SOLO_SOURCE_ICON_IDS = ('hand-down-1',)
REFERENCE_EXPORT_SHA256 = 'fb4623487415fddfd564be9944deab4c5d09d02d5f1924be5c7ac64fa58eb37d'

class Drawing(Sub32):
    icon_id = 'hand-down-1-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (24, 5), ((21, 7), (18, 8), (15, 8)))
        self.add_bezier('p1-r1-2', (15, 8), ((11, 8), (5, 12), (2, 15)))
        self.add_bezier('p1-r1-3', (2, 15), ((2, 17), (3, 17), (4, 17)))
        self.add_bezier('p1-r1-4', (4, 17), ((5, 17), (8, 16), (11, 15)))
        self.add_line('p1-r1-5', (11, 15), (6, 22))
        self.add_bezier('p1-r1-6', (6, 22), ((6, 23), (5, 24), (5, 25)))
        self.add_bezier('p1-r1-7', (5, 25), ((5, 26), (7, 27), (10, 27)))
        self.add_line('p1-r1-8', (10, 27), (15, 27))
        self.add_bezier('p1-r1-9', (15, 27), ((17, 27), (17, 25), (19, 24)))
        self.add_line('p1-r1-10', (19, 24), (30, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
