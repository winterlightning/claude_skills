"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '4a06d69f-2edd-4b80-be80-a8b144c9e4ee'
SOURCE_PATH = 'icon_set/model/icons/symbol/yen_symbol_content_sub32_4a06d69f_2edd_4b80_be80_a8b144c9e4ee.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '90af313f05f54f24440839aa7abec3af9f4927e05aced5d14443d5881668ad77'
SOURCE_REFERENCES = (('4a06d69f-2edd-4b80-be80-a8b144c9e4ee', 'icon_set/dist/gallery/combination-originals/4a06d69f-2edd-4b80-be80-a8b144c9e4ee.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'yen-symbol-content-sub32-resize'
    variant_of = 'yen-symbol-content-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (10, 12))
        self.add_line('p1-r1-2', (10, 12), (18, 2))
        self.add_line('p2-r1-1', (10, 12), (10, 22))
        self.add_line('p3-r1-1', (4, 14), (10, 14))
        self.add_line('p3-r1-2', (10, 14), (16, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
