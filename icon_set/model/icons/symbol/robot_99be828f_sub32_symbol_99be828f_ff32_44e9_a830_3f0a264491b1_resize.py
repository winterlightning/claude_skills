"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '99be828f-ff32-44e9-a830-3f0a264491b1'
SOURCE_PATH = 'icon_set/model/icons/symbol/robot_99be828f_sub32_symbol_99be828f_ff32_44e9_a830_3f0a264491b1.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'f2baa01191a3c970d818c3131c45b9dbf16cb645c83d3e0ca073d3eb9e96cd0a'
SOURCE_REFERENCES = (('99be828f-ff32-44e9-a830-3f0a264491b1', 'pictographic-primitives/artificial-intelligence/robot_99be828f-ff32-44e9-a830-3f0a264491b1.svg'), ('a1bb0d4a-25ef-4c7a-beac-38a58444a803', 'pictographic-primitives/artificial-intelligence/robot_a1bb0d4a-25ef-4c7a-beac-38a58444a803.svg'), ('e46fb630-ba38-428c-8b2e-adf342a25e31', 'pictographic-primitives/artificial-intelligence/robot_e46fb630-ba38-428c-8b2e-adf342a25e31.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'robot-99be828f-sub32-symbol-resize'
    variant_of = 'robot-99be828f-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'artificial-intelligence'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (12, 2), (12, 8))
        self.add_line('p1-r1-2', (12, 8), (5, 8))
        self.add_arc('p1-r1-3', (5, 8), (2, 11), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p1-r1-4', (2, 11), (2, 19))
        self.add_arc('p1-r1-5', (2, 19), (5, 22), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p1-r1-6', (5, 22), (19, 22))
        self.add_arc('p1-r1-7', (19, 22), (22, 19), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p1-r1-8', (22, 19), (22, 11))
        self.add_arc('p1-r1-9', (22, 11), (19, 8), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p1-r1-10', (19, 8), (12, 8))
        self.add_line('p2-r1-1', (8, 13), (8, 16))
        self.add_line('p3-r1-1', (16, 13), (16, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
