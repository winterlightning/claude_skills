"""Independent 32px profile of open-umbrella-with-scalloped-canopy.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '05df3587-30f8-46af-94fa-4633b7974c08'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/umbrella_05df3587-30f8-46af-94fa-4633b7974c08.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('05df3587-30f8-46af-94fa-4633b7974c08', 'pictographic-primitives/accessories/batch-07/umbrella_05df3587-30f8-46af-94fa-4633b7974c08.svg'),)
PROFILE_SOURCE_KEYS = ('solo/open-umbrella-with-scalloped-canopy',)
SOLO_SOURCE_ICON_IDS = ('open-umbrella-with-scalloped-canopy',)
REFERENCE_EXPORT_SHA256 = '947def58691580e182065cef706ba5b5a87cce0b6073970284ce50b3c640fda6'

class Drawing(Sub32):
    icon_id = 'open-umbrella-with-scalloped-canopy-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'accessories'
    categories = ('accessories', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 18), (30, 18), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 18), (22, 18), radius_x=4, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('p1-r1-3', (22, 18), (10, 18), radius_x=6, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('p1-r1-4', (10, 18), (2, 18), radius_x=4, radius_y=2, large_arc=False, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=True)
        self.add_line('p2-r1-1', (16, 2), (16, 4))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 14), (16, 26))
        self.add_arc('p3-r1-2', (16, 26), (8, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'path-1-1', 'path-2-1')
        self.relate('connect', 'path-1-1', 'path-3-1')
