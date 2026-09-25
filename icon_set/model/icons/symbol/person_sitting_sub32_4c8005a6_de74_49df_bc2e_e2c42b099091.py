"""Independent 32px profile of person-sitting.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4c8005a6-de74-49df-bc2e-e2c42b099091'
SOURCE_PATH = 'pictographic-primitives/symbol/person sitting_4c8005a6-de74-49df-bc2e-e2c42b099091.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4c8005a6-de74-49df-bc2e-e2c42b099091', 'pictographic-primitives/symbol/person sitting_4c8005a6-de74-49df-bc2e-e2c42b099091.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person-sitting',)
SOLO_SOURCE_ICON_IDS = ('person-sitting',)
REFERENCE_EXPORT_SHA256 = '79b1bd3cf57b53c2d13e9ebcb5577027c99ef780e9309c5b11fbb834528fd78c'

class Drawing(Sub32):
    icon_id = 'person-sitting-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (9, 6), (17, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (17, 6), (9, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (10, 17), (5, 23))
        self.add_line('p2-r1-2', (5, 23), (19, 23))
        self.add_line('p2-r1-3', (19, 23), (27, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (10, 17), (24, 17))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
