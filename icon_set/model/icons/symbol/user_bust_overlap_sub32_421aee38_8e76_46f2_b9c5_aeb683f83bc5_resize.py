"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '421aee38-8e76-46f2-b9c5-aeb683f83bc5'
SOURCE_PATH = 'icon_set/model/icons/symbol/user_bust_overlap_sub32_421aee38_8e76_46f2_b9c5_aeb683f83bc5.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '04c37626fbe7ef3fe21d209226a8ee0cbf6fb397ee361f412cae72691896ebcc'
SOURCE_REFERENCES = (('421aee38-8e76-46f2-b9c5-aeb683f83bc5', 'pictographic-primitives/symbol/person 1_421aee38-8e76-46f2-b9c5-aeb683f83bc5.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'user-bust-overlap-sub32-resize'
    variant_of = 'user-bust-overlap-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (10, 14), (10, 2), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (10, 2), (10, 14), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p2-r1-1', (2, 22), (10, 14), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (10, 14), (18, 22), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
