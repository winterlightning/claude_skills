"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '52860099-ee8d-46b2-84ff-237a2c5f681c'
SOURCE_PATH = 'icon_set/model/icons/symbol/geometric_three_toed_paw_sub32_symbol_52860099_ee8d_46b2_84ff_237a2c5f681c.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '1e216b4b30d27de2023dd43f4a9703932f23a7379dd26fefb21e495c5e1361c8'
SOURCE_REFERENCES = (('52860099-ee8d-46b2-84ff-237a2c5f681c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/paw print_52860099-ee8d-46b2-84ff-237a2c5f681c.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'geometric-three-toed-paw-sub32-symbol-resize'
    variant_of = 'geometric-three-toed-paw-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/container-components'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (10, 4), ((10, 4), (10, 3), (10, 3)), ((10, 3), (10, 3), (11, 3)), ((11, 2), (11, 2), (11, 2)), ((11, 2), (12, 2), (12, 2)))
        self.add_bezier('p1-r1-2', (12, 2), ((12, 2), (13, 2), (13, 2)), ((13, 2), (13, 2), (13, 3)), ((14, 3), (14, 3), (14, 3)), ((14, 3), (14, 4), (14, 4)))
        self.add_bezier('p1-r1-3', (14, 4), ((14, 4), (14, 5), (14, 5)), ((14, 5), (14, 5), (13, 5)), ((13, 6), (13, 6), (13, 6)), ((13, 6), (12, 6), (12, 6)))
        self.add_bezier('p1-r1-4', (12, 6), ((12, 6), (11, 6), (11, 6)), ((11, 6), (11, 6), (11, 5)), ((10, 5), (10, 5), (10, 5)), ((10, 5), (10, 4), (10, 4)))
        self.add_bezier('p2-r1-1', (2, 11), ((2, 11), (2, 10), (2, 10)), ((2, 10), (2, 10), (2, 10)), ((2, 10), (2, 9), (2, 9)), ((3, 9), (3, 8), (3, 8)), ((3, 8), (4, 8), (4, 8)), ((4, 8), (4, 8), (4, 8)))
        self.add_bezier('p2-r1-2', (4, 8), ((4, 8), (4, 8), (4, 8)), ((5, 8), (5, 8), (5, 8)), ((6, 8), (6, 9), (6, 9)), ((6, 9), (6, 10), (6, 10)), ((6, 10), (6, 10), (6, 10)), ((6, 10), (6, 11), (6, 11)))
        self.add_bezier('p2-r1-3', (6, 11), ((6, 11), (6, 12), (6, 12)), ((6, 12), (6, 12), (6, 12)), ((5, 13), (5, 13), (5, 13)), ((5, 13), (4, 13), (4, 13)))
        self.add_bezier('p2-r1-4', (4, 13), ((3, 13), (3, 13), (3, 13)))
        self.add_bezier('p2-r1-5', (3, 13), ((2, 12), (2, 11), (2, 11)))
        self.add_bezier('p3-r1-1', (18, 11), ((18, 11), (18, 10), (18, 10)), ((18, 10), (18, 10), (18, 10)), ((18, 10), (18, 9), (18, 9)), ((18, 9), (18, 8), (19, 8)), ((19, 8), (19, 8), (20, 8)), ((20, 8), (20, 8), (20, 8)))
        self.add_bezier('p3-r1-2', (20, 8), ((20, 8), (20, 8), (20, 8)), ((20, 8), (21, 8), (21, 8)), ((21, 8), (21, 9), (22, 9)), ((22, 9), (22, 10), (22, 10)), ((22, 10), (22, 10), (22, 10)), ((22, 10), (22, 11), (22, 11)))
        self.add_bezier('p3-r1-3', (22, 11), ((22, 11), (22, 12), (21, 13)))
        self.add_bezier('p3-r1-4', (21, 13), ((21, 13), (21, 13), (20, 13)))
        self.add_bezier('p3-r1-5', (20, 13), ((20, 13), (19, 13), (19, 13)), ((19, 13), (19, 13), (18, 12)), ((18, 12), (18, 12), (18, 12)), ((18, 12), (18, 11), (18, 11)))
        self.add_line('p4-r1-1', (12, 13), (6, 22))
        self.add_line('p4-r1-2', (6, 22), (18, 22))
        self.add_line('p4-r1-3', (18, 22), (12, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
