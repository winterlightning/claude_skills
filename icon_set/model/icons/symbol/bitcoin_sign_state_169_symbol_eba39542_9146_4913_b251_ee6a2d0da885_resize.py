"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'eba39542-9146-4913-b251-ee6a2d0da885'
SOURCE_PATH = 'icon_set/model/icons/symbol/bitcoin_sign_state_169_symbol_eba39542_9146_4913_b251_ee6a2d0da885.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '16f722ad58ed274f7b6fb3c97daac818753df241710188d41c752d6e9a9281d3'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'bitcoin-sign-state-169-symbol-resize'
    variant_of = 'bitcoin-sign-state-169-symbol'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'primitives/mark'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('stem', (3, 5), (3, 19))
        self.add_line('upper-top', (2, 5), (14, 5))
        self.add_bezier('upper-bowl', (14, 5), ((16, 5), (17, 6), (18, 6)), ((19, 7), (19, 8), (19, 8)), ((19, 9), (19, 10), (18, 11)), ((17, 11), (16, 12), (14, 12)))
        self.add_line('middle', (14, 12), (3, 12))
        self.add_line('lower-top', (3, 12), (14, 12))
        self.add_bezier('lower-bowl', (14, 12), ((16, 12), (17, 13), (18, 13)), ((19, 14), (19, 15), (19, 16)), ((19, 16), (19, 17), (18, 18)), ((17, 18), (16, 19), (14, 19)))
        self.add_line('lower-bottom', (14, 19), (2, 19))
        self.add_line('top-10', (7, 2), (7, 5))
        self.add_line('bottom-10', (7, 19), (7, 22))
        self.add_line('top-18', (14, 2), (14, 5))
        self.add_line('bottom-18', (14, 19), (14, 22))
        self.add_contour('upper', 'upper-top', 'upper-bowl', 'middle', closed=False)
        self.add_contour('lower', 'lower-top', 'lower-bowl', 'lower-bottom', closed=False)
        self.relate('connect', 'stem', 'upper')
        self.relate('connect', 'stem', 'lower')
        self.relate('connect', 'upper', 'lower')
        self.relate('connect', 'upper', 'top-10')
        self.relate('connect', 'lower', 'bottom-10')
        self.relate('connect', 'upper', 'top-18')
        self.relate('connect', 'lower', 'bottom-18')
