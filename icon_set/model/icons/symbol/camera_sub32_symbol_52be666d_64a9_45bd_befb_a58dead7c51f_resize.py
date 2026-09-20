"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '52be666d-64a9-45bd-befb-a58dead7c51f'
SOURCE_PATH = 'icon_set/model/icons/symbol/camera_sub32_symbol_52be666d_64a9_45bd_befb_a58dead7c51f.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '08a3257c5d48e46c9c7e2a0121678395c606e81e903cb94d591ff27e96cea58a'
SOURCE_REFERENCES = (('52be666d-64a9-45bd-befb-a58dead7c51f', 'pictographic-primitives/video/camera_52be666d-64a9-45bd-befb-a58dead7c51f.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'camera-sub32-symbol-resize'
    variant_of = 'camera-sub32-symbol'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'objects/media'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (4, 5), (6, 5))
        self.add_line('p1-r1-2', (6, 5), (9, 2))
        self.add_line('p1-r1-3', (9, 2), (15, 2))
        self.add_line('p1-r1-4', (15, 2), (18, 5))
        self.add_line('p1-r1-5', (18, 5), (20, 5))
        self.add_arc('p1-r1-6', (20, 5), (22, 7), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (22, 7), (22, 16))
        self.add_arc('p1-r1-8', (22, 16), (20, 18), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (20, 18), (4, 18))
        self.add_arc('p1-r1-10', (4, 18), (2, 16), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-11', (2, 16), (2, 7))
        self.add_arc('p1-r1-12', (2, 7), (4, 5), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p2-r1-1', (9, 11), (15, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (15, 11), (9, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
