"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '05c80477-9896-4d21-a898-62918b362b22'
SOURCE_PATH = 'icon_set/model/icons/symbol/arrows_circular_chevron_sub32_05c80477_9896_4d21_a898_62918b362b22.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'bdf176517c3a2c13deea180b019805f52f9687ea9f7674e0f534fc26b63e3fa5'
SOURCE_REFERENCES = (('05c80477-9896-4d21-a898-62918b362b22', 'pictographic-primitives/symbol/circular arrows_05c80477-9896-4d21-a898-62918b362b22.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'arrows-circular-chevron-sub32-resize'
    variant_of = 'arrows-circular-chevron-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'symbols/standalone'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (2, 14), (11, 6), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (11, 6), (16, 6))
        self.add_line('p2-r1-1', (12, 2), (16, 6))
        self.add_line('p2-r1-2', (16, 6), (12, 8))
        self.add_arc('p3-r1-1', (22, 10), (13, 18), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_line('p3-r1-2', (13, 18), (8, 18))
        self.add_line('p4-r1-1', (12, 16), (8, 18))
        self.add_line('p4-r1-2', (8, 18), (12, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-2')
