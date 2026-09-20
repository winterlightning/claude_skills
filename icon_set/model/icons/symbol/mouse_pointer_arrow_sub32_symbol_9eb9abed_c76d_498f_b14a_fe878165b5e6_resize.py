"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '9eb9abed-c76d-498f-b14a-fe878165b5e6'
SOURCE_PATH = 'icon_set/model/icons/symbol/mouse_pointer_arrow_sub32_symbol_9eb9abed_c76d_498f_b14a_fe878165b5e6.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '9d1aaff825d20bc3efdd26538713f887353533fd1665d9043f42847bf694e1a6'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'mouse-pointer-arrow-sub32-symbol-resize'
    variant_of = 'mouse-pointer-arrow-sub32-symbol'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('pointer-1', (2, 2), (19, 13))
        self.add_line('pointer-2', (19, 13), (10, 16))
        self.add_line('pointer-3', (10, 16), (6, 22))
        self.add_line('pointer-4', (6, 22), (2, 2))
        self.add_contour('pointer', 'pointer-1', 'pointer-2', 'pointer-3', 'pointer-4', closed=True)
