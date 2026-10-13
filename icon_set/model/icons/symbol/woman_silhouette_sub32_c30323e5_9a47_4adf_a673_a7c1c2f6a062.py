"""Independent 32px profile of woman-silhouette.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c30323e5-9a47-4adf-a673-a7c1c2f6a062'
SOURCE_PATH = 'pictographic-primitives/symbol/women_c30323e5-9a47-4adf-a673-a7c1c2f6a062.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c30323e5-9a47-4adf-a673-a7c1c2f6a062', 'pictographic-primitives/symbol/women_c30323e5-9a47-4adf-a673-a7c1c2f6a062.svg'),)
PROFILE_SOURCE_KEYS = ('solo/woman-silhouette',)
SOLO_SOURCE_ICON_IDS = ('woman-silhouette',)
REFERENCE_EXPORT_SHA256 = '9bf899d7cfe29f1b0b9a65ae33a5248fa78dc58e0b557fc714e0c4a00c6b5492'

class Drawing(Sub32):
    icon_id = 'woman-silhouette-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 19), (2, 16))
        self.add_arc('p1-r1-2', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 16), (30, 19))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (2, 30), (2, 28))
        self.add_line('p2-r1-2', (2, 28), (12, 24))
        self.add_line('p2-r1-3', (12, 24), (12, 22))
        self.add_arc('p2-r1-4', (12, 22), (11, 18), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (11, 18), (11, 14))
        self.add_line('p2-r1-6', (11, 14), (16, 10))
        self.add_line('p2-r1-7', (16, 10), (21, 14))
        self.add_line('p2-r1-8', (21, 14), (21, 18))
        self.add_arc('p2-r1-9', (21, 18), (20, 22), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-10', (20, 22), (20, 24))
        self.add_line('p2-r1-11', (20, 24), (30, 28))
        self.add_line('p2-r1-12', (30, 28), (30, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', 'p2-r1-12', closed=False)
