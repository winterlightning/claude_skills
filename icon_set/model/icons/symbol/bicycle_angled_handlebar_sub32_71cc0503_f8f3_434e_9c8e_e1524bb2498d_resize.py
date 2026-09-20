"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '71cc0503-f8f3-434e-9c8e-e1524bb2498d'
SOURCE_PATH = 'icon_set/model/icons/symbol/bicycle_angled_handlebar_sub32_71cc0503_f8f3_434e_9c8e_e1524bb2498d.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '32493d65ad9ab8c582147631a2bd5efd2aa566ac720d0637f3e5e4edd1f403c9'
SOURCE_REFERENCES = (('71cc0503-f8f3-434e-9c8e-e1524bb2498d', 'pictographic-primitives/transportation/bicycle_71cc0503-f8f3-434e-9c8e-e1524bb2498d.svg'), ('7e9c7c99-94c3-4ae5-a57d-56a00190f3e6', 'pictographic-primitives/transportation/bicycle_7e9c7c99-94c3-4ae5-a57d-56a00190f3e6.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'bicycle-angled-handlebar-sub32-resize'
    variant_of = 'bicycle-angled-handlebar-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'objects/transportation'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (2, 13), ((2, 13), (2, 14), (2, 14)), ((2, 15), (2, 16), (3, 16)), ((3, 17), (4, 18), (6, 18)), ((7, 18), (8, 17), (9, 16)), ((9, 16), (10, 15), (10, 14)), ((10, 14), (9, 13), (9, 13)))
        self.add_bezier('p1-r1-2', (9, 13), ((9, 12), (10, 12), (10, 11)), ((10, 10), (9, 10), (9, 9)), ((8, 8), (7, 7), (6, 7)), ((4, 7), (3, 8), (3, 9)), ((2, 10), (2, 10), (2, 11)), ((2, 12), (2, 12), (2, 13)))
        self.add_bezier('p2-r1-1', (15, 13), ((15, 13), (14, 14), (14, 14)), ((14, 15), (15, 16), (15, 16)), ((16, 17), (17, 18), (18, 18)), ((20, 18), (21, 17), (21, 16)), ((22, 16), (22, 15), (22, 14)), ((22, 14), (22, 13), (22, 13)))
        self.add_bezier('p2-r1-2', (22, 13), ((22, 12), (22, 12), (22, 11)), ((22, 10), (22, 10), (21, 9)), ((21, 8), (20, 7), (18, 7)), ((17, 7), (16, 8), (15, 9)), ((15, 10), (14, 10), (14, 11)), ((14, 12), (15, 12), (15, 13)))
        self.add_line('p3-r1-1', (6, 10), (10, 6))
        self.add_line('p3-r1-2', (10, 6), (15, 6))
        self.add_line('p3-r1-3', (15, 6), (18, 10))
        self.add_line('p4-r1-1', (4, 2), (8, 2))
        self.add_line('p4-r1-2', (8, 2), (10, 6))
        self.add_line('p5-r1-1', (15, 6), (15, 3))
        self.add_line('p5-r1-2', (15, 3), (18, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
        self.relate('connect', 'p3-r1-2', 'p4-r1-2')
        self.relate('connect', 'p3-r1-2', 'p5-r1-1')
        self.relate('connect', 'p3-r1-3', 'p5-r1-1')
