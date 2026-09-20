"""Independent 32px profile of crossed-arrow.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'fbeb6dcd-ae52-4f65-a738-3e8d379b4665'
SOURCE_PATH = 'pictographic-primitives/symbol/crossed arrow_fbeb6dcd-ae52-4f65-a738-3e8d379b4665.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fbeb6dcd-ae52-4f65-a738-3e8d379b4665', 'pictographic-primitives/symbol/crossed arrow_fbeb6dcd-ae52-4f65-a738-3e8d379b4665.svg'),)
PROFILE_SOURCE_KEYS = ('solo/crossed-arrow',)
SOLO_SOURCE_ICON_IDS = ('crossed-arrow',)
REFERENCE_EXPORT_SHA256 = '6fc18413677f2ef6594eef2c59c828f05d400889716c5893bde876ca0cad5749'

class Drawing(Sub32):
    icon_id = 'crossed-arrow-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (13, 4))
        self.add_line('p1-r1-2', (13, 4), (4, 13))
        self.add_line('p1-r1-3', (4, 13), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (30, 2), (19, 4))
        self.add_line('p2-r1-2', (19, 4), (28, 13))
        self.add_line('p2-r1-3', (28, 13), (30, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (8, 8), (16, 16))
        self.add_line('p3-r1-2', (16, 16), (24, 24))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (24, 8), (16, 16))
        self.add_line('p4-r1-2', (16, 16), (8, 24))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_bezier('p5-r1-1', (2, 25), ((2, 23), (3, 22), (5, 22)))
        self.add_bezier('p5-r1-2', (5, 22), ((6, 22), (7, 23), (8, 24)))
        self.add_bezier('p5-r1-3', (8, 24), ((9, 25), (10, 26), (10, 27)))
        self.add_bezier('p5-r1-4', (10, 27), ((10, 29), (9, 30), (7, 30)))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
        self.add_bezier('p6-r1-1', (30, 25), ((30, 23), (29, 22), (27, 22)))
        self.add_bezier('p6-r1-2', (27, 22), ((26, 22), (25, 23), (24, 24)))
        self.add_bezier('p6-r1-3', (24, 24), ((23, 25), (22, 26), (22, 27)))
        self.add_bezier('p6-r1-4', (22, 27), ((22, 29), (23, 30), (25, 30)))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', closed=False)
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-2')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-2')
        self.relate("connect", 'p3-r1-2', 'p6-r1-2')
        self.relate("connect", 'p3-r1-2', 'p6-r1-3')
        self.relate("connect", 'p4-r1-2', 'p5-r1-2')
        self.relate("connect", 'p4-r1-2', 'p5-r1-3')
