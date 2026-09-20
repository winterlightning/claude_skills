"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '4ee8d4ed-d05c-4307-bf33-7c6e7ef0dbfc'
SOURCE_PATH = 'icon_set/model/icons/symbol/turn_left_sub32_4ee8d4ed_d05c_4307_bf33_7c6e7ef0dbfc.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '89d4d0268bef925a8edc61591151d9f3e09097cf88fe0655e18a8cc843e3eb85'
SOURCE_REFERENCES = (('4ee8d4ed-d05c-4307-bf33-7c6e7ef0dbfc', 'pictographic-primitives/transportation/turn left_4ee8d4ed-d05c-4307-bf33-7c6e7ef0dbfc.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'turn-left-sub32-resize'
    variant_of = 'turn-left-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'transportation'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 6), (12, 6))
        self.add_arc('p1-r1-2', (12, 6), (18, 12), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (18, 12), (18, 22))
        self.add_line('p2-r1-1', (6, 2), (2, 6))
        self.add_line('p2-r1-2', (2, 6), (6, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
