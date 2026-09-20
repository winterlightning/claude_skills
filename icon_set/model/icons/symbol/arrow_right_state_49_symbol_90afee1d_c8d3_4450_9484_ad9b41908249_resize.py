"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '90afee1d-c8d3-4450-9484-ad9b41908249'
SOURCE_PATH = 'icon_set/model/icons/symbol/arrow_right_state_49_symbol_90afee1d_c8d3_4450_9484_ad9b41908249.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'cf8e2b5eb864aa085771ac553a29ffaa93871b3464c146eb42284f12fbced020'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'arrow-right-state-49-symbol-resize'
    variant_of = 'arrow-right-state-49-symbol'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'primitives/mark'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('shaft', (2, 10), (22, 10))
        self.add_line('head-1', (13, 2), (22, 10))
        self.add_line('head-2', (22, 10), (13, 19))
        self.add_contour('head', 'head-1', 'head-2', closed=False)
        self.relate('connect', 'shaft', 'head')
