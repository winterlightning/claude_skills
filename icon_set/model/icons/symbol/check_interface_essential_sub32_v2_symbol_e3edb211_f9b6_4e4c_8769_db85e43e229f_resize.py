"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'e3edb211-f9b6-4e4c-8769-db85e43e229f'
SOURCE_PATH = 'icon_set/model/icons/symbol/check_interface_essential_sub32_v2_symbol_e3edb211_f9b6_4e4c_8769_db85e43e229f.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '482af4066bf07b18b62aa629b8a728366a0a94f749b4b2eeab3883ed2c1ed1bf'
SOURCE_REFERENCES = (('e3edb211-f9b6-4e4c-8769-db85e43e229f', 'pictographic-primitives/interface-essential/check_e3edb211-f9b6-4e4c-8769-db85e43e229f.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'check-interface-essential-sub32-v2-symbol-resize'
    variant_of = 'check-interface-essential-sub32-v2-symbol'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (22, 2), (10, 19))
        self.add_line('p1-r1-2', (10, 19), (2, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
