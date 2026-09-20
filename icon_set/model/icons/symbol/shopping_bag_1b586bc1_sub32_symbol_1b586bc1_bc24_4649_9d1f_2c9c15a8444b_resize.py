"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '1b586bc1-bc24-4649-9d1f-2c9c15a8444b'
SOURCE_PATH = 'icon_set/model/icons/symbol/shopping_bag_1b586bc1_sub32_symbol_1b586bc1_bc24_4649_9d1f_2c9c15a8444b.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'a8cb283d54148dafae234df0a7a404bb45502be9785abb81d88fd9bc35298a6b'
SOURCE_REFERENCES = (('1b586bc1-bc24-4649-9d1f-2c9c15a8444b', 'pictographic-primitives/shopping/shopping bag_1b586bc1-bc24-4649-9d1f-2c9c15a8444b.svg'), ('80985b68-e4c6-544f-91e4-19b090803024', 'pictographic-primitives/accessories/batch-07/bag carry_80985b68-e4c6-544f-91e4-19b090803024.svg'), ('a00cf782-226f-44d9-baca-8f8157db6f9a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/battery 2_a00cf782-226f-44d9-baca-8f8157db6f9a.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'shopping-bag-1b586bc1-sub32-symbol-resize'
    variant_of = 'shopping-bag-1b586bc1-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'shopping'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 22), (2, 8))
        self.add_line('p1-r1-2', (2, 8), (6, 8))
        self.add_line('p1-r1-3', (6, 8), (14, 8))
        self.add_line('p1-r1-4', (14, 8), (18, 8))
        self.add_line('p1-r1-5', (18, 8), (18, 22))
        self.add_line('p1-r1-6', (18, 22), (2, 22))
        self.add_line('p2-r1-1', (6, 11), (6, 8))
        self.add_line('p2-r1-2', (6, 8), (6, 6))
        self.add_arc('p2-r1-3', (6, 6), (14, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (14, 6), (14, 8))
        self.add_line('p2-r1-5', (14, 8), (14, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-4')
        self.relate('connect', 'p1-r1-3', 'p2-r1-5')
        self.relate('connect', 'p1-r1-4', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p2-r1-5')
