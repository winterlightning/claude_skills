"""Tall rounded card containing a left-facing crescent moon."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import rounded_rect

SOURCE_ICON_ID = "23e48a73-6f3a-4649-8e2c-1ae7c754ab02"
SOURCE_PATH = "pictographic-primitives/other/card moon_23e48a73-6f3a-4649-8e2c-1ae7c754ab02.svg"
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('open-bottom card with rounded top', 'left-facing crescent')
REPAIR_PLAN = {'concept': 'Crescent Moon Card', 'core_parts': ('open-bottom card with rounded top', 'left-facing crescent'), 'flexible_parts': 'card and moon curve proportions', 'ladder': 'Opened the card bottom and widened the crescent'}



class DrawingVariant2(Sub32):
    icon_id = "crescent-moon-card-v2"
    variant_label = 'Opened the card bottom and widened the crescent'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/symbol"
    aliases = ("moon-card",)
    keywords = ("crescent", "moon", "card", "night")

    def build(self):
        self.add_arc("top-left", (4, 7), (9, 2), radius_x=5)
        self.add_line("top", (9, 2), (23, 2))
        self.add_arc("top-right", (23, 2), (28, 7), radius_x=5)
        self.add_line("right", (28, 7), (28, 30))
        self.add_contour("card", "top-left", "top", "top-right", "right")
        self.add_line("left", (4, 7), (4, 30))
        self.relate("connect", "card", "left")
        self.add_bezier("moon", (21, 9), ((7, 9), (7, 23), (21, 23)), ((16, 21), (16, 11), (21, 9)))
        self.add_contour("crescent", "moon", closed=True)
