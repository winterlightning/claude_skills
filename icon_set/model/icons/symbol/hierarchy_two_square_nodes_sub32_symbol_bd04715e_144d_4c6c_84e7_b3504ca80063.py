"""Independent 32px profile of hierarchy-two-square-nodes.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'bd04715e-144d-4c6c-84e7-b3504ca80063'
SOURCE_PATH = 'pictographic-primitives/programing/hierarchy_bd04715e-144d-4c6c-84e7-b3504ca80063.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bd04715e-144d-4c6c-84e7-b3504ca80063', 'pictographic-primitives/programing/hierarchy_bd04715e-144d-4c6c-84e7-b3504ca80063.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hierarchy-two-square-nodes',)
SOLO_SOURCE_ICON_IDS = ('hierarchy-two-square-nodes',)
REFERENCE_EXPORT_SHA256 = 'aef39f16091aa56e8e083fb4c5fda10865b79c2467ffdd9c7b10c0340367cc80'

class DrawingContainerSymbol(Sub32):
    icon_id = 'hierarchy-two-square-nodes-sub32-symbol'
    related_origin_icon_id = 'hierarchy-two-square-nodes-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/hierarchy-two-square-nodes-sub32'
    counterpart_icon_id = 'hierarchy-two-square-nodes-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/programming'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 2), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (19, 2))
        self.add_line('p1-r1-3', (19, 2), (19, 8))
        self.add_line('p1-r1-4', (19, 8), (16, 8))
        self.add_line('p1-r1-5', (16, 8), (13, 8))
        self.add_line('p1-r1-6', (13, 8), (13, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (16, 8), (16, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 16), (6, 16))
        self.add_line('p3-r1-2', (6, 16), (6, 22))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (2, 22), (6, 22))
        self.add_line('p4-r1-2', (6, 22), (10, 22))
        self.add_line('p4-r1-3', (10, 22), (10, 30))
        self.add_line('p4-r1-4', (10, 30), (6, 30))
        self.add_line('p4-r1-5', (6, 30), (2, 30))
        self.add_line('p4-r1-6', (2, 30), (2, 22))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', closed=False)
        self.add_line('p5-r1-1', (16, 16), (26, 16))
        self.add_line('p5-r1-2', (26, 16), (26, 22))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (22, 22), (26, 22))
        self.add_line('p6-r1-2', (26, 22), (30, 22))
        self.add_line('p6-r1-3', (30, 22), (30, 30))
        self.add_line('p6-r1-4', (30, 30), (26, 30))
        self.add_line('p6-r1-5', (26, 30), (22, 30))
        self.add_line('p6-r1-6', (22, 30), (22, 22))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', 'p6-r1-5', 'p6-r1-6', closed=False)
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-2')
        self.relate('connect', 'p5-r1-2', 'p6-r1-1')
        self.relate('connect', 'p5-r1-2', 'p6-r1-2')
