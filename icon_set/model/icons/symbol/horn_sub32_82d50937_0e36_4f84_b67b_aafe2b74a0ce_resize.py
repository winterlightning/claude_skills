"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '82d50937-0e36-4f84-b67b-aafe2b74a0ce'
SOURCE_PATH = 'icon_set/model/icons/symbol/horn_sub32_82d50937_0e36_4f84_b67b_aafe2b74a0ce.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'a3948f71d638aa2fd81e4a88f033533dcb4e97ddec90954ad064a004443f8bf6'
SOURCE_REFERENCES = (('82d50937-0e36-4f84-b67b-aafe2b74a0ce', 'pictographic-primitives/transportation/horn_82d50937-0e36-4f84-b67b-aafe2b74a0ce.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'horn-sub32-resize'
    variant_of = 'horn-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'transportation'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (7, 7))
        self.add_line('p1-r1-2', (7, 7), (17, 7))
        self.add_line('p1-r1-3', (17, 7), (22, 2))
        self.add_line('p1-r1-4', (22, 2), (22, 14))
        self.add_line('p1-r1-5', (22, 14), (17, 11))
        self.add_line('p1-r1-6', (17, 11), (7, 11))
        self.add_line('p1-r1-7', (7, 11), (2, 14))
        self.add_line('p1-r1-8', (2, 14), (2, 2))
        self.add_line('p2-r1-1', (7, 11), (7, 16))
        self.add_arc('p2-r1-2', (7, 16), (9, 18), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('p2-r1-3', (9, 18), (15, 18))
        self.add_arc('p2-r1-4', (15, 18), (17, 16), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('p2-r1-5', (17, 16), (17, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.relate('connect', 'p1-r1-5', 'p2-r1-5')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-5')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
