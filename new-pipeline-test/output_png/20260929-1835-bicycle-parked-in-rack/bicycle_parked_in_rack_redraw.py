"""bicycle-parked-in-rack (redraw of the new-pipeline traced SVG).

Plan: side-view bicycle facing right, an inverted-U parking hoop standing
just behind its front wheel, on HRECT_M (centerline box (4,10)-(44,38)).
- wheels: two equal circles r5 (smallest radius with a 6-unit ink hole and
  integer 3-4-5 rim points), centres (9,33) and (31,33): x 4..14 and 26..36,
  12 apart so the bottom bracket can sit 8 clear of both rims.
- frame: the generated PNG's diamond cannot keep 6-unit openings at stroke 4
  in a 40x28 box, so it is opened into the step-through V that still reads as
  a bike: chain stay from the rear rim (13,30) up to the bottom bracket
  (20,26), down tube to the head (25,17), fork down to the front rim (28,29)
  on a 1:4 line; the seat tube leaves the bracket at 3:7 to the saddle post
  (14,12).
- saddle: flat (10,12)-(16,12); its nose sits 8 behind the stem top.
- handlebar: the stem continues the fork line to (24,13), a quarter arc r3
  lifts it to y=10 and the grip runs forward to (31,10).
- rack: flat-topped hoop standing behind the front wheel. Left leg lands on
  the rim at the 3-4-5 point (35,30) (the wheel hides the rest), rises to
  y=25, two quarter arcs r4 with a 1-unit top run at y=21 carry it to the
  right leg, which reaches the ground at the x=44 extreme, 8 clear of the
  rim. Legs are 9 apart (integer radii cannot make a 9-wide semicircle).
Lucide `bike`: only the equal round wheels and open frame idea; no hubs
(a spoke to the hub splits the 6-unit wheel hole).

Metric issues (bicycle-parked-in-rack_metrics.json):
- clearance errors (e0..e6 fused wheels/frame/rack): fixed -- touching parts
  share integer endpoints and are declared `connect`; every other pair keeps
  8 on centerlines.
- holes 2.34 / 1.81 / 2.0 inscribed (frame triangles, wheels): fixed -- wheel
  holes are 6, the frame is open.
- keyshape-short-axis (y filled 66%): fixed -- handlebar reaches y=10,
  wheels and hoop leg reach y=38; x runs 4 (rear wheel) to 44 (hoop leg).
- stroke-count 7 vs 6: fixed -- 2 wheels, frame, seat tube + saddle,
  handlebar, rack.
- stroke-width (trace 2.65): redrawn at stroke 4.
Not kept: the free-standing rack with a white gap beside the front wheel --
two r5 wheels + 8 gap + a hoop 8 wide + two 8 gaps need 48 of the 40-unit
box, so the hoop stands behind the wheel with its left leg on the rim.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f7ac223a-3452-4084-8389-29ffab6bfcef"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1835-bicycle-parked-in-rack/bicycle-parked-in-rack_raw.svg"
AUTHOR = "claude-opus-5-5"

R = 5
WHEEL_Y = 33
REAR_X, FRONT_X = 9, 31
REAR_JOINT = (REAR_X + 4, WHEEL_Y - 3)      # (13,30) chain stay
FORK_JOINT = (FRONT_X - 3, WHEEL_Y - 4)     # (28,29) fork
HOOP_JOINT = (FRONT_X + 4, WHEEL_Y - 3)     # (35,30) hoop left leg
BRACKET = (20, 26)
HEAD = (25, 17)                             # on the 1:4 fork line
STEM_TOP = (24, 13)
SADDLE_POST = (14, 12)                      # seat tube 3:7 from the bracket
SADDLE = ((10, 12), (16, 12))
BAR_R = 3
GRIP_END = (31, 10)
HOOP_R = 4
HOOP_Y = 25                                 # leg tops; hoop top at y=21
HOOP_RIGHT = 44


class BicycleParkedInRackRedraw(Solo48):
    icon_id = "bicycle-parked-in-rack-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ("bike parking", "bicycle stand", "parked bike")
    keywords = ("bicycle", "bike", "parking", "rack", "stand", "hoop", "transport", "cycling")

    def _wheel(self, name: str, cx: int, cy: int, *nodes: tuple[int, int]) -> None:
        """Circle split at the given rim nodes (plus the four cardinals), clockwise."""
        pts = {(cx, cy - R), (cx + R, cy), (cx, cy + R), (cx - R, cy), *nodes}
        ordered = sorted(pts, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
        members = []
        for i, a in enumerate(ordered):
            b = ordered[(i + 1) % len(ordered)]
            pid = f"{name}-{i + 1}"
            self.add_arc(pid, a, b, radius_x=R, sweep=True)
            members.append(pid)
        self.add_contour(name, *members, closed=True)

    def build(self) -> None:
        self._wheel("rear-wheel", REAR_X, WHEEL_Y, REAR_JOINT)
        self._wheel("front-wheel", FRONT_X, WHEEL_Y, FORK_JOINT, HOOP_JOINT)

        # Frame: chain stay -> bracket -> down tube -> head -> fork, one open run.
        self.add_polyline("frame", REAR_JOINT, BRACKET, HEAD, FORK_JOINT)
        self.relate("connect", "frame", "rear-wheel")
        self.relate("connect", "frame", "front-wheel")

        # Seat tube and saddle.
        self.add_line("seat-tube", BRACKET, SADDLE_POST)
        self.add_line("saddle-rear", SADDLE[0], SADDLE_POST)
        self.add_line("saddle-nose", SADDLE_POST, SADDLE[1])
        self.add_contour("saddle", "saddle-rear", "saddle-nose")
        self.relate("connect", "seat-tube", "frame")
        self.relate("connect", "seat-tube", "saddle")

        # Stem on the fork line, bar lifting forward into a flat grip.
        sx, sy = STEM_TOP
        self.add_line("stem", HEAD, STEM_TOP)
        self.add_arc("bar-rise", STEM_TOP, (sx + BAR_R, sy - BAR_R), radius_x=BAR_R, sweep=True)
        self.add_line("grip", (sx + BAR_R, sy - BAR_R), GRIP_END)
        self.add_contour("handlebar", "stem", "bar-rise", "grip")
        self.relate("connect", "handlebar", "frame")

        # Hoop behind the front wheel: left leg on the rim, right leg on the ground.
        left = HOOP_JOINT[0]
        top = HOOP_Y - HOOP_R
        self.add_line("hoop-left", HOOP_JOINT, (left, HOOP_Y))
        self.add_arc("hoop-rise", (left, HOOP_Y), (left + HOOP_R, top), radius_x=HOOP_R, sweep=True)
        self.add_line("hoop-top", (left + HOOP_R, top), (HOOP_RIGHT - HOOP_R, top))
        self.add_arc("hoop-fall", (HOOP_RIGHT - HOOP_R, top), (HOOP_RIGHT, HOOP_Y), radius_x=HOOP_R, sweep=True)
        self.add_line("hoop-right", (HOOP_RIGHT, HOOP_Y), (HOOP_RIGHT, WHEEL_Y + R))
        self.add_contour("hoop", "hoop-left", "hoop-rise", "hoop-top", "hoop-fall", "hoop-right")
        self.relate("connect", "hoop", "front-wheel")
