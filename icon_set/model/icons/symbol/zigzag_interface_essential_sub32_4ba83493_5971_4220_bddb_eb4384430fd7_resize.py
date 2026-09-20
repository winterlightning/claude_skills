"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '4ba83493-5971-4220-bddb-eb4384430fd7'
SOURCE_PATH = 'icon_set/model/icons/symbol/zigzag_interface_essential_sub32_4ba83493_5971_4220_bddb_eb4384430fd7.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '3ca89fef41bde7886ffda79f22e5e6c368611ca0c3401454101ddafffaec9326'
SOURCE_REFERENCES = (('4ba83493-5971-4220-bddb-eb4384430fd7', 'pictographic-primitives/interface-essential/zigzag_4ba83493-5971-4220-bddb-eb4384430fd7.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'zigzag-interface-essential-sub32-resize'
    variant_of = 'zigzag-interface-essential-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (15, 13), (18, 16))
        self.add_line('p1-r1-2', (18, 16), (14, 18))
        self.add_line('p1-r1-3', (14, 18), (18, 22))
        self.add_line('p2-r1-1', (4, 12), (6, 16))
        self.add_line('p2-r1-2', (6, 16), (2, 18))
        self.add_line('p2-r1-3', (2, 18), (5, 22))
        self.add_line('p3-r1-1', (8, 2), (11, 5))
        self.add_line('p3-r1-2', (11, 5), (8, 8))
        self.add_line('p3-r1-3', (8, 8), (11, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
