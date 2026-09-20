"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '3ec61357-503d-46af-90a8-2fa210293e19'
SOURCE_PATH = 'icon_set/model/icons/symbol/heart_pulse_sub32_symbol_3ec61357_503d_46af_90a8_2fa210293e19.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '1bc82bb6cbf4fa48b339019e8e17352525e2803637454f9cc87fcafde6fe7998'
SOURCE_REFERENCES = (('3ec61357-503d-46af-90a8-2fa210293e19', 'pictographic-primitives/symbol/heart throb_3ec61357-503d-46af-90a8-2fa210293e19.svg'), ('a9dc34df-bbc3-4ab4-a859-ebdb7d92a804', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/sports/heart rate_a9dc34df-bbc3-4ab4-a859-ebdb7d92a804.svg'), ('468beab8-6edf-4e7f-9ee2-0f23f5c3b360', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/sports/heart rate_468beab8-6edf-4e7f-9ee2-0f23f5c3b360.svg'), ('a954f676-1cce-4e19-81eb-ec067ec52edc', 'icon_set/dist/gallery/combination-originals/a954f676-1cce-4e19-81eb-ec067ec52edc.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'heart-pulse-sub32-symbol-resize'
    variant_of = 'heart-pulse-sub32-symbol'
    variant_label = 'Resize 38 × 32'
    canvas_width = 38
    canvas_height = 32
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (2, 7), ((2, 6), (3, 5), (4, 4)), ((6, 3), (8, 2), (10, 2)), ((13, 2), (15, 3), (17, 4)), ((18, 5), (19, 6), (19, 7)))
        self.add_bezier('p1-r1-2', (19, 7), ((19, 6), (20, 5), (21, 4)), ((23, 3), (25, 2), (28, 2)), ((30, 2), (32, 3), (34, 4)), ((35, 5), (36, 6), (36, 7)))
        self.add_bezier('p1-r1-3', (36, 7), ((36, 11), (36, 14), (35, 18)))
        self.add_line('p1-r1-4', (35, 18), (19, 30))
        self.add_line('p1-r1-5', (19, 30), (3, 18))
        self.add_bezier('p1-r1-6', (3, 18), ((2, 14), (2, 11), (2, 7)))
        self.add_line('p2-r1-1', (3, 18), (9, 18))
        self.add_line('p2-r1-2', (9, 18), (12, 12))
        self.add_line('p2-r1-3', (12, 12), (19, 19))
        self.add_line('p2-r1-4', (19, 19), (24, 13))
        self.add_line('p2-r1-5', (24, 13), (26, 18))
        self.add_line('p2-r1-6', (26, 18), (35, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-6')
        self.relate('connect', 'p1-r1-4', 'p2-r1-6')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
