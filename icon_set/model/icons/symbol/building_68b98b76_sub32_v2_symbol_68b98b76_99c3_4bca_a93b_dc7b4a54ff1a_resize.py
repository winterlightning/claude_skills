"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '68b98b76-99c3-4bca-a93b-dc7b4a54ff1a'
SOURCE_PATH = 'icon_set/model/icons/symbol/building_68b98b76_sub32_v2_symbol_68b98b76_99c3_4bca_a93b_dc7b4a54ff1a.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '38482674e232fb53d807343bf5a46ab43a3b8e45c442dc6f28f4a93b29c7462a'
SOURCE_REFERENCES = (('68b98b76-99c3-4bca-a93b-dc7b4a54ff1a', 'pictographic-primitives/building/building_68b98b76-99c3-4bca-a93b-dc7b4a54ff1a.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'building-68b98b76-sub32-v2-symbol-resize'
    variant_of = 'building-68b98b76-sub32-v2-symbol'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'building'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (10, 22), (10, 7))
        self.add_line('p1-r1-2', (10, 7), (19, 2))
        self.add_line('p1-r1-3', (19, 2), (19, 22))
        self.add_line('p1-r1-4', (19, 22), (10, 22))
        self.add_line('p2-r1-1', (10, 12), (2, 12))
        self.add_line('p2-r1-2', (2, 12), (2, 22))
        self.add_line('p2-r1-3', (2, 22), (10, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-4', 'p2-r1-3')
