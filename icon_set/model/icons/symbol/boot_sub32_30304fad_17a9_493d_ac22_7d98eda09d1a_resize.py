"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '30304fad-17a9-493d-ac22-7d98eda09d1a'
SOURCE_PATH = 'icon_set/model/icons/symbol/boot_sub32_30304fad_17a9_493d_ac22_7d98eda09d1a.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'f10c70ea8df08f61db928e254828108f0aea3f48af1c56646a8f5518f0bc002c'
SOURCE_REFERENCES = (('30304fad-17a9-493d-ac22-7d98eda09d1a', 'pictographic-primitives/symbol/boot_30304fad-17a9-493d-ac22-7d98eda09d1a.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'boot-sub32-resize'
    variant_of = 'boot-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'symbols/standalone'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (12, 2))
        self.add_line('p1-r1-2', (12, 2), (12, 8))
        self.add_line('p1-r1-3', (12, 8), (12, 12))
        self.add_arc('p1-r1-4', (12, 12), (16, 16), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (16, 16), (18, 16))
        self.add_arc('p1-r1-6', (18, 16), (22, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (22, 20), (22, 22))
        self.add_line('p1-r1-8', (22, 22), (11, 22))
        self.add_line('p1-r1-9', (11, 22), (8, 20))
        self.add_line('p1-r1-10', (8, 20), (2, 20))
        self.add_line('p1-r1-11', (2, 20), (2, 2))
        self.add_line('p2-r1-1', (12, 8), (16, 8))
        self.add_line('p3-r1-1', (12, 12), (16, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
