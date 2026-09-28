"""Independent 32px profile of clapperboard-play-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '157c8513-84c8-4095-a71f-ec04c857771a'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/157c8513-84c8-4095-a71f-ec04c857771a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('157c8513-84c8-4095-a71f-ec04c857771a', 'icon_set/dist/gallery/combination-originals/157c8513-84c8-4095-a71f-ec04c857771a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/clapperboard-play-content',)
SOLO_SOURCE_ICON_IDS = ('clapperboard-play-content',)
REFERENCE_EXPORT_SHA256 = 'ecb4dadbe1558cc816fce95e698913af2a6a88ef971762211f8399be06bb96fa'

class Drawing(Sub32):
    icon_id = 'clapperboard-play-content-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 2), (24, 2))
        self.add_arc('p1-r1-2', (24, 2), (27, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (27, 5), (27, 27))
        self.add_arc('p1-r1-4', (27, 27), (24, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (24, 30), (8, 30))
        self.add_arc('p1-r1-6', (8, 30), (5, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (5, 27), (5, 5))
        self.add_arc('p1-r1-8', (5, 5), (8, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (5, 8), (27, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 2), (10, 8))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (11, 14), (11, 24))
        self.add_line('p4-r1-2', (11, 24), (21, 19))
        self.add_line('p4-r1-3', (21, 19), (11, 14))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
