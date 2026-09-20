"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '90d410c8-e7a9-4588-a960-cf1c08159a8a'
SOURCE_PATH = 'icon_set/model/icons/symbol/two_left_aligned_text_lines_sub32_90d410c8_e7a9_4588_a960_cf1c08159a8a.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '3ab0e087da1095b9e106538563bef38cce4c9dc635527e2f694dc8c65f8b2e41'
SOURCE_REFERENCES = (('90d410c8-e7a9-4588-a960-cf1c08159a8a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/comment_90d410c8-e7a9-4588-a960-cf1c08159a8a.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'two-left-aligned-text-lines-sub32-resize'
    variant_of = 'two-left-aligned-text-lines-sub32'
    variant_label = 'Resize 24 × 20'
    canvas_width = 24
    canvas_height = 20
    category = 'objects/container-components'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (22, 2))
        self.add_line('p2-r1-1', (2, 18), (15, 18))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
