"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'a4e06e7b-9f6c-4283-b751-e75fde558688'
SOURCE_PATH = 'icon_set/model/icons/symbol/woman_long_hair_sub32_a4e06e7b_9f6c_4283_b751_e75fde558688.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'defeb153032c4732d58e4056427b368248f6152076644caecfb9913a69da101c'
SOURCE_REFERENCES = (('a4e06e7b-9f6c-4283-b751-e75fde558688', 'pictographic-primitives/symbol/women_a4e06e7b-9f6c-4283-b751-e75fde558688.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'woman-long-hair-sub32-resize'
    variant_of = 'woman-long-hair-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 22), (2, 12))
        self.add_arc('p1-r1-2', (2, 12), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (22, 12), (22, 22))
        self.add_line('p2-r1-1', (8, 16), (8, 11))
        self.add_line('p2-r1-2', (8, 11), (12, 8))
        self.add_line('p2-r1-3', (12, 8), (16, 11))
        self.add_line('p2-r1-4', (16, 11), (16, 16))
        self.add_arc('p2-r1-5', (16, 16), (8, 16), radius_x=4, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
