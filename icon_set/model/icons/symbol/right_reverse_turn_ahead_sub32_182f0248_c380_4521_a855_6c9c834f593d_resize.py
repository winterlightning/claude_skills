"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '182f0248-c380-4521-a855-6c9c834f593d'
SOURCE_PATH = 'icon_set/model/icons/symbol/right_reverse_turn_ahead_sub32_182f0248_c380_4521_a855_6c9c834f593d.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '7047ab02d2fd0ddeae48d70e4eb4a6c82098d8edfd86d92a06239c2d259b4b62'
SOURCE_REFERENCES = (('182f0248-c380-4521-a855-6c9c834f593d', 'pictographic-primitives/transportation/right reverse turn ahead_182f0248-c380-4521-a855-6c9c834f593d.svg'), ('7740d388-2c2b-4378-bd9e-8bad227a64cf', 'pictographic-primitives/symbol/right reverse turn ahead 1_7740d388-2c2b-4378-bd9e-8bad227a64cf.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'right-reverse-turn-ahead-sub32-resize'
    variant_of = 'right-reverse-turn-ahead-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'transportation'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 22), (2, 11))
        self.add_line('p1-r1-2', (2, 11), (13, 11))
        self.add_line('p1-r1-3', (13, 11), (13, 2))
        self.add_line('p1-r1-4', (13, 2), (9, 6))
        self.add_line('p2-r1-1', (13, 2), (18, 6))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
