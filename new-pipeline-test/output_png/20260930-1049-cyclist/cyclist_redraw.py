"""cyclist (redraw of the new-pipeline traced SVG).

Plan: a right-facing side-view stick cyclist on SQUARE (centerline box
(6,6)-(42,42)), built like Lucide `bike` (two wheels + one zigzag rider +
small head) at this family's stroke 4, following the generated PNG's pose:
head up front, back leaning forward at about 34 degrees, bent arm ending in a
level hand over the front wheel, one leg bent down to the pedal.
- wheels: two r5 rings of cardinal quarter arcs about (11,37) and (37,37);
  they set the left 6, right 42 and bottom 42 extremes exactly (inscribed
  hole 6).
- head: a r2 ring about (27,8) (paints solid, top 6 = the top extreme).
- torso: a vertical neck stub (27,18)-(27,20) exactly 8 below the head
  outline (4-unit ink gap), flagged with mark_human_figure; the back then
  slants from the shoulder (27,20) to the hip (18,26). A diagonal head/neck
  gap only certifies as `review`, the vertical stub certifies.
- arm: shoulder -> elbow (31,23) -> hand (35,23), the level grip of the PNG;
  it leaves the shoulder downward, so it stays 10 from the head centre.
- leg: hip -> knee (25,31) -> ankle (24,35), pedalling down between wheels.
Clearances on centerlines: hip 8.04 from the rear rim, knee 8.4 / ankle
8.15 / shin 8.1 from the rims, hand 9.1 from the front rim, knee 8.04 from
the back and 10 from the arm.
Lucide: `bike` gave the construction (wheels + zigzag rider, compact head).
Human reference: icon_set/references/human_ref (detached head, straight
round-ended limbs, exact 4-unit head gap).

Keyshape: SQUARE instead of the suggested HRECT_L. HRECT_L leaves only 22
units between the head top (8) and the wheel tops (30); a certified head gap
(vertical stub) plus a hip 8 clear of the wheel then forces an almost flat
back (tried: it read as a bar, not a rider). SQUARE's 36-unit height gives
the PNG's forward-leaning pose; the metrics scored SQUARE fill x 1.0.

Metric issues (cyclist_metrics.json) and how they were handled:
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- keyshape-short-axis (HRECT_L x fill 92%): moot on SQUARE; the wheels
  reach x 6 / x 42 / y 42 and the head y 6, so every extreme is exact.
- clearance e0/e1 (head 3.3 from the body): the head is detached, exactly
  8 on centerlines above the neck and 10 from the arm.
- clearance e1/e2 (body 3.5 from the front wheel): knee, shin and hand are
  8.1+ from the front rim.
- clearance e1/e3 (leg 3.9 from the rear wheel): hip and ankle are 8+ from
  the rear rim.
- hole 2.24 (head): the head is a solid r2 ring with no enclosed hole; a
  hollow r5 head (6 inscribed) would be as big as the wheels and does not
  fit above the rider.
- hole 4.65 (torso/arm/leg triangle): the arm and leg no longer meet, so the
  rider encloses nothing.
- no-head: the head is a real ring, marked as the figure's head.
Not kept: the far arm/leg (hidden in the brief too), the PNG's toe kick (no
room 8 clear of the front wheel) and its rounded hip/knee joints.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "162b8606-09be-5a25-a153-6f51561b636a"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1049-cyclist/cyclist_raw.svg"
AUTHOR = "claude-opus-5-5"

WHEEL_R = 5
WHEEL_Y = 37                          # wheels span y 32..42
WHEEL_XS = (11, 37)                   # rims touch x 6 and x 42
HEAD = (27, 8)                        # small ring head, top y 6
HEAD_R = 2
NECK = (HEAD[0], HEAD[1] + HEAD_R + 8)  # (27, 18): exactly 8 below the head
SHOULDER = (NECK[0], NECK[1] + 2)     # short vertical neck stub
HIP = (18, 26)
ELBOW = (31, 23)
HAND = (35, 23)
KNEE = (25, 31)
ANKLE = (24, 35)


class CyclistRedraw(Solo48):
    icon_id = "cyclist-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/cycling"
    aliases = ("cycling", "bike rider", "bicycle rider", "biking")
    keywords = ("cyclist", "cycling", "bike", "bicycle", "rider", "sport", "person", "ride")

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
        self.add_line("torso", NECK, SHOULDER)
        self.add_line("back", SHOULDER, HIP)
        self.add_polyline("arm", SHOULDER, ELBOW, HAND)
        self.add_polyline("leg", HIP, KNEE, ANKLE)
        self.relate("connect", "torso", "back")
        self.relate("connect", "torso", "arm")
        self.relate("connect", "back", "arm")
        self.relate("connect", "back", "leg")
        self.mark_human_figure("cyclist", head="head", torso="torso", torso_junction="start")
