"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '265ecf16-9a75-43f1-970c-76948410da91'
SOURCE_PATH = 'icon_set/model/icons/symbol/building_building_sub32_symbol_265ecf16_9a75_43f1_970c_76948410da91.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '160c4d4e11d0b1fdb70ba9a3742a79c9a4656dbaaa66ca6cf098451296af1e88'
SOURCE_REFERENCES = (('265ecf16-9a75-43f1-970c-76948410da91', 'pictographic-primitives/building/building_265ecf16-9a75-43f1-970c-76948410da91.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'building-building-sub32-symbol-resize'
    variant_of = 'building-building-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'building'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (4, 22), (4, 2))
        self.add_line('p1-r1-2', (4, 2), (16, 2))
        self.add_line('p1-r1-3', (16, 2), (16, 22))
        self.add_line('p2-r1-1', (16, 8), (22, 11))
        self.add_line('p2-r1-2', (22, 11), (22, 22))
        self.add_line('p2-r1-3', (22, 22), (2, 22))
        self.add_line('p3-r1-1', (9, 8), (11, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
