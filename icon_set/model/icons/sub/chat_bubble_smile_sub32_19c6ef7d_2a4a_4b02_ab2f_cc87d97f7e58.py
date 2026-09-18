"""Independent 32px profile of chat-bubble-smile.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '19c6ef7d-2a4a-4b02-ab2f-cc87d97f7e58'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble round smile_19c6ef7d-2a4a-4b02-ab2f-cc87d97f7e58.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('19c6ef7d-2a4a-4b02-ab2f-cc87d97f7e58', 'pictographic-primitives/symbol/messages bubble round smile_19c6ef7d-2a4a-4b02-ab2f-cc87d97f7e58.svg'),)
PROFILE_SOURCE_KEYS = ('solo/chat-bubble-smile',)
SOLO_SOURCE_ICON_IDS = ('chat-bubble-smile',)
REFERENCE_EXPORT_SHA256 = '8923ba53661b908a7f96607eef4c0e70762b0897a21ef7e8d2b08956c4d888fd'

class Drawing(Sub32):
    icon_id = 'chat-bubble-smile-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 15), ((2, 9), (8, 5), (16, 5)))
        self.add_bezier('p1-r1-2', (16, 5), ((24, 5), (30, 9), (30, 15)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (30, 15), ((30, 22), (23, 27), (16, 27)))
        self.add_bezier('p2-r1-2', (16, 27), ((12, 27), (10, 27), (8, 24)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (8, 24), (2, 27))
        self.add_line('p3-r1-2', (2, 27), (4, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_bezier('p4-r1-1', (4, 21), ((3, 20), (2, 17), (2, 15)))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (12, 12), (12, 12))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (20, 12), (20, 12))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_arc('p7-r1-1', (12, 19), (20, 19), radius_x=4, radius_y=2, large_arc=False, sweep=False)
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p4-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
