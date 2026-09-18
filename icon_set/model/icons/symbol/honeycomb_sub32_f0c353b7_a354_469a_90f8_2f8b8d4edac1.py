"""Independent 32px profile of honeycomb.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'f0c353b7-a354-469a-90f8-2f8b8d4edac1'
SOURCE_PATH = 'pictographic-primitives/symbol/honeycomb_f0c353b7-a354-469a-90f8-2f8b8d4edac1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f0c353b7-a354-469a-90f8-2f8b8d4edac1', 'pictographic-primitives/symbol/honeycomb_f0c353b7-a354-469a-90f8-2f8b8d4edac1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/honeycomb',)
SOLO_SOURCE_ICON_IDS = ('honeycomb',)
REFERENCE_EXPORT_SHA256 = 'c6a0e6dbe23d2cc34c1cc08a833e9aeb86591a05e03e23eb77ce5bf823fcb4b2'

class Drawing(Sub32):
    icon_id = 'honeycomb-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (24, 7))
        self.add_line('p1-r1-2', (24, 7), (24, 16))
        self.add_line('p1-r1-3', (24, 16), (16, 21))
        self.add_line('p1-r1-4', (16, 21), (8, 16))
        self.add_line('p1-r1-5', (8, 16), (8, 7))
        self.add_line('p1-r1-6', (8, 7), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (8, 16), (2, 20))
        self.add_line('p2-r1-2', (2, 20), (2, 26))
        self.add_line('p2-r1-3', (2, 26), (8, 30))
        self.add_line('p2-r1-4', (8, 30), (16, 26))
        self.add_line('p2-r1-5', (16, 26), (16, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (24, 16), (30, 20))
        self.add_line('p3-r1-2', (30, 20), (30, 26))
        self.add_line('p3-r1-3', (30, 26), (24, 30))
        self.add_line('p3-r1-4', (24, 30), (16, 26))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-5')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-5')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p2-r1-4', 'p3-r1-4')
        self.relate('connect', 'p2-r1-5', 'p3-r1-4')
