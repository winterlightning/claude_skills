"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '0683af89-a794-45d7-baf4-2a77d813dbe0'
SOURCE_PATH = 'icon_set/model/icons/symbol/brightness_sub32_0683af89_a794_45d7_baf4_2a77d813dbe0.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'b4b0e92aa7aa94971d30d9f8e7967addcd2e774b9d5a5b041a617944ef3ad39b'
SOURCE_REFERENCES = (('0683af89-a794-45d7-baf4-2a77d813dbe0', 'pictographic-primitives/interface-essential/brightness_0683af89-a794-45d7-baf4-2a77d813dbe0.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'brightness-sub32-resize'
    variant_of = 'brightness-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (9, 12), (15, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (15, 12), (9, 12), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (12, 2), (12, 4))
        self.add_line('p3-r1-1', (12, 20), (12, 22))
        self.add_line('p4-r1-1', (2, 12), (4, 12))
        self.add_line('p5-r1-1', (20, 12), (22, 12))
        self.add_line('p6-r1-1', (6, 6), (6, 6))
        self.add_line('p7-r1-1', (18, 6), (18, 6))
        self.add_line('p8-r1-1', (6, 18), (6, 18))
        self.add_line('p9-r1-1', (18, 18), (18, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
