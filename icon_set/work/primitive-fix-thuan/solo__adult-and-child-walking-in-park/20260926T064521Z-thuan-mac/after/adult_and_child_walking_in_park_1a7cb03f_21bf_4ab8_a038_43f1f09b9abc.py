"""An adult and a small child walking hand in hand past a pine tree in a park.

Symbol plan (revision per review: taller adult with a centred head; smaller, lower child
with one arm reaching diagonally left and bent legs; a pointed pine instead of the round
tree). Adult: r4 head centred over a vertical torso at x 10 (head (10, 12), neck (10, 24):
outline exactly 8 above the neck), hip (10, 32), legs to (6, 40) and (14, 40), left arm
out to (4, 30), right arm down to the joined hands (18, 28). Child: r3 head (approved
6-diameter circle) at (25, 15), neck (25, 26) exactly 8 below it, hip (25, 33); its one
arm reaches diagonally left to the hands, and both legs bend at the knee: (22, 37) down to
(22, 40) and (30, 36) down to (30, 40), 8 apart. The child's second arm is dropped: next
to the bent legs it cannot keep 8 units in the 7-unit torso. An r2 child head (attempts/v2-*) rendered as a filled dot,
almost as tall as the adult. Tree: a closed triangle, apex
(40, 8), base (35, 22)-(44, 22), with a short trunk to (40, 28).
Human reference: icon_set/references/human_ref/full_body_ref.png (round heads, single
round-ended strokes, 4-unit detached head gaps).
Lucide construction: 'person-standing' joints; 'tree-pine' triangle crown with trunk.
Keyshape HRECT_L: centerline x 4..44 (adult arm, tree base), y 8..40 (adult head, tree
apex, feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1a7cb03f-21bf-4ab8-a038-43f1f09b9abc"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__adult-and-child-walking-in-park/20260926T064521Z-thuan-mac/reference/family walk park_1a7cb03f-21bf-4ab8-a038-43f1f09b9abc.svg"
AUTHOR = "claude-opus-5-5"


class AdultAndChildWalkingInPark(Solo48):
    icon_id = "adult-and-child-walking-in-park"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "wayfinding"
    aliases = ("family walk park", "parent and child walk", "park walk")
    keywords = ("adult", "child", "family", "walking", "park", "tree", "parent", "kid", "outdoors")

    def ring(self, name, cx, cy, r):
        pts = [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]
        names = tuple(f"{name}-{q}" for q in ("w", "n", "e", "s"))
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=r)
        self.add_contour(name, *names, closed=True)

    def build(self) -> None:
        hands = (18, 28)
        # adult
        self.ring("adult-head", 10, 12, 4)
        self.add_line("adult-torso", (10, 24), (10, 32))
        self.add_polyline("adult-legs", (6, 40), (10, 32), (14, 40))
        self.add_line("adult-arm-left", (10, 24), (4, 30))
        self.add_line("adult-arm-right", (10, 24), hands)
        for part in ("adult-legs", "adult-arm-left", "adult-arm-right"):
            self.relate("connect", "adult-torso", part)
        self.relate("connect", "adult-arm-left", "adult-arm-right")
        self.mark_human_figure("adult", head="adult-head", torso="adult-torso", torso_junction="start")
        # child
        self.ring("child-head", 25, 15, 3)
        self.add_line("child-torso", (25, 26), (25, 33))
        self.add_line("child-arm", (25, 26), hands)
        self.add_polyline("child-legs", (22, 40), (22, 37), (25, 33), (30, 36), (30, 40))
        self.relate("connect", "child-torso", "child-legs")
        self.relate("connect", "child-torso", "child-arm")
        self.relate("connect", "adult-arm-right", "child-arm")
        self.mark_human_figure("child", head="child-head", torso="child-torso", torso_junction="start")
        # pine tree
        self.add_polyline("pine", (40, 8), (44, 22), (40, 22), (35, 22), closed=True)
        self.add_line("pine-trunk", (40, 22), (40, 28))
        self.relate("connect", "pine", "pine-trunk")
