"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '4e457d2e-149f-4085-a06c-b3f6cb685191'
SOURCE_PATH = 'icon_set/model/icons/symbol/text_wrap_right_layout_sub32_4e457d2e_149f_4085_a06c_b3f6cb685191.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'e0b792bb9ebb119016e6055b532625307dbb87fd9ec1dfa88f6e99f9ef04009b'
SOURCE_REFERENCES = (('4e457d2e-149f-4085-a06c-b3f6cb685191', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/lines with small square_4e457d2e-149f-4085-a06c-b3f6cb685191.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'text-wrap-right-layout-sub32-resize'
    variant_of = 'text-wrap-right-layout-sub32'
    variant_label = 'Resize 40 × 32'
    canvas_width = 40
    canvas_height = 32
    category = 'objects/container-components'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (24, 2), (38, 2))
        self.add_line('p1-r1-2', (38, 2), (38, 16))
        self.add_line('p1-r1-3', (38, 16), (24, 16))
        self.add_line('p1-r1-4', (24, 16), (24, 2))
        self.add_line('p2-r1-1', (2, 2), (15, 2))
        self.add_line('p3-r1-1', (2, 16), (15, 16))
        self.add_line('p4-r1-1', (2, 30), (38, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
