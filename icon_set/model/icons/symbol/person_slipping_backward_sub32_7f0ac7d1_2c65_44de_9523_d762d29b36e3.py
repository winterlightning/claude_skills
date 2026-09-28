"""Independent 32px profile of person-slipping-backward.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '7f0ac7d1-2c65-44de-9523-d762d29b36e3'
SOURCE_PATH = 'pictographic-primitives/symbol/person slipping rocky_7f0ac7d1-2c65-44de-9523-d762d29b36e3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7f0ac7d1-2c65-44de-9523-d762d29b36e3', 'pictographic-primitives/symbol/person slipping rocky_7f0ac7d1-2c65-44de-9523-d762d29b36e3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person-slipping-backward',)
SOLO_SOURCE_ICON_IDS = ('person-slipping-backward',)
REFERENCE_EXPORT_SHA256 = '249ebfd3a3f94ea1b895bb5f53fe21256f6291890c951fdd8fe4ffdc3b53946b'

class Drawing(Sub32):
    icon_id = 'person-slipping-backward-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 6), (24, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (24, 6), (16, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (16, 15), ((15, 18), (14, 20), (13, 22)))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (13, 22), (8, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 15), (8, 13))
        self.add_line('p4-r1-2', (8, 13), (5, 5))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (16, 15), (25, 19))
        self.add_line('p5-r1-2', (25, 19), (30, 22))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (13, 22), (5, 21))
        self.add_line('p6-r1-2', (5, 21), (2, 27))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p2-r1-1', 'p6-r1-1')
        self.relate('connect', 'p3-r1-1', 'p6-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
