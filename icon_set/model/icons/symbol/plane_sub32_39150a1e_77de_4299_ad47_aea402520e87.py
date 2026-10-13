"""Independent 32px profile of plane.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '39150a1e-77de-4299-ad47-aea402520e87'
SOURCE_PATH = 'pictographic-primitives/travel/plane_39150a1e-77de-4299-ad47-aea402520e87.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('39150a1e-77de-4299-ad47-aea402520e87', 'pictographic-primitives/travel/plane_39150a1e-77de-4299-ad47-aea402520e87.svg'), ('18f96efa-93ca-4c4e-9556-e131c14f8073', 'pictographic-primitives/travel/plane 1_18f96efa-93ca-4c4e-9556-e131c14f8073.svg'))
PROFILE_SOURCE_KEYS = ('solo/plane', 'solo/plane-1')
SOLO_SOURCE_ICON_IDS = ('plane', 'plane-1')
REFERENCE_EXPORT_SHA256 = '5b934e420dd373c44ac38f1b5bd3cc796c83de6b81f026a6148be9dbcc821100'

class Drawing(Sub32):
    icon_id = 'plane-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'travel'
    categories = ('travel', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 12), (26, 12))
        self.add_arc('p1-r1-2', (26, 12), (26, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (26, 20), (6, 20))
        self.add_arc('p1-r1-4', (6, 20), (6, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=True)
        self.add_line('p2-r1-1', (20, 12), (16, 4))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (20, 20), (16, 28))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (8, 12), (6, 4))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (8, 20), (6, 28))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p5-r1-1')
