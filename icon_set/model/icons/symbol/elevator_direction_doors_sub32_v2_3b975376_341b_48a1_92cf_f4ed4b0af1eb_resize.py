"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '3b975376-341b-48a1-92cf-f4ed4b0af1eb'
SOURCE_PATH = 'icon_set/model/icons/symbol/elevator_direction_doors_sub32_v2_3b975376_341b_48a1_92cf_f4ed4b0af1eb.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'ce4335b8f414d0078d7168025314faa4012982e9e65f6020bc1eb58019fb9768'
SOURCE_REFERENCES = (('3b975376-341b-48a1-92cf-f4ed4b0af1eb', 'icon_set/dist/gallery/combination-originals/3b975376-341b-48a1-92cf-f4ed4b0af1eb.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'elevator-direction-doors-sub32-v2-resize'
    variant_of = 'elevator-direction-doors-sub32-v2'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (4, 8), (20, 8))
        self.add_arc('p1-r1-2', (20, 8), (22, 10), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (22, 10), (22, 16))
        self.add_arc('p1-r1-4', (22, 16), (20, 19), radius_x=2, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (20, 19), (4, 19))
        self.add_arc('p1-r1-6', (4, 19), (2, 16), radius_x=2, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 16), (2, 10))
        self.add_arc('p1-r1-8', (2, 10), (4, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (12, 8), (12, 19))
        self.add_line('p3-r1-1', (4, 4), (7, 2))
        self.add_line('p3-r1-2', (7, 2), (10, 4))
        self.add_line('p4-r1-1', (14, 2), (17, 4))
        self.add_line('p4-r1-2', (17, 4), (20, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
