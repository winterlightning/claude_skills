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
        # Board with a clapper band (one stripe) and a play chevron.
        self.add_line('p1-r1-1', (7, 2), (25, 2))
        self.add_arc('p1-r1-2', (25, 2), (28, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (28, 5), (28, 27))
        self.add_arc('p1-r1-4', (28, 27), (25, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (25, 30), (7, 30))
        self.add_arc('p1-r1-6', (7, 30), (4, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (4, 27), (4, 5))
        self.add_arc('p1-r1-8', (4, 5), (7, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=True)
        self.add_line('p2-r1-1', (4, 10), (28, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (12, 10), (20, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (14, 18), (18, 20))
        self.add_line('p4-r1-2', (18, 20), (14, 22))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
