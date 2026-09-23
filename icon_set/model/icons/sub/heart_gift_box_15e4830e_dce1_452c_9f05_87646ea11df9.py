"""Gift box with two-loop bow and centered heart on its front."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import rounded_rect

SOURCE_ICON_ID = "15e4830e-dce1-452c-9f05-87646ea11df9"
SOURCE_PATH = "pictographic-primitives/romance/love gift box heart_15e4830e-dce1-452c-9f05-87646ea11df9.svg"
AUTHOR = "gpt-5"


class Drawing(Sub32):
    icon_id = "heart-gift-box"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/symbol"
    aliases = ("love-gift",)
    keywords = ("heart", "gift", "box", "present", "romance")

    def build(self):
        rounded_rect(self, "box", 4, 12, 28, 30, 3)
        self.add_bezier("bow-left", (16, 12), ((9, 12), (7, 10), (7, 7)), ((7, 4), (11, 4), (16, 12)))
        self.add_bezier("bow-right", (16, 12), ((21, 4), (25, 4), (25, 7)), ((25, 10), (23, 12), (16, 12)))
        self.add_contour("bow", "bow-left", "bow-right", closed=True)
        self.relate("connect", "box", "bow")
        self.add_bezier("heart", (16, 26), ((10, 22), (10, 17), (14, 17)), ((15, 17), (16, 19), (16, 19)), ((16, 19), (17, 17), (19, 17)), ((23, 17), (22, 22), (16, 26)))
        self.add_contour("heart-shape", "heart", closed=True)
