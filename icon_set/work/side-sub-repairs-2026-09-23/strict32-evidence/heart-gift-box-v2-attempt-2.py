"""Gift box with two-loop bow and centered heart on its front."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import rounded_rect

SOURCE_ICON_ID = "15e4830e-dce1-452c-9f05-87646ea11df9"
SOURCE_PATH = "pictographic-primitives/romance/love gift box heart_15e4830e-dce1-452c-9f05-87646ea11df9.svg"
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('gift box', 'two bow loops and knot', 'heart')
REPAIR_PLAN = {'concept': 'heart gift box', 'core_parts': ('gift box', 'two bow loops and knot', 'heart'), 'flexible_parts': 'Only minor curves and spacing may be simplified for 32px clearance', 'ladder': 'Rebalance and redraw on the strict SUB32 canvas'}



class DrawingVariant2(Sub32):
    icon_id = "heart-gift-box-v2"
    variant_of = "heart-gift-box"
    variant_label = "Strict 32x32 repair draft"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/symbol"
    aliases = ("love-gift",)
    keywords = ("heart", "gift", "box", "present", "romance")

    def build(self):
        rounded_rect(self, "box", 2, 10, 30, 30, 3)
        self.add_bezier("bow-left", (16, 10), ((10, 10), (8, 8), (8, 5)), ((8, 2), (11, 2), (16, 10)))
        self.add_bezier("bow-right", (16, 10), ((21, 2), (24, 2), (24, 5)), ((24, 8), (22, 10), (16, 10)))
        self.add_contour("bow", "bow-left", "bow-right", closed=True)
        self.relate("connect", "box", "bow")
        self.add_bezier("heart", (16, 23), ((12, 20), (12, 17), (14, 16)), ((15, 16), (16, 18), (16, 18)), ((16, 18), (17, 16), (18, 16)), ((20, 17), (20, 20), (16, 23)))
        self.add_contour("heart-shape", "heart", closed=True)
