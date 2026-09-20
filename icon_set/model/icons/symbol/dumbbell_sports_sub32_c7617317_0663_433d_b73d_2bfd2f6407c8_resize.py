"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'c7617317-0663-433d-b73d-2bfd2f6407c8'
SOURCE_PATH = 'icon_set/model/icons/symbol/dumbbell_sports_sub32_c7617317_0663_433d_b73d_2bfd2f6407c8.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '13cf824c13c40dc5e13a8e3d99a02f24ad11b9f940f5dc1c2f052a435ec01d41'
SOURCE_REFERENCES = (('c7617317-0663-433d-b73d-2bfd2f6407c8', 'pictographic-primitives/sports/dumbbell_c7617317-0663-433d-b73d-2bfd2f6407c8.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'dumbbell-sports-sub32-resize'
    variant_of = 'dumbbell-sports-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'sports'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (18, 10), (6, 10))
        self.add_line('p2-r1-1', (2, 18), (2, 2))
        self.add_line('p2-r1-2', (2, 2), (6, 2))
        self.add_line('p2-r1-3', (6, 2), (6, 18))
        self.add_line('p2-r1-4', (6, 18), (2, 18))
        self.add_line('p3-r1-1', (18, 2), (22, 2))
        self.add_line('p3-r1-2', (22, 2), (22, 18))
        self.add_line('p3-r1-3', (22, 18), (18, 18))
        self.add_line('p3-r1-4', (18, 18), (18, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
