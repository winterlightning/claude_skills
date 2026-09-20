"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '0f5b2ebf-9ca8-4f74-bcf3-e9448134158b'
SOURCE_PATH = 'icon_set/model/icons/symbol/bag_sub32_0f5b2ebf_9ca8_4f74_bcf3_e9448134158b.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '76fd54f97e439872e2199878b1068a28af645d99a734cb10bc46fd8711827d00'
SOURCE_REFERENCES = (('0f5b2ebf-9ca8-4f74-bcf3-e9448134158b', 'pictographic-primitives/photography/bag_0f5b2ebf-9ca8-4f74-bcf3-e9448134158b.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'bag-sub32-resize'
    variant_of = 'bag-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'photography'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (8, 8), (8, 6))
        self.add_arc('p1-r1-2', (8, 6), (16, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (16, 6), (16, 8))
        self.add_line('p2-r1-1', (4, 8), (8, 8))
        self.add_line('p2-r1-2', (8, 8), (16, 8))
        self.add_line('p2-r1-3', (16, 8), (20, 8))
        self.add_bezier('p2-r1-4', (20, 8), ((21, 11), (22, 13), (22, 16)))
        self.add_bezier('p2-r1-5', (22, 16), ((22, 21), (20, 22), (16, 22)))
        self.add_line('p2-r1-6', (16, 22), (8, 22))
        self.add_bezier('p2-r1-7', (8, 22), ((4, 22), (2, 21), (2, 16)))
        self.add_bezier('p2-r1-8', (2, 16), ((2, 13), (3, 11), (4, 8)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
