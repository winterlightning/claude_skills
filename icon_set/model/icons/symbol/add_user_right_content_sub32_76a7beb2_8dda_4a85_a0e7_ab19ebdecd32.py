"""Independent 32px profile of add-user-right-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '76a7beb2-8dda-4a85-a0e7-ab19ebdecd32'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/76a7beb2-8dda-4a85-a0e7-ab19ebdecd32.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('76a7beb2-8dda-4a85-a0e7-ab19ebdecd32', 'icon_set/dist/gallery/combination-originals/76a7beb2-8dda-4a85-a0e7-ab19ebdecd32.svg'), ('e68e4095-a045-40e9-81f2-491f7d5b6a83', 'icon_set/dist/gallery/combination-originals/e68e4095-a045-40e9-81f2-491f7d5b6a83.svg'))
PROFILE_SOURCE_KEYS = ('solo/add-user-right-content', 'solo/add-user-profile-content')
SOLO_SOURCE_ICON_IDS = ('add-user-right-content', 'add-user-profile-content')
REFERENCE_EXPORT_SHA256 = 'dedb42ba8d37a0a70f138cb724d23a5b9e2dcbeb071e8ce2d06a970d11794b36'

class Drawing(Sub32):
    icon_id = 'add-user-right-content-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (8, 9), (16, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 9), (8, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (2, 27), (22, 27), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (27, 9), (24, 9))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (27, 9), (30, 9))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (27, 9), (27, 6))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (27, 9), (27, 12))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p6-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p6-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
