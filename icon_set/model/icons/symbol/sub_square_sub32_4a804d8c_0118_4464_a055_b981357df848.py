"""Independent 32px profile of sub-square.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4a804d8c-0118-4464-a055-b981357df848'
SOURCE_PATH = 'pictographic-primitives/symbol/sub square_4a804d8c-0118-4464-a055-b981357df848.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4a804d8c-0118-4464-a055-b981357df848', 'pictographic-primitives/symbol/sub square_4a804d8c-0118-4464-a055-b981357df848.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sub-square',)
SOLO_SOURCE_ICON_IDS = ('sub-square',)
REFERENCE_EXPORT_SHA256 = 'a3d3397e9b1db55a7bcfaa1442d2d3832268111d6f6b8d138b437cacef995d04'

class Drawing(Sub32):
    icon_id = 'sub-square-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (11, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 2), (2, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 2), (11, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (22, 2), (30, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (21, 11), (30, 2))
        self.add_line('p5-r1-2', (30, 2), (30, 11))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (21, 21), (30, 30))
        self.add_line('p6-r1-2', (30, 30), (30, 21))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (21, 30), (30, 30))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (11, 21), (2, 30))
        self.add_line('p8-r1-2', (2, 30), (2, 21))
        self.add_contour('path-8-1', 'p8-r1-1', 'p8-r1-2', closed=False)
        self.add_line('p9-r1-1', (2, 30), (10, 30))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-2')
        self.relate('connect', 'p6-r1-1', 'p7-r1-1')
        self.relate('connect', 'p6-r1-2', 'p7-r1-1')
        self.relate('connect', 'p8-r1-1', 'p9-r1-1')
        self.relate('connect', 'p8-r1-2', 'p9-r1-1')
