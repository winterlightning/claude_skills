"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '9f1aeae0-d56e-4c60-8db2-c377d1b6ef06'
SOURCE_PATH = 'icon_set/model/icons/symbol/search_magnifying_glass_sub32_symbol_9f1aeae0_d56e_4c60_8db2_c377d1b6ef06.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '3ec188915e1719fae91ed14575b8086d095002dae797bde0c24d764da9e6f842'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'search-magnifying-glass-sub32-symbol-resize'
    variant_of = 'search-magnifying-glass-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('ring-a', (2, 11), (11, 2), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('ring-b', (11, 2), (18, 11), radius_x=8, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('ring-c', (18, 11), (16, 17), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('ring-d', (16, 17), (2, 11), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_line('handle', (16, 17), (22, 22))
        self.add_contour('lens', 'ring-a', 'ring-b', 'ring-c', 'ring-d', closed=True)
        self.relate('connect', 'lens', 'handle')
