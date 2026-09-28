"""Fork and spoon side by side (restaurant).

Symbol plan: fork = U-shaped bowl (two quarter arcs r8 on a shared centre)
with three tines at 8-unit pitch; the middle tine and handle form one axis
x=14 meeting the U at its bottom node. Spoon = oval bowl (rx6, ry8) on axis
x=36 with a straight handle. Both bowls end at y=22, both handles at y=42.
Revision: the rejected drawing squared off the fork bowl and shortened the
middle tine; the reference has a rounded U and a full-height middle tine.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b9ee892d-5b94-4998-8475-ee9a5cbfd67b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__fork-and-spoon-batch-011-07/20260927T153253Z-thuan-mac-1/reference/restaurant fork spoon_b9ee892d-5b94-4998-8475-ee9a5cbfd67b.svg"
AUTHOR = "claude-opus-5-5"


class ForkAndSpoon(Solo48):
    icon_id = "fork-and-spoon-batch-011-07"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ("restaurant", "cutlery")
    keywords = ("fork", "spoon", "cutlery", "utensils", "meal", "dining", "restaurant")

    def build(self) -> None:
        fx, top, bowl, bottom, r = 14, 6, 22, 42, 8
        self.add_line("fork-left-tine", (fx - r, top), (fx - r, bowl - r))
        self.add_arc("fork-left-arc", (fx - r, bowl - r), (fx, bowl), radius_x=r, sweep=False)
        self.add_contour("fork-left", "fork-left-tine", "fork-left-arc")
        self.add_arc("fork-right-arc", (fx, bowl), (fx + r, bowl - r), radius_x=r, sweep=False)
        self.add_line("fork-right-tine", (fx + r, bowl - r), (fx + r, top))
        self.add_contour("fork-right", "fork-right-arc", "fork-right-tine")
        self.add_line("fork-middle-tine", (fx, top), (fx, bowl))
        self.add_line("fork-handle", (fx, bowl), (fx, bottom))
        self.relate("connect", "fork-left", "fork-right")
        self.relate("connect", "fork-left", "fork-middle-tine")
        self.relate("connect", "fork-right", "fork-middle-tine")
        self.relate("connect", "fork-middle-tine", "fork-handle")
        self.relate("connect", "fork-left", "fork-handle")
        self.relate("connect", "fork-right", "fork-handle")

        sx, rx, ry = 36, 6, 8
        cy = top + ry
        self.add_arc("spoon-1", (sx, top), (sx + rx, cy), radius_x=rx, radius_y=ry, sweep=True)
        self.add_arc("spoon-2", (sx + rx, cy), (sx, bowl), radius_x=rx, radius_y=ry, sweep=True)
        self.add_arc("spoon-3", (sx, bowl), (sx - rx, cy), radius_x=rx, radius_y=ry, sweep=True)
        self.add_arc("spoon-4", (sx - rx, cy), (sx, top), radius_x=rx, radius_y=ry, sweep=True)
        self.add_contour("spoon", "spoon-1", "spoon-2", "spoon-3", "spoon-4", closed=True)
        self.add_line("spoon-handle", (sx, bowl), (sx, bottom))
        self.relate("connect", "spoon", "spoon-handle")
