"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'bf5296da-9358-4863-98b8-b6dd1fe60594'
SOURCE_PATH = 'icon_set/model/icons/symbol/bag_bf5296da_sub32_v2_symbol_bf5296da_9358_4863_98b8_b6dd1fe60594.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '62462efe14ff94f34126cd493ec86d60b0db88a2a1a0beabe39d8b201d27e4bf'
SOURCE_REFERENCES = (('bf5296da-9358-4863-98b8-b6dd1fe60594', 'pictographic-primitives/photography/bag_bf5296da-9358-4863-98b8-b6dd1fe60594.svg'), ('e213494f-7bcb-44b0-a54e-8a069e24c6ea', 'pictographic-primitives/shopping/bag_e213494f-7bcb-44b0-a54e-8a069e24c6ea.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'bag-bf5296da-sub32-v2-symbol-resize'
    variant_of = 'bag-bf5296da-sub32-v2-symbol'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'photography'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (8, 7), (8, 3))
        self.add_bezier('p1-r1-2', (8, 3), ((8, 3), (9, 3), (9, 2)), ((10, 2), (10, 2), (10, 2)), ((11, 2), (11, 2), (12, 2)), ((12, 3), (13, 3), (13, 3)))
        self.add_line('p1-r1-3', (13, 3), (13, 7))
        self.add_line('p2-r1-1', (5, 7), (8, 7))
        self.add_line('p2-r1-2', (8, 7), (13, 7))
        self.add_line('p2-r1-3', (13, 7), (16, 7))
        self.add_line('p2-r1-4', (16, 7), (19, 22))
        self.add_line('p2-r1-5', (19, 22), (2, 22))
        self.add_line('p2-r1-6', (2, 22), (5, 7))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
