"""congregation-beneath-rising-sun (redraw of the new-pipeline traced SVG).

Plan: two worshipper busts under a rising sun, on SQUARE (the suggested
keyshape, centerline box (6,6)-(42,42)), mirrored about x=24.
- sun: half disc as two quarter arcs, rx6 ry5, centre (24,11); its apex is
  the y=6 extreme. Slightly flattened so it reads as a sun on the horizon
  and stays wide without crowding the heads.
- busts: one repeated definition at x=13 and x=35 (FIG_DX=11 about 24).
  - shoulders: quarter arc r5 up from the foot, flat top of 4 at y=37,
    quarter arc r5 down; feet on y=42 (the bottom extreme), open at the
    bottom. Outer feet are the x=6 and x=42 extremes; inner feet (20, 28)
    are 8 apart. The flat top is split at the axis so the neck junction is
    an endpoint for mark_human_figure.
  - head: circle r5, centre (cx,24); its bottom (cx,29) is exactly 8 on
    centerlines above the shoulder top (4-unit ink gap); r5 leaves a
    6-unit inscribed hole.
- sun to head: sun feet (18,11)/(30,11) are 13.93 from the head centres,
  8.93 from the head outlines.
Reference: icon_set/references/human_ref/user.svg (circular head, broad
rounded shoulders with a short flat top, open bottom, detached 4-unit gap).
Lucide `users` / `user` informed the bust: circle head over a rounded,
flat-topped shoulder arc.

Metric issues fixed:
- clearance e2-e5, e3-e4 (head vs shoulders 2.2): exact 8 on centerlines.
- hole x2 (4.6 inscribed): head r5 -> 6 inscribed.
- clearance e1-e2, e1-e3 (sun vs heads 4.3): sun narrowed and raised to the
  top extreme, now 8.93 from both heads.
- clearance e4-e5 (shoulders 5.5 apart): inner shoulder feet exactly 8 apart.
- no-head (warn): heads are true circles and each bust is marked with
  mark_human_figure.
- stroke-width (info): drawn at stroke 4, every gap budgeted for it.
Not fixed / dropped:
- clearance e0-e1: the short vertical ray above the sun is removed. The
  column ray + 8 + sun + 8 + head(10) + 8 + shoulders(5) needs well over
  the 36 (SQUARE) or 40 (VRECT_L) centerline height, and the rows cannot
  interleave because the heads sit under the sun's ends. The half disc on
  its own keeps the rising-sun reading.
Candidates compared (all valid): VRECT_L with a larger r8 sun and
semicircle or flat-topped shoulders (heads outweighed the 12-wide shoulders),
SQUARE with a circular r5 sun (too small) and rx7 ry5 (reads as a lid).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f7860911-157a-4fff-a6a5-f904dc8d19e7"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1057-congregation-beneath-rising-sun-batch-014-04/"
    "congregation-beneath-rising-sun-batch-014-04_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
TOP_Y, BASE_Y = 6, 42          # SQUARE centerline extremes
SUN_RX, SUN_RY = 6, 5
SUN_CY = TOP_Y + SUN_RY        # 11
FIG_DX = 11                    # bust centres at 13 and 35
SHOULDER_W = 7                 # half width: outer feet on x=6 / x=42
SHOULDER_R = 5                 # corner radius; flat top half width 2
SHOULDER_TOP = BASE_Y - SHOULDER_R          # 37
HEAD_R = 5                     # 6-unit inscribed hole
HEAD_CY = SHOULDER_TOP - 8 - HEAD_R         # 24: exact detached-head gap


class CongregationBeneathRisingSunRedraw(Solo48):
    icon_id = "congregation-beneath-rising-sun-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/religion"
    aliases = ("worshippers at sunrise", "congregation", "sunrise prayer")
    keywords = ("congregation", "worship", "people", "sun", "sunrise", "group", "prayer")

    def build(self) -> None:
        apex = (AXIS, TOP_Y)
        self.add_arc("sun-left", (AXIS - SUN_RX, SUN_CY), apex,
                     radius_x=SUN_RX, radius_y=SUN_RY, sweep=True)
        self.add_arc("sun-right", apex, (AXIS + SUN_RX, SUN_CY),
                     radius_x=SUN_RX, radius_y=SUN_RY, sweep=True)
        self.add_contour("sun", "sun-left", "sun-right")

        for side, cx in (("left", AXIS - FIG_DX), ("right", AXIS + FIG_DX)):
            r = HEAD_R
            self.add_arc(f"{side}-head-top", (cx - r, HEAD_CY), (cx + r, HEAD_CY),
                         radius_x=r, sweep=True)
            self.add_arc(f"{side}-head-bottom", (cx + r, HEAD_CY), (cx - r, HEAD_CY),
                         radius_x=r, sweep=True)
            self.add_contour(f"{side}-head", f"{side}-head-top", f"{side}-head-bottom",
                             closed=True)

            w, k = SHOULDER_W, SHOULDER_R
            flat = w - k
            self.add_arc(f"{side}-shoulder-a", (cx - w, BASE_Y), (cx - flat, SHOULDER_TOP),
                         radius_x=k, sweep=True)
            self.add_line(f"{side}-neck-a", (cx - flat, SHOULDER_TOP), (cx, SHOULDER_TOP))
            self.add_line(f"{side}-neck-b", (cx, SHOULDER_TOP), (cx + flat, SHOULDER_TOP))
            self.add_arc(f"{side}-shoulder-b", (cx + flat, SHOULDER_TOP), (cx + w, BASE_Y),
                         radius_x=k, sweep=True)
            self.add_contour(f"{side}-shoulders", f"{side}-shoulder-a", f"{side}-neck-a",
                             f"{side}-neck-b", f"{side}-shoulder-b")
            self.mark_human_figure(f"{side}-worshipper", head=f"{side}-head",
                                   torso=f"{side}-neck-a", torso_junction="end")
