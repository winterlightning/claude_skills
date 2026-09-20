"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'c30323e5-9a47-4adf-a673-a7c1c2f6a062'
SOURCE_PATH = 'icon_set/model/icons/symbol/woman_silhouette_sub32_c30323e5_9a47_4adf_a673_a7c1c2f6a062.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '0bb23aba0ab87f7172b587ef456352a7464b5d7f9848a5e2a442fc2b01e68aaa'
SOURCE_REFERENCES = (('c30323e5-9a47-4adf-a673-a7c1c2f6a062', 'pictographic-primitives/symbol/women_c30323e5-9a47-4adf-a673-a7c1c2f6a062.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'woman-silhouette-sub32-resize'
    variant_of = 'woman-silhouette-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 16), (2, 12))
        self.add_arc('p1-r1-2', (2, 12), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (22, 12), (22, 16))
        self.add_line('p2-r1-1', (2, 22), (2, 21))
        self.add_line('p2-r1-2', (2, 21), (10, 18))
        self.add_line('p2-r1-3', (10, 18), (10, 16))
        self.add_arc('p2-r1-4', (10, 16), (8, 13), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (8, 13), (8, 11))
        self.add_line('p2-r1-6', (8, 11), (12, 8))
        self.add_line('p2-r1-7', (12, 8), (16, 11))
        self.add_line('p2-r1-8', (16, 11), (16, 13))
        self.add_arc('p2-r1-9', (16, 13), (14, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-10', (14, 16), (14, 18))
        self.add_line('p2-r1-11', (14, 18), (22, 21))
        self.add_line('p2-r1-12', (22, 21), (22, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', 'p2-r1-12', closed=False)
