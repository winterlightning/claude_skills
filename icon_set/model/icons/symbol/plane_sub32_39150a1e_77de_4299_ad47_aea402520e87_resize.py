"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '39150a1e-77de-4299-ad47-aea402520e87'
SOURCE_PATH = 'icon_set/model/icons/symbol/plane_sub32_39150a1e_77de_4299_ad47_aea402520e87.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '66a7bb6e8bcb94e1f348ee10235afcfd8de7ccafa6fd2f4a0e2f20b88b4285fa'
SOURCE_REFERENCES = (('39150a1e-77de-4299-ad47-aea402520e87', 'pictographic-primitives/travel/plane_39150a1e-77de-4299-ad47-aea402520e87.svg'), ('18f96efa-93ca-4c4e-9556-e131c14f8073', 'pictographic-primitives/travel/plane 1_18f96efa-93ca-4c4e-9556-e131c14f8073.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'plane-sub32-resize'
    variant_of = 'plane-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'travel'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 13), (7, 15))
        self.add_line('p1-r1-2', (7, 15), (11, 12))
        self.add_line('p1-r1-3', (11, 12), (10, 18))
        self.add_line('p1-r1-4', (10, 18), (16, 16))
        self.add_line('p1-r1-5', (16, 16), (16, 10))
        self.add_line('p1-r1-6', (16, 10), (20, 8))
        self.add_bezier('p1-r1-7', (20, 8), ((21, 7), (22, 6), (22, 5)))
        self.add_bezier('p1-r1-8', (22, 5), ((22, 3), (21, 3), (20, 3)))
        self.add_bezier('p1-r1-9', (20, 3), ((20, 3), (19, 3), (18, 3)))
        self.add_line('p1-r1-10', (18, 3), (16, 4))
        self.add_line('p1-r1-11', (16, 4), (10, 2))
        self.add_bezier('p1-r1-12', (10, 2), ((8, 2), (7, 3), (7, 4)))
        self.add_bezier('p1-r1-13', (7, 4), ((7, 5), (7, 5), (7, 6)))
        self.add_line('p1-r1-14', (7, 6), (11, 8))
        self.add_line('p1-r1-15', (11, 8), (7, 10))
        self.add_line('p1-r1-16', (7, 10), (3, 9))
        self.add_line('p1-r1-17', (3, 9), (2, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', closed=False)
