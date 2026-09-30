"""cycling (redraw of the new-pipeline traced SVG).

Plan: a side-view stick cyclist on HRECT_L (centerline box (4,8)-(44,40)),
built like Lucide `bike` (two wheels + one zigzag body + small head) at this
family's stroke 4.
- wheels: two r5 rings of cardinal quarter arcs about (9,35) and (39,35);
  they set the left 4, right 44 and bottom 40 extremes exactly.
- head: a r2 ring about (30,10) (paints solid, top 8 = the top extreme).
- torso: one line from the neck (30,20), exactly 8 below the head outline
  (4-unit ink gap), leaning back and down to the hip (19,25); flagged with
  mark_human_figure.
- leg: hip -> knee (26,31) -> foot (22,37), pedalling down between the
  wheels; arm: neck -> hand (37,22) on the handlebar over the front wheel.
  Every body point stays 13+ from each wheel centre (8+ from the rim).
Lucide: `bike` gave the construction (wheels + zigzag rider, compact head).
Human reference: icon_set/references/human_ref (detached head, straight
round-ended limbs, exact 4-unit head gap).

Metric issues (cycling_metrics.json) and how they were handled:
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- keyshape-short-axis (HRECT_L x fill 93%): the wheels now reach x 4 and
  x 44, the head y 8 and the wheel bottoms y 40, so every extreme is exact.
- clearance e0/e2, e0/e3 (head 6.9 / 2.9 from arm and shoulder hump): the
  head sits 8 above the neck and 9.3+ from the arm.
- clearance e1/e2, e1/e3 (leg 7.7 from arm and torso): the knee is 8.4 from
  the torso and 11.7 from the arm.
- clearance e1/e4, e1/e5, e3/e4, e3/e5, e2/e5 (body touching or crowding the
  wheels, 2.8-5.9): the hip, knee, foot and hand are all 13.1-14.1 from the
  wheel centres (8.1+ from the rims).
- hole 1.79 (head): the head is a solid r2 ring (no enclosed hole); a hollow
  r5 head (6 inscribed) needs 18 units of height above the neck, which leaves
  no room for the body above r5 wheels in a 32-unit box.
- head-gap (e4 as head): the metrics mistook the rear wheel for the head;
  the real head is exactly 8 on centerlines above the neck.
Not kept: the far arm/leg of the brief and a hollow head (width/height
budget above); the leg is straight-segmented instead of rounded joints.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8d3730da-df45-48a8-9d4e-6cf0a350df28"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1044-cycling/cycling_raw.svg"
AUTHOR = "claude-opus-5-5"

WHEEL_R = 5
WHEEL_Y = 35                          # wheels span y 30..40
WHEEL_XS = (9, 39)                    # rims touch x 4 and x 44
HEAD = (30, 10)                       # small ring head, top y 8
HEAD_R = 2
NECK = (30, HEAD[1] + HEAD_R + 8)     # (30, 20): exactly 8 below the head
HIP = (19, 25)
KNEE = (26, 31)
FOOT = (22, 37)
HAND = (37, 22)


class CyclingRedraw(Solo48):
    icon_id = "cycling-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/cycling"
    aliases = ("cyclist", "bike rider", "bicycle rider", "biking")
    keywords = ("cycling", "cyclist", "bike", "bicycle", "rider", "sport", "person", "ride")

    def _ring(self, name: str, c: tuple[int, int], r: int) -> None:
        x, y = c
        self.add_arc(f"{name}-tr", (x + r, y), (x, y - r), radius_x=r, sweep=False)
        self.add_arc(f"{name}-tl", (x, y - r), (x - r, y), radius_x=r, sweep=False)
        self.add_arc(f"{name}-bl", (x - r, y), (x, y + r), radius_x=r, sweep=False)
        self.add_arc(f"{name}-br", (x, y + r), (x + r, y), radius_x=r, sweep=False)
        self.add_contour(name, f"{name}-tr", f"{name}-tl", f"{name}-bl", f"{name}-br", closed=True)

    def build(self) -> None:
        for side, x in zip(("rear", "front"), WHEEL_XS):
            self._ring(f"wheel-{side}", (x, WHEEL_Y), WHEEL_R)

        self._ring("head", HEAD, HEAD_R)
        self.add_line("torso", NECK, HIP)
        self.add_polyline("leg", HIP, KNEE, FOOT)
        self.add_line("arm", NECK, HAND)
        self.relate("connect", "torso", "leg")
        self.relate("connect", "torso", "arm")
        self.mark_human_figure("cyclist", head="head", torso="torso", torso_junction="start")
