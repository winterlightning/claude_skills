"""Independent 32px profile of star-burst.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'dcbfa235-b6ab-4926-bc2a-34d5ce7146d8'
SOURCE_PATH = 'pictographic-primitives/symbol/star burst_dcbfa235-b6ab-4926-bc2a-34d5ce7146d8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dcbfa235-b6ab-4926-bc2a-34d5ce7146d8', 'pictographic-primitives/symbol/star burst_dcbfa235-b6ab-4926-bc2a-34d5ce7146d8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/star-burst',)
SOLO_SOURCE_ICON_IDS = ('star-burst',)
REFERENCE_EXPORT_SHA256 = '508bdac55c1781bf024449e5ba27e16a8a0045c18316b9a42abf9540e951bf17'

class Drawing(Sub32):
    icon_id = 'star-burst-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 27), (9, 22))
        self.add_line('p1-r1-2', (9, 22), (2, 21))
        self.add_line('p1-r1-3', (2, 21), (6, 16))
        self.add_line('p1-r1-4', (6, 16), (3, 10))
        self.add_line('p1-r1-5', (3, 10), (10, 10))
        self.add_line('p1-r1-6', (10, 10), (13, 5))
        self.add_line('p1-r1-7', (13, 5), (19, 10))
        self.add_line('p1-r1-8', (19, 10), (26, 8))
        self.add_line('p1-r1-9', (26, 8), (26, 14))
        self.add_line('p1-r1-10', (26, 14), (30, 18))
        self.add_line('p1-r1-11', (30, 18), (23, 20))
        self.add_line('p1-r1-12', (23, 20), (21, 26))
        self.add_line('p1-r1-13', (21, 26), (16, 22))
        self.add_line('p1-r1-14', (16, 22), (10, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', closed=False)
