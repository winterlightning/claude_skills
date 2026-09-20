"""Independent grid-snapped resize candidate; see validation report before use."""
from ._resize_base import ResizeSymbol
SOURCE_ICON_ID = '5ee1d8ff-a85e-4f98-8d10-414df21c0f8a'
SOURCE_PATH = 'icon_set/model/icons/symbol/happy_face_with_closed_eyes_sub32_5ee1d8ff_a85e_4f98_8d10_414df21c0f8a.py'
AUTHOR = 'gpt-6'
SOURCE_MODEL_SHA256 = 'ef975d44de91753cb927233d5100fb73106a4ee21c6329324d5c1ba6171eabac'
SOURCE_REFERENCES = (('5ee1d8ff-a85e-4f98-8d10-414df21c0f8a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/smiley face_5ee1d8ff-a85e-4f98-8d10-414df21c0f8a.svg'),)

class DrawingResize(ResizeSymbol):
    icon_id = 'happy-face-with-closed-eyes-sub32-resize'
    variant_of = 'happy-face-with-closed-eyes-sub32'
    variant_label = 'Resize 24 × 22'
    canvas_width = 24
    canvas_height = 22
    category = 'objects/container-components'
    semantic_kind = 'modifier'

    def build(self):
        self.add_bezier('p1-r1-1', (2, 3), ((2, 3), (3, 3), (3, 2)), ((4, 2), (4, 2), (5, 2)), ((6, 2), (6, 2), (7, 2)), ((7, 3), (8, 3), (8, 3)))
        self.add_bezier('p2-r1-1', (16, 3), ((16, 3), (17, 3), (17, 2)), ((18, 2), (18, 2), (19, 2)), ((20, 2), (20, 2), (21, 2)), ((21, 3), (22, 3), (22, 3)))
        self.add_bezier('p3-r1-1', (3, 12), ((3, 14), (4, 16), (6, 18)), ((7, 19), (10, 20), (12, 20)), ((14, 20), (17, 19), (18, 18)), ((20, 16), (21, 14), (21, 12)))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
