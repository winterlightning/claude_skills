"""Independent 32px profile of boot.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '30304fad-17a9-493d-ac22-7d98eda09d1a'
SOURCE_PATH = 'pictographic-primitives/symbol/boot_30304fad-17a9-493d-ac22-7d98eda09d1a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('30304fad-17a9-493d-ac22-7d98eda09d1a', 'pictographic-primitives/symbol/boot_30304fad-17a9-493d-ac22-7d98eda09d1a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/boot',)
SOLO_SOURCE_ICON_IDS = ('boot',)
REFERENCE_EXPORT_SHA256 = '788278e8832821aae48003727b315481e98a74c217693b2d0ca0d1fb7bc45c10'

class Drawing(Sub32):
    icon_id = 'boot-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (16, 10))
        self.add_line('p1-r1-3', (16, 10), (16, 16))
        self.add_arc('p1-r1-4', (16, 16), (22, 22), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (22, 22), (25, 22))
        self.add_arc('p1-r1-6', (25, 22), (30, 27), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (30, 27), (30, 30))
        self.add_line('p1-r1-8', (30, 30), (14, 30))
        self.add_line('p1-r1-9', (14, 30), (11, 27))
        self.add_line('p1-r1-10', (11, 27), (2, 27))
        self.add_line('p1-r1-11', (2, 27), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_line('p2-r1-1', (16, 10), (21, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 16), (21, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
