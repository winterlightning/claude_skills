"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '110050c0-02bc-446a-8b93-961566ce20f7'
SOURCE_PATH = 'icon_set/model/icons/symbol/train_front_sub32_110050c0_02bc_446a_8b93_961566ce20f7.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '4206fe933e2fc5114dd6814787350b256ffbaae080caa3563cbe81cdcfe02024'
SOURCE_REFERENCES = (('110050c0-02bc-446a-8b93-961566ce20f7', 'pictographic-primitives/symbol/train_110050c0-02bc-446a-8b93-961566ce20f7.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'train-front-sub32-resize'
    variant_of = 'train-front-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (8, 2), (16, 2))
        self.add_line('p2-r1-1', (8, 8), (16, 8))
        self.add_arc('p2-r1-2', (16, 8), (20, 11), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (20, 11), (20, 13))
        self.add_line('p2-r1-4', (20, 13), (20, 16))
        self.add_arc('p2-r1-5', (20, 16), (16, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-6', (16, 18), (16, 18))
        self.add_line('p2-r1-7', (16, 18), (8, 18))
        self.add_line('p2-r1-8', (8, 18), (8, 18))
        self.add_arc('p2-r1-9', (8, 18), (4, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-10', (4, 16), (4, 13))
        self.add_line('p2-r1-11', (4, 13), (4, 11))
        self.add_arc('p2-r1-12', (4, 11), (8, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p3-r1-1', (4, 13), (20, 13))
        self.add_line('p4-r1-1', (8, 18), (2, 22))
        self.add_line('p5-r1-1', (16, 18), (22, 22))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', 'p2-r1-12', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
        self.relate('connect', 'p2-r1-4', 'p3-r1-1')
        self.relate('connect', 'p2-r1-6', 'p5-r1-1')
        self.relate('connect', 'p2-r1-7', 'p4-r1-1')
        self.relate('connect', 'p2-r1-7', 'p5-r1-1')
        self.relate('connect', 'p2-r1-8', 'p4-r1-1')
        self.relate('connect', 'p2-r1-10', 'p3-r1-1')
        self.relate('connect', 'p2-r1-11', 'p3-r1-1')
