"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '15a300e5-b82d-4912-8a2a-869d03bdf837'
SOURCE_PATH = 'icon_set/model/icons/symbol/person_digging_with_shovel_sub32_15a300e5_b82d_4912_8a2a_869d03bdf837.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'fdae0f72ab83446a3d1225b2f83e8ffdbcac0baf8d5ef882e36ce3bc56685b92'
SOURCE_REFERENCES = (('15a300e5-b82d-4912-8a2a-869d03bdf837', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/person with a shovel_15a300e5-b82d-4912-8a2a-869d03bdf837.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'person-digging-with-shovel-sub32-resize'
    variant_of = 'person-digging-with-shovel-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/container-components'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (12, 5), (15, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (15, 2), (18, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (18, 5), (15, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (15, 8), (12, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('p2-r1-1', (15, 12), ((15, 16), (11, 18), (8, 18)))
        self.add_line('p3-r1-1', (15, 12), (18, 16))
        self.add_line('p4-r1-1', (2, 22), (8, 18))
        self.add_line('p4-r1-2', (8, 18), (11, 22))
        self.add_line('p5-r1-1', (2, 12), (15, 12))
        self.add_line('p5-r1-2', (15, 12), (18, 18))
        self.add_line('p6-r1-1', (18, 18), (21, 16))
        self.add_line('p6-r1-2', (21, 16), (22, 22))
        self.add_line('p6-r1-3', (22, 22), (16, 21))
        self.add_line('p6-r1-4', (16, 21), (18, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-2')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-2')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-2')
        self.relate('connect', 'p5-r1-2', 'p6-r1-1')
        self.relate('connect', 'p5-r1-2', 'p6-r1-4')
