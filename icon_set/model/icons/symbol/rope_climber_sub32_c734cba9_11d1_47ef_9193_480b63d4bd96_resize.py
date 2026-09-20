"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'c734cba9-11d1-47ef-9193-480b63d4bd96'
SOURCE_PATH = 'icon_set/model/icons/symbol/rope_climber_sub32_c734cba9_11d1_47ef_9193_480b63d4bd96.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'd5acd11cfe642d7d643f7f792592174d7ea7b3bd551580eb7c4c3c83c74e4c91'
SOURCE_REFERENCES = (('c734cba9-11d1-47ef-9193-480b63d4bd96', 'pictographic-primitives/sports/climbing sports_c734cba9-11d1-47ef-9193-480b63d4bd96.svg'), ('64bc05d2-25cd-4e18-83c2-a00814ef966b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/climbing_64bc05d2-25cd-4e18-83c2-a00814ef966b.svg'))

class DrawingResize(ResizeSymbol):
    icon_id = 'rope-climber-sub32-resize'
    variant_of = 'rope-climber-sub32'
    variant_label = 'Resize 24 × 24'
    canvas_width = 24
    canvas_height = 24
    category = 'objects/sports'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (7, 5), (11, 5), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (11, 5), (7, 5), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-1', (22, 2), (22, 8))
        self.add_line('p3-r1-1', (10, 12), (10, 16))
        self.add_line('p4-r1-1', (10, 12), (4, 12))
        self.add_line('p4-r1-2', (4, 12), (2, 8))
        self.add_line('p5-r1-1', (10, 12), (16, 8))
        self.add_line('p5-r1-2', (16, 8), (22, 8))
        self.add_line('p6-r1-1', (6, 16), (10, 16))
        self.add_line('p6-r1-2', (10, 16), (16, 16))
        self.add_line('p7-r1-1', (10, 16), (4, 22))
        self.add_line('p8-r1-1', (10, 16), (16, 18))
        self.add_line('p8-r1-2', (16, 18), (16, 22))
        self.add_arc('p9-r1-1', (22, 8), (16, 16), radius_x=6, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_contour('path-8-1', 'p8-r1-1', 'p8-r1-2', closed=False)
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p5-r1-2')
        self.relate('connect', 'p2-r1-1', 'p9-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p6-r1-1')
        self.relate('connect', 'p3-r1-1', 'p6-r1-2')
        self.relate('connect', 'p3-r1-1', 'p7-r1-1')
        self.relate('connect', 'p3-r1-1', 'p8-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p5-r1-2', 'p9-r1-1')
        self.relate('connect', 'p6-r1-1', 'p7-r1-1')
        self.relate('connect', 'p6-r1-1', 'p8-r1-1')
        self.relate('connect', 'p6-r1-2', 'p7-r1-1')
        self.relate('connect', 'p6-r1-2', 'p8-r1-1')
        self.relate('connect', 'p6-r1-2', 'p9-r1-1')
        self.relate('connect', 'p7-r1-1', 'p8-r1-1')
