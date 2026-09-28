"""A child jumping rope: a child in a dress with arms out holding a rope that arcs high over the head.

Symbol plan: symmetric about x=24. The child follows the shared human reference: a ring
head (r4) exactly 8 above the body on centerlines (4 units of ink), a closed trapezoid
dress body from narrow shoulders to a wider hem (the reference's child silhouette), two
straight arms from the shoulders out to the hands, and two splayed legs from the hem.
The rope is one bezier arch (two mirrored cubics, flat at the top y=4) from hand to
hand over the head; its ends are the hands (shared endpoints).
A stick-figure version (torso line, T arms) read as an eye in a dome at 48 and a
rope-under-the-feet version read as a figure in a bowl; both were rejected in review.
Lucide construction: no rope icon; figure per icon_set/references/human_ref/full_body_ref.png
(dress figure) with a child's larger head.
Keyshape VRECT_L: centerline x 8..40 (hands / rope ends), y 4..44 (rope top, feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e35559ad-6d05-4f05-b6ee-d5792132dd83"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__child-jumping-rope/20260926T034135Z-thuan-mac/reference/family child jumping rope_e35559ad-6d05-4f05-b6ee-d5792132dd83.svg"
AUTHOR = "claude-opus-5-5"


class ChildJumpingRope(Solo48):
    icon_id = "child-jumping-rope"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/activity"
    aliases = ("jump rope", "skipping rope", "child skipping")
    keywords = ("child", "kid", "jump rope", "skipping", "play", "exercise", "family", "fitness")

    def build(self) -> None:
        ax = 24
        head_cy, head_r = 17, 4
        neck = head_cy + head_r + 8
        sh, hem_y, hem = 4, 38, 8  # shoulder half-width, hem y, hem half-width
        hand_l, hand_r = (8, neck + 3), (40, neck + 3)
        # head
        pts = [(ax - head_r, head_cy), (ax, head_cy - head_r), (ax + head_r, head_cy), (ax, head_cy + head_r)]
        names = ("head-nw", "head-ne", "head-se", "head-sw")
        for i, name in enumerate(names):
            self.add_arc(name, pts[i], pts[(i + 1) % 4], radius_x=head_r)
        self.add_contour("head", *names, closed=True)
        # dress body
        self.add_line("shoulders", (ax - sh, neck), (ax + sh, neck))
        self.add_line("side-r", (ax + sh, neck), (ax + hem, hem_y))
        self.add_line("hem-r", (ax + hem, hem_y), (ax + 3, hem_y))
        self.add_line("hem-m", (ax + 3, hem_y), (ax - 3, hem_y))
        self.add_line("hem-l", (ax - 3, hem_y), (ax - hem, hem_y))
        self.add_line("side-l", (ax - hem, hem_y), (ax - sh, neck))
        self.add_contour("dress", "shoulders", "side-r", "hem-r", "hem-m", "hem-l", "side-l", closed=True)
        self.mark_human_figure("child", head="head", torso="shoulders", torso_junction="start")
        # arms and legs
        self.add_line("arm-l", (ax - sh, neck), hand_l)
        self.add_line("arm-r", (ax + sh, neck), hand_r)
        self.add_line("leg-l", (ax - 3, hem_y), (ax - 5, 44))
        self.add_line("leg-r", (ax + 3, hem_y), (ax + 5, 44))
        for part in ("arm-l", "arm-r", "leg-l", "leg-r"):
            self.relate("connect", "dress", part)
        # rope over the head, hand to hand
        self.add_bezier("rope", hand_l, ((8, 20), (12, 4), (ax, 4)), ((36, 4), (40, 20), hand_r))
        self.relate("connect", "rope", "arm-l")
        self.relate("connect", "rope", "arm-r")
