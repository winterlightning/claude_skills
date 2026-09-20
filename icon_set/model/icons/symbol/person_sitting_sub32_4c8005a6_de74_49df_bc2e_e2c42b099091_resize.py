"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '4c8005a6-de74-49df-bc2e-e2c42b099091'
SOURCE_PATH = 'icon_set/model/icons/symbol/person_sitting_sub32_4c8005a6_de74_49df_bc2e_e2c42b099091.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'ab226a697ba5557f128edc56c25e9b04a18afbc4dde147750e6bef133b4a5425'
SOURCE_REFERENCES = (('4c8005a6-de74-49df-bc2e-e2c42b099091', 'pictographic-primitives/symbol/person sitting_4c8005a6-de74-49df-bc2e-e2c42b099091.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'person-sitting-sub32-resize'
    variant_of = 'person-sitting-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (5, 5), (11, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (11, 5), (5, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (6, 13), (2, 17))
        self.add_line('p2-r1-2', (2, 17), (12, 17))
        self.add_line('p2-r1-3', (12, 17), (18, 22))
        self.add_line('p3-r1-1', (6, 13), (16, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
