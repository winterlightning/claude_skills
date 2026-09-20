"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '6e120b10-f09c-4f71-9e1d-244b8eb9fd47'
SOURCE_PATH = 'icon_set/model/icons/symbol/car_horn_sub32_6e120b10_f09c_4f71_9e1d_244b8eb9fd47.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'f280028481e81c7d92ba8e966d86421a83fe457fae9ef73f7f4223660c95afa3'
SOURCE_REFERENCES = (('6e120b10-f09c-4f71-9e1d-244b8eb9fd47', 'pictographic-primitives/transportation/horn_6e120b10-f09c-4f71-9e1d-244b8eb9fd47.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'car-horn-sub32-resize'
    variant_of = 'car-horn-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'objects/transportation'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 6), (9, 10))
        self.add_line('p1-r1-2', (9, 10), (2, 14))
        self.add_line('p1-r1-3', (2, 14), (2, 6))
        self.add_line('p2-r1-1', (9, 10), (14, 10))
        self.add_line('p2-r1-2', (14, 10), (20, 10))
        self.add_line('p2-r1-3', (20, 10), (21, 10))
        self.add_line('p3-r1-1', (14, 10), (14, 15))
        self.add_arc('p3-r1-2', (14, 15), (17, 18), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('p3-r1-3', (17, 18), (20, 15), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p3-r1-4', (20, 15), (20, 10))
        self.add_line('p4-r1-1', (14, 2), (16, 2))
        self.add_line('p5-r1-1', (20, 2), (22, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-4')
        self.relate('connect', 'p2-r1-3', 'p3-r1-4')
