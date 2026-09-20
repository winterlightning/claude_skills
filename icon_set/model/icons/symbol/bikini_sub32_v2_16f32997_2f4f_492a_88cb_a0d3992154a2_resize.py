"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '16f32997-2f4f-492a-88cb-a0d3992154a2'
SOURCE_PATH = 'icon_set/model/icons/symbol/bikini_sub32_v2_16f32997_2f4f_492a_88cb_a0d3992154a2.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '847117ea82615e1763129613eb4f200e3324e9148cff47e2f5e367e5adfa44b7'
SOURCE_REFERENCES = (('16f32997-2f4f-492a-88cb-a0d3992154a2', 'pictographic-primitives/symbol/bikini_16f32997-2f4f-492a-88cb-a0d3992154a2.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'bikini-sub32-v2-resize'
    variant_of = 'bikini-sub32-v2'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (5, 8), ((8, 10), (10, 12), (10, 15)))
        self.add_bezier('p1-r1-2', (10, 15), ((10, 18), (8, 19), (6, 19)))
        self.add_bezier('p1-r1-3', (6, 19), ((3, 19), (2, 18), (2, 15)))
        self.add_bezier('p1-r1-4', (2, 15), ((2, 12), (3, 10), (5, 8)))
        self.add_line('p2-r1-1', (5, 8), (12, 2))
        self.add_line('p2-r1-2', (12, 2), (15, 2))
        self.add_bezier('p3-r1-1', (19, 8), ((16, 10), (14, 12), (14, 15)))
        self.add_bezier('p3-r1-2', (14, 15), ((14, 18), (16, 19), (18, 19)))
        self.add_bezier('p3-r1-3', (18, 19), ((21, 19), (22, 18), (22, 15)))
        self.add_bezier('p3-r1-4', (22, 15), ((22, 12), (21, 10), (19, 8)))
        self.add_line('p4-r1-1', (19, 8), (12, 2))
        self.add_line('p4-r1-2', (12, 2), (9, 2))
        self.add_line('p5-r1-1', (10, 15), (14, 15))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p5-r1-1')
        self.relate('connect', 'p1-r1-2', 'p5-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-2')
        self.relate('connect', 'p2-r1-2', 'p4-r1-1')
        self.relate('connect', 'p2-r1-2', 'p4-r1-2')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-2', 'p5-r1-1')
        self.relate('connect', 'p3-r1-4', 'p4-r1-1')
