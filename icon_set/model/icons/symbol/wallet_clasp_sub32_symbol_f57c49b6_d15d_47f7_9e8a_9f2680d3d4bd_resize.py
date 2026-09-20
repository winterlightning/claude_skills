"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'f57c49b6-d15d-47f7-9e8a-9f2680d3d4bd'
SOURCE_PATH = 'icon_set/model/icons/symbol/wallet_clasp_sub32_symbol_f57c49b6_d15d_47f7_9e8a_9f2680d3d4bd.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '0c6d6ef1ae7119ab3a0b0a32bcbadb8a91e907ea7a0f88affe077f86785c6c0f'
SOURCE_REFERENCES = (('f57c49b6-d15d-47f7-9e8a-9f2680d3d4bd', 'pictographic-primitives/symbol/wallet_f57c49b6-d15d-47f7-9e8a-9f2680d3d4bd.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'wallet-clasp-sub32-symbol-resize'
    variant_of = 'wallet-clasp-sub32-symbol'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (7, 2), (33, 2))
        self.add_arc('p1-r1-2', (33, 2), (38, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (38, 7), (38, 12))
        self.add_line('p1-r1-4', (38, 12), (38, 24))
        self.add_line('p1-r1-5', (38, 24), (38, 25))
        self.add_arc('p1-r1-6', (38, 25), (33, 30), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (33, 30), (7, 30))
        self.add_arc('p1-r1-8', (7, 30), (2, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (2, 25), (2, 10))
        self.add_line('p1-r1-10', (2, 10), (2, 7))
        self.add_arc('p1-r1-11', (2, 7), (7, 2), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (2, 10), (20, 10))
        self.add_line('p3-r1-1', (38, 12), (29, 12))
        self.add_arc('p3-r1-2', (29, 12), (29, 24), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p3-r1-3', (29, 24), (38, 24))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-3')
        self.relate('connect', 'p1-r1-5', 'p3-r1-3')
        self.relate('connect', 'p1-r1-9', 'p2-r1-1')
        self.relate('connect', 'p1-r1-10', 'p2-r1-1')
