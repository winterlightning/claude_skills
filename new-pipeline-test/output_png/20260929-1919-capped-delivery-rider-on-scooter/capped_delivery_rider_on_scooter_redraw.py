"""capped-delivery-rider-on-scooter (redraw of the new-pipeline traced SVG).

Plan: a seated stick-figure rider facing right on SQUARE (centerline box
(6,6)-(42,42)), with a delivery box over the rear wheel and a steering column
down to the front wheel. Directional subject, so no mirroring.
- head: circle r5 at (24,11) built from four cardinal quarter arcs; its top
  is the y=6 extreme. The cap is a bill leaving the crown point (24,6) and
  dipping forward to (31,8) (a level tangent bill read as a sigma at 48).
- rider: torso a standalone line (24,24)-(24,34), exactly 8 on centerlines
  (4 ink) below the head outline on the head axis, flagged with
  mark_human_figure; the arm leaves the neck down to the hand (34,28).
- body: one open contour: seat deck from the hip back to the box, the box
  bottom (split where the rear wheel touches at (11,34)), then the box walls
  and top (6..16 x 22..34, a 6x8 ink hole). The left wall is the x=6 extreme.
- wheels: r4 circles (small-circle hole exemption) at (11,38) and (38,38);
  their bottoms are the y=42 extreme, the front wheel's right side the x=42
  extreme. Each touches the frame at its top point, a shared arc endpoint.
- column: straight line from the front wheel top (38,34) up to the hand.
Dropped: the bent leg (no room between hip, box and front wheel at 8
clearance), the rear rack stub and the front fender arc (both sat 2-4 units
from a wheel). No useful Lucide match (Lucide `bike` has no rider); human
proportions follow icon_set/references/human_ref/full_body_ref.png.

Metric issues (capped-delivery-rider-on-scooter_metrics.json) and how they
were handled:
- stroke-width (info, trace 2.76): redrawn at stroke 4, every gap budgeted.
- stroke-count (11, budget 6): now 8 strokes (head, bill, arm, torso, body,
  column, two wheels); the bill and the separate arm/torso lines are needed
  for the cap and for the certified head gap, so the budget of 6 is not met.
- clearance e0/e5, e1/e2, e1/e3, e2/e5, e3/e5 (cap pieces crowding the head
  and arm/torso): the cap is one bill sharing the head's crown point; the
  neck sits exactly 8 below the head.
- clearance e2/e6, e5/e6, e5/e7, e5/e8, e5/e10, e6/e8, e6/e9 (box, rack, arm,
  handlebar and fender 2-7.9 apart): box and deck are one contour, the arm
  ends on the column top, fender and rack stub are gone; every unconnected
  pair is >= 8 apart.
- holes (1.65-3.8 inscribed): the cap hole is gone, the box hole is 6x8 ink,
  the wheels are r4 circles (exempt).
- human head gap (reported on the wheels, a misdetection): the real head is
  now exactly 8 on centerlines / 4 ink above the torso junction.
Validation: validate_icon valid, build_gate.py PASS (0 errors, 0 warnings).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "54079a5b-25ea-4346-8fc4-d2b5f8239da0"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1919-capped-delivery-rider-on-scooter/capped-delivery-rider-on-scooter_raw.svg"
AUTHOR = "claude-opus-5-5"

HEAD_X, HEAD_Y, HEAD_R = 24, 11, 5
VISOR_END = (31, 8)                       # visor tip, dipping forward of the crown
NECK_Y, HIP_Y = 24, 34                    # torso on x = HEAD_X
HAND = (34, 28)
BOX_L, BOX_R, BOX_T = 6, 16, 22           # box bottom is the deck, y = HIP_Y
WHEEL_R, WHEEL_Y = 4, 38
REAR_X, FRONT_X = 11, 38


class CappedDeliveryRiderOnScooterRedraw(Solo48):
    icon_id = "capped-delivery-rider-on-scooter-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/delivery"
    aliases = ("delivery scooter", "courier on scooter", "food delivery rider")
    keywords = ("delivery", "courier", "scooter", "rider", "moped", "box", "cap", "shipping")

    def _wheel(self, name: str, cx: int) -> None:
        top, bottom = (cx, WHEEL_Y - WHEEL_R), (cx, WHEEL_Y + WHEEL_R)
        self.add_arc(f"{name}-r", top, bottom, radius_x=WHEEL_R, sweep=True)
        self.add_arc(f"{name}-l", bottom, top, radius_x=WHEEL_R, sweep=True)
        self.add_contour(name, f"{name}-r", f"{name}-l", closed=True)

    def build(self) -> None:
        hx, hy, hr = HEAD_X, HEAD_Y, HEAD_R

        # Head: four quarter arcs; the visor leaves the crown point forward.
        n, e, so, w = (hx, hy - hr), (hx + hr, hy), (hx, hy + hr), (hx - hr, hy)
        self.add_arc("head-ne", n, e, radius_x=hr, sweep=True)
        self.add_arc("head-se", e, so, radius_x=hr, sweep=True)
        self.add_arc("head-sw", so, w, radius_x=hr, sweep=True)
        self.add_arc("head-nw", w, n, radius_x=hr, sweep=True)
        self.add_contour("head", "head-ne", "head-se", "head-sw", "head-nw", closed=True)
        self.add_line("visor", n, VISOR_END)
        self.relate("connect", "visor", "head")

        # Rider: arm from the hand back to the neck, torso down to the hip.
        self.add_line("arm", HAND, (hx, NECK_Y))
        self.add_line("torso", (hx, NECK_Y), (hx, HIP_Y))
        self.relate("connect", "arm", "torso")
        self.mark_human_figure("rider", head="head", torso="torso", torso_junction="start")

        # Body: seat deck, box bottom split at the rear wheel, box walls.
        y = HIP_Y
        self.add_line("deck", (hx, y), (BOX_R, y))
        self.add_line("box-bottom-r", (BOX_R, y), (REAR_X, y))
        self.add_line("box-bottom-l", (REAR_X, y), (BOX_L, y))
        self.add_line("box-left", (BOX_L, y), (BOX_L, BOX_T))
        self.add_line("box-top", (BOX_L, BOX_T), (BOX_R, BOX_T))
        self.add_line("box-right", (BOX_R, BOX_T), (BOX_R, y))
        self.add_contour(
            "body", "deck", "box-bottom-r", "box-bottom-l", "box-left", "box-top", "box-right",
        )
        self.relate("connect", "torso", "body")

        # Wheels hang from their top points; the column rises to the hand.
        self._wheel("rear-wheel", REAR_X)
        self._wheel("front-wheel", FRONT_X)
        self.relate("connect", "rear-wheel", "body")
        self.add_line("column", (FRONT_X, WHEEL_Y - WHEEL_R), HAND)
        self.relate("connect", "column", "front-wheel")
        self.relate("connect", "column", "arm")
