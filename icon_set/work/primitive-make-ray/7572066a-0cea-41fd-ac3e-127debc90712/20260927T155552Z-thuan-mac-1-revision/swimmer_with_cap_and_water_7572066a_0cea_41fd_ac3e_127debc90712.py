"""Capped swimmer with visible shoulders and waterline."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7572066a-0cea-41fd-ac3e-127debc90712"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__swimmer-with-cap-and-water/20260927T155415Z-thuan-mac-1/reference/swim compete_7572066a-0cea-41fd-ac3e-127debc90712.svg"
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = "swimmer-with-cap-and-water"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "state"
    aliases = ("swim-compete",)
    keywords = ("swimmer", "cap", "water", "swimming")

    def build(self):
        # Three stacked reference elements: round capped head, shoulders, wave.
        self.add_arc("head-top", (16, 14), (32, 14), radius_x=8)
        self.add_arc("head-bottom", (32, 14), (16, 14), radius_x=8)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        self.add_line("cap-seam", (16, 14), (32, 14))
        self.relate("connect", "head", "cap-seam")
        self.add_bezier("shoulders", (12, 31), ((14, 30), (34, 30), (36, 31)))
        self.add_bezier("water-left", (6, 42), ((12, 39), (12, 39), (18, 42)))
        self.add_bezier("water-middle", (18, 42), ((24, 39), (24, 39), (30, 42)))
        self.add_bezier("water-right", (30, 42), ((36, 39), (36, 39), (42, 42)))
        self.add_contour("water", "water-left", "water-middle", "water-right")
        self.human_construction = "bust"
