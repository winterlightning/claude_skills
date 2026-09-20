"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '7099417a-0fa8-4ad5-84bf-e77a845b942a'
SOURCE_PATH = 'icon_set/model/icons/symbol/telephone_handset_state_204_symbol_7099417a_0fa8_4ad5_84bf_e77a845b942a.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '14db9de0a99c38c593bafb67d2e50669364d48fb065b6ae0def645c4bed0bb71'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'telephone-handset-state-204-symbol-resize'
    variant_of = 'telephone-handset-state-204-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'primitives/shape'
    semantic_kind = 'noun'

    def build(self):
        self.add_arc('upper-corner', (2, 5), (5, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('upper-edge', (5, 2), (9, 6))
        self.add_arc('upper-turn', (9, 6), (9, 9), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('upper-neck', (9, 9), (8, 11))
        self.add_arc('grip', (8, 11), (13, 16), radius_x=13, radius_y=13, large_arc=False, sweep=False)
        self.add_line('lower-neck', (13, 16), (15, 15))
        self.add_arc('lower-turn', (15, 15), (18, 15), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('lower-edge', (18, 15), (22, 19))
        self.add_arc('lower-corner', (22, 19), (19, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('outer', (19, 22), (2, 5), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_contour('handset', 'upper-corner', 'upper-edge', 'upper-turn', 'upper-neck', 'grip', 'lower-neck', 'lower-turn', 'lower-edge', 'lower-corner', 'outer', closed=True)
