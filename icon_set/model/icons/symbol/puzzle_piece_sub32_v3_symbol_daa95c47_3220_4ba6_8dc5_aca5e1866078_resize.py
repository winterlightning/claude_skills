"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'daa95c47-3220-4ba6-8dc5-aca5e1866078'
SOURCE_PATH = 'icon_set/model/icons/symbol/puzzle_piece_sub32_v3_symbol_daa95c47_3220_4ba6_8dc5_aca5e1866078.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '426476a180660602d203ca771b164367726f7e34b9eddd0fb8fbe18e28b76a09'
SOURCE_REFERENCES = (('daa95c47-3220-4ba6-8dc5-aca5e1866078', 'pictographic-primitives/symbol/puzzle piece_daa95c47-3220-4ba6-8dc5-aca5e1866078.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'puzzle-piece-sub32-v3-symbol-resize'
    variant_of = 'puzzle-piece-sub32-v3-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('tab', (8, 6), (16, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('top-right', (16, 6), (22, 6))
        self.add_line('right-upper', (22, 6), (22, 11))
        self.add_arc('right-socket', (22, 11), (22, 17), radius_x=4, radius_y=3, large_arc=False, sweep=False)
        self.add_line('right-lower', (22, 17), (22, 22))
        self.add_line('base', (22, 22), (2, 22))
        self.add_line('left-lower', (2, 22), (2, 17))
        self.add_arc('left-socket', (2, 17), (2, 11), radius_x=4, radius_y=3, large_arc=False, sweep=False)
        self.add_line('left-upper', (2, 11), (2, 6))
        self.add_line('top-left', (2, 6), (8, 6))
        self.add_contour('piece', 'tab', 'top-right', 'right-upper', 'right-socket', 'right-lower', 'base', 'left-lower', 'left-socket', 'left-upper', 'top-left', closed=True)
