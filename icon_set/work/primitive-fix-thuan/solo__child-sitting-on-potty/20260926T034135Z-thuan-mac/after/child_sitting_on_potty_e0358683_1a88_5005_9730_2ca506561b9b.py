"""A child sitting on a potty: a small figure seated on a potty chair with a tall backrest.

Symbol plan: the potty (left) is one closed outline - a backrest 8 wide with a round r4
top, a flat seat, a front wall and a flat base 8 below the seat. The child follows the
shared full-body reference with a child's large head: ring head (r5) straight above the
neck, exactly 8 on centerlines (4 units of ink); a straight torso leaning back from the
neck to the hip (the neck is its point nearest the head), which sits on the seat's front corner (shared endpoint); a thigh
rising forward to the raised knee, a shin straight down to the floor, and one arm from the neck resting its hand
on the knee (shared endpoint). The reference's arch cutout in the potty base is dropped:
the base must stay 8 below the seat, which leaves no height for an arch.
Lucide construction: none; figure from icon_set/references/human_ref/full_body_ref.png
(seated pose).
Keyshape SQUARE: centerline x 6..42 (potty back, foot), y 6..42 (head top, base / foot).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e0358683-1a88-5005-9730-2ca506561b9b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__child-sitting-on-potty/20260926T034135Z-thuan-mac/reference/urinal baby sit_e0358683-1a88-5005-9730-2ca506561b9b.svg"
AUTHOR = "claude-opus-5-5"


class ChildSittingOnPotty(Solo48):
    icon_id = "child-sitting-on-potty"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/family"
    aliases = ("baby potty", "potty training", "urinal baby sit")
    keywords = ("child", "baby", "toddler", "potty", "toilet", "potty training", "bathroom", "family")

    def build(self) -> None:
        # potty
        back, rest_front, rest_top, seat, front, base = 6, 14, 24, 34, 26, 42
        rr = (rest_front - back) // 2
        self.add_line("back-wall", (back, base), (back, rest_top))
        self.add_arc("rest-top", (back, rest_top), (rest_front, rest_top), radius_x=rr)
        self.add_line("rest-front", (rest_front, rest_top), (rest_front, seat))
        self.add_line("seat", (rest_front, seat), (front, seat))
        self.add_line("front-wall", (front, seat), (front, base))
        self.add_line("base", (front, base), (back, base))
        self.add_contour("potty", "back-wall", "rest-top", "rest-front", "seat", "front-wall", "base",
                         closed=True)
        # child
        hx, hy, hr = 30, 11, 5
        neck = (hx, hy + hr + 8)
        hip = (front, seat)
        knee = (42, 28)
        pts = [(hx - hr, hy), (hx, hy - hr), (hx + hr, hy), (hx, hy + hr)]
        names = ("head-nw", "head-ne", "head-se", "head-sw")
        for i, name in enumerate(names):
            self.add_arc(name, pts[i], pts[(i + 1) % 4], radius_x=hr)
        self.add_contour("head", *names, closed=True)
        self.add_line("torso", neck, hip)
        self.add_line("thigh", hip, knee)
        self.add_line("shin", knee, (42, 42))
        self.add_line("arm", neck, knee)
        self.add_contour("body", "torso", "thigh", "shin")
        self.mark_human_figure("child", head="head", torso="torso", torso_junction="start")
        self.relate("connect", "body", "arm")
        self.relate("connect", "body", "potty")
