"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '29604065-1175-4732-a32c-afa455c4c9ab'
SOURCE_PATH = 'icon_set/model/icons/symbol/heart_state_63_symbol_29604065_1175_4732_a32c_afa455c4c9ab.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '7cb9316902dc8c1c649fcc432a461eeefc3ee0ae013efc7a7be6740aa319797b'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'heart-state-63-symbol-resize'
    variant_of = 'heart-state-63-symbol'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'primitives/mark'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('lobe-left-inner', (12, 5), (8, 2), radius_x=4, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('lobe-left-outer', (8, 2), (2, 8), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('shoulder-left', (2, 8), (5, 13), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('side-left', (5, 13), (12, 19))
        self.add_line('side-right', (12, 19), (19, 13))
        self.add_arc('shoulder-right', (19, 13), (22, 8), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('lobe-right-outer', (22, 8), (16, 2), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('lobe-right-inner', (16, 2), (12, 5), radius_x=4, radius_y=3, large_arc=False, sweep=False)
        self.add_contour('outline', 'lobe-left-inner', 'lobe-left-outer', 'shoulder-left', 'side-left', 'side-right', 'shoulder-right', 'lobe-right-outer', 'lobe-right-inner', closed=True)
