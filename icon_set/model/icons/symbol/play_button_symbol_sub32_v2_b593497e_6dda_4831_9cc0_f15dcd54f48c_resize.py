"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'b593497e-6dda-4831-9cc0-f15dcd54f48c'
SOURCE_PATH = 'icon_set/model/icons/symbol/play_button_symbol_sub32_v2_b593497e_6dda_4831_9cc0_f15dcd54f48c.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'b2c90d92201c3f36d0c612a4a54f1522516754e2c32754833bc5975ef44bbf78'
SOURCE_REFERENCES = (('b593497e-6dda-4831-9cc0-f15dcd54f48c', 'pictographic-primitives/symbol/play button_b593497e-6dda-4831-9cc0-f15dcd54f48c.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'play-button-symbol-sub32-v2-resize'
    variant_of = 'play-button-symbol-sub32-v2'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (19, 12), (2, 2))
        self.add_line('p1-r1-2', (2, 2), (2, 22))
        self.add_line('p1-r1-3', (2, 22), (19, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
