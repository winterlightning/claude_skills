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
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 20), (9, 23))
        self.add_line('p1-r1-2', (9, 23), (15, 19))
        self.add_line('p1-r1-3', (15, 19), (13, 27))
        self.add_line('p1-r1-4', (13, 27), (21, 24))
        self.add_line('p1-r1-5', (21, 24), (22, 16))
        self.add_line('p1-r1-6', (22, 16), (27, 13))
        self.add_bezier('p1-r1-7', (27, 13), ((29, 12), (30, 10), (30, 9)))
        self.add_bezier('p1-r1-8', (30, 9), ((30, 7), (29, 6), (27, 6)))
        self.add_bezier('p1-r1-9', (27, 6), ((27, 6), (26, 6), (25, 7)))
        self.add_line('p1-r1-10', (25, 7), (22, 8))
        self.add_line('p1-r1-11', (22, 8), (13, 5))
        self.add_bezier('p1-r1-12', (13, 5), ((11, 5), (9, 7), (9, 8)))
        self.add_bezier('p1-r1-13', (9, 8), ((9, 9), (9, 9), (9, 10)))
        self.add_line('p1-r1-14', (9, 10), (15, 13))
        self.add_line('p1-r1-15', (15, 13), (9, 16))
        self.add_line('p1-r1-16', (9, 16), (3, 14))
        self.add_line('p1-r1-17', (3, 14), (2, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', closed=False)
