"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'e4631868-0084-4122-843e-7c08bc60fa13'
SOURCE_PATH = 'icon_set/model/icons/symbol/arrow_up_state_270_symbol_e4631868_0084_4122_843e_7c08bc60fa13.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'baea76732512539d430b40809fb6174c19576cce856c4ecf66ea4d9acd3d3c56'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'arrow-up-state-270-symbol-resize'
    variant_of = 'arrow-up-state-270-symbol'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'primitives/mark'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('shaft', (10, 22), (10, 2))
        self.add_line('head-1', (2, 11), (10, 2))
        self.add_line('head-2', (10, 2), (19, 11))
        self.add_contour('head', 'head-1', 'head-2', closed=False)
        self.relate('connect', 'shaft', 'head')
