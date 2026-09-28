"""Chess rook: a tall tower piece with a notched crown, tapered body and rounded base.

Revision of the disapproved drawing, a squat wide block that read as a toaster. Plan
(VRECT_L, centerline (8,4)-(40,44)) mirrored about x=24: crown block (8,4)-(40,20)
with one 8-wide, 8-deep notch (merlons 12 wide, so every parallel pair keeps 8);
crown seam at y=20; body sides tapering from x=14/34 down to 12/36 at the base seam
y=34; base with r4 rounded shoulders to the full width and a flat bottom at 44.
The reference's three merlons become two: three outlined merlons need 40 units on
this profile. Lucide `castle` informs the notched crown.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6827ce25-bda1-54bb-bc4b-11e435eb0b3f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__chess-rook-wide-battlements/20260927T150749Z-thuan-mac-1/reference/chess rook_6827ce25-bda1-54bb-bc4b-11e435eb0b3f.svg"
AUTHOR = "claude-fable-5-1"


class ChessRookWideBattlements(Solo48):
    icon_id = "chess-rook-wide-battlements"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    aliases = ("rook", "castle piece")
    keywords = ("chess", "rook", "castle", "tower", "piece", "game")

    def build(self) -> None:
        self.add_polyline("crown", (14, 20), (8, 20), (8, 4), (20, 4), (20, 12), (28, 12), (28, 4), (40, 4), (40, 20), (34, 20))
        self.add_line("body-right", (34, 20), (36, 34))
        self.add_arc("base-tr", (36, 34), (40, 38), radius_x=4)
        self.add_polyline("base", (40, 38), (40, 44), (8, 44), (8, 38))
        self.add_arc("base-tl", (8, 38), (12, 34), radius_x=4)
        self.add_line("body-left", (12, 34), (14, 20))
        self.add_contour("piece", *(f"crown-{i}" for i in range(1, 10)), "body-right", "base-tr",
                         "base-1", "base-2", "base-3", "base-tl", "body-left", closed=True)
        self.contours[:] = [c for c in self.contours if c.contour_id not in ("crown", "base")]
        self.add_line("crown-seam", (14, 20), (34, 20))
        self.add_line("base-seam", (12, 34), (36, 34))
        self.relate("connect", "piece", "crown-seam")
        self.relate("connect", "piece", "base-seam")
