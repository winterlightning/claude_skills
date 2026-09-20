"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'dcbfa235-b6ab-4926-bc2a-34d5ce7146d8'
SOURCE_PATH = 'icon_set/model/icons/symbol/star_burst_sub32_dcbfa235_b6ab_4926_bc2a_34d5ce7146d8.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '8d01acba52690ff0df62a4ae30ff82991d8c4844bebce3d42509497dca4b6ec6'
SOURCE_REFERENCES = (('dcbfa235-b6ab-4926-bc2a-34d5ce7146d8', 'pictographic-primitives/symbol/star burst_dcbfa235-b6ab-4926-bc2a-34d5ce7146d8.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'star-burst-sub32-resize'
    variant_of = 'star-burst-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (8, 18), (7, 14))
        self.add_line('p1-r1-2', (7, 14), (2, 14))
        self.add_line('p1-r1-3', (2, 14), (5, 10))
        self.add_line('p1-r1-4', (5, 10), (3, 6))
        self.add_line('p1-r1-5', (3, 6), (8, 6))
        self.add_line('p1-r1-6', (8, 6), (10, 2))
        self.add_line('p1-r1-7', (10, 2), (14, 6))
        self.add_line('p1-r1-8', (14, 6), (19, 4))
        self.add_line('p1-r1-9', (19, 4), (19, 9))
        self.add_line('p1-r1-10', (19, 9), (22, 11))
        self.add_line('p1-r1-11', (22, 11), (17, 13))
        self.add_line('p1-r1-12', (17, 13), (16, 17))
        self.add_line('p1-r1-13', (16, 17), (12, 14))
        self.add_line('p1-r1-14', (12, 14), (8, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', closed=False)
