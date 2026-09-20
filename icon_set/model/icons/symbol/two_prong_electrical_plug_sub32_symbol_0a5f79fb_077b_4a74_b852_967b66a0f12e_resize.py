"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '0a5f79fb-077b-4a74-b852-967b66a0f12e'
SOURCE_PATH = 'icon_set/model/icons/symbol/two_prong_electrical_plug_sub32_symbol_0a5f79fb_077b_4a74_b852_967b66a0f12e.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'f4f952b402f9b8c14c7fa15ee4f67bf05e3c20cb983d00fa6b9f99198f323256'
SOURCE_REFERENCES = (('0a5f79fb-077b-4a74-b852-967b66a0f12e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/plug_0a5f79fb-077b-4a74-b852-967b66a0f12e.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'two-prong-electrical-plug-sub32-symbol-resize'
    variant_of = 'two-prong-electrical-plug-sub32-symbol'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'objects/container-components'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 8), (6, 8))
        self.add_line('p1-r1-2', (6, 8), (14, 8))
        self.add_line('p1-r1-3', (14, 8), (18, 8))
        self.add_line('p1-r1-4', (18, 8), (18, 13))
        self.add_arc('p1-r1-5', (18, 13), (10, 18), radius_x=8, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (10, 18), (2, 13), radius_x=8, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 13), (2, 8))
        self.add_line('p2-r1-1', (6, 2), (6, 8))
        self.add_line('p3-r1-1', (14, 2), (14, 8))
        self.add_line('p4-r1-1', (10, 18), (10, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p4-r1-1')
        self.relate('connect', 'p1-r1-6', 'p4-r1-1')
