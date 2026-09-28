"""A couple: two head-and-shoulder busts side by side.

Human construction: icon_set/references/human_ref/user.svg (circular outlined head,
broad smooth shoulders, open bottom). Shared parameters for both people: head radius 6,
head centre y=16, shoulder crest y=30, so the detached head sits exactly 8 above its
shoulders on centerlines (4 visible): 16 + 6 + 8 = 30, and the crest point directly
under the head is the nearest body point. Shoulders are broad, shallow cubic runs (16 wide,
8 tall) from the base corners up to the crest with a horizontal tangent there. Busts are mirrored copies
centred at x=12 and x=36, 8 apart at the base.
Lucide construction: 'users' - equal circular heads over rounded shoulder arcs.
Keyshape HRECT_M: centerline x 4..44 (shoulder feet), y 10..38 (head tops, shoulder feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a76c7c2d-a4c9-4c4a-8eec-dac04079bf30"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__couple-busts/20260926T035939Z-thuan-mac/reference/couple_a76c7c2d-a4c9-4c4a-8eec-dac04079bf30.svg"
AUTHOR = "claude-opus-5-5"

HEAD_R, HEAD_Y, CREST_Y, BASE_Y, HALF = 6, 16, 30, 38, 8


class CoupleBusts(Solo48):
    icon_id = "couple-busts"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/groups"
    aliases = ("couple", "two-people", "pair")
    keywords = ("couple", "people", "users", "pair", "partners", "friends", "relationship", "avatar")

    def build(self) -> None:
        for name, cx in (("left", 12), ("right", 36)):
            self.add_arc(f"{name}-head-top", (cx - HEAD_R, HEAD_Y), (cx + HEAD_R, HEAD_Y), radius_x=HEAD_R, sweep=True)
            self.add_arc(f"{name}-head-bottom", (cx + HEAD_R, HEAD_Y), (cx - HEAD_R, HEAD_Y), radius_x=HEAD_R, sweep=True)
            self.add_contour(f"{name}-head", f"{name}-head-top", f"{name}-head-bottom", closed=True)
            self.add_bezier(f"{name}-shoulders", (cx - HALF, BASE_Y),
                            ((cx - HALF, 33.5), (cx - 5, CREST_Y), (cx, CREST_Y)),
                            ((cx + 5, CREST_Y), (cx + HALF, 33.5), (cx + HALF, BASE_Y)))
            self.mark_human_figure(name, head=f"{name}-head", torso=f"{name}-shoulders", torso_junction="start")
