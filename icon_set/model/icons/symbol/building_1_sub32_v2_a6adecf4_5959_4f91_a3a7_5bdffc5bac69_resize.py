"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'a6adecf4-5959-4f91-a3a7-5bdffc5bac69'
SOURCE_PATH = 'icon_set/model/icons/symbol/building_1_sub32_v2_a6adecf4_5959_4f91_a3a7_5bdffc5bac69.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '0125ab87e4e2a9159e5d4c9d032ddcf7eaf83bfb83d721bcb9e9eda7bc257185'
SOURCE_REFERENCES = (('a6adecf4-5959-4f91-a3a7-5bdffc5bac69', 'pictographic-primitives/building/building 1_a6adecf4-5959-4f91-a3a7-5bdffc5bac69.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'building-1-sub32-v2-resize'
    variant_of = 'building-1-sub32-v2'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'building'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 22), (2, 2))
        self.add_line('p1-r1-2', (2, 2), (19, 11))
        self.add_line('p1-r1-3', (19, 11), (19, 22))
        self.add_line('p1-r1-4', (19, 22), (2, 22))
        self.add_line('p2-r1-1', (8, 14), (12, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
