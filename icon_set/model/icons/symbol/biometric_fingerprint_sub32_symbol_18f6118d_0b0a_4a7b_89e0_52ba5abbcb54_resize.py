"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '18f6118d-0b0a-4a7b-89e0-52ba5abbcb54'
SOURCE_PATH = 'icon_set/model/icons/symbol/biometric_fingerprint_sub32_symbol_18f6118d_0b0a_4a7b_89e0_52ba5abbcb54.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '1dd8a7ff696f29d308c6d6184f15928774fc0a7a1f71d0a6971c61909d0fe044'
SOURCE_REFERENCES = (('18f6118d-0b0a-4a7b-89e0-52ba5abbcb54', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/fingerprint_18f6118d-0b0a-4a7b-89e0-52ba5abbcb54.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'biometric-fingerprint-sub32-symbol-resize'
    variant_of = 'biometric-fingerprint-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/container-components'
    semantic_kind = 'modifier'

    def build(self):
        self.add_line('p1-r1-1', (2, 16), (2, 12))
        self.add_arc('p1-r1-2', (2, 12), (22, 12), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (22, 12), (22, 16))
        self.add_bezier('p2-r1-1', (6, 18), ((8, 16), (7, 12), (8, 11)))
        self.add_bezier('p2-r1-2', (8, 11), ((8, 8), (10, 7), (12, 7)))
        self.add_bezier('p2-r1-3', (12, 7), ((15, 7), (17, 8), (17, 11)))
        self.add_line('p2-r1-4', (17, 11), (17, 16))
        self.add_bezier('p2-r1-5', (17, 16), ((17, 18), (18, 21), (18, 22)))
        self.add_bezier('p3-r1-1', (12, 13), ((12, 16), (12, 20), (10, 22)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
