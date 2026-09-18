"""Independent 32px profile of chili-peppers-two.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2d596f49-a091-4ed3-be42-188e0442128e'
SOURCE_PATH = 'pictographic-primitives/symbol/two chilies_2d596f49-a091-4ed3-be42-188e0442128e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2d596f49-a091-4ed3-be42-188e0442128e', 'pictographic-primitives/symbol/two chilies_2d596f49-a091-4ed3-be42-188e0442128e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/chili-peppers-two',)
SOLO_SOURCE_ICON_IDS = ('chili-peppers-two',)
REFERENCE_EXPORT_SHA256 = 'e31d3953a889cb4e8b0deaeace4e1636607ac8791d85bb8d367f85ad7069ab67'

class Drawing(Sub32):
    icon_id = 'chili-peppers-two-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 5), (24, 4), radius_x=31, radius_y=31, large_arc=False, sweep=False)
        self.add_arc('p1-r1-2', (24, 4), (28, 8), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (28, 8), (24, 13), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (24, 13), (2, 5), radius_x=22, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (28, 8), (30, 7))
        self.add_line('p2-r1-2', (30, 7), (30, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (2, 22), (24, 21), radius_x=31, radius_y=31, large_arc=False, sweep=False)
        self.add_arc('p3-r1-2', (24, 21), (28, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (28, 25), (24, 30), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (24, 30), (2, 22), radius_x=22, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (28, 25), (30, 24))
        self.add_line('p4-r1-2', (30, 24), (30, 19))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-3', 'p4-r1-1')
