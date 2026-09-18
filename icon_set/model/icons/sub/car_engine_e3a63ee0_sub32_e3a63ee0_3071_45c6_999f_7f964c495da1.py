"""Independent 32px profile of car-engine-e3a63ee0.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e3a63ee0-3071-45c6-999f-7f964c495da1'
SOURCE_PATH = 'pictographic-primitives/transportation/car engine_e3a63ee0-3071-45c6-999f-7f964c495da1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e3a63ee0-3071-45c6-999f-7f964c495da1', 'pictographic-primitives/transportation/car engine_e3a63ee0-3071-45c6-999f-7f964c495da1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/car-engine-e3a63ee0',)
SOLO_SOURCE_ICON_IDS = ('car-engine-e3a63ee0',)
REFERENCE_EXPORT_SHA256 = 'dfac30424efb30f536d2f35ae82f55be693c5f26c5dc6c4936eaaf572dfc9203'

class Drawing(Sub32):
    icon_id = 'car-engine-e3a63ee0-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 16), (8, 10))
        self.add_line('p1-r1-2', (8, 10), (19, 10))
        self.add_line('p1-r1-3', (19, 10), (23, 15))
        self.add_line('p1-r1-4', (23, 15), (30, 15))
        self.add_line('p1-r1-5', (30, 15), (30, 27))
        self.add_line('p1-r1-6', (30, 27), (15, 27))
        self.add_line('p1-r1-7', (15, 27), (10, 22))
        self.add_line('p1-r1-8', (10, 22), (2, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (2, 13), (2, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 16), (8, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (10, 5), (19, 5))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (15, 5), (15, 10))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
