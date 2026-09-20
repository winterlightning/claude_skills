"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '908d485e-3113-4818-aeae-2057781ce2d5'
SOURCE_PATH = 'icon_set/model/icons/symbol/plain_car_front_sub32_symbol_908d485e_3113_4818_aeae_2057781ce2d5.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '85fbf73b8d644165cd7f248cc04267ebd1133fbcb93d4450e6b1cf2196712aed'
SOURCE_REFERENCES = (('908d485e-3113-4818-aeae-2057781ce2d5', 'pictographic-primitives/transportation/car 1_908d485e-3113-4818-aeae-2057781ce2d5.svg'), ('8156415b-cbe0-4085-a1b2-de1314bf33de', 'pictographic-primitives/transportation/car_8156415b-cbe0-4085-a1b2-de1314bf33de.svg'), ('b90b17e9-30a0-4203-bb54-82de55a03dae', 'pictographic-primitives/transportation/car_b90b17e9-30a0-4203-bb54-82de55a03dae.svg'), ('b2a2cd39-2c37-46cd-9a88-38b142304d18', 'pictographic-primitives/transportation/car_b2a2cd39-2c37-46cd-9a88-38b142304d18.svg'), ('55d4a39f-2307-4a74-8263-cac55d88920b', 'pictographic-primitives/transportation/car 1_55d4a39f-2307-4a74-8263-cac55d88920b.svg'), ('6eaf361a-c125-4908-a062-3aee68b537ed', 'pictographic-primitives/transportation/car 1_6eaf361a-c125-4908-a062-3aee68b537ed.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'plain-car-front-sub32-symbol-resize'
    variant_of = 'plain-car-front-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/transportation'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (4, 8), (4, 8))
        self.add_line('p1-r1-2', (4, 8), (20, 8))
        self.add_line('p1-r1-3', (20, 8), (20, 8))
        self.add_bezier('p1-r1-4', (20, 8), ((21, 8), (21, 8), (21, 8)), ((21, 8), (21, 8), (21, 8)), ((22, 8), (22, 8), (22, 8)), ((22, 9), (22, 9), (22, 9)), ((22, 9), (22, 9), (22, 9)), ((22, 10), (22, 10), (21, 10)))
        self.add_line('p1-r1-5', (21, 10), (21, 13))
        self.add_line('p1-r1-6', (21, 13), (21, 18))
        self.add_bezier('p1-r1-7', (21, 18), ((21, 18), (21, 18), (21, 18)), ((21, 18), (21, 18), (21, 18)), ((21, 18), (21, 18), (21, 18)), ((21, 18), (21, 18), (20, 18)))
        self.add_line('p1-r1-8', (20, 18), (20, 18))
        self.add_line('p1-r1-9', (20, 18), (16, 18))
        self.add_line('p1-r1-10', (16, 18), (8, 18))
        self.add_line('p1-r1-11', (8, 18), (4, 18))
        self.add_line('p1-r1-12', (4, 18), (4, 18))
        self.add_bezier('p1-r1-13', (4, 18), ((3, 18), (3, 18), (3, 18)), ((3, 18), (3, 18), (3, 18)), ((3, 18), (3, 18), (3, 18)), ((3, 18), (3, 18), (3, 18)))
        self.add_line('p1-r1-14', (3, 18), (3, 13))
        self.add_line('p1-r1-15', (3, 13), (3, 10))
        self.add_bezier('p1-r1-16', (3, 10), ((2, 10), (2, 10), (2, 9)), ((2, 9), (2, 9), (2, 9)), ((2, 9), (2, 9), (2, 8)), ((2, 8), (2, 8), (3, 8)), ((3, 8), (3, 8), (3, 8)), ((3, 8), (3, 8), (4, 8)))
        self.add_line('p2-r1-1', (4, 8), (8, 2))
        self.add_line('p2-r1-2', (8, 2), (16, 2))
        self.add_line('p2-r1-3', (16, 2), (20, 8))
        self.add_line('p3-r1-1', (4, 18), (4, 22))
        self.add_line('p4-r1-1', (20, 18), (20, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-3')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
        self.relate('connect', 'p1-r1-8', 'p4-r1-1')
        self.relate('connect', 'p1-r1-9', 'p4-r1-1')
        self.relate('connect', 'p1-r1-11', 'p3-r1-1')
        self.relate('connect', 'p1-r1-12', 'p3-r1-1')
