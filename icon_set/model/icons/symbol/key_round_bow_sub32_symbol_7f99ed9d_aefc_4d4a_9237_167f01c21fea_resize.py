"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '7f99ed9d-aefc-4d4a-9237-167f01c21fea'
SOURCE_PATH = 'icon_set/model/icons/symbol/key_round_bow_sub32_symbol_7f99ed9d_aefc_4d4a_9237_167f01c21fea.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = '692ba94a75568e961671d60863d00d4f215108e94257568652108bcb08d625d4'
SOURCE_REFERENCES = (('7f99ed9d-aefc-4d4a-9237-167f01c21fea', 'pictographic-primitives/symbol/state key_7f99ed9d-aefc-4d4a-9237-167f01c21fea.svg'), ('8d4e51db-4d2a-4285-a400-fd2f7b20a987', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-05/key_8d4e51db-4d2a-4285-a400-fd2f7b20a987.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'key-round-bow-sub32-symbol-resize'
    variant_of = 'key-round-bow-sub32-symbol'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/symbols'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (16, 16), ((16, 19), (12, 22), (8, 22)))
        self.add_bezier('p1-r1-2', (8, 22), ((7, 22), (6, 21), (4, 20)))
        self.add_bezier('p1-r1-3', (4, 20), ((3, 18), (2, 17), (2, 16)))
        self.add_bezier('p1-r1-4', (2, 16), ((2, 12), (5, 8), (8, 8)))
        self.add_line('p2-r1-1', (8, 8), (16, 2))
        self.add_line('p2-r1-2', (16, 2), (22, 2))
        self.add_line('p2-r1-3', (22, 2), (22, 8))
        self.add_line('p2-r1-4', (22, 8), (16, 16))
        self.add_bezier('p3-r1-1', (7, 16), ((7, 14), (8, 13), (8, 13)))
        self.add_bezier('p3-r1-2', (8, 13), ((10, 13), (11, 14), (11, 16)))
        self.add_bezier('p3-r1-3', (11, 16), ((11, 16), (10, 17), (8, 17)))
        self.add_bezier('p3-r1-4', (8, 17), ((8, 17), (7, 16), (7, 16)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
