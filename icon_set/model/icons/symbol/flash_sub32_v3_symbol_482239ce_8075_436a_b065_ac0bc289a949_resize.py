"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '482239ce-8075-436a-b065-ac0bc289a949'
SOURCE_PATH = 'icon_set/model/icons/symbol/flash_sub32_v3_symbol_482239ce_8075_436a_b065_ac0bc289a949.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'e887afe7a16578e24dd598d6ad8d5086c89c935451c9b2185bab21b358e8b273'
SOURCE_REFERENCES = (('482239ce-8075-436a-b065-ac0bc289a949', 'pictographic-primitives/interface-essential/flash_482239ce-8075-436a-b065-ac0bc289a949.svg'), ('821a0fbf-70fd-4f18-bc5d-1a46c93ca7e9', 'pictographic-primitives/interface-essential/flash_821a0fbf-70fd-4f18-bc5d-1a46c93ca7e9.svg'), ('83a0452b-f452-49a0-a7c6-99e9bc8331a8', 'pictographic-primitives/interface-essential/flash_83a0452b-f452-49a0-a7c6-99e9bc8331a8.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'flash-sub32-v3-symbol-resize'
    variant_of = 'flash-sub32-v3-symbol'
    variant_label = 'Resize 18 × 24'
    canvas_width = 18
    canvas_height = 24
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('bolt-1', (8, 2), (16, 2))
        self.add_line('bolt-2', (16, 2), (10, 10))
        self.add_line('bolt-3', (10, 10), (16, 10))
        self.add_line('bolt-4', (16, 10), (4, 22))
        self.add_line('bolt-5', (4, 22), (8, 14))
        self.add_line('bolt-6', (8, 14), (2, 14))
        self.add_line('bolt-7', (2, 14), (8, 2))
        self.add_contour('bolt', 'bolt-1', 'bolt-2', 'bolt-3', 'bolt-4', 'bolt-5', 'bolt-6', 'bolt-7', closed=True)
