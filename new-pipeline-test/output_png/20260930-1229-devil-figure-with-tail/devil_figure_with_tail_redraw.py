"""devil-figure-with-tail (redraw of the new-pipeline traced SVG).

Plan: front-facing stick figure on the axis x=FX with a ring head carrying two
curved horns, an inverted-V arm stroke from the neck, an inverted-V leg stroke
from the hip, and one tail that leaves the hip to the right, dips, and rises
into an open arrowhead. VRECT_L, centerline box (8,4)-(40,44).
- head: 4-cardinal-arc circle r5 about (FX,11) (6-unit hole), so the exact
  8-unit head gap to the standalone vertical torso certifies.
- horns: mirrored cubics from the 3-4-5 points (FX-+4, 8) of the ring, bowing
  outward and turning up to tips at (FX-+7, 4); tip y=4 is the keyshape top and
  the left tip is the x=8 extreme.
- neck (FX,24) = head bottom 16 + 8 (4-unit ink gap, human-reference.md);
  torso to the hip (FX,36).
- arms: one polyline hand-neck-hand, hands at (FX-+7, 27); the left hand is
  the x=8 extreme.
- legs: one polyline foot-hip-foot, feet at (FX-+6, 44) on the bottom edge.
- tail: one cubic that leaves the hip level (>= 60 degrees off the right leg,
  so the two stay 8 apart beyond the joint), passes 8+ under the right hand,
  dips and curls up at 1:3 into the tip (38,27); arrowhead = one polyline
  (34,29)-(38,27)-(40,31) symmetric about the tail's end tangent, its right
  barb end is the x=40 extreme.

Metric issues (devil-figure-with-tail_metrics.json):
- stroke-width (trace 2.67 after fit): fixed, stroke 4 throughout, all gaps
  budgeted at 8 on centerlines.
- keyshape-short-axis (VRECT_M x fill 86%): changed to VRECT_L. At stroke 4 the
  right hand, the tail and the right leg need 8 between each other, and a
  sweep over VRECT_M's 28-unit width found no hand/tail/leg layout at 8; on
  VRECT_L's 32 units it fits. All four extremes
  sit exactly on the box.
- clearance e0/e5, e0/e9 (head touching shoulders, 2.6): fixed, exact 8-unit
  centerline head gap (4 ink).
- clearance e2/e3 (horn parts 6.63): fixed, horns are single strokes whose
  nearest points (the bases) are 8 apart.
- clearance e4/e5, e4/e9, e5/e6, e5/e7, e5/e8, e5/e9, e8/e9 (arms, legs, tail
  and arrowhead crowding): fixed, every non-joined pair is >= 8 apart and
  joined pairs are >= 8 apart beyond 8 units of their joint.
- loose-join e1/e3 (horn crescent open by 0.79): fixed, the filled crescent
  horns became single strokes that end on the head ring and are declared
  `connect`.
- narrow-join e6/e8, e7/e8 (tail fused into barbs): fixed, barbs sit at 45
  degrees either side of the tail's end tangent.
- human head gap (-4 ink): fixed, 4 ink.
- stroke-count (10 vs 6): reduced to 8 strokes (head, 2 horns, torso, arms,
  legs, tail, arrowhead); not 6 because the torso must stay a standalone line
  for the head gap to certify and each horn is its own stroke.
Reference: icon_set/references/human_ref/full_body_ref.png (ring head, single
stroke limbs from neck and hip). No useful Lucide match for a devil figure.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "08403821-8001-5c1f-9788-1e4dc890984f"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1229-devil-figure-with-tail/"
    "devil-figure-with-tail_raw.svg"
)
AUTHOR = "claude-opus-5-5"

FX = 15                      # figure axis
HEAD_C, HEAD_R = (FX, 11), 5
NECK = (FX, 24)              # head bottom 16 + 8
HIP = (FX, 36)
HAND_DX, HAND_Y = 7, 27
FOOT_DX, FOOT_Y = 6, 44
HORN_BASE = (4, -3)          # 3-4-5 point of the r5 ring, mirrored
TIP = (38, 27)
TAIL_C1, TAIL_C2 = (32, 33), (34, 39)   # C2 = TIP - 4*(1,-3): end tangent 1:3
BARBS = ((34, 29), (40, 31))            # TIP + (-4,2) / (2,4): +-45 deg off the tangent


class DevilFigureWithTailRedraw(Solo48):
    icon_id = "devil-figure-with-tail-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ("devil", "demon", "imp")
    keywords = ("devil", "demon", "horns", "tail", "halloween", "evil", "stick figure")

    def build(self) -> None:
        cx, cy = HEAD_C
        r = HEAD_R
        ring = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
        for i, p in enumerate(ring):
            self.add_arc(f"head-{i + 1}", p, ring[(i + 1) % 4], radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        bx, by = HORN_BASE
        for side, s in (("l", -1), ("r", 1)):
            self.add_bezier(
                f"horn-{side}", (cx + s * bx, cy + by),
                ((cx + s * 6, cy - 5), (cx + s * 7, cy - 6), (cx + s * 7, 4)),
            )
            self.relate("connect", f"horn-{side}", "head")

        self.add_line("torso", NECK, HIP)
        self.mark_human_figure("devil", head="head", torso="torso", torso_junction="start")

        self.add_polyline("arms", (FX - HAND_DX, HAND_Y), NECK, (FX + HAND_DX, HAND_Y))
        self.add_polyline("legs", (FX - FOOT_DX, FOOT_Y), HIP, (FX + FOOT_DX, FOOT_Y))
        self.relate("connect", "arms", "torso")
        self.relate("connect", "legs", "torso")

        self.add_bezier("tail", HIP, (TAIL_C1, TAIL_C2, TIP))
        self.add_polyline("arrowhead", BARBS[0], TIP, BARBS[1])
        self.relate("connect", "tail", "torso")
        self.relate("connect", "tail", "legs")
        self.relate("connect", "tail", "arrowhead")
