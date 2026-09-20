"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '378dbc4a-8e49-4c92-8de6-23be0bf1d811'
SOURCE_PATH = 'icon_set/model/icons/symbol/medical_health_protection_shield_sub32_symbol_378dbc4a_8e49_4c92_8de6_23be0bf1d811.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'b397b2807968dad2e1b8a983b4d5b1b2561e10a0ad153f7b1e623207301a0c1d'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'medical-health-protection-shield-sub32-symbol-resize'
    variant_of = 'medical-health-protection-shield-sub32-symbol'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('shield', (10, 2), ((8, 3), (5, 5), (2, 5)), ((2, 13), (2, 18), (10, 22)), ((19, 18), (19, 13), (19, 5)), ((16, 5), (13, 3), (10, 2)))
        self.add_line('cross-h-1', (7, 11), (10, 11))
        self.add_line('cross-h-2', (10, 11), (14, 11))
        self.add_line('cross-v-1', (10, 8), (10, 11))
        self.add_line('cross-v-2', (10, 11), (10, 15))
        self.add_contour('outline', 'shield', closed=True)
        self.add_contour('cross-h', 'cross-h-1', 'cross-h-2', closed=False)
        self.add_contour('cross-v', 'cross-v-1', 'cross-v-2', closed=False)
        self.relate('connect', 'cross-h', 'cross-v')
