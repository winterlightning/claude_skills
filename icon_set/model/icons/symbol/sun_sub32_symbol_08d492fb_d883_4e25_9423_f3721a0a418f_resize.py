"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '08d492fb-d883-4e25-9423-f3721a0a418f'
SOURCE_PATH = 'icon_set/model/icons/symbol/sun_sub32_symbol_08d492fb_d883_4e25_9423_f3721a0a418f.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'bd794744515a8b3bc6b5e86b0b7497634b1d59c8cd6d12352fbab7bbd25e1c06'
SOURCE_REFERENCES = (('08d492fb-d883-4e25-9423-f3721a0a418f', 'pictographic-primitives/weather/weather sun_08d492fb-d883-4e25-9423-f3721a0a418f.svg'), ('e1640603-3ce9-5ec9-a1ab-06e3fe5239a4', 'pictographic-primitives/weather/weather sun_e1640603-3ce9-5ec9-a1ab-06e3fe5239a4.svg'), ('9612aa29-9678-40f4-95b4-380662a7ece5', 'pictographic-primitives/weather/weather sun_9612aa29-9678-40f4-95b4-380662a7ece5.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'sun-sub32-symbol-resize'
    variant_of = 'sun-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/weather'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (7, 12), (17, 12), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (17, 12), (7, 12), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (12, 2), (12, 2))
        self.add_line('p3-r1-1', (12, 22), (12, 22))
        self.add_line('p4-r1-1', (2, 12), (2, 12))
        self.add_line('p5-r1-1', (22, 12), (22, 12))
        self.add_line('p6-r1-1', (4, 4), (5, 5))
        self.add_line('p7-r1-1', (19, 19), (20, 20))
        self.add_line('p8-r1-1', (4, 20), (5, 19))
        self.add_line('p9-r1-1', (19, 5), (20, 4))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
