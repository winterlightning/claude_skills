"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '90c55c1b-6141-40f9-8dfb-e0b9bed3cb5e'
SOURCE_PATH = 'icon_set/model/icons/symbol/hidden_visibility_eye_symbol_sub32_symbol_90c55c1b_6141_40f9_8dfb_e0b9bed3cb5e.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'ac263455b9e87cd7e9fa09918b75e31d74413ef7b3307fe620283eea3486649b'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'hidden-visibility-eye-symbol-sub32-symbol-resize'
    variant_of = 'hidden-visibility-eye-symbol-sub32-symbol'
    variant_label = 'Resize 24 × 21'
    canvas_width = 24
    canvas_height = 21
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('upper', (2, 10), ((4, 5), (8, 2), (12, 2)), ((16, 2), (20, 5), (22, 10)))
        self.add_bezier('lower', (22, 10), ((20, 16), (16, 19), (12, 19)), ((8, 19), (4, 16), (2, 10)))
        self.add_line('slash', (5, 19), (19, 2))
        self.add_contour('eye', 'upper', 'lower', closed=True)
        self.relate('connect', 'eye', 'slash')
