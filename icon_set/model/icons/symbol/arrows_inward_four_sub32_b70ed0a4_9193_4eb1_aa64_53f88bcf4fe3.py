"""Independent 32px profile of arrows-inward-four.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b70ed0a4-9193-4eb1-aa64-53f88bcf4fe3'
SOURCE_PATH = 'pictographic-primitives/symbol/four arrows pointing_b70ed0a4-9193-4eb1-aa64-53f88bcf4fe3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b70ed0a4-9193-4eb1-aa64-53f88bcf4fe3', 'pictographic-primitives/symbol/four arrows pointing_b70ed0a4-9193-4eb1-aa64-53f88bcf4fe3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrows-inward-four',)
SOLO_SOURCE_ICON_IDS = ('arrows-inward-four',)
REFERENCE_EXPORT_SHA256 = '019485938787eedb32841a29098c77074f5d56d97a38c4f7b06d45d5aa4aed4e'

class Drawing(Sub32):
    icon_id = 'arrows-inward-four-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (16, 10))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (11, 5), (16, 10))
        self.add_line('p2-r1-2', (16, 10), (21, 5))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (30, 16), (22, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (27, 11), (22, 16))
        self.add_line('p4-r1-2', (22, 16), (27, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (16, 30), (16, 22))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (21, 27), (16, 22))
        self.add_line('p6-r1-2', (16, 22), (11, 27))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (2, 16), (10, 16))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (5, 21), (10, 16))
        self.add_line('p8-r1-2', (10, 16), (5, 11))
        self.add_contour('path-8-1', 'p8-r1-1', 'p8-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-2')
        self.relate('connect', 'p7-r1-1', 'p8-r1-1')
        self.relate('connect', 'p7-r1-1', 'p8-r1-2')
