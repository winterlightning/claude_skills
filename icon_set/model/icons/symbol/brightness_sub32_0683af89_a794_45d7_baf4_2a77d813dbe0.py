"""Independent 32px profile of brightness.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '0683af89-a794-45d7-baf4-2a77d813dbe0'
SOURCE_PATH = 'pictographic-primitives/interface-essential/brightness_0683af89-a794-45d7-baf4-2a77d813dbe0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0683af89-a794-45d7-baf4-2a77d813dbe0', 'pictographic-primitives/interface-essential/brightness_0683af89-a794-45d7-baf4-2a77d813dbe0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/brightness',)
SOLO_SOURCE_ICON_IDS = ('brightness',)
REFERENCE_EXPORT_SHA256 = '748a551c9827230ebfc129520b93c5bcf871c47d776c9cbf0610074f475ce779'

class Drawing(Sub32):
    icon_id = 'brightness-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (12, 16), (20, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (20, 16), (12, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 5))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 27), (16, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 16), (5, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (27, 16), (30, 16))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (7, 7), (8, 8))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (24, 8), (25, 7))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (7, 25), (8, 24))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (24, 24), (25, 25))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
