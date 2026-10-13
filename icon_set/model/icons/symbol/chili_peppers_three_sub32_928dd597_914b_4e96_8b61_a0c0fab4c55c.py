"""Independent 32px profile of chili-peppers-three.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '928dd597-914b-4e96-8b61-a0c0fab4c55c'
SOURCE_PATH = 'pictographic-primitives/symbol/three chilies_928dd597-914b-4e96-8b61-a0c0fab4c55c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('928dd597-914b-4e96-8b61-a0c0fab4c55c', 'pictographic-primitives/symbol/three chilies_928dd597-914b-4e96-8b61-a0c0fab4c55c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/chili-peppers-three',)
SOLO_SOURCE_ICON_IDS = ('chili-peppers-three',)
REFERENCE_EXPORT_SHA256 = 'd0c2b34b6b095d42ff727be1b01fd5394b486e06a726d35ae5c88ce8ea7f9036'

class Drawing(Sub32):
    icon_id = 'chili-peppers-three-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 4), (10, 4))
        self.add_bezier('p1-r1-2', (10, 4), ((10, 9), (7, 13), (3, 16)))
        self.add_bezier('p1-r1-3', (3, 16), ((2, 13), (2, 9), (2, 4)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=True)
        self.add_line('p2-r1-1', (6, 4), (6, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (22, 4), (30, 4))
        self.add_bezier('p3-r1-2', (30, 4), ((30, 9), (30, 13), (29, 16)))
        self.add_bezier('p3-r1-3', (29, 16), ((25, 13), (22, 9), (22, 4)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=True)
        self.add_line('p4-r1-1', (26, 4), (26, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (12, 20), (20, 20))
        self.add_bezier('p5-r1-2', (20, 20), ((20, 24), (19, 27), (14, 30)))
        self.add_bezier('p5-r1-3', (14, 30), ((12, 27), (12, 24), (12, 20)))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=True)
        self.add_line('p6-r1-1', (16, 20), (16, 16))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
