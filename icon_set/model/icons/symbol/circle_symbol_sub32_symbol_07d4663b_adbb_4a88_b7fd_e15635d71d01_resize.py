"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '07d4663b-adbb-4a88-b7fd-e15635d71d01'
SOURCE_PATH = 'icon_set/model/icons/symbol/circle_symbol_sub32_symbol_07d4663b_adbb_4a88_b7fd_e15635d71d01.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '2bcb0607f42aa42f97f542d22acffd0c3e54d9fa2e94c30c5936da3ea306dd18'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'circle-symbol-sub32-symbol-resize'
    variant_of = 'circle-symbol-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'noun'

    def build(self):
        self.add_arc('e0-top', (2, 12), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('e0-bottom', (22, 12), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
