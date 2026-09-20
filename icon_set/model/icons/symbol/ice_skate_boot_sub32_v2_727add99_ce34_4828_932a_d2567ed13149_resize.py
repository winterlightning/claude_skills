"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '727add99-ce34-4828-932a-d2567ed13149'
SOURCE_PATH = 'icon_set/model/icons/symbol/ice_skate_boot_sub32_v2_727add99_ce34_4828_932a_d2567ed13149.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '88d482242a3b04618d205e0693e67db58eb97c6cafbb0b6ac9e091eaa02073dc'
SOURCE_REFERENCES = (('727add99-ce34-4828-932a-d2567ed13149', 'pictographic-primitives/symbol/skate ice_727add99-ce34-4828-932a-d2567ed13149.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'ice-skate-boot-sub32-v2-resize'
    variant_of = 'ice-skate-boot-sub32-v2'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (4, 4), (12, 2))
        self.add_line('p1-r1-2', (12, 2), (12, 7))
        self.add_arc('p1-r1-3', (12, 7), (16, 11), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_bezier('p1-r1-4', (16, 11), ((18, 11), (19, 13), (19, 16)))
        self.add_line('p1-r1-5', (19, 16), (16, 16))
        self.add_line('p1-r1-6', (16, 16), (8, 16))
        self.add_line('p1-r1-7', (8, 16), (4, 16))
        self.add_line('p1-r1-8', (4, 16), (4, 4))
        self.add_line('p2-r1-1', (2, 22), (8, 22))
        self.add_line('p2-r1-2', (8, 22), (16, 22))
        self.add_line('p2-r1-3', (16, 22), (18, 22))
        self.add_arc('p3-r1-1', (18, 22), (22, 18), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p4-r1-1', (8, 16), (8, 22))
        self.add_line('p5-r1-1', (16, 16), (16, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-5', 'p5-r1-1')
        self.relate('connect', 'p1-r1-6', 'p4-r1-1')
        self.relate('connect', 'p1-r1-6', 'p5-r1-1')
        self.relate('connect', 'p1-r1-7', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-2', 'p4-r1-1')
        self.relate('connect', 'p2-r1-2', 'p5-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p5-r1-1')
