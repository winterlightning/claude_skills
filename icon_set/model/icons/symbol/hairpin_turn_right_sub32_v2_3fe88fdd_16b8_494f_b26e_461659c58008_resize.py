"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '3fe88fdd-16b8-494f-b26e-461659c58008'
SOURCE_PATH = 'icon_set/model/icons/symbol/hairpin_turn_right_sub32_v2_3fe88fdd_16b8_494f_b26e_461659c58008.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'b11ed394dcef8c22afb1403c6d31a5710ffdd618c3493e3ecebc3596b7635f74'
SOURCE_REFERENCES = (('3fe88fdd-16b8-494f-b26e-461659c58008', 'pictographic-primitives/transportation/hairpin turn right_3fe88fdd-16b8-494f-b26e-461659c58008.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'hairpin-turn-right-sub32-v2-resize'
    variant_of = 'hairpin-turn-right-sub32-v2'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'transportation'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('head-left', (13, 14), (16, 17))
        self.add_line('head-right', (16, 17), (19, 14))
        self.add_line('shaft-right', (16, 17), (16, 9))
        self.add_arc('turn', (16, 9), (2, 9), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('shaft-left', (2, 9), (2, 22))
        self.add_contour('head', 'head-left', 'head-right', closed=False)
        self.add_contour('shaft', 'shaft-right', 'turn', 'shaft-left', closed=False)
        self.relate('connect', 'head-left', 'shaft-right')
        self.relate('connect', 'head-right', 'shaft-right')
