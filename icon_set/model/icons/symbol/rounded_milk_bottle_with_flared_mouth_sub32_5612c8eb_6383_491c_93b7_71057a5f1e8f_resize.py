"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '5612c8eb-6383-491c-93b7-71057a5f1e8f'
SOURCE_PATH = 'icon_set/model/icons/symbol/rounded_milk_bottle_with_flared_mouth_sub32_5612c8eb_6383_491c_93b7_71057a5f1e8f.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '8a751431f4c817982682851781b91803151b956f9f6be39fa7eb9dc6147e48e5'
SOURCE_REFERENCES = (('5612c8eb-6383-491c-93b7-71057a5f1e8f', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/milk_5612c8eb-6383-491c-93b7-71057a5f1e8f.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'rounded-milk-bottle-with-flared-mouth-sub32-resize'
    variant_of = 'rounded-milk-bottle-with-flared-mouth-sub32'
    variant_label = 'Resize 18 × 24'
    canvas_width = 18
    canvas_height = 24
    category = 'drinks'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (5, 6), (5, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (5, 2), (13, 2))
        self.add_arc('p1-r1-3', (13, 2), (13, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (13, 6), (5, 6))
        self.add_line('p2-r1-1', (5, 6), (5, 8))
        self.add_arc('p2-r1-2', (5, 8), (3, 11), radius_x=1, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (3, 11), (2, 14), radius_x=1, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p2-r1-4', (2, 14), (2, 19))
        self.add_arc('p2-r1-5', (2, 19), (5, 22), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p2-r1-6', (5, 22), (13, 22))
        self.add_arc('p2-r1-7', (13, 22), (16, 19), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p2-r1-8', (16, 19), (16, 14))
        self.add_arc('p2-r1-9', (16, 14), (15, 11), radius_x=1, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('p2-r1-10', (15, 11), (13, 8), radius_x=1, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-11', (13, 8), (13, 6))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-11')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-11')
