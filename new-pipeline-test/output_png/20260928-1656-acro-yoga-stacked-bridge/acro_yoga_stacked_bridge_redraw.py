"""acro-yoga-stacked-bridge (redraw of the new-pipeline traced SVG).

Plan: two stick figures in a backbend (bridge / wheel pose), stacked, on
SQUARE (centerline box (6,6)-(42,42)), the metrics' suggested keyshape.
- base: a clean bridge dome. Straight leg (6,42)-(6,32), an r10 torso arc
  about (16,32) over the top (16,22) to the shoulder (26,32), straight arm
  down to (26,42). The arc is split at the lattice knots Q=(10,24) and
  P=(22,24) (centre +(-6,-8) / +(6,-8)) so the flyer's contacts are shared
  endpoints, each >= 8.9 from the base's hip/shoulder and 12 apart.
- flyer: a second bridge standing on the base's back: legs splay up from Q
  to the hip (7,14), an rx9/ry8 elliptic torso over the top (16,6) to the
  shoulder (25,14), arms down to P.
- heads: r3 rings (the trace's heads are r2.4) level beside a 2-long neck
  run at each shoulder, exactly 8 centerline units (4 ink) from it: base
  (39,32), flyer (38,14). Keeping both heads outside the domes to the right
  of the arms follows the generated image; r4 heads would force the base
  dome to 18 wide and it read as a keyhole.
Each body is one open contour (round joins at hips/shoulders); with the
two necks and two heads the icon has 6 strokes.
Extremes: left 6 (base leg), right 42 (base head), top 6 (flyer torso),
bottom 42 (base foot and hand).
References: icon_set/references/human_ref (ring heads, single-stroke limbs,
detached head with a 4-unit ink gap on a level neck run). No useful Lucide
match: Lucide has no partner-yoga / backbend figure.

Metric issues fixed:
- clearance e0/e1, e0/e2, e0/e3, e0/e4, e2/e3, e2/e4 (3.5-7.1, the flyer's
  double leg strokes and the base's split legs crowding the hip and back):
  each figure now has one leg stroke and one arm stroke; the flyer's feet
  and hands land on shared knots of the base's back, and every unconnected
  pair is >= 8 apart (validate_icon is valid with no warnings).
- clearance e1/e5, e5/e7, e0/e7, e1/e7 and head-gap e7 (1.9-4.5, the
  foot ticks and the base head jammed against the arm/back): foot ticks
  (e5, and e3/e4's ends) are dropped, and both heads sit level beside
  their neck run at exactly 8 on centerlines.
- clearance e0/e6 (4.49, the flyer's head traced as a dot against its
  back): the flyer head is a real r3 ring, 8 from its neck.
- narrow-join e3/e4 (30 deg wedge) and loose-join e3/e4 (1.4 short): the
  split legs are one straight leg joined to the torso at a shared node.
- keyshape-short-axis (x filled 86%): the head reaches x=42 and the leg
  x=6, so all four SQUARE extremes are exact.
- stroke-count (8 vs budget 6): 6 paths (two body contours, two necks,
  two heads).
- stroke-width (2.39 trace): redrawn at stroke 4 with every gap budgeted
  at 8.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e90b7491-c523-516a-bb5e-3f47ddbb4cab"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1656-acro-yoga-stacked-bridge/"
    "acro-yoga-stacked-bridge_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HEAD_R = 3
GAP = 8
NECK_RUN = 2

# base (lower bridge): straight leg and arm under an r10 dome about
# BASE_C, split at the lattice knots where the flyer stands (Q) and rests
# its hands (P)
BASE_C = (16, 32)
BASE_R = 10
BASE_FOOT = (6, 42)
BASE_HIP = (6, 32)
BASE_Q = (10, 24)              # BASE_C + (-6, -8)
BASE_P = (22, 24)              # BASE_C + (6, -8)
BASE_SHOULDER = (26, 32)
BASE_HAND = (26, 42)
# flyer (upper bridge): splayed limbs up from Q and P to an elliptic torso
FLYER_HIP = (7, 14)
FLYER_SHOULDER = (25, 14)

def neck_and_head(shoulder):
    neck = (shoulder[0] + NECK_RUN, shoulder[1])
    return neck, (neck[0] + GAP + HEAD_R, shoulder[1])


class AcroYogaStackedBridgeRedraw(Solo48):
    icon_id = "acro-yoga-stacked-bridge-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("stacked wheel pose", "partner bridge", "double backbend")
    keywords = ("acro yoga", "yoga", "bridge", "wheel pose", "backbend", "partner", "balance")

    def _head(self, name, centre):
        cx, cy = centre
        r = HEAD_R
        self.add_arc(f"{name}-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc(f"{name}-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour(name, f"{name}-1", f"{name}-2", f"{name}-3", f"{name}-4", closed=True)

    def build(self) -> None:
        # Base bridge
        self.add_line("base-leg", BASE_FOOT, BASE_HIP)
        self.add_arc("base-back", BASE_HIP, BASE_Q, radius_x=BASE_R)
        self.add_arc("base-belly", BASE_Q, BASE_P, radius_x=BASE_R)
        self.add_arc("base-chest", BASE_P, BASE_SHOULDER, radius_x=BASE_R)
        self.add_line("base-arm", BASE_SHOULDER, BASE_HAND)
        self.add_contour("base-body", "base-leg", "base-back", "base-belly", "base-chest", "base-arm")
        neck, head = neck_and_head(BASE_SHOULDER)
        self.add_line("base-neck", BASE_SHOULDER, neck)
        self._head("base-head", head)
        self.mark_human_figure("base", head="base-head", torso="base-neck", torso_junction="end")
        # Flyer bridge
        self.add_line("flyer-leg", BASE_Q, FLYER_HIP)
        self.add_arc("flyer-torso", FLYER_HIP, FLYER_SHOULDER, radius_x=9, radius_y=8, sweep=True)
        self.add_line("flyer-arm", FLYER_SHOULDER, BASE_P)
        self.add_contour("flyer-body", "flyer-leg", "flyer-torso", "flyer-arm")
        neck, head = neck_and_head(FLYER_SHOULDER)
        self.add_line("flyer-neck", FLYER_SHOULDER, neck)
        self._head("flyer-head", head)
        self.mark_human_figure("flyer", head="flyer-head", torso="flyer-neck", torso_junction="end")

        for a, b in (
            ("base-leg", "base-back"), ("base-back", "base-belly"), ("base-belly", "base-chest"),
            ("base-chest", "base-arm"), ("base-chest", "base-neck"), ("base-arm", "base-neck"),
            ("flyer-leg", "base-back"), ("flyer-leg", "base-belly"),
            ("flyer-arm", "base-belly"), ("flyer-arm", "base-chest"),
            ("flyer-leg", "flyer-torso"),
            ("flyer-torso", "flyer-arm"), ("flyer-torso", "flyer-neck"), ("flyer-arm", "flyer-neck"),
        ):
            self.relate("connect", a, b)
