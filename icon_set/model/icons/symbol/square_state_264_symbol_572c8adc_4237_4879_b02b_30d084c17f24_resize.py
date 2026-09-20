"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '572c8adc-4237-4879-b02b-30d084c17f24'
SOURCE_PATH = 'icon_set/model/icons/symbol/square_state_264_symbol_572c8adc_4237_4879_b02b_30d084c17f24.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '73c604771cadf90d6fdbae4ae63df61e65ce91650824ce6c3ea38c650eccdb96'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'square-state-264-symbol-resize'
    variant_of = 'square-state-264-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'primitives/shape'
    semantic_kind = 'noun'

    def build(self):
        self.add_line('square-1', (2, 2), (22, 2))
        self.add_line('square-2', (22, 2), (22, 22))
        self.add_line('square-3', (22, 22), (2, 22))
        self.add_line('square-4', (2, 22), (2, 2))
        self.add_contour('square', 'square-1', 'square-2', 'square-3', 'square-4', closed=True)
