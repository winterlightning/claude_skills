"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'e79d0d3c-9833-42da-b29a-025ab29b3d7b'
SOURCE_PATH = 'icon_set/model/icons/symbol/face_sub32_e79d0d3c_9833_42da_b29a_025ab29b3d7b.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'bbc74948942fec7e2aa8c3dd8e71fbec7f583f2420c5beab22bde0c72d34c182'
SOURCE_REFERENCES = (('e79d0d3c-9833-42da-b29a-025ab29b3d7b', 'pictographic-primitives/symbol/face_e79d0d3c-9833-42da-b29a-025ab29b3d7b.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'face-sub32-resize'
    variant_of = 'face-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (2, 12), (12, 2), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (12, 2), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (22, 12), (12, 22), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (12, 22), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_bezier('p2-r1-1', (2, 12), ((6, 12), (10, 9), (12, 6)))
        self.add_bezier('p2-r1-2', (12, 6), ((14, 9), (18, 12), (22, 12)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
