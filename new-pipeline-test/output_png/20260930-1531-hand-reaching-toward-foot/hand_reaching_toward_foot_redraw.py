"""hand-reaching-toward-foot (redraw of the new-pipeline traced SVG).

Plan: stick figure bent forward, reaching down toward its front foot, on
HRECT_L (centerline box (4,8)-(44,40)). The subject is wider than tall
(trace aspect 1.15); SQUARE would need a 1.15 vertical stretch, HRECT_L fits
both axes without distortion.
- head: 4-cardinal-arc circle r5 about (39,13): right extreme x=44, top y=8.
- torso: lower torso slopes 7:2 from the hip (10,9) down to the shoulder
  (24,13), then a short level neck run (24,13)->(26,13); the head sits level
  beside the neck, exactly 8 centerline units from the head outline
  (4-unit ink gap, human-reference.md) on the torso's direction.
- arm: one straight line branching from the shoulder vertex (not the neck, so
  it never approaches the head) steeper than the front leg, down to a rounded
  hand at (31,31), 9 above the front toe.
- legs: one polyline, back toe -> back heel (4,40) -> hip -> front heel
  (26,40) -> front toe (32,40); the legs splay 38 degrees at the hip.
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs). No useful Lucide match (Lucide has no
bending figure); construction follows Lucide's person-standing strokes.

Metric issues:
- clearance e0/e1 (head vs torso/arm, 4.58): fixed; the head is 8 from the
  neck and 9 from the arm on centerlines.
- clearance e1/e2 (legs vs torso/arm, 7.49): fixed; the legs splay wider and
  the shoulder sits 10.6, the hand 8.6 from the front leg.
- hole (head 3.54 wide): fixed; r5 ring leaves a 6-wide hole.
- no-head: fixed; the head is a true circle flagged with mark_human_figure.
- keyshape-short-axis (SQUARE 87% on y): fixed by choosing HRECT_L, every
  extreme lands exactly on its box.
- stroke-width (trace 2.4): redrawn at stroke 4 with all gaps re-measured.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "06de442e-575d-48bb-ae42-82d8ef6c23c5"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1531-hand-reaching-toward-foot/"
    "hand-reaching-toward-foot_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HEAD_C = (39, 13)
HEAD_R = 5
NECK = (26, 13)          # HEAD_C.x - HEAD_R - 8, level with the head centre
SHOULDER = (24, 13)
HIP = (10, 9)
HAND = (31, 31)
BACK_HEEL, BACK_TOE = (4, 40), (10, 40)
FRONT_HEEL, FRONT_TOE = (26, 40), (32, 40)


class HandReachingTowardFootRedraw(Solo48):
    icon_id = "hand-reaching-toward-foot-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/activity"
    aliases = ("toe touch", "forward bend")
    keywords = ("stretch", "toe touch", "bend", "reach", "foot", "exercise", "flexibility")

    def build(self) -> None:
        cx, cy = HEAD_C
        r = HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        self.add_line("back", HIP, SHOULDER)
        self.add_line("torso", SHOULDER, NECK)
        self.relate("connect", "back", "torso")
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="end")

        self.add_line("arm", SHOULDER, HAND)
        self.relate("connect", "arm", "back")
        self.relate("connect", "arm", "torso")

        self.add_polyline("legs", BACK_TOE, BACK_HEEL, HIP, FRONT_HEEL, FRONT_TOE)
        self.relate("connect", "legs", "back")
