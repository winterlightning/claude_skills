"""bowler-approaching-a-pin (redraw of the new-pipeline traced SVG).

Plan: a right-facing stick bowler in a forward lunge, a bowling ball in the
rear hand, and one upright pin on the right, on HRECT_L (centerline box
(4,8)-(44,40)), rebuilt on the 48 grid from the image, not the trace.
- head: 4-arc circle r4 at (HX,12); its top is the y=8 extreme.
- neck: 2-unit vertical stub straight under the head, exactly 8 centerline
  units below the head outline (4-unit ink gap, human-reference.md); the
  lower torso then leans back to the hip, giving the forward lean.
- arms branch at the shoulder node (bottom of the stub): one line across the
  shoulders, back-up to the ball (ending on its right cardinal knot, declared
  connect) and a short level front arm reaching toward the pin.
- legs from the hip: the rear leg a straight 45-ish diagonal to the floor,
  the front leg knee forward, vertical shin, short toe; floor y=40.
- ball: circle r4, its left side is the x=4 extreme.
- pin: a ring head r3 sitting on the pointed top of a bellied body; the
  narrow neck is that single shared knot, the body is mirrored cubics about
  x=PX swelling to the belly (the x=44 extreme) and tapering to a flat foot.
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs). No local Lucide bowling match; the pin
follows Lucide circle-plus-cubic bottle construction.

Metric issues:
- keyshape-short-axis (HRECT_M, x filled 96%): changed to HRECT_L (score
  1.16, next to 1.21). HRECT_M's 28-unit height cannot hold head 8 + head
  gap 8 + torso + legs; HRECT_L's four extremes are met exactly.
- clearance e0/e2, e0/e3 and head-gap: the head is detached exactly 8 above
  the neck stub; the arms leave the shoulder 2 lower and stay 9+ away.
  (The metrics mistook the ball e5 for the head; the real head is e0.)
- clearance e2/e3: arms branch at the shoulder and legs at the hip, so the
  arm line and the legs never run side by side.
- clearance e1/e3, e1/e5, e3/e5, e4/e5 (hand, front leg, ball and pin
  crowding): fixed by moving the ball. 40 units of width cannot hold figure,
  ball and pin at 8-unit gaps with the ball on the floor ahead of the front
  foot (the pin needs 10, the ball 8, three gaps 24, leaving the figure 0),
  so the ball is in the backswing, held in the rear hand.
- holes: head hole 8 (r4), ball 8 (r4), pin head 6 (r3 ring), pin belly
  10 wide; the torso/arm/leg triangle hole is gone (no closed limb loop).
- stroke-width (trace 2.55): redrawn at stroke 4 with 8-unit clearances.
Deliberate change: ball moved from beside the front hand to the backswing
(width budget above). validate_icon(): valid, 0 warnings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a2a08b2a-e688-4bab-8c8e-c60515c88862"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1912-bowler-approaching-a-pin/"
    "bowler-approaching-a-pin_raw.svg"
)
AUTHOR = "claude-opus-5-5"

# Bowler
HX, HEAD_CY, HEAD_R = 22, 12, 4
NECK = (HX, HEAD_CY + HEAD_R + 8)
SHOULDER = (HX, NECK[1] + 2)
HIP = (16, 32)
REAR_FOOT = (6, 40)
FRONT_KNEE, FRONT_HEEL, FRONT_TOE = (24, 34), (24, 40), (26, 40)
FRONT_HAND = (28, 26)
# Ball, held back in the rear hand
BALL_C, BALL_R = (8, 21), 4
# Pin
PX, PIN_HEAD_CY, PIN_R = 39, 21, 3
BELLY, BELLY_Y = 5, 35
FOOT, FLOOR = 3, 40


def circle(icon, name, c, r):
    x, y = c
    pts = [(x, y - r), (x + r, y), (x, y + r), (x - r, y)]
    names = []
    for i in range(4):
        n = f"{name}-{i}"
        icon.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=r, sweep=True)
        names.append(n)
    icon.add_contour(name, *names, closed=True)


class BowlerApproachingAPinRedraw(Solo48):
    icon_id = "bowler-approaching-a-pin-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("bowler", "ten pin bowling", "bowling player")
    keywords = ("bowling", "bowler", "ball", "pin", "sport", "game", "alley", "person")

    def build(self) -> None:
        circle(self, "head", (HX, HEAD_CY), HEAD_R)
        self.add_line("torso", NECK, SHOULDER)
        self.add_line("lower-torso", SHOULDER, HIP)
        self.mark_human_figure("bowler", head="head", torso="torso", torso_junction="start")
        bx, by = BALL_C
        self.add_line("rear-arm", SHOULDER, (bx + BALL_R, by))
        self.add_line("front-arm", SHOULDER, FRONT_HAND)
        self.add_line("rear-leg", HIP, REAR_FOOT)
        self.add_polyline("front-leg", HIP, FRONT_KNEE, FRONT_HEEL, FRONT_TOE)
        circle(self, "ball", BALL_C, BALL_R)

        # Pin: a ring head sitting on the pointed top of a bellied body, so
        # the narrow neck is the single shared knot.
        circle(self, "pin-head", (PX, PIN_HEAD_CY), PIN_R)
        top = (PX, PIN_HEAD_CY + PIN_R)
        self.add_bezier("pin-right", top,
                        ((PX + 1, top[1] + 3), (PX + BELLY, BELLY_Y - 5), (PX + BELLY, BELLY_Y)),
                        ((PX + BELLY, BELLY_Y + 2), (PX + FOOT + 1, FLOOR - 1), (PX + FOOT, FLOOR)))
        self.add_line("pin-base", (PX + FOOT, FLOOR), (PX - FOOT, FLOOR))
        self.add_bezier("pin-left", (PX - FOOT, FLOOR),
                        ((PX - FOOT - 1, FLOOR - 1), (PX - BELLY, BELLY_Y + 2), (PX - BELLY, BELLY_Y)),
                        ((PX - BELLY, BELLY_Y - 5), (PX - 1, top[1] + 3), top))
        self.add_contour("pin", "pin-right", "pin-base", "pin-left", closed=True)
        self.relate("connect", "pin-head", "pin")

        for a, b in [
            ("torso", "lower-torso"),
            ("torso", "rear-arm"), ("torso", "front-arm"),
            ("lower-torso", "rear-arm"), ("lower-torso", "front-arm"),
            ("rear-arm", "front-arm"),
            ("lower-torso", "rear-leg"), ("lower-torso", "front-leg"),
            ("rear-leg", "front-leg"),
            ("rear-arm", "ball"),
        ]:
            self.relate("connect", a, b)
