"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '4aa8fd4e-dd20-4ab4-9374-89370bfa9188'
SOURCE_PATH = 'icon_set/model/icons/symbol/unlock_sub32_symbol_4aa8fd4e_dd20_4ab4_9374_89370bfa9188.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'dcac7713c757692811e4a5fe63d0b904edad1a5d76a2739fcb924a5b151ba650'
SOURCE_REFERENCES = (('4aa8fd4e-dd20-4ab4-9374-89370bfa9188', 'pictographic-primitives/state/unlock_4aa8fd4e-dd20-4ab4-9374-89370bfa9188.svg'), ('90a6ff07-21bc-47ed-b588-aacc1c25c397', 'pictographic-primitives/symbol/unlock_90a6ff07-21bc-47ed-b588-aacc1c25c397.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'unlock-sub32-symbol-resize'
    variant_of = 'unlock-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'state'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (4, 11), (16, 11))
        self.add_arc('p1-r1-2', (16, 11), (18, 13), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (18, 13), (18, 20))
        self.add_arc('p1-r1-4', (18, 20), (16, 22), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (16, 22), (4, 22))
        self.add_arc('p1-r1-6', (4, 22), (2, 20), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 20), (2, 13))
        self.add_arc('p1-r1-8', (2, 13), (4, 11), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (5, 11), (5, 7))
        self.add_arc('p2-r1-2', (5, 7), (15, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
