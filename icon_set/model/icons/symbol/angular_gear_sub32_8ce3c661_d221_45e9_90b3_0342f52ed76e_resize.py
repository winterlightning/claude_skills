"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '8ce3c661-d221-45e9-90b3-0342f52ed76e'
SOURCE_PATH = 'icon_set/model/icons/symbol/angular_gear_sub32_8ce3c661_d221_45e9_90b3_0342f52ed76e.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '78c73cd0356a3c3bb03ec9ee5936ae40481ba6c3155d4d97890f7fb582139a85'
SOURCE_REFERENCES = (('8ce3c661-d221-45e9-90b3-0342f52ed76e', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_8ce3c661-d221-45e9-90b3-0342f52ed76e.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'angular-gear-sub32-resize'
    variant_of = 'angular-gear-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/interface-essential'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (11, 2), (9, 6))
        self.add_line('p1-r1-2', (9, 6), (7, 6))
        self.add_line('p1-r1-3', (7, 6), (4, 6))
        self.add_line('p1-r1-4', (4, 6), (2, 8))
        self.add_line('p1-r1-5', (2, 8), (4, 11))
        self.add_line('p1-r1-6', (4, 11), (3, 12))
        self.add_line('p1-r1-7', (3, 12), (2, 13))
        self.add_line('p1-r1-8', (2, 13), (3, 18))
        self.add_line('p1-r1-9', (3, 18), (6, 18))
        self.add_line('p1-r1-10', (6, 18), (6, 22))
        self.add_line('p1-r1-11', (6, 22), (10, 22))
        self.add_line('p1-r1-12', (10, 22), (10, 18))
        self.add_line('p1-r1-13', (10, 18), (12, 18))
        self.add_line('p1-r1-14', (12, 18), (14, 18))
        self.add_line('p1-r1-15', (14, 18), (14, 22))
        self.add_line('p1-r1-16', (14, 22), (18, 22))
        self.add_line('p1-r1-17', (18, 22), (18, 18))
        self.add_line('p1-r1-18', (18, 18), (21, 18))
        self.add_line('p1-r1-19', (21, 18), (22, 13))
        self.add_line('p1-r1-20', (22, 13), (21, 12))
        self.add_line('p1-r1-21', (21, 12), (20, 11))
        self.add_line('p1-r1-22', (20, 11), (22, 8))
        self.add_line('p1-r1-23', (22, 8), (20, 6))
        self.add_line('p1-r1-24', (20, 6), (17, 6))
        self.add_line('p1-r1-25', (17, 6), (15, 6))
        self.add_line('p1-r1-26', (15, 6), (13, 2))
        self.add_line('p1-r1-27', (13, 2), (11, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', 'p1-r1-19', 'p1-r1-20', 'p1-r1-21', 'p1-r1-22', 'p1-r1-23', 'p1-r1-24', 'p1-r1-25', 'p1-r1-26', 'p1-r1-27', closed=False)
