"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '3d724858-fd0e-4b7f-a29c-165c62b8e0f2'
SOURCE_PATH = 'icon_set/model/icons/symbol/tulip_with_curved_leaves_sub32_symbol_3d724858_fd0e_4b7f_a29c_165c62b8e0f2.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'a668acbb01d29ca750c05ed63580f447cbda315800a4a17499f7fc1740a3171d'
SOURCE_REFERENCES = (('3d724858-fd0e-4b7f-a29c-165c62b8e0f2', 'pictographic-primitives/nature/flower_3d724858-fd0e-4b7f-a29c-165c62b8e0f2.svg'), ('3e0aa5f5-7bc6-4864-acd6-4434c86246fe', 'pictographic-primitives/nature/flower_3e0aa5f5-7bc6-4864-acd6-4434c86246fe.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'tulip-with-curved-leaves-sub32-symbol-resize'
    variant_of = 'tulip-with-curved-leaves-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'nature/batch-01'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (4, 8), (4, 2))
        self.add_line('p1-r1-2', (4, 2), (10, 6))
        self.add_line('p1-r1-3', (10, 6), (16, 2))
        self.add_line('p1-r1-4', (16, 2), (16, 8))
        self.add_arc('p1-r1-5', (16, 8), (10, 14), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (10, 14), (4, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (10, 14), (10, 22))
        self.add_arc('p3-r1-1', (2, 17), (10, 22), radius_x=8, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p4-r1-1', (10, 22), (18, 17), radius_x=8, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
