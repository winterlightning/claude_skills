"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '7099417a-0fa8-4ad5-84bf-e77a845b942a'
SOURCE_PATH = 'icon_set/model/icons/symbol/telephone_handset_state_204_v2_symbol_7099417a_0fa8_4ad5_84bf_e77a845b942a.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '30c2742e2fbd5fa65a71ff5e27ce6f64f0b6a7e0f72624e62c02b4f3c61944d1'
SOURCE_REFERENCES = ()

class DrawingResize(ResizeSymbol):
    icon_id = 'telephone-handset-state-204-v2-symbol-resize'
    variant_of = 'telephone-handset-state-204-v2-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'state'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('handset-0-0', (6, 2), (11, 7))
        self.add_line('handset-0-1', (11, 7), (8, 10))
        self.add_bezier('handset-0-2', (8, 10), ((10, 13), (12, 15), (15, 16)))
        self.add_line('handset-0-3', (15, 16), (17, 13))
        self.add_line('handset-0-4', (17, 13), (22, 18))
        self.add_bezier('handset-0-5', (22, 18), ((22, 21), (20, 22), (18, 22)))
        self.add_bezier('handset-0-6', (18, 22), ((11, 21), (3, 13), (2, 6)))
        self.add_bezier('handset-0-7', (2, 6), ((2, 4), (3, 2), (6, 2)))
        self.add_contour('handset-0', 'handset-0-0', 'handset-0-1', 'handset-0-2', 'handset-0-3', 'handset-0-4', 'handset-0-5', 'handset-0-6', 'handset-0-7', closed=True)
