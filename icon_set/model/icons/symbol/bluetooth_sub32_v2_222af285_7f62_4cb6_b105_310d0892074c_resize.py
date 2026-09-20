"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '222af285-7f62-4cb6-b105-310d0892074c'
SOURCE_PATH = 'icon_set/model/icons/symbol/bluetooth_sub32_v2_222af285_7f62_4cb6_b105_310d0892074c.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '3bc125bc461b823d995792928b10368b02b7a630ba992960ffad3310b92c44fc'
SOURCE_REFERENCES = (('222af285-7f62-4cb6-b105-310d0892074c', 'pictographic-primitives/networks/bluetooth_222af285-7f62-4cb6-b105-310d0892074c.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'bluetooth-sub32-v2-resize'
    variant_of = 'bluetooth-sub32-v2'
    variant_label = 'Resize 21 × 24'
    canvas_width = 21
    canvas_height = 24
    category = 'networks'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 8), (9, 12))
        self.add_line('p2-r1-1', (2, 16), (9, 12))
        self.add_line('p3-r1-1', (9, 12), (19, 17))
        self.add_line('p3-r1-2', (19, 17), (9, 22))
        self.add_line('p3-r1-3', (9, 22), (9, 12))
        self.add_line('p4-r1-1', (9, 12), (9, 2))
        self.add_line('p4-r1-2', (9, 2), (19, 7))
        self.add_line('p4-r1-3', (19, 7), (9, 12))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-3')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-3')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-3')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-3')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-3')
        self.relate('connect', 'p3-r1-3', 'p4-r1-1')
        self.relate('connect', 'p3-r1-3', 'p4-r1-3')
