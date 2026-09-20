"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'dcdcb7b9-e416-44a0-b02f-72fb6b50c853'
SOURCE_PATH = 'icon_set/model/icons/symbol/cursor_dcdcb7b9_sub32_symbol_dcdcb7b9_e416_44a0_b02f_72fb6b50c853.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '7ced98985dc8e6f48a3bb2cac3afc1b88848ab0713e2b404e77779bd668ee055'
SOURCE_REFERENCES = (('dcdcb7b9-e416-44a0-b02f-72fb6b50c853', 'pictographic-primitives/interface-essential/cursor_dcdcb7b9-e416-44a0-b02f-72fb6b50c853.svg'), ('4b8a1949-3e5f-4bab-9f8a-db37b07f0bc0', 'pictographic-primitives/interface-essential/cursor_4b8a1949-3e5f-4bab-9f8a-db37b07f0bc0.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'cursor-dcdcb7b9-sub32-symbol-resize'
    variant_of = 'cursor-dcdcb7b9-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (22, 22), (12, 2))
        self.add_line('p1-r1-2', (12, 2), (2, 22))
        self.add_line('p1-r1-3', (2, 22), (12, 16))
        self.add_line('p1-r1-4', (12, 16), (22, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
