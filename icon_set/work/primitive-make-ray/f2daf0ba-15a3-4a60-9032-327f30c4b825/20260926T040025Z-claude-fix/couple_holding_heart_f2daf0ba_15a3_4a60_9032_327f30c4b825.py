"""Two people holding a heart between them.

Human construction: icon_set/references/human_ref/user.svg (circular heads, smooth rounded
shoulders, open bottom) and full_body_ref.png. Shared parameters: head radius 5, head
centres (11,11) and (37,11), shoulder crests (11,24) and (37,24), so each detached head
sits exactly 8 above its own shoulder crest on centerlines (4 visible): 11 + 5 + 8 = 24;
the crest is each body's nearest point to its head.
Mirrored about x=24. Each body is an outer shoulder curving from the crest down the side
to the bottom edge, and an arm running inward from the crest to the heart's side point
H. The heart spans the two arms: two lobes (cubic bumps, tops at y=24) meet at a notch
(24,27), and two straight sides fall from H=(14,29) to the tip (24,40), as in the reference where
the arms flow into the heart's lobes.
Lucide construction: 'heart' - two round lobes and straight sides to a point; 'users' -
circular heads over rounded shoulders.
Keyshape SQUARE: centerline x 6..42 (body sides), y 6..42 (head tops, body sides).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f2daf0ba-15a3-4a60-9032-327f30c4b825"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__couple-holding-heart/20260926T035939Z-thuan-mac/reference/two persons with heart_f2daf0ba-15a3-4a60-9032-327f30c4b825.svg"
AUTHOR = "claude-opus-5-5"


class CoupleHoldingHeart(Solo48):
    icon_id = "couple-holding-heart"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/relationships"
    aliases = ("two-persons-with-heart", "couple-heart", "love-couple")
    keywords = ("couple", "love", "heart", "people", "relationship", "partners", "romance", "care", "together")

    def build(self) -> None:
        for side, f in (("left", lambda p: p), ("right", lambda p: (48 - p[0], p[1]))):
            hx = f((11, 0))[0]
            self.add_arc(f"{side}-head-top", (hx - 5, 11), (hx + 5, 11), radius_x=5, sweep=True)
            self.add_arc(f"{side}-head-bottom", (hx + 5, 11), (hx - 5, 11), radius_x=5, sweep=True)
            self.add_contour(f"{side}-head", f"{side}-head-top", f"{side}-head-bottom", closed=True)
            crest, H = f((11, 24)), f((14, 29))
            self.add_bezier(f"{side}-shoulder", crest, (f((8, 24)), f((6, 26)), f((6, 29))),
                            (f((6, 33)), f((6, 38)), f((6, 42))))
            self.add_bezier(f"{side}-arm", crest, (f((12.5, 24)), f((12.5, 27.5)), H))
            self.add_line(f"heart-side-{side}", H, (24, 40))
            self.relate("connect", f"{side}-shoulder", f"{side}-arm")
            self.relate("connect", f"{side}-arm", f"heart-lobe-{side}")
            self.relate("connect", f"{side}-arm", f"heart-side-{side}")
            self.relate("connect", f"heart-lobe-{side}", f"heart-side-{side}")
            self.mark_human_figure(side, head=f"{side}-head", torso=f"{side}-shoulder", torso_junction="start")
        self.add_bezier("heart-lobe-left", (14, 29), ((15, 27), (16.5, 24), (19, 24)),
                        ((21.5, 24), (24, 25), (24, 27)))
        self.add_bezier("heart-lobe-right", (24, 27), ((24, 25), (26.5, 24), (29, 24)),
                        ((31.5, 24), (33, 27), (34, 29)))
        self.relate("connect", "heart-lobe-left", "heart-lobe-right")
        self.relate("connect", "heart-side-left", "heart-side-right")
