"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'f9355663-65dc-4eff-a52d-6442ba084c4a'
SOURCE_PATH = 'icon_set/model/icons/symbol/hand_saw_sub32_f9355663_65dc_4eff_a52d_6442ba084c4a.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '5c64d55aab2261fc541b4f236bb5e39b2cbaf7298afeec8001884876db1e056a'
SOURCE_REFERENCES = (('f9355663-65dc-4eff-a52d-6442ba084c4a', 'pictographic-primitives/symbol/saw_f9355663-65dc-4eff-a52d-6442ba084c4a.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'hand-saw-sub32-resize'
    variant_of = 'hand-saw-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 6), (6, 2))
        self.add_line('p1-r1-2', (6, 2), (16, 11))
        self.add_line('p1-r1-3', (16, 11), (21, 16))
        self.add_bezier('p1-r1-4', (21, 16), ((21, 16), (22, 17), (22, 18)))
        self.add_bezier('p1-r1-5', (22, 18), ((22, 19), (21, 20), (21, 20)))
        self.add_line('p1-r1-6', (21, 20), (18, 22))
        self.add_line('p1-r1-7', (18, 22), (10, 16))
        self.add_line('p1-r1-8', (10, 16), (8, 14))
        self.add_line('p1-r1-9', (8, 14), (8, 11))
        self.add_line('p1-r1-10', (8, 11), (4, 11))
        self.add_line('p1-r1-11', (4, 11), (4, 8))
        self.add_line('p1-r1-12', (4, 8), (2, 8))
        self.add_line('p1-r1-13', (2, 8), (2, 6))
        self.add_line('p2-r1-1', (16, 11), (12, 14))
        self.add_line('p2-r1-2', (12, 14), (10, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-2')
        self.relate('connect', 'p1-r1-8', 'p2-r1-2')
