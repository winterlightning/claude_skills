"""Independent 32px profile of cup.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'db8ea339-df43-4389-a7c4-43da211daa67'
SOURCE_PATH = 'pictographic-primitives/symbol/cup_db8ea339-df43-4389-a7c4-43da211daa67.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('db8ea339-df43-4389-a7c4-43da211daa67', 'pictographic-primitives/symbol/cup_db8ea339-df43-4389-a7c4-43da211daa67.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cup',)
SOLO_SOURCE_ICON_IDS = ('cup',)
REFERENCE_EXPORT_SHA256 = '2ff267cb759b0a34844979a2e7f1160228fb7e6b13753a11deb3d8f40d659b18'

class Drawing(Sub32):
    icon_id = 'cup-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (22, 5))
        self.add_line('p1-r1-2', (22, 5), (22, 10))
        self.add_line('p1-r1-3', (22, 10), (22, 20))
        self.add_arc('p1-r1-4', (22, 20), (15, 27), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (15, 27), (9, 27))
        self.add_arc('p1-r1-6', (9, 27), (2, 20), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 20), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (22, 10), (24, 10))
        self.add_arc('p2-r1-2', (24, 10), (30, 16), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (30, 16), (24, 22), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (24, 22), (22, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
