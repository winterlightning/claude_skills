"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '25032f12-63bc-403a-9b53-69083f3313cb'
SOURCE_PATH = 'icon_set/model/icons/symbol/lock_sub32_symbol_25032f12_63bc_403a_9b53_69083f3313cb.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '7e81fbd53e6eb371a14f309a6e11aa0e4509fec0a7533204df8d660d8e3fc6a7'
SOURCE_REFERENCES = (('25032f12-63bc-403a-9b53-69083f3313cb', 'pictographic-primitives/interface-essential/lock_25032f12-63bc-403a-9b53-69083f3313cb.svg'), ('e43b261d-5d07-450c-ab97-9058803311d6', 'pictographic-primitives/interface-essential/lock_e43b261d-5d07-450c-ab97-9058803311d6.svg'), ('ee9cb073-d745-4a2a-a54b-ab36b6f8efb7', 'pictographic-primitives/interface-essential/lock_ee9cb073-d745-4a2a-a54b-ab36b6f8efb7.svg'), ('386cb547-821f-4d23-a0b8-bb7f43205473', 'pictographic-primitives/interface-essential/lock_386cb547-821f-4d23-a0b8-bb7f43205473.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'lock-sub32-symbol-resize'
    variant_of = 'lock-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (10, 2), (9, 2))
        self.add_bezier('p1-r1-2', (9, 2), ((8, 2), (8, 2), (7, 2)), ((6, 3), (6, 3), (5, 3)), ((5, 4), (5, 4), (4, 5)), ((4, 6), (4, 6), (4, 7)))
        self.add_line('p1-r1-3', (4, 7), (4, 10))
        self.add_line('p1-r1-4', (4, 10), (16, 10))
        self.add_line('p1-r1-5', (16, 10), (16, 7))
        self.add_bezier('p1-r1-6', (16, 7), ((16, 6), (16, 6), (15, 5)), ((15, 5), (15, 4), (14, 4)), ((14, 3), (13, 3), (13, 3)), ((12, 2), (12, 2), (11, 2)))
        self.add_line('p1-r1-7', (11, 2), (10, 2))
        self.add_line('p2-r1-1', (10, 22), (4, 22))
        self.add_bezier('p2-r1-2', (4, 22), ((4, 22), (3, 22), (3, 22)), ((3, 21), (3, 21), (3, 21)), ((2, 21), (2, 20), (2, 20)), ((2, 20), (2, 19), (2, 19)), ((2, 19), (2, 19), (2, 19)))
        self.add_line('p2-r1-3', (2, 19), (2, 11))
        self.add_bezier('p2-r1-4', (2, 11), ((2, 11), (2, 11), (2, 11)), ((3, 10), (3, 10), (3, 10)), ((3, 10), (3, 10), (3, 10)), ((4, 10), (4, 10), (4, 10)), ((4, 10), (4, 10), (4, 10)))
        self.add_line('p3-r1-1', (10, 22), (16, 22))
        self.add_bezier('p3-r1-2', (16, 22), ((16, 22), (17, 22), (17, 22)), ((17, 21), (17, 21), (17, 21)), ((18, 21), (18, 20), (18, 20)), ((18, 20), (18, 19), (18, 19)), ((18, 19), (18, 19), (18, 19)))
        self.add_line('p3-r1-3', (18, 19), (18, 19))
        self.add_line('p3-r1-4', (18, 19), (18, 11))
        self.add_bezier('p3-r1-5', (18, 11), ((18, 11), (18, 11), (18, 11)), ((17, 10), (17, 10), (17, 10)), ((17, 10), (17, 10), (17, 10)), ((16, 10), (16, 10), (16, 10)), ((16, 10), (16, 10), (16, 10)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p3-r1-5')
        self.relate('connect', 'p1-r1-5', 'p3-r1-5')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
