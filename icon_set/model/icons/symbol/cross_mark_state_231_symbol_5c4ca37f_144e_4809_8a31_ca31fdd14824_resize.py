"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '5c4ca37f-144e-4809-8a31-ca31fdd14824'
SOURCE_PATH = 'icon_set/model/icons/symbol/cross_mark_state_231_symbol_5c4ca37f_144e_4809_8a31_ca31fdd14824.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'dac032f0883dc3485edef9eae7eba56269466c6f4bd61eb28fb79b7855fe5b7d'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'cross-mark-state-231-symbol-resize'
    variant_of = 'cross-mark-state-231-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'primitives/mark'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('down', (2, 2), (22, 22))
        self.add_line('up', (2, 22), (22, 2))
        self.relate('connect', 'down', 'up')
