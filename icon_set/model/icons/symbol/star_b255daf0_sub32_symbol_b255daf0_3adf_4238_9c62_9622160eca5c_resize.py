"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'b255daf0-3adf-4238-9c62-9622160eca5c'
SOURCE_PATH = 'icon_set/model/icons/symbol/star_b255daf0_sub32_symbol_b255daf0_3adf_4238_9c62_9622160eca5c.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'a3647939177edf7a3deecc07251718181160610d072e8434e4ba9f161065bf0f'
SOURCE_REFERENCES = (('b255daf0-3adf-4238-9c62-9622160eca5c', 'pictographic-primitives/holidays/star_b255daf0-3adf-4238-9c62-9622160eca5c.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'star-b255daf0-sub32-symbol-resize'
    variant_of = 'star-b255daf0-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'holidays'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (12, 2), (15, 8))
        self.add_line('p1-r1-2', (15, 8), (22, 10))
        self.add_line('p1-r1-3', (22, 10), (16, 15))
        self.add_line('p1-r1-4', (16, 15), (18, 22))
        self.add_line('p1-r1-5', (18, 22), (12, 18))
        self.add_line('p1-r1-6', (12, 18), (6, 22))
        self.add_line('p1-r1-7', (6, 22), (8, 15))
        self.add_line('p1-r1-8', (8, 15), (2, 10))
        self.add_line('p1-r1-9', (2, 10), (9, 8))
        self.add_line('p1-r1-10', (9, 8), (12, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
