"""athlete-pole-vaulting (redraw of the new-pipeline traced SVG).

Subject: a pole vaulter hanging from a long bowed pole: a detached circular
head, a straight hanging torso, one arm reaching up to grip the pole, one
leg lifted forward with a bent knee and one trailing leg, and the pole
curving from its top tip down to its planted end at the bottom right.

Plan: VRECT_L, centerline box (8,4)-(40,44).
- head: 4 cardinal arcs, r=5 about (13,9); left extreme x=8, ink hole 6.
- neck (13,22)-(13,26), a standalone vertical line straight below the head,
  so the head outline is exactly 8 from the neck on centerlines (4 ink);
  torso (13,26)-(13,34) continues it on the same axis.
- arm: shoulder (13,26) -> grip (32,11), a T on the pole; the head centre
  is 13.3 from the arm line, so the arm clears the head outline by 8.
- pole: two cubics joined tangent-continuously at the grip; top tip (26,4)
  gives the top extreme, planted end (40,44) the right and bottom extremes.
- legs: forward leg hip -> knee (23,31) -> foot (23,39), lifted and bent;
  trailing leg hip -> knee (15,40) -> foot (11,44).

Changed from the trace on purpose:
- the two parallel arms (2.3 apart) are merged into one arm; at stroke 4 two
  arms cannot be told apart and cannot clear each other.
- the torso hangs straight down instead of leaning (a diagonal exact-8 head
  gap is not certified); the arm leaves a shoulder point 4 below the neck
  instead of the neck, and the grip sits a fifth of the way down the pole
  instead of at its tip, so the arm clears the head by the full 8. The
  pole tip still extends past the hands.
- the forward foot hangs down from the knee instead of kicking toward the
  pole, so it clears the pole.
- VRECT_L instead of the suggested VRECT_M: head (10) + 8 + arm and pole
  clearances + the forward knee need more than VRECT_M's 28-unit width.

Metric issues:
- clearance e1/e2 (the two arms, 2.31): fixed, merged into one arm.
- clearance e1/e4, e2/e4, e3/e4 (arms/torso/pole to the head dot): fixed,
  the head is a real circle 8 clear of torso, arm and pole.
- clearance e0/e2 (forward leg to arm, 6.19): fixed, the knee is 10.1 from
  the arm line.
- clearance e0/e3 (forward foot to pole, 4.72): fixed, the foot hangs from
  the knee and clears the pole.
- narrow-join e2/e1 (28.5 deg arm/torso wedge): fixed, the arm leaves the
  torso at about 52 degrees.
- no-head: fixed, the head is a true circle, marked with mark_human_figure.
- keyshape-short-axis (x fill 78%): fixed on VRECT_L; head x=8, pole end
  x=40 and y=44, pole tip y=4.
- stroke-width (info): redrawn at stroke 4; every gap measured at 4.
References: icon_set/skills/icon-design/human-reference.md and
icon_set/references/human_ref/full_body_ref.png (circular detached head on
the torso axis, straight round-ended limbs). No useful local Lucide match
for a pole vaulter.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "756dc826-ac42-5822-a4ca-d5598175bce1"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1820-athlete-pole-vaulting/"
    "athlete-pole-vaulting_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HEAD, HEAD_R = (13, 9), 5
NECK = (HEAD[0], HEAD[1] + HEAD_R + 8)    # straight below: 8 from the outline
SHOULDER = (NECK[0], NECK[1] + 4)
HIP = (SHOULDER[0], SHOULDER[1] + 8)
GRIP = (32, 11)
POLE_TOP, POLE_END = (26, 4), (40, 44)
FRONT_KNEE, FRONT_FOOT = (23, 31), (23, 39)
BACK_KNEE, BACK_FOOT = (15, 40), (11, 44)

class AthletePoleVaultingRedraw(Solo48):
    icon_id = "athlete-pole-vaulting-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/sports"
    aliases = ("pole vault", "pole vaulter", "vaulting athlete")
    keywords = ("pole vault", "athletics", "track and field", "jump",
                "athlete", "sport", "olympics", "vault", "person")

    def build(self) -> None:
        cx, cy = HEAD
        r = HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        self.add_line("neck", NECK, SHOULDER)
        self.mark_human_figure("vaulter", head="head", torso="neck",
                               torso_junction="start")
        self.add_line("torso", SHOULDER, HIP)
        self.relate("connect", "neck", "torso")

        self.add_line("arm", SHOULDER, GRIP)
        self.relate("connect", "neck", "arm")
        self.relate("connect", "torso", "arm")

        # Pole: tangent (4,5) through the grip, vertical-leaning at the plant.
        self.add_bezier("pole-top", POLE_TOP, ((28, 4.8), (30, 8.5), GRIP))
        self.add_bezier("pole-bottom", GRIP, ((36, 16), (39.5, 27), POLE_END))
        self.add_contour("pole", "pole-top", "pole-bottom")
        self.relate("connect", "arm", "pole-top")
        self.relate("connect", "arm", "pole-bottom")

        self.add_polyline("leg-front", HIP, FRONT_KNEE, FRONT_FOOT)
        self.add_polyline("leg-back", HIP, BACK_KNEE, BACK_FOOT)
        self.relate("connect", "torso", "leg-front-1")
        self.relate("connect", "torso", "leg-back-1")
        self.relate("connect", "leg-front-1", "leg-back-1")
