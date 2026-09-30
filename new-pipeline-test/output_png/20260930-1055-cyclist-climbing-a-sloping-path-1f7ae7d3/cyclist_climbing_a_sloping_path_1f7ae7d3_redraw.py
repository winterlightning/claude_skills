"""cyclist-climbing-a-sloping-path (redraw of the new-pipeline traced SVG).

Plan: a right-facing stick cyclist riding up a 1-in-4 slope, on SQUARE
(centerline box (6,6)-(42,42)), the keyshape the metrics suggested.
- path: one straight line (6,42)-(42,33). It sets the left 6, right 42 and
  bottom 42 extremes, and its 1:4 rise matches the generated image's slope.
- wheels: two r5 rings of cardinal quarter arcs, rear (11,27) and front
  (37,20). The front wheel sits 7 higher, so the bike visibly climbs the
  slope. Each rim clears the path by 8.3-8.8 on centerlines, and the
  inscribed hole is 6.
- head: an r2 ring at (27,8); it paints solid, and its top at 6 is the top
  extreme. The head is held forward of the shoulders, level with them.
- torso: one hunched cubic from the neck (17,8) to the hip (9,12). It leaves
  the neck level, so the head sits exactly 8 to its right on centerlines
  (4-unit ink gap), flagged with mark_human_figure.
- leg: hip -> knee (22,17) -> foot (25,28), pedalling down between the
  wheels, 8+ from both rims and 9 from the path.
Lucide: `bike` gave the construction: two wheels plus a zigzag rider with a
small head, and no frame. Human reference: icon_set/references/human_ref
(detached head, straight round-ended limbs, exact 4-unit head gap).
Deliberately asymmetric: the rider faces uphill to the right.

Pose change and dropped part. The image's upright rider, with its head above
the shoulder and a reaching arm, cannot fit SQUARE at stroke 4. A certified
head gap only works straight above a vertical neck or beside a level one; a
diagonal gap comes back `review`. A head above the neck needs 12 units of
height over the shoulder, which puts the hip within 13 of a wheel centre.
The wheels themselves are pinned 13 above the path. A layout search over
SQUARE, VRECT_L and HRECT_L, slopes 1:4 to 1:9, level and vertical necks,
and arms from the shoulder or from mid-back found no placement where an
arm clears the head (10), both wheel centres (13) and the leg (8). So the
rider is a crouched climber, head forward of a hunched back, and the
reaching arm is dropped.

Metric issues (cyclist-climbing-a-sloping-path-1f7ae7d3_metrics.json):
- stroke-width (info, 2.39): redrawn at stroke 4, with every gap budgeted for 4.
- stroke-count (warn, 11 strokes vs 6): now 6 parts (path, 2 wheels, head,
  torso, leg).
- keyshape-short-axis (warn, y fill 86%): the head top (6) and the path's
  left end (42) now span the full y box; x runs from the path's 6 to 42.
- clearance errors e0-e10 (27 pairs, 2.3-6.7): every pair of unconnected
  parts is 8+ apart; validate_icon and build_gate report no MIC findings.
- loose-join e2/e4, e3/e4, e4/e6, e5/e6 and narrow-join e3/e4 (32.6 deg):
  the zigzag trace is rebuilt as one torso curve plus one leg polyline
  sharing the hip node, declared connect.
- holes 3.93 (rider/wheel pocket) and 5.23 / 5.26 (wheels): the rider
  encloses nothing; the wheels are r5 rings with 6 inscribed.
- head-gap e8 / e9: the trace detector took the wheels for heads. The real
  head is a ring exactly 8 from the level neck on centerlines.
Not fixed: none of the listed issues. The reaching arm was dropped instead
(see above).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1f7ae7d3-ecbe-4b15-9965-79c8913e76e0"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1055-cyclist-climbing-a-sloping-path-1f7ae7d3/cyclist-climbing-a-sloping-path-1f7ae7d3_raw.svg"
AUTHOR = "claude-opus-5-5"

PATH_START, PATH_END = (6, 42), (42, 33)   # rises 1 in 4
WHEEL_R = 5
REAR, FRONT = (11, 27), (37, 20)    # rims clear the path by 8+
HEAD, HEAD_R = (27, 8), 2
NECK = (HEAD[0] - HEAD_R - 8, HEAD[1])     # (17, 8): exactly 8 left of the head
HIP = (9, 12)
KNEE = (22, 17)
FOOT = (25, 28)


class CyclistClimbingASlopingPathRedraw(Solo48):
    icon_id = "cyclist-climbing-a-sloping-path-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/cycling"
    aliases = ("uphill cycling", "cyclist climbing", "bike climb", "hill climb")
    keywords = ("cyclist", "cycling", "bike", "bicycle", "uphill", "climb",
                "slope", "hill", "path", "rider", "sport", "person")

    def _ring(self, name: str, c: tuple[int, int], r: int) -> None:
        x, y = c
        self.add_arc(f"{name}-tr", (x + r, y), (x, y - r), radius_x=r, sweep=False)
        self.add_arc(f"{name}-tl", (x, y - r), (x - r, y), radius_x=r, sweep=False)
        self.add_arc(f"{name}-bl", (x - r, y), (x, y + r), radius_x=r, sweep=False)
        self.add_arc(f"{name}-br", (x, y + r), (x + r, y), radius_x=r, sweep=False)
        self.add_contour(name, f"{name}-tr", f"{name}-tl", f"{name}-bl", f"{name}-br", closed=True)

    def build(self) -> None:
        self.add_line("path", PATH_START, PATH_END)
        self._ring("wheel-rear", REAR, WHEEL_R)
        self._ring("wheel-front", FRONT, WHEEL_R)

        self._ring("head", HEAD, HEAD_R)
        self.add_bezier("torso", NECK, ((NECK[0] - 5, NECK[1]), (HIP[0], HIP[1] - 2), HIP))
        self.add_polyline("leg", HIP, KNEE, FOOT)
        self.relate("connect", "torso", "leg")
        self.mark_human_figure("cyclist", head="head", torso="torso", torso_junction="start")
