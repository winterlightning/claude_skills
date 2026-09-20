"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'f0327d2c-bb99-5e91-9ec2-af95814cf0fe'
SOURCE_PATH = 'icon_set/model/icons/symbol/three_leaf_sprout_sub32_symbol_f0327d2c_bb99_5e91_9ec2_af95814cf0fe.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '68e2172c1ac6ba3fe9f4b5fef6b94d102811305e58e3b52b41b0a71380a7c7bd'
SOURCE_REFERENCES = (('f0327d2c-bb99-5e91-9ec2-af95814cf0fe', 'pictographic-primitives/nature/plant_f0327d2c-bb99-5e91-9ec2-af95814cf0fe.svg'), ('4a47df00-a455-41d9-84a4-6416eb861ee6', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/leaf_4a47df00-a455-41d9-84a4-6416eb861ee6.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'three-leaf-sprout-sub32-symbol-resize'
    variant_of = 'three-leaf-sprout-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'nature/batch-02'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (10, 2), (10, 10), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (10, 10), (10, 2), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (10, 10), (10, 20))
        self.add_line('p3-r1-1', (10, 20), (10, 22))
        self.add_arc('p4-r1-1', (2, 13), (10, 20), radius_x=8, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (10, 20), (2, 13), radius_x=8, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p5-r1-1', (18, 13), (10, 20), radius_x=8, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('p5-r1-2', (10, 20), (18, 13), radius_x=8, radius_y=7, large_arc=False, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-2')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-2')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-2')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-2')
        self.relate('connect', 'p4-r1-2', 'p5-r1-1')
        self.relate('connect', 'p4-r1-2', 'p5-r1-2')
