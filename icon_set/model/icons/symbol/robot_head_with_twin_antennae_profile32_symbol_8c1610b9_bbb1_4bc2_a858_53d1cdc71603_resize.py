"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '8c1610b9-bbb1-4bc2-a858-53d1cdc71603'
SOURCE_PATH = 'icon_set/model/icons/symbol/robot_head_with_twin_antennae_profile32_symbol_8c1610b9_bbb1_4bc2_a858_53d1cdc71603.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '0b13f413a5fd2c45cdf7e1753f27e8f0870a982e50df35a92b4d3c42f75726d9'
SOURCE_REFERENCES = (('8c1610b9-bbb1-4bc2-a858-53d1cdc71603', 'pictographic-primitives/artificial-intelligence/robot_8c1610b9-bbb1-4bc2-a858-53d1cdc71603.svg'), ('dbe0f105-1e06-44cc-8dc4-597b67509f96', 'pictographic-primitives/artificial-intelligence/robot_dbe0f105-1e06-44cc-8dc4-597b67509f96.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'robot-head-with-twin-antennae-profile32-symbol-resize'
    variant_of = 'robot-head-with-twin-antennae-profile32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'artificial-intelligence'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 8), (8, 8))
        self.add_line('p1-r1-2', (8, 8), (16, 8))
        self.add_line('p1-r1-3', (16, 8), (22, 8))
        self.add_line('p1-r1-4', (22, 8), (22, 14))
        self.add_arc('p1-r1-5', (22, 14), (14, 22), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (14, 22), (10, 22))
        self.add_arc('p1-r1-7', (10, 22), (2, 14), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (2, 14), (2, 8))
        self.add_line('p2-r1-1', (8, 2), (8, 8))
        self.add_line('p3-r1-1', (8, 13), (8, 16))
        self.add_line('p4-r1-1', (16, 2), (16, 8))
        self.add_line('p5-r1-1', (16, 13), (16, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-3', 'p4-r1-1')
