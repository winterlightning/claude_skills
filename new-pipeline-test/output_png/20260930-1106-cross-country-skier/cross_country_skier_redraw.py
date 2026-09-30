"""cross-country-skier (redraw of the new-pipeline traced SVG).

Plan: right-facing striding skier on HRECT_L (centerline box (4,8)-(44,40)).
- head: 4-cardinal-arc circle, r4, centre (26,12); its top is the y=8 extreme.
- torso: one cubic from the hip (16,31) to the neck (26,24). It leaves the
  hip on the rear leg's own line, so leg and back read as the classic stride
  diagonal, and arrives vertical under the head. The neck sits exactly 8
  centerline units under the head outline (4-unit ink gap, human-reference.md).
- arm: neck -> elbow (31,30) -> hand (37,27), reaching forward.
- pole: hand -> planted on the front ski at (38,40) (shared node, connect).
- legs: wide straight stride from the hip to the rear boot (8,40) and the
  front boot (26,40).
- skis: two collinear skis on the baseline y=40, 8 apart end to end
  (rear 4..14, front 22..40). The front ski's upturned r4 tip ends at
  (44,36), the x=44 extreme; the rear ski's tail is the x=4 extreme.
References: icon_set/references/human_ref/full_body_ref.png (ring head,
single-stroke round-ended limbs). Lucide has no skier, so no Lucide original
applied beyond round caps/joins and a quarter-arc ski tip.

Metric issues:
- keyshape-short-axis (HRECT_M fills y 94%): changed to HRECT_L. The head
  (8) plus the required 8-unit head gap leave only 12 units of HRECT_M height
  for the torso and legs. On HRECT_L every extreme sits exactly on the box.
- no-head (the trace lost the head ring to a dot, e0): redrawn as a real r4 ring.
- clearance e0/e2 (head 4.93 from the body): the neck is now exactly 8 below
  the head outline, directly under it on a vertical torso tangent.
- clearance e1/e5 (the two skis 2 apart): the skis cannot stack 8 apart
  vertically under a 4-unit head gap in 32 units of height. They are now
  collinear with an 8 gap end to end.
- clearance e1/e2 (the pole tip fused into the ski tip): the pole is planted
  on the front ski at a shared node, 6 behind the tip.
- clearance e2/e5, e3/e5, e4/e5 (the rear leg, front leg and boot crowding
  the rear ski): each leg meets exactly one ski at its boot node. The bent
  rear knee and the separate boot stroke are dropped.
- loose-join e3/e4, e4/e1 and narrow-join e4/e1 (the 10-degree boot sliver):
  the boot stroke is removed. Legs, pole and skis share exact endpoints
  and are declared with relate("connect").
- hole at (23.6,29.1) 5.22 wide: the only enclosed region left, between
  the front leg, torso, arm, pole and front ski, is well over 6 inscribed.
- stroke-width (trace 2.63): redrawn at stroke 4 with 8-unit centerline gaps.
None left unrepaired. validate_icon() valid, build_gate.py PASS (0/0).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4ed29164-79b1-5c31-a787-c6eaf3105619"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1106-cross-country-skier/"
    "cross-country-skier_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HX = 26                 # head / neck axis
HEAD_R = 4
HEAD_CY = 12            # head top at y=8 (HRECT_L top)
NECK = (HX, 24)         # HEAD_CY + HEAD_R + 8
HIP = (16, 31)
ELBOW = (31, 30)
HAND = (37, 27)
GROUND = 40
REAR_SKI = (4, 14)      # x from, x to
FRONT_SKI = (22, 40)    # x from, x where the tip arc starts
TIP_R = 4
REAR_FOOT = (8, GROUND)
FRONT_FOOT = (26, GROUND)
POLE_FOOT = (38, GROUND)


class CrossCountrySkierRedraw(Solo48):
    icon_id = "cross-country-skier-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("nordic skier", "xc skiing", "skier")
    keywords = ("cross country", "skiing", "skier", "nordic", "ski", "pole",
                "winter", "sport", "snow")

    def build(self) -> None:
        cx, cy, r = HX, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        # Hunched back: leaves the hip at 45 degrees, arrives vertical at the neck.
        hx, hy = HIP
        nx, ny = NECK
        self.add_bezier("torso", HIP, ((hx + 4, hy - 4.5), (nx, ny + 4.5), NECK))
        self.mark_human_figure("skier", head="head", torso="torso", torso_junction="end")

        self.add_polyline("arm", NECK, ELBOW, HAND)
        self.relate("connect", "arm", "torso")

        self.add_line("rear-leg", HIP, REAR_FOOT)
        self.add_line("front-leg", HIP, FRONT_FOOT)
        self.relate("connect", "rear-leg", "torso")
        self.relate("connect", "front-leg", "torso")
        self.relate("connect", "front-leg", "rear-leg")

        # Rear ski, split under the boot.
        a, b = REAR_SKI
        self.add_line("rear-ski-tail", (a, GROUND), REAR_FOOT)
        self.add_line("rear-ski-nose", REAR_FOOT, (b, GROUND))
        self.add_contour("rear-ski", "rear-ski-tail", "rear-ski-nose")
        self.relate("connect", "rear-ski", "rear-leg")

        # Front ski, split under the boot and the pole, with an upturned tip.
        a, b = FRONT_SKI
        self.add_line("front-ski-tail", (a, GROUND), FRONT_FOOT)
        self.add_line("front-ski-mid", FRONT_FOOT, POLE_FOOT)
        self.add_line("front-ski-fore", POLE_FOOT, (b, GROUND))
        self.add_arc("front-ski-tip", (b, GROUND), (b + TIP_R, GROUND - TIP_R),
                     radius_x=TIP_R, sweep=False)
        self.add_contour("front-ski", "front-ski-tail", "front-ski-mid",
                         "front-ski-fore", "front-ski-tip")
        self.relate("connect", "front-ski", "front-leg")

        self.add_line("pole", HAND, POLE_FOOT)
        self.relate("connect", "pole", "arm")
        self.relate("connect", "pole", "front-ski")
