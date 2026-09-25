"""Pin add: a map pin with a plus sign at its lower right - add a location.

Symbol plan: the pin is one closed outline - a radius-10 half-circle
head about (16,16) and two mirrored convex cubic flanks leaving its widest
points vertically and meeting in a pointed tip at (16,42). The plus is four
arms of length 6 sharing its
centre node, 8+ from the pin. The reference's ring around the plus is
omitted: a ring needs radius 11+ to hold a readable plus 8 inside it, and
at that size it would collide with the pin.
Keyshape SQUARE, centerline box (6,6)-(42,42).
Lucide construction: map-pin-plus (pin head and flanks into a tip, plus
beside it).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "edc387fb-8345-489a-a276-38ea07c6e827"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__pin-add/20260925T092530Z-thuan-mac/reference/pin add_edc387fb-8345-489a-a276-38ea07c6e827.svg"
AUTHOR = "claude-opus-5-5"


class PinAdd(Solo48):
    icon_id = "pin-add"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "maps"
    aliases = ("add location", "map pin plus", "new place")
    keywords = ("pin", "add", "location", "map", "plus", "marker")

    def build(self) -> None:
        cx, cy, r = 16, 16, 10
        tip = (cx, 42)
        self.add_arc("pin-1", (cx - r, cy), (cx, cy - r), radius_x=r)
        self.add_arc("pin-2", (cx, cy - r), (cx + r, cy), radius_x=r)
        # Convex flanks leave the head's widest points vertically and meet
        # at the tip at about 53 degrees.
        self.add_bezier("pin-3", (cx + r, cy), ((cx + r, 26), (cx + 4, 34), tip))
        self.add_bezier("pin-4", tip, ((cx - 4, 34), (cx - r, 26), (cx - r, cy)))
        self.add_contour("pin", *[f"pin-{i}" for i in range(1, 5)], closed=True)
        px, py, arm = 36, 36, 6
        for name, end in (("plus-left", (px - arm, py)), ("plus-right", (px + arm, py)),
                          ("plus-up", (px, py - arm)), ("plus-down", (px, py + arm))):
            self.add_line(name, (px, py), end)
        self.relate("connect", "plus-left", "plus-right", "plus-up", "plus-down")
