"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '9c8857a3-198d-47d1-be28-3a6d0762e293'
SOURCE_PATH = 'icon_set/model/icons/symbol/dumbbell_tall_plates_sub32_9c8857a3_198d_47d1_be28_3a6d0762e293.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '752f3c8a34378c8cdd951a5cfc5df29db24688746b0fa22a0d8a285de8ba1f1f'
SOURCE_REFERENCES = (('9c8857a3-198d-47d1-be28-3a6d0762e293', 'pictographic-primitives/sports/dumbbell_9c8857a3-198d-47d1-be28-3a6d0762e293.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'dumbbell-tall-plates-sub32-resize'
    variant_of = 'dumbbell-tall-plates-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/sports'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (6, 3), (8, 3))
        self.add_bezier('p1-r1-2', (8, 3), ((8, 3), (8, 3), (8, 3)), ((8, 3), (8, 3), (8, 3)), ((8, 3), (8, 3), (8, 3)), ((8, 3), (8, 3), (8, 4)))
        self.add_line('p1-r1-3', (8, 4), (8, 12))
        self.add_line('p1-r1-4', (8, 12), (8, 20))
        self.add_bezier('p1-r1-5', (8, 20), ((8, 21), (8, 21), (8, 21)), ((8, 21), (8, 21), (8, 21)), ((8, 21), (8, 21), (8, 21)), ((8, 21), (8, 21), (8, 21)))
        self.add_line('p1-r1-6', (8, 21), (6, 21))
        self.add_bezier('p1-r1-7', (6, 21), ((6, 22), (6, 22), (5, 22)), ((5, 22), (5, 22), (5, 22)), ((5, 22), (5, 22), (4, 22)), ((4, 22), (4, 22), (4, 21)), ((4, 21), (4, 21), (4, 21)), ((4, 21), (4, 21), (4, 20)))
        self.add_line('p1-r1-8', (4, 20), (4, 12))
        self.add_line('p1-r1-9', (4, 12), (4, 4))
        self.add_bezier('p1-r1-10', (4, 4), ((4, 3), (4, 3), (4, 3)), ((4, 3), (4, 3), (4, 3)), ((4, 2), (4, 2), (4, 2)), ((5, 2), (5, 2), (5, 2)), ((5, 2), (5, 2), (5, 2)), ((6, 2), (6, 2), (6, 3)))
        self.add_line('p2-r1-1', (16, 3), (18, 3))
        self.add_bezier('p2-r1-2', (18, 3), ((18, 2), (18, 2), (19, 2)), ((19, 2), (19, 2), (19, 2)), ((19, 2), (19, 2), (20, 2)), ((20, 2), (20, 2), (20, 3)), ((20, 3), (20, 3), (20, 3)), ((20, 3), (20, 3), (20, 4)))
        self.add_line('p2-r1-3', (20, 4), (20, 12))
        self.add_line('p2-r1-4', (20, 12), (20, 20))
        self.add_bezier('p2-r1-5', (20, 20), ((20, 21), (20, 21), (20, 21)), ((20, 21), (20, 21), (20, 21)), ((20, 22), (20, 22), (20, 22)), ((19, 22), (19, 22), (19, 22)), ((19, 22), (19, 22), (19, 22)), ((18, 22), (18, 22), (18, 21)))
        self.add_line('p2-r1-6', (18, 21), (16, 21))
        self.add_bezier('p2-r1-7', (16, 21), ((16, 21), (16, 21), (16, 21)), ((16, 21), (16, 21), (16, 21)), ((16, 21), (16, 21), (16, 21)), ((16, 21), (16, 21), (16, 20)))
        self.add_line('p2-r1-8', (16, 20), (16, 12))
        self.add_line('p2-r1-9', (16, 12), (16, 4))
        self.add_bezier('p2-r1-10', (16, 4), ((16, 3), (16, 3), (16, 3)), ((16, 3), (16, 3), (16, 3)), ((16, 3), (16, 3), (16, 3)), ((16, 3), (16, 3), (16, 3)))
        self.add_line('p3-r1-1', (8, 12), (16, 12))
        self.add_line('p4-r1-1', (2, 12), (4, 12))
        self.add_line('p5-r1-1', (20, 12), (22, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-8', 'p4-r1-1')
        self.relate('connect', 'p1-r1-9', 'p4-r1-1')
        self.relate('connect', 'p2-r1-3', 'p5-r1-1')
        self.relate('connect', 'p2-r1-4', 'p5-r1-1')
        self.relate('connect', 'p2-r1-8', 'p3-r1-1')
        self.relate('connect', 'p2-r1-9', 'p3-r1-1')
