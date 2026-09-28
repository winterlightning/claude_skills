"""Japanese bento / ekiben lunch box.

Symbol plan: square-cornered box (x 6..42, rim y=11, floor y=42) split by a
vertical divider at x=22 and a right-hand shelf at y=26. The top-right
compartment is heaped with food: two r5 scallops (tops at y=6) replace the
rim there, as the reference's rolls rise above the box. Rice in the left
compartment and a round item in the bottom-right are dots, each 8 from its
standalone walls.
Revision: the rejected drawing was an empty rounded box with two dots that
did not read as food; the reference's identifying feature is food spilling
above the top-right compartment.
Omitted: the separate balls overlapping the bottom-right divider (no 8-unit
clearance), reduced to one item.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ba617c30-affd-453a-9840-5a1b6cb3e0ff"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__japanese-bento-meal/20260927T153253Z-thuan-mac-1/reference/japanese launchbox bento ekiben_ba617c30-affd-453a-9840-5a1b6cb3e0ff.svg"
AUTHOR = "claude-opus-5-5"


class JapaneseBentoMeal(Solo48):
    icon_id = "japanese-bento-meal"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ("bento", "ekiben", "lunch box")
    keywords = ("bento", "ekiben", "japanese", "lunch", "box", "meal", "food")

    def build(self) -> None:
        L, R, T, B, D, M = 6, 42, 11, 42, 22, 26
        self.add_arc("food-1", (D, T), (32, T), radius_x=5, sweep=True)
        self.add_arc("food-2", (32, T), (R, T), radius_x=5, sweep=True)
        self.add_contour("food", "food-1", "food-2")
        walls = {
            "rim": ((L, T), (D, T)),
            "left": ((L, T), (L, B)),
            "floor-left": ((L, B), (D, B)),
            "floor-right": ((D, B), (R, B)),
            "right-top": ((R, T), (R, M)),
            "right-bottom": ((R, M), (R, B)),
            "divider-top": ((D, T), (D, M)),
            "divider-bottom": ((D, M), (D, B)),
            "shelf": ((D, M), (R, M)),
        }
        for name, (p, q) in walls.items():
            self.add_line(name, p, q)
        joins = (("food", "rim"), ("food", "divider-top"), ("food", "right-top"),
                 ("rim", "left"), ("rim", "divider-top"), ("left", "floor-left"),
                 ("floor-left", "floor-right"), ("floor-left", "divider-bottom"),
                 ("floor-right", "divider-bottom"), ("floor-right", "right-bottom"),
                 ("right-top", "right-bottom"), ("right-top", "shelf"), ("right-bottom", "shelf"),
                 ("divider-top", "divider-bottom"), ("divider-top", "shelf"),
                 ("divider-bottom", "shelf"))
        for a, b in joins:
            self.relate("connect", a, b)
        self.add_dot("rice", (14, 26))
        self.add_dot("side-dish", (32, 34))
