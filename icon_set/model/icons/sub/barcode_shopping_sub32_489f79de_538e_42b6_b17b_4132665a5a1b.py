"""Independent 32px profile of barcode-shopping.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '489f79de-538e-42b6-b17b-4132665a5a1b'
SOURCE_PATH = 'pictographic-primitives/shopping/barcode_489f79de-538e-42b6-b17b-4132665a5a1b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('489f79de-538e-42b6-b17b-4132665a5a1b', 'pictographic-primitives/shopping/barcode_489f79de-538e-42b6-b17b-4132665a5a1b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/barcode-shopping',)
SOLO_SOURCE_ICON_IDS = ('barcode-shopping',)
REFERENCE_EXPORT_SHA256 = 'f60bec9fb1ed24ae0f22bb9e0851ed4348efb649ba0533f2d9f75e86d83c92dd'

class Drawing(Sub32):
    icon_id = 'barcode-shopping-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'shopping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 5), (26, 5))
        self.add_arc('p1-r1-2', (26, 5), (30, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 9), (30, 23))
        self.add_arc('p1-r1-4', (30, 23), (26, 27), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (26, 27), (6, 27))
        self.add_arc('p1-r1-6', (6, 27), (2, 23), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 23), (2, 9))
        self.add_arc('p1-r1-8', (2, 9), (6, 5), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (9, 12), (9, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 12), (16, 20))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (23, 12), (23, 20))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
