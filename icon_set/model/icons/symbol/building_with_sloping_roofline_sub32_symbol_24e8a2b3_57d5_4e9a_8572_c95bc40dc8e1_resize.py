"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '24e8a2b3-57d5-4e9a-8572-c95bc40dc8e1'
SOURCE_PATH = 'icon_set/model/icons/symbol/building_with_sloping_roofline_sub32_symbol_24e8a2b3_57d5_4e9a_8572_c95bc40dc8e1.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'cb638bc8c68e966d98bf5bac20432e9e17ce39abf8bd4c850ec2ce2e2810f0c9'
SOURCE_REFERENCES = (('24e8a2b3-57d5-4e9a-8572-c95bc40dc8e1', 'pictographic-primitives/building/building_24e8a2b3-57d5-4e9a-8572-c95bc40dc8e1.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'building-with-sloping-roofline-sub32-symbol-resize'
    variant_of = 'building-with-sloping-roofline-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'building'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (12, 6))
        self.add_line('p1-r1-2', (12, 6), (22, 11))
        self.add_line('p1-r1-3', (22, 11), (22, 16))
        self.add_line('p1-r1-4', (22, 16), (22, 22))
        self.add_line('p1-r1-5', (22, 22), (12, 22))
        self.add_line('p1-r1-6', (12, 22), (2, 22))
        self.add_line('p1-r1-7', (2, 22), (2, 2))
        self.add_line('p2-r1-1', (12, 2), (12, 6))
        self.add_line('p2-r1-2', (12, 6), (12, 22))
        self.add_line('p3-r1-1', (18, 16), (22, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-2')
        self.relate('connect', 'p1-r1-6', 'p2-r1-2')
