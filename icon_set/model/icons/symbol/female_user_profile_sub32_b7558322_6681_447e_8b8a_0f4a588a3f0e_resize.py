"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = 'b7558322-6681-447e-8b8a-0f4a588a3f0e'
SOURCE_PATH = 'icon_set/model/icons/symbol/female_user_profile_sub32_b7558322_6681_447e_8b8a_0f4a588a3f0e.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'aa8bd64a2c2b10a4b3f4181ca4561809be3d010ae3cdd8527f341ff141dcee39'
SOURCE_REFERENCES = (('b7558322-6681-447e-8b8a-0f4a588a3f0e', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/images/woman_b7558322-6681-447e-8b8a-0f4a588a3f0e.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'female-user-profile-sub32-resize'
    variant_of = 'female-user-profile-sub32'
    variant_label = 'Resize 20 × 24'
    canvas_width = 20
    canvas_height = 24
    category = 'objects/images'
    semantic_kind = 'modifier'

    def build(self):
        self.add_arc('p1-r1-1', (5, 7), (15, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (15, 7), (5, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('p2-r1-1', (5, 7), ((7, 7), (9, 6), (10, 5)))
        self.add_bezier('p2-r1-2', (10, 5), ((11, 6), (13, 7), (15, 7)))
        self.add_arc('p3-r1-1', (2, 22), (10, 16), radius_x=8, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (10, 16), (18, 22), radius_x=8, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
