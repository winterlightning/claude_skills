"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'b3826549-0cc8-4855-a250-66873df772a9'
SOURCE_PATH = 'icon_set/model/icons/symbol/minimal_happy_smiling_face_sub32_b3826549_0cc8_4855_a250_66873df772a9.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'db2bda51a8a2dd1477e2feb206d0518f7dbb90e16e3d0575a1925d73152fd225'
SOURCE_REFERENCES = (('b3826549-0cc8-4855-a250-66873df772a9', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/smiley face_b3826549-0cc8-4855-a250-66873df772a9.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'minimal-happy-smiling-face-sub32-resize'
    variant_of = 'minimal-happy-smiling-face-sub32'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'objects/container-components'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (10, 2), (10, 7))
        self.add_line('p2-r1-1', (30, 2), (30, 7))
        self.add_arc('p3-r1-1', (2, 17), (38, 17), radius_x=18, radius_y=13, large_arc=False, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
