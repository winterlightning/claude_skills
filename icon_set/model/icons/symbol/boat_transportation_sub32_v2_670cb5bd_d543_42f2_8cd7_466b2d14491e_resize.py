"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '670cb5bd-d543-42f2-8cd7-466b2d14491e'
SOURCE_PATH = 'icon_set/model/icons/symbol/boat_transportation_sub32_v2_670cb5bd_d543_42f2_8cd7_466b2d14491e.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '654863e9cf0de364256f38281681b97913e5b0133ec0c1c1f30f5ba12136ac45'
SOURCE_REFERENCES = (('670cb5bd-d543-42f2-8cd7-466b2d14491e', 'pictographic-primitives/transportation/boat_670cb5bd-d543-42f2-8cd7-466b2d14491e.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'boat-transportation-sub32-v2-resize'
    variant_of = 'boat-transportation-sub32-v2'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'transportation'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (6, 10), (8, 2))
        self.add_line('p1-r1-2', (8, 2), (16, 2))
        self.add_line('p1-r1-3', (16, 2), (18, 10))
        self.add_line('p2-r1-1', (2, 10), (6, 10))
        self.add_line('p2-r1-2', (6, 10), (18, 10))
        self.add_line('p2-r1-3', (18, 10), (22, 10))
        self.add_line('p2-r1-4', (22, 10), (19, 19))
        self.add_bezier('p2-r1-5', (19, 19), ((17, 19), (16, 17), (15, 17)))
        self.add_bezier('p2-r1-6', (15, 17), ((14, 17), (13, 18), (12, 19)))
        self.add_bezier('p2-r1-7', (12, 19), ((11, 18), (10, 17), (9, 17)))
        self.add_bezier('p2-r1-8', (9, 17), ((8, 17), (7, 19), (5, 19)))
        self.add_line('p2-r1-9', (5, 19), (2, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
