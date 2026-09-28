"""Independent 32px profile of rain-cloud-slanted.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4e4a67db-a059-47f2-8135-65269c56d9fb'
SOURCE_PATH = 'pictographic-primitives/symbol/rain cloud_4e4a67db-a059-47f2-8135-65269c56d9fb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4e4a67db-a059-47f2-8135-65269c56d9fb', 'pictographic-primitives/symbol/rain cloud_4e4a67db-a059-47f2-8135-65269c56d9fb.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rain-cloud-slanted',)
SOLO_SOURCE_ICON_IDS = ('rain-cloud-slanted',)
REFERENCE_EXPORT_SHA256 = 'c46cd1db85db73ef8169a9a941daa9d31fb6a06129a91a3201569cfa8bd8b7ef'

class Drawing(Sub32):
    icon_id = 'rain-cloud-slanted-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (8, 10), (24, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (24, 10), (30, 14), radius_x=6, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (30, 14), (24, 18), radius_x=6, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (24, 18), (8, 18))
        self.add_arc('p1-r1-5', (8, 18), (2, 14), radius_x=6, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (2, 14), (8, 10), radius_x=6, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (8, 25), (3, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (18, 25), (13, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (28, 25), (23, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
