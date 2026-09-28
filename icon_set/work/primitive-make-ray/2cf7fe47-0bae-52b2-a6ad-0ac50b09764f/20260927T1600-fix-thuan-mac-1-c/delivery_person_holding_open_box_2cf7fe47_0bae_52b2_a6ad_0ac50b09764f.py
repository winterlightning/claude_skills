"""Delivery person holding an open box: a courier in side view carrying a box with its lid up.

Revision of the disapproved drawing, whose bent arm and floating flap were unreadable.
Plan (SQUARE, centerline (6,6)-(42,42)): head r5 at (11,11) from cardinal quarter arcs
(the reference cap brim is dropped: a tangent line off a r5 ring read as a
sigma at 48); straight torso from (11,24) (exactly 8 below the head,
4 visible) to (11,42); one arm from (11,28) to the box wall node (26,32); box
(26,26)-(42,38) with one raised lid line from (42,26) to (34,16). Human reference:
icon_set/references/human_ref/full_body_ref.png (reaching pose); Lucide
`package-open` informs the lid. Side view is deliberate asymmetry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2cf7fe47-0bae-52b2-a6ad-0ac50b09764f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__delivery-person-holding-open-box/20260927T150749Z-thuan-mac-1/reference/folding pocket knife_2cf7fe47-0bae-52b2-a6ad-0ac50b09764f.svg"
AUTHOR = "claude-fable-5-1"


class DeliveryPersonHoldingOpenBox(Solo48):
    icon_id = "delivery-person-holding-open-box"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "construction"
    aliases = ("courier with open box", "delivery worker")
    keywords = ("delivery", "person", "courier", "box", "open", "parcel", "package")

    def build(self) -> None:
        x, y, r = 11, 11, 5
        pts = [(x - r, y), (x, y - r), (x + r, y), (x, y + r)]
        for j in range(4):
            self.add_arc(f"head-{j}", pts[j], pts[(j + 1) % 4], radius_x=r)
        self.add_contour("head", "head-0", "head-1", "head-2", "head-3", closed=True)
        self.add_line("torso", (11, 24), (11, 28))
        self.add_line("body", (11, 28), (11, 42))
        self.add_line("arm", (11, 28), (26, 32))
        self.relate("connect", "torso", "body")
        self.relate("connect", "torso", "arm")
        self.relate("connect", "body", "arm")
        self.mark_human_figure("courier", head="head", torso="torso", torso_junction="start")
        self.add_polyline("box", (26, 26), (42, 26), (42, 38), (26, 38), (26, 32), closed=True)
        self.relate("connect", "box", "arm")
        self.add_line("lid", (42, 26), (34, 16))
        self.relate("connect", "lid", "box")
