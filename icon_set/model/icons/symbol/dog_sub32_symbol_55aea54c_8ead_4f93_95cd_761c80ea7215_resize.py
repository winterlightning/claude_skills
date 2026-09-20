"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '55aea54c-8ead-4f93-95cd-761c80ea7215'
SOURCE_PATH = 'icon_set/model/icons/symbol/dog_sub32_symbol_55aea54c_8ead_4f93_95cd_761c80ea7215.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'eb1e6ffd89b3a14ee692608bddeb0f2207c0423d7f74c6449817dad40666f9bc'
SOURCE_REFERENCES = (('55aea54c-8ead-4f93-95cd-761c80ea7215', 'pictographic-primitives/pets/dog_55aea54c-8ead-4f93-95cd-761c80ea7215.svg'), ('c099ef25-3154-4ff5-ba1a-7e0f9f82bb67', 'pictographic-primitives/pets/dog_c099ef25-3154-4ff5-ba1a-7e0f9f82bb67.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'dog-sub32-symbol-resize'
    variant_of = 'dog-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'pets'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (2, 18), ((4, 12), (7, 6), (11, 2)))
        self.add_line('p1-r1-2', (11, 2), (12, 7))
        self.add_bezier('p1-r1-3', (12, 7), ((13, 8), (16, 8), (18, 8)))
        self.add_bezier('p1-r1-4', (18, 8), ((21, 9), (22, 11), (22, 13)))
        self.add_bezier('p1-r1-5', (22, 13), ((22, 16), (18, 16), (13, 17)))
        self.add_line('p1-r1-6', (13, 17), (11, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
