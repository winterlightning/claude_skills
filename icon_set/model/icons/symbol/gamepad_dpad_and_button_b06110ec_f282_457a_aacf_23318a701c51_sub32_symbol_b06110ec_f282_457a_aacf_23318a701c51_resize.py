"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'b06110ec-f282-457a-aacf-23318a701c51'
SOURCE_PATH = 'icon_set/model/icons/symbol/gamepad_dpad_and_button_b06110ec_f282_457a_aacf_23318a701c51_sub32_symbol_b06110ec_f282_457a_aacf_23318a701c51.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '5ca42f36a058dbf792834cc54dd357f42ec18b8753b0ba3b3ff03e563633a0ce'
SOURCE_REFERENCES = (('b06110ec-f282-457a-aacf-23318a701c51', 'pictographic-primitives/medias/gaming_b06110ec-f282-457a-aacf-23318a701c51.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'gamepad-dpad-and-button-b06110ec-f282-457a-aacf-23318a701c51-sub32-symbol-resize'
    variant_of = 'gamepad-dpad-and-button-b06110ec-f282-457a-aacf-23318a701c51-sub32-symbol'
    variant_label = 'Resize 42 × 32'
    canvas_width = 42
    canvas_height = 32
    category = 'objects/media'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (12, 2), (30, 2))
        self.add_bezier('p1-r1-2', (30, 2), ((31, 2), (33, 3), (34, 4)), ((35, 5), (36, 7), (37, 9)), ((38, 11), (39, 13), (39, 16)), ((40, 19), (40, 22), (40, 25)))
        self.add_bezier('p1-r1-3', (40, 25), ((39, 26), (38, 28), (37, 29)), ((36, 30), (34, 30), (32, 30)), ((31, 30), (29, 30), (28, 29)), ((27, 28), (26, 26), (25, 25)))
        self.add_bezier('p1-r1-4', (25, 25), ((25, 25), (25, 24), (24, 24)), ((23, 24), (22, 24), (21, 24)), ((20, 24), (19, 24), (18, 24)), ((17, 24), (17, 25), (17, 25)))
        self.add_bezier('p1-r1-5', (17, 25), ((16, 26), (15, 28), (14, 29)), ((13, 30), (11, 30), (10, 30)), ((8, 30), (6, 30), (5, 29)), ((4, 28), (3, 26), (2, 25)))
        self.add_bezier('p1-r1-6', (2, 25), ((2, 22), (2, 19), (3, 16)), ((3, 13), (4, 11), (5, 9)), ((6, 7), (7, 5), (8, 4)), ((9, 3), (11, 2), (12, 2)))
        self.add_line('p2-r1-1', (14, 14), (12, 14))
        self.add_line('p3-r1-1', (14, 14), (17, 14))
        self.add_line('p4-r1-1', (14, 14), (14, 12))
        self.add_line('p5-r1-1', (14, 14), (14, 17))
        self.add_line('p6-r1-1', (29, 14), (29, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
