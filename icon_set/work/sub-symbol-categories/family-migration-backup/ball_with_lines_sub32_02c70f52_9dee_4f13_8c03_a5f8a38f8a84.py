"""Independent 32px profile of ball-with-lines.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '02c70f52-9dee-4f13-8c03-a5f8a38f8a84'
SOURCE_PATH = 'pictographic-primitives/symbol/ball with lines_02c70f52-9dee-4f13-8c03-a5f8a38f8a84.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('02c70f52-9dee-4f13-8c03-a5f8a38f8a84', 'pictographic-primitives/symbol/ball with lines_02c70f52-9dee-4f13-8c03-a5f8a38f8a84.svg'),)
PROFILE_SOURCE_KEYS = ('solo/ball-with-lines',)
SOLO_SOURCE_ICON_IDS = ('ball-with-lines',)
REFERENCE_EXPORT_SHA256 = 'edcaccf2aa1dcf1b62b748fabe78aa61fd55ee72354fec029f28633d12128f1c'

class Drawing(Sub32):
    icon_id = 'ball-with-lines-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 2), (27, 8), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (27, 8), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (30, 16), (27, 24), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (27, 24), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (16, 30), (5, 24), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (5, 24), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-7', (2, 16), (5, 8), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-8', (5, 8), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (16, 8), (23, 12))
        self.add_line('p2-r1-2', (23, 12), (23, 20))
        self.add_line('p2-r1-3', (23, 20), (16, 24))
        self.add_line('p2-r1-4', (16, 24), (9, 20))
        self.add_line('p2-r1-5', (9, 20), (9, 12))
        self.add_line('p2-r1-6', (9, 12), (16, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (16, 8), (16, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (23, 12), (27, 8))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (23, 20), (27, 24))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (16, 24), (16, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (9, 20), (5, 24))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (9, 12), (5, 8))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-1', 'p4-r1-1')
        self.relate("connect", 'p1-r1-2', 'p4-r1-1')
        self.relate("connect", 'p1-r1-3', 'p5-r1-1')
        self.relate("connect", 'p1-r1-4', 'p5-r1-1')
        self.relate("connect", 'p1-r1-4', 'p6-r1-1')
        self.relate("connect", 'p1-r1-5', 'p6-r1-1')
        self.relate("connect", 'p1-r1-5', 'p7-r1-1')
        self.relate("connect", 'p1-r1-6', 'p7-r1-1')
        self.relate("connect", 'p1-r1-7', 'p8-r1-1')
        self.relate("connect", 'p1-r1-8', 'p3-r1-1')
        self.relate("connect", 'p1-r1-8', 'p8-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-2', 'p4-r1-1')
        self.relate("connect", 'p2-r1-2', 'p5-r1-1')
        self.relate("connect", 'p2-r1-3', 'p5-r1-1')
        self.relate("connect", 'p2-r1-3', 'p6-r1-1')
        self.relate("connect", 'p2-r1-4', 'p6-r1-1')
        self.relate("connect", 'p2-r1-4', 'p7-r1-1')
        self.relate("connect", 'p2-r1-5', 'p7-r1-1')
        self.relate("connect", 'p2-r1-5', 'p8-r1-1')
        self.relate("connect", 'p2-r1-6', 'p3-r1-1')
        self.relate("connect", 'p2-r1-6', 'p8-r1-1')
