"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '2de22ab7-b36e-43f7-805d-727e72c62f15'
SOURCE_PATH = 'icon_set/model/icons/symbol/t_shirt_sub32_symbol_2de22ab7_b36e_43f7_805d_727e72c62f15.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '077e321706e06e92b5a50d862ff13cd2c23b4b9df4e7a1d3c1123b2a7d6c0f3b'
SOURCE_REFERENCES = (('2de22ab7-b36e-43f7-805d-727e72c62f15', 'pictographic-primitives/clothes/t shirt_2de22ab7-b36e-43f7-805d-727e72c62f15.svg'), ('5f0ac9bd-d1ec-43e8-ba78-79f54033a5b7', 'pictographic-primitives/clothes/t shirt_5f0ac9bd-d1ec-43e8-ba78-79f54033a5b7.svg'), ('9aa1a37e-7127-4719-8aeb-03b09b01c294', 'pictographic-primitives/clothes/t shirt_9aa1a37e-7127-4719-8aeb-03b09b01c294.svg'), ('45dc1629-c2e7-477c-80d5-ad5686c1271e', 'pictographic-primitives/clothes/t shirt_45dc1629-c2e7-477c-80d5-ad5686c1271e.svg'), ('bc825952-a086-4761-9814-673ca2bec10b', 'pictographic-primitives/clothes/t shirt_bc825952-a086-4761-9814-673ca2bec10b.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 't-shirt-sub32-symbol-resize'
    variant_of = 't-shirt-sub32-symbol'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'clothes'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (12, 2), (28, 2), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_bezier('p1-r1-2', (28, 2), ((34, 2), (38, 6), (38, 11)))
        self.add_line('p1-r1-3', (38, 11), (38, 17))
        self.add_line('p1-r1-4', (38, 17), (30, 17))
        self.add_line('p1-r1-5', (30, 17), (30, 30))
        self.add_line('p1-r1-6', (30, 30), (10, 30))
        self.add_line('p1-r1-7', (10, 30), (10, 17))
        self.add_line('p1-r1-8', (10, 17), (2, 17))
        self.add_line('p1-r1-9', (2, 17), (2, 11))
        self.add_bezier('p1-r1-10', (2, 11), ((2, 6), (6, 2), (12, 2)))
        self.add_line('p2-r1-1', (10, 17), (10, 11))
        self.add_line('p3-r1-1', (30, 17), (30, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
