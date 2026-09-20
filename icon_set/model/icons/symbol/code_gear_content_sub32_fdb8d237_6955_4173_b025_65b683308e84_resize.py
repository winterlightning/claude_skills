"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'fdb8d237-6955-4173-b025-65b683308e84'
SOURCE_PATH = 'icon_set/model/icons/symbol/code_gear_content_sub32_fdb8d237_6955_4173_b025_65b683308e84.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '0914068f97bf1b57ec33a1ce5757343688711b2f397d15fca0f6693252186abc'
SOURCE_REFERENCES = (('fdb8d237-6955-4173-b025-65b683308e84', 'icon_set/dist/gallery/combination-originals/fdb8d237-6955-4173-b025-65b683308e84.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'code-gear-content-sub32-resize'
    variant_of = 'code-gear-content-sub32'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (24, 2))
        self.add_line('p1-r1-2', (24, 2), (24, 8))
        self.add_line('p1-r1-3', (24, 8), (29, 12))
        self.add_line('p1-r1-4', (29, 12), (29, 21))
        self.add_line('p1-r1-5', (29, 21), (24, 24))
        self.add_line('p1-r1-6', (24, 24), (24, 30))
        self.add_line('p1-r1-7', (24, 30), (16, 30))
        self.add_line('p1-r1-8', (16, 30), (16, 24))
        self.add_line('p1-r1-9', (16, 24), (11, 21))
        self.add_line('p1-r1-10', (11, 21), (11, 12))
        self.add_line('p1-r1-11', (11, 12), (16, 8))
        self.add_line('p1-r1-12', (16, 8), (16, 2))
        self.add_line('p2-r1-1', (3, 11), (2, 16))
        self.add_line('p2-r1-2', (2, 16), (3, 21))
        self.add_line('p3-r1-1', (37, 11), (38, 16))
        self.add_line('p3-r1-2', (38, 16), (37, 21))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
