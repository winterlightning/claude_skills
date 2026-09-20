"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'cb316a68-9f9f-4995-a2c1-7130db0c4b84'
SOURCE_PATH = 'icon_set/model/icons/symbol/three_node_share_symbol_sub32_symbol_cb316a68_9f9f_4995_a2c1_7130db0c4b84.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '23d71fffccec1653de8f87cada76275adb7c4452854cf5d84e731cc3685b9002'
SOURCE_REFERENCES = (('cb316a68-9f9f-4995-a2c1-7130db0c4b84', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/share 1_cb316a68-9f9f-4995-a2c1-7130db0c4b84.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'three-node-share-symbol-sub32-symbol-resize'
    variant_of = 'three-node-share-symbol-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (12, 2), (18, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (18, 8), (16, 12), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 12), (12, 13), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (12, 13), (8, 12), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (8, 12), (6, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (6, 8), (12, 2), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p2-r1-1', (5, 16), (6, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (6, 17), (8, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (8, 19), (5, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-4', (5, 22), (2, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-5', (2, 19), (5, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-1', (8, 12), (6, 17))
        self.add_arc('p4-r1-1', (18, 17), (19, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (19, 16), (22, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p4-r1-3', (22, 19), (19, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p4-r1-4', (19, 22), (16, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p4-r1-5', (16, 19), (18, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p5-r1-1', (16, 12), (18, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p5-r1-1')
        self.relate('connect', 'p1-r1-3', 'p5-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-5', 'p5-r1-1')
