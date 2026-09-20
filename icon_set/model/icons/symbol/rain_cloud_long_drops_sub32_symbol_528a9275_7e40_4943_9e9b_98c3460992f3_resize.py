"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '528a9275-7e40-4943-9e9b-98c3460992f3'
SOURCE_PATH = 'icon_set/model/icons/symbol/rain_cloud_long_drops_sub32_symbol_528a9275_7e40_4943_9e9b_98c3460992f3.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '85c3c355313127cc3d8443b480b30e1ff405e29c864421dba1ef52060ffb0f7b'
SOURCE_REFERENCES = (('528a9275-7e40-4943-9e9b-98c3460992f3', 'pictographic-primitives/symbol/rain_528a9275-7e40-4943-9e9b-98c3460992f3.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'rain-cloud-long-drops-sub32-symbol-resize'
    variant_of = 'rain-cloud-long-drops-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (6, 6), ((6, 5), (7, 4), (8, 3)), ((9, 2), (10, 2), (12, 2)), ((14, 2), (15, 2), (16, 3)), ((17, 4), (18, 5), (18, 6)))
        self.add_bezier('p1-r1-2', (18, 6), ((18, 6), (19, 6), (19, 6)), ((20, 6), (20, 6), (20, 7)), ((21, 7), (21, 7), (21, 7)), ((21, 7), (21, 8), (21, 8)))
        self.add_bezier('p1-r1-3', (21, 8), ((22, 8), (22, 9), (22, 9)), ((22, 9), (22, 9), (22, 9)), ((22, 9), (22, 10), (21, 10)), ((21, 10), (20, 11), (20, 11)), ((19, 11), (19, 11), (18, 11)), ((18, 11), (18, 11), (18, 11)))
        self.add_line('p1-r1-4', (18, 11), (6, 11))
        self.add_bezier('p1-r1-5', (6, 11), ((6, 11), (6, 11), (6, 11)), ((5, 11), (5, 11), (4, 11)), ((4, 11), (3, 10), (3, 10)), ((2, 10), (2, 9), (2, 9)), ((2, 9), (2, 9), (2, 9)), ((2, 9), (2, 8), (3, 8)))
        self.add_bezier('p1-r1-6', (3, 8), ((3, 8), (3, 7), (3, 7)), ((3, 7), (3, 7), (4, 7)), ((4, 6), (4, 6), (5, 6)), ((5, 6), (6, 6), (6, 6)))
        self.add_line('p2-r1-1', (6, 16), (6, 22))
        self.add_line('p3-r1-1', (13, 16), (12, 22))
        self.add_line('p4-r1-1', (20, 16), (18, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
