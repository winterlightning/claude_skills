"""cyclist-above-two-open-wheels (redraw of the new-pipeline traced SVG).

Plan: a side-view stick cyclist leaning forward over two open wheels, on
SQUARE (centerline box (6,6)-(42,42)). The trace is square (aspect 1.00) and
HRECT_L leaves only 20 units above r6 wheels for head, gap, torso and limbs,
so SQUARE's extra 4 units of height are what let the rider fit.
- wheels: two r6 rings of cardinal quarter arcs about (12,36) and (36,36);
  they set the left 6, right 42 and bottom 42 extremes exactly and leave a
  12-wide gap between the rims (the trace had 6.1).
- head: an r2 ring about (36,8) (paints as a solid 8-wide dot), top y 6 =
  the top extreme, above the front wheel as in the image.
- torso: the hip (14,18) rises at 45 degrees to the shoulder (24,8) (the
  trace's 44-degree lean), then a 2-long level neck run to (26,8). The head
  sits level on that run's axis, exactly 8 from its outline on centerlines
  (4-unit ink gap). Axis-aligned, so the gap certifies; flagged with
  mark_human_figure (torso = the neck run, junction at its end).
- arm: shoulder -> elbow (29,20) -> hand (35,21), the trace's bent arm with a
  near-level forearm to the handlebar; 11+ from the head outline.
- leg: hip -> knee (21,24) -> foot (24,28), pedalling down into the gap
  between the wheels; 8.4+ from the rims and 8.9 from the elbow.
Lucide: no rider icon; `bike` informed plain circular wheels with no spokes.
Human reference: icon_set/references/human_ref/full_body_ref.png (round-
ended straight limbs, circular detached head, exact 4-unit ink head gap).

Metric issues (cyclist-above-two-open-wheels_metrics.json):
- stroke-width (info, trace 2.47 vs 4): redrawn at stroke 4 with every gap
  budgeted for it.
- keyshape-short-axis (HRECT_L x fill 80%): switched to SQUARE, which the
  metrics also score 1.0 with full fill on both axes; head top y 6, wheels
  x 6 / x 42 / y 42 make the fit exact.
- clearance e0/e1 (head 4.23 from the body): the head is 8 from the neck
  run and 11+ from the arm.
- clearance e1/e2, e1/e3 (leg 3.78 / 2.58 from the wheels, overlapping ink):
  the foot stops at (24,28), 14.4 from both wheel centres (8.4 from rims);
  the knee is 15 from the rear centre (9 from the rim).
- clearance e2/e3 (wheels 6.14 apart): rims are now 12 apart.
- head-gap (4.23, need exactly 8): exactly 8, head centred on the neck axis.
- hole (head 2.4 wide, need 6): repaired by removing the hole, not by
  widening it. The image's head is hollow, but a hollow r5 head (the
  smallest with a 6-wide hole) needs 18 units of height for head + gap and
  blocks the arm's path to the handlebar (head and front wheel would need
  27 between centres; 25 are available). An r3 ring (small-circle
  exception) was tried and rendered: its 2-wide pinhole shows as a grey
  speck at 48 px, so the head is a solid r2 dot.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5d94706e-5e90-41ee-bd73-a7f28a558ba3"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1053-cyclist-above-two-open-wheels/"
    "cyclist-above-two-open-wheels_raw.svg"
)
AUTHOR = "claude-opus-5-5"

WHEEL_R = 6
WHEEL_Y = 36                          # wheels span y 30..42
WHEEL_XS = (12, 36)                   # rims touch x 6 and x 42
HEAD_R = 2
HEAD = (36, 6 + HEAD_R)               # (36, 8): top y 6
NECK = (HEAD[0] - HEAD_R - 8, HEAD[1])  # (26, 8): exactly 8 from the outline
SHOULDER = (NECK[0] - 2, HEAD[1])     # (24, 8): level 2-long neck run
HIP = (14, 18)                        # 45-degree torso
ELBOW = (29, 20)
HAND = (35, 21)
KNEE = (21, 24)
FOOT = (24, 28)


class CyclistAboveTwoOpenWheelsRedraw(Solo48):
    icon_id = "cyclist-above-two-open-wheels-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/cycling"
    aliases = ("cyclist", "bike rider", "bicycle rider", "biking")
    keywords = ("cycling", "cyclist", "bike", "bicycle", "rider", "wheels", "sport", "person", "ride")

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
        self.add_line("torso", HIP, SHOULDER)
        self.add_line("neck", SHOULDER, NECK)
        self.add_polyline("arm", SHOULDER, ELBOW, HAND)
        self.add_polyline("leg", HIP, KNEE, FOOT)
        self.relate("connect", "torso", "neck")
        self.relate("connect", "torso", "arm")
        self.relate("connect", "neck", "arm")
        self.relate("connect", "torso", "leg")
        self.mark_human_figure("cyclist", head="head", torso="neck", torso_junction="end")
