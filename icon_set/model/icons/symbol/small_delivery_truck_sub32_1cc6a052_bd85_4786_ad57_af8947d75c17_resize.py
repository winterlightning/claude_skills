"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '1cc6a052-bd85-4786-ad57-af8947d75c17'
SOURCE_PATH = 'icon_set/model/icons/symbol/small_delivery_truck_sub32_1cc6a052_bd85_4786_ad57_af8947d75c17.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '8bf87ca68710f9afc98ea1939fd42eb28ab8a3f8a66009f0ba6f736a3ee2e569'
SOURCE_REFERENCES = (('1cc6a052-bd85-4786-ad57-af8947d75c17', 'pictographic-primitives/transportation/truck_1cc6a052-bd85-4786-ad57-af8947d75c17.svg'), ('7fa4b356-9d73-4875-94fd-29e892bef9d8', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/transportation/truck_7fa4b356-9d73-4875-94fd-29e892bef9d8.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'small-delivery-truck-sub32-resize'
    variant_of = 'small-delivery-truck-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'transportation'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (3, 16), (2, 16))
        self.add_line('p1-r1-2', (2, 16), (2, 2))
        self.add_line('p1-r1-3', (2, 2), (12, 2))
        self.add_line('p1-r1-4', (12, 2), (12, 6))
        self.add_line('p1-r1-5', (12, 6), (12, 16))
        self.add_line('p1-r1-6', (12, 16), (8, 16))
        self.add_line('p2-r1-1', (12, 6), (16, 6))
        self.add_bezier('p3-r1-1', (16, 6), ((19, 6), (22, 9), (22, 12)))
        self.add_line('p4-r1-1', (22, 12), (22, 16))
        self.add_line('p4-r1-2', (22, 16), (21, 16))
        self.add_line('p5-r1-1', (12, 16), (16, 16))
        self.add_bezier('p6-r1-1', (3, 16), ((3, 15), (4, 14), (6, 14)))
        self.add_bezier('p6-r1-2', (6, 14), ((7, 14), (8, 15), (8, 16)))
        self.add_bezier('p6-r1-3', (8, 16), ((8, 17), (7, 18), (6, 18)))
        self.add_bezier('p6-r1-4', (6, 18), ((4, 18), (3, 17), (3, 16)))
        self.add_bezier('p7-r1-1', (16, 16), ((16, 15), (17, 14), (18, 14)))
        self.add_bezier('p7-r1-2', (18, 14), ((20, 14), (21, 15), (21, 16)))
        self.add_bezier('p7-r1-3', (21, 16), ((21, 17), (20, 18), (18, 18)))
        self.add_bezier('p7-r1-4', (18, 18), ((17, 18), (16, 17), (16, 16)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', closed=False)
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', 'p7-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p6-r1-1')
        self.relate('connect', 'p1-r1-1', 'p6-r1-4')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p5-r1-1')
        self.relate('connect', 'p1-r1-6', 'p5-r1-1')
        self.relate('connect', 'p1-r1-6', 'p6-r1-2')
        self.relate('connect', 'p1-r1-6', 'p6-r1-3')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p4-r1-2', 'p7-r1-2')
        self.relate('connect', 'p4-r1-2', 'p7-r1-3')
        self.relate('connect', 'p5-r1-1', 'p7-r1-1')
        self.relate('connect', 'p5-r1-1', 'p7-r1-4')
