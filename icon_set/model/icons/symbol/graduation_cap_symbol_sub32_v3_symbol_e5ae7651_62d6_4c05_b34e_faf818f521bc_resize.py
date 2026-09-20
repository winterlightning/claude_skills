"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'e5ae7651-62d6-4c05-b34e-faf818f521bc'
SOURCE_PATH = 'icon_set/model/icons/symbol/graduation_cap_symbol_sub32_v3_symbol_e5ae7651_62d6_4c05_b34e_faf818f521bc.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'd600690ab697d8a657d043909eb5373155cb59b67266b1d725ad924b49d08d2b'
SOURCE_REFERENCES = (('e5ae7651-62d6-4c05-b34e-faf818f521bc', 'pictographic-primitives/symbol/graduation cap_e5ae7651-62d6-4c05-b34e-faf818f521bc.svg'), ('ac0c8839-9020-4a65-9a30-af5a45d63503', 'pictographic-primitives/accessories/batch-07/cap_ac0c8839-9020-4a65-9a30-af5a45d63503.svg'), ('5f6ee542-cdce-408a-b798-b60860e5b325', 'pictographic-primitives/accessories/batch-06/cap_5f6ee542-cdce-408a-b798-b60860e5b325.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'graduation-cap-symbol-sub32-v3-symbol-resize'
    variant_of = 'graduation-cap-symbol-sub32-v3-symbol'
    variant_label = 'Resize 43 × 32'
    canvas_width = 43
    canvas_height = 32
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('board-1', (2, 12), (22, 2))
        self.add_line('board-2', (22, 2), (41, 12))
        self.add_line('board-3', (41, 12), (22, 22))
        self.add_line('board-4', (22, 22), (2, 12))
        self.add_line('right', (33, 16), (33, 23))
        self.add_bezier('br', (33, 23), ((33, 27), (27, 30), (22, 30)))
        self.add_bezier('bl', (22, 30), ((16, 30), (10, 27), (10, 23)))
        self.add_line('left', (10, 23), (10, 16))
        self.add_contour('board', 'board-1', 'board-2', 'board-3', 'board-4', closed=True)
        self.add_contour('band', 'right', 'br', 'bl', 'left', closed=False)
        self.relate('connect', 'board', 'band')
