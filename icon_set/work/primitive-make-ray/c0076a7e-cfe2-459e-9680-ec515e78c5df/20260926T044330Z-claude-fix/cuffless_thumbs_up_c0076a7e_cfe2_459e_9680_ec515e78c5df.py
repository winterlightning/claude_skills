"""A thumbs-up without a cuff: a plain fist outline with the thumb raised.

Symbol plan: one closed outline: a rounded fist (r4 corners on the left), a thumb rising
from the top with a diagonal back edge, an r4 rounded tip and a short front edge that
curves into the fist's top, then three finger bumps (r4 half circles, series step 8) down
the right side to the flat bottom.
No knuckle lines (the reference shows the plain fist outline).
Lucide construction: 'thumbs-up' - fist with a raised thumb.
Keyshape SQUARE: centerline x 6..42 (fist back, finger bumps), y 6..42 (thumb tip, fist bottom).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c0076a7e-cfe2-459e-9680-ec515e78c5df"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__cuffless-thumbs-up/20260926T044250Z-thuan-mac/reference/like_c0076a7e-cfe2-459e-9680-ec515e78c5df.svg"
AUTHOR = "claude-opus-5-5"


class CufflessThumbsUp(Solo48):
    icon_id = "cuffless-thumbs-up"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/gesture"
    aliases = ("like", "thumbs up", "approve")
    keywords = ("thumbs up", "like", "approve", "good", "ok", "yes", "hand", "gesture", "agree")

    def build(self) -> None:
        r = 4
        members = []

        def line(n, a, b):
            self.add_line(n, a, b)
            members.append(n)

        def arc(n, a, b, **kw):
            self.add_arc(n, a, b, radius_x=r, **kw)
            members.append(n)

        arc("corner-tl", (6, 24), (10, 20))
        line("top-left", (10, 20), (12, 20))
        line("thumb-back", (12, 20), (20, 10))
        arc("thumb-tip", (20, 10), (28, 10))
        line("thumb-front", (28, 10), (28, 14))
        self.add_bezier("thumb-crease", (28, 14), ((28, 17), (29, 18), (31, 18)))
        members.append("thumb-crease")
        line("top-right", (31, 18), (38, 18))
        for i, y in enumerate((18, 26, 34)):
            arc(f"finger-{i}", (38, y), (38, y + 8))
        line("bottom", (38, 42), (10, 42))
        arc("corner-bl", (10, 42), (6, 38))
        line("back", (6, 38), (6, 24))
        self.add_contour("hand", *members, closed=True)
