"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '4458e707-6b88-4e46-8b5b-6a58a4c07dc7'
SOURCE_PATH = 'icon_set/model/icons/symbol/rand_sub32_4458e707_6b88_4e46_8b5b_6a58a4c07dc7.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'bdb2383ac11fe8b93a1762de8ba48622aaec4feb7cad2c9ea4c06a235ed1e40b'
SOURCE_REFERENCES = (('4458e707-6b88-4e46-8b5b-6a58a4c07dc7', 'pictographic-primitives/money/rand_4458e707-6b88-4e46-8b5b-6a58a4c07dc7.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'rand-sub32-resize'
    variant_of = 'rand-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'money'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 22), (2, 2))
        self.add_line('p1-r1-2', (2, 2), (12, 2))
        self.add_arc('p1-r1-3', (12, 2), (12, 14), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (12, 14), (2, 14))
        self.add_line('p2-r1-1', (12, 14), (18, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
