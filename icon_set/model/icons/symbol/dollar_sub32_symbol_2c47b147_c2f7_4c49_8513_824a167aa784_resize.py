"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '2c47b147-c2f7-4c49-8513-824a167aa784'
SOURCE_PATH = 'icon_set/model/icons/symbol/dollar_sub32_symbol_2c47b147_c2f7_4c49_8513_824a167aa784.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '4f7216105d67e078985dbfe3047b4147b22b60dea1d2d8ba2ef7d69b5062bcc1'
SOURCE_REFERENCES = (('2c47b147-c2f7-4c49-8513-824a167aa784', 'pictographic-primitives/symbol/dollar_2c47b147-c2f7-4c49-8513-824a167aa784.svg'), ('7930e153-2438-44ec-8db7-960bb9aa10cc', 'pictographic-primitives/state/dollar sign_7930e153-2438-44ec-8db7-960bb9aa10cc.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'dollar-sub32-symbol-resize'
    variant_of = 'dollar-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (17, 7), ((16, 5), (13, 4), (10, 4)))
        self.add_bezier('p1-r1-2', (10, 4), ((6, 4), (2, 5), (2, 8)))
        self.add_bezier('p1-r1-3', (2, 8), ((2, 11), (6, 11), (10, 12)))
        self.add_bezier('p1-r1-4', (10, 12), ((14, 13), (18, 13), (18, 16)))
        self.add_bezier('p1-r1-5', (18, 16), ((18, 19), (14, 20), (10, 20)))
        self.add_bezier('p1-r1-6', (10, 20), ((7, 20), (4, 19), (3, 17)))
        self.add_line('p2-r1-1', (10, 2), (10, 4))
        self.add_line('p2-r1-2', (10, 4), (10, 12))
        self.add_line('p2-r1-3', (10, 12), (10, 20))
        self.add_line('p2-r1-4', (10, 20), (10, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-3')
        self.relate('connect', 'p1-r1-5', 'p2-r1-3')
        self.relate('connect', 'p1-r1-5', 'p2-r1-4')
        self.relate('connect', 'p1-r1-6', 'p2-r1-3')
        self.relate('connect', 'p1-r1-6', 'p2-r1-4')
