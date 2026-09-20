"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'e3a175a4-e3aa-43f8-8841-6f146bd5990b'
SOURCE_PATH = 'icon_set/model/icons/symbol/divided_circle_arch_sub32_e3a175a4_e3aa_43f8_8841_6f146bd5990b.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'a83f7250ad6c8af9884c743529de9091b0a490299fa6eb71a03c84f6a7872772'
SOURCE_REFERENCES = (('e3a175a4-e3aa-43f8-8841-6f146bd5990b', 'pictographic-primitives/symbol/divided face_e3a175a4-e3aa-43f8-8841-6f146bd5990b.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'divided-circle-arch-sub32-resize'
    variant_of = 'divided-circle-arch-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'symbols/standalone'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (12, 2), (12, 22), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (12, 22), (12, 2), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (12, 2), (12, 15))
        self.add_line('p2-r1-2', (12, 15), (12, 22))
        self.add_arc('p3-r1-1', (8, 17), (12, 15), radius_x=4, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (12, 15), (16, 17), radius_x=4, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-2')
