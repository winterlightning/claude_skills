"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'ef18ef0e-e836-4934-9efb-25902b8f8869'
SOURCE_PATH = 'icon_set/model/icons/symbol/arrow_down_arrows_sub32_v2_symbol_ef18ef0e_e836_4934_9efb_25902b8f8869.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '7e8f70050b63738bb0fbd11e0582dcc0c608becfda481985a65ef385b065709c'
SOURCE_REFERENCES = (('ef18ef0e-e836-4934-9efb-25902b8f8869', 'pictographic-primitives/arrows/arrow down_ef18ef0e-e836-4934-9efb-25902b8f8869.svg'), ('b6a9ec80-0591-424e-824e-f6719ae172f4', 'pictographic-primitives/symbol/arrow thin bottom_b6a9ec80-0591-424e-824e-f6719ae172f4.svg'), ('da8197be-3886-4dca-a884-f78ecdff8eaf', 'pictographic-primitives/interface-essential/keyboard arrow down_da8197be-3886-4dca-a884-f78ecdff8eaf.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'arrow-down-arrows-sub32-v2-symbol-resize'
    variant_of = 'arrow-down-arrows-sub32-v2-symbol'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'arrows'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 16), (10, 22))
        self.add_line('p2-r1-1', (10, 22), (10, 2))
        self.add_line('p3-r1-1', (10, 22), (19, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
