"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '02755e11-4acb-4979-8f00-254954a86d5c'
SOURCE_PATH = 'icon_set/model/icons/symbol/sparkle_four_point_rounded_sub32_symbol_02755e11_4acb_4979_8f00_254954a86d5c.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '6a9eea32e84e8a2840d7eb232ded332467fe6fd7ff592ac9acb95b9aa35faa1c'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'sparkle-four-point-rounded-sub32-symbol-resize'
    variant_of = 'sparkle-four-point-rounded-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'noun'

    def build(self):
        self.add_arc('side-0', (12, 2), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('side-1', (22, 12), (12, 22), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('side-2', (12, 22), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('side-3', (2, 12), (12, 2), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_contour('sparkle', 'side-0', 'side-1', 'side-2', 'side-3', closed=True)
