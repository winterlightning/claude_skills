"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '1791bde9-d3d7-4a85-9cfe-95949447c94e'
SOURCE_PATH = 'icon_set/model/icons/symbol/star_of_david_hexagram_sub32_1791bde9_d3d7_4a85_9cfe_95949447c94e.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'f3151bb2ab4a4c2b7870a015783afea7741679a1c061586d03cc3314b6f7fbad'
SOURCE_REFERENCES = (('1791bde9-d3d7-4a85-9cfe-95949447c94e', 'pictographic-primitives/symbol/star of david_1791bde9-d3d7-4a85-9cfe-95949447c94e.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'star-of-david-hexagram-sub32-resize'
    variant_of = 'star-of-david-hexagram-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (12, 2), (16, 7))
        self.add_line('p1-r1-2', (16, 7), (18, 12))
        self.add_line('p1-r1-3', (18, 12), (22, 17))
        self.add_line('p1-r1-4', (22, 17), (16, 17))
        self.add_line('p1-r1-5', (16, 17), (8, 17))
        self.add_line('p1-r1-6', (8, 17), (2, 17))
        self.add_line('p1-r1-7', (2, 17), (6, 12))
        self.add_line('p1-r1-8', (6, 12), (8, 7))
        self.add_line('p1-r1-9', (8, 7), (12, 2))
        self.add_line('p2-r1-1', (2, 7), (8, 7))
        self.add_line('p2-r1-2', (8, 7), (16, 7))
        self.add_line('p2-r1-3', (16, 7), (22, 7))
        self.add_line('p2-r1-4', (22, 7), (18, 12))
        self.add_line('p2-r1-5', (18, 12), (16, 17))
        self.add_line('p2-r1-6', (16, 17), (12, 22))
        self.add_line('p2-r1-7', (12, 22), (8, 17))
        self.add_line('p2-r1-8', (8, 17), (6, 12))
        self.add_line('p2-r1-9', (6, 12), (2, 7))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-1', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p1-r1-2', 'p2-r1-4')
        self.relate('connect', 'p1-r1-2', 'p2-r1-5')
        self.relate('connect', 'p1-r1-3', 'p2-r1-4')
        self.relate('connect', 'p1-r1-3', 'p2-r1-5')
        self.relate('connect', 'p1-r1-4', 'p2-r1-5')
        self.relate('connect', 'p1-r1-4', 'p2-r1-6')
        self.relate('connect', 'p1-r1-5', 'p2-r1-5')
        self.relate('connect', 'p1-r1-5', 'p2-r1-6')
        self.relate('connect', 'p1-r1-5', 'p2-r1-7')
        self.relate('connect', 'p1-r1-5', 'p2-r1-8')
        self.relate('connect', 'p1-r1-6', 'p2-r1-7')
        self.relate('connect', 'p1-r1-6', 'p2-r1-8')
        self.relate('connect', 'p1-r1-7', 'p2-r1-8')
        self.relate('connect', 'p1-r1-7', 'p2-r1-9')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-2')
        self.relate('connect', 'p1-r1-8', 'p2-r1-8')
        self.relate('connect', 'p1-r1-8', 'p2-r1-9')
        self.relate('connect', 'p1-r1-9', 'p2-r1-1')
        self.relate('connect', 'p1-r1-9', 'p2-r1-2')
