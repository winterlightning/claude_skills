"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '159051f0-87aa-4c05-9b9f-53abd2ca05ef'
SOURCE_PATH = 'icon_set/model/icons/symbol/thumbs_up_symbol_sub32_symbol_159051f0_87aa_4c05_9b9f_53abd2ca05ef.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '154751d4a0d06abaec213ee6d47514aba3e0b0e9daedc56671c672d2d4b4deb5'
SOURCE_REFERENCES = (('159051f0-87aa-4c05-9b9f-53abd2ca05ef', 'pictographic-primitives/symbol/thumbs up_159051f0-87aa-4c05-9b9f-53abd2ca05ef.svg'), ('5680cb28-5cf7-4d7c-98be-ae372bac6440', 'pictographic-primitives/symbol/thumbs up_5680cb28-5cf7-4d7c-98be-ae372bac6440.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'thumbs-up-symbol-sub32-symbol-resize'
    variant_of = 'thumbs-up-symbol-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'symbol'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 12), (6, 12))
        self.add_line('p1-r1-2', (6, 12), (6, 22))
        self.add_line('p1-r1-3', (6, 22), (2, 22))
        self.add_line('p1-r1-4', (2, 22), (2, 12))
        self.add_line('p2-r1-1', (6, 12), (11, 6))
        self.add_line('p2-r1-2', (11, 6), (11, 2))
        self.add_line('p2-r1-3', (11, 2), (16, 2))
        self.add_line('p2-r1-4', (16, 2), (18, 6))
        self.add_line('p2-r1-5', (18, 6), (16, 11))
        self.add_line('p2-r1-6', (16, 11), (18, 11))
        self.add_arc('p3-r1-1', (18, 11), (22, 14), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p4-r1-1', (22, 14), (22, 18))
        self.add_arc('p5-r1-1', (22, 18), (18, 22), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p6-r1-1', (18, 22), (6, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p6-r1-1')
        self.relate('connect', 'p1-r1-3', 'p6-r1-1')
        self.relate('connect', 'p2-r1-6', 'p3-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
