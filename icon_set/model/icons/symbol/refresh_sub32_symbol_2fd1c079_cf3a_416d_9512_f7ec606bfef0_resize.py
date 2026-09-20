"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '2fd1c079-cf3a-416d-9512-f7ec606bfef0'
SOURCE_PATH = 'icon_set/model/icons/symbol/refresh_sub32_symbol_2fd1c079_cf3a_416d_9512_f7ec606bfef0.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'f822712e5220af6ac92c10a7a564fddff529019b6823c45a7ecd0eb2f7b72bf0'
SOURCE_REFERENCES = (('2fd1c079-cf3a-416d-9512-f7ec606bfef0', 'pictographic-primitives/interface-essential/refresh_2fd1c079-cf3a-416d-9512-f7ec606bfef0.svg'), ('d1b39612-4343-4bf6-ac61-b3e0ef51391b', 'pictographic-primitives/interface-essential/refresh_d1b39612-4343-4bf6-ac61-b3e0ef51391b.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'refresh-sub32-symbol-resize'
    variant_of = 'refresh-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (22, 12), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (2, 12), (12, 2), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-3', (12, 2), ((16, 2), (18, 4), (21, 8)))
        self.add_line('p2-r1-1', (21, 2), (21, 8))
        self.add_line('p2-r1-2', (21, 8), (16, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
