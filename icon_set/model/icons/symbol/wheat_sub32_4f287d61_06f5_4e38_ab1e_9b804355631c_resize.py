"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '4f287d61-06f5-4e38-ab1e-9b804355631c'
SOURCE_PATH = 'icon_set/model/icons/symbol/wheat_sub32_4f287d61_06f5_4e38_ab1e_9b804355631c.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '10193f9a24d209f4adf940820c885468cf28e4b58f071d7c463d5348d706b517'
SOURCE_REFERENCES = (('4f287d61-06f5-4e38-ab1e-9b804355631c', 'pictographic-primitives/farming/wheat_4f287d61-06f5-4e38-ab1e-9b804355631c.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'wheat-sub32-resize'
    variant_of = 'wheat-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'farming'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (10, 2), ((12, 3), (14, 3), (14, 6)))
        self.add_bezier('p1-r1-2', (14, 6), ((14, 8), (12, 9), (10, 10)))
        self.add_bezier('p1-r1-3', (10, 10), ((8, 10), (6, 8), (6, 6)))
        self.add_bezier('p1-r1-4', (6, 6), ((6, 3), (8, 3), (10, 2)))
        self.add_line('p2-r1-1', (10, 10), (10, 17))
        self.add_line('p2-r1-2', (10, 17), (10, 22))
        self.add_bezier('p3-r1-1', (10, 17), ((9, 15), (5, 13), (2, 13)))
        self.add_bezier('p3-r1-2', (2, 13), ((2, 16), (4, 18), (7, 18)))
        self.add_bezier('p3-r1-3', (7, 18), ((8, 18), (9, 17), (10, 17)))
        self.add_bezier('p4-r1-1', (10, 17), ((11, 15), (15, 13), (18, 13)))
        self.add_bezier('p4-r1-2', (18, 13), ((18, 16), (16, 18), (13, 18)))
        self.add_bezier('p4-r1-3', (13, 18), ((12, 18), (11, 17), (10, 17)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-3')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-3')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-3')
        self.relate('connect', 'p2-r1-2', 'p4-r1-1')
        self.relate('connect', 'p2-r1-2', 'p4-r1-3')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-3')
        self.relate('connect', 'p3-r1-3', 'p4-r1-1')
        self.relate('connect', 'p3-r1-3', 'p4-r1-3')
