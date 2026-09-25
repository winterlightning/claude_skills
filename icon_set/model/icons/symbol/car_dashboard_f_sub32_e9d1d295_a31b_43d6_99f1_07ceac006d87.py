"""Independent 32px profile of car-dashboard-f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e9d1d295-a31b-43d6-99f1-07ceac006d87'
SOURCE_PATH = 'pictographic-primitives/transportation/car dashboard f_e9d1d295-a31b-43d6-99f1-07ceac006d87.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e9d1d295-a31b-43d6-99f1-07ceac006d87', 'pictographic-primitives/transportation/car dashboard f_e9d1d295-a31b-43d6-99f1-07ceac006d87.svg'),)
PROFILE_SOURCE_KEYS = ('solo/car-dashboard-f',)
SOLO_SOURCE_ICON_IDS = ('car-dashboard-f',)
REFERENCE_EXPORT_SHA256 = '98a3260a53748bf5ef5c2b92fb7f9f72bdce55b45fa8e2e82b029b64e6c9b4cf'

class Drawing(Sub32):
    icon_id = 'car-dashboard-f-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    categories = ('transportation', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (14, 2), (2, 2))
        self.add_line('p1-r1-2', (2, 2), (2, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 21), (2, 13))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (11, 12), (2, 12))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (30, 7), (11, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
