"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'a392fc8f-838e-40fb-a666-e78597be5c78'
SOURCE_PATH = 'icon_set/model/icons/symbol/u_turn_left_sub32_a392fc8f_838e_40fb_a666_e78597be5c78.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'b1221800a098e8869017b8a15b22c7abf7a22960ac16fb83ee522926aa49a242'
SOURCE_REFERENCES = (('a392fc8f-838e-40fb-a666-e78597be5c78', 'pictographic-primitives/transportation/u turn left_a392fc8f-838e-40fb-a666-e78597be5c78.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'u-turn-left-sub32-resize'
    variant_of = 'u-turn-left-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'transportation'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (22, 22), (22, 10))
        self.add_arc('p1-r1-2', (22, 10), (6, 10), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (6, 10), (6, 18))
        self.add_line('p2-r1-1', (2, 13), (6, 18))
        self.add_line('p2-r1-2', (6, 18), (11, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
