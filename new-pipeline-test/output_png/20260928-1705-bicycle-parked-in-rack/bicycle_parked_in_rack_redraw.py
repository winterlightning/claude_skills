"""bicycle-parked-in-rack (redraw of the new-pipeline traced SVG).

Plan: side-view bicycle facing right with its front wheel standing in an
inverted-U parking hoop, on HRECT_M (centerline box (4,10)-(44,38)).
- wheels: two equal 4-arc circles, r5, centres (9,33) and (30,33); r5 is the
  smallest radius whose rim has integer points off the axes (3-4-5), and its
  6-unit ink hole meets the opening floor.
- hoop: stands behind the front wheel. Left leg ends on the rim at (34,30)
  (the wheel hides its lower part), semicircular top r5 about (39,23), right
  leg drops to the ground at the x=44 extreme, 8 clear of the rim.
- frame: one open run -- rear stay from the rear rim (12,29) to the bottom
  bracket (19,24), seat tube up-back to (16,18), top tube to the head (23,18),
  fork down to the front rim at (26,30), 8 from the hoop joint. The seat post
  continues the seat tube (slope 1:2) to a flat saddle at y=10; the stem
  continues the fork line (slope 1:4) to (21,10) and a drop bar hooks forward.
  Saddle nose (13,10) sits exactly 8 behind the stem top.
- no hubs, no closed frame triangles: at stroke 4 a hub-to-hub diamond frame
  cannot hold 6-unit openings in this 40x28 box.
Lucide `bike` informed the equal round wheels; the generated PNG gave the
hoop-around-front-wheel reading and the drop handlebar.

Metric issues (bicycle-parked-in-rack_metrics.json):
- clearance errors (15, wheel/frame/rack/handlebar all fused in the trace):
  fixed -- every touching pair now shares an integer endpoint and is declared
  `connect`; every other pair keeps 8 on centerlines.
- holes 2.6 / 2.97 / 2.63 inscribed: fixed -- wheel holes are 6, the frame is
  open, the hoop is open at the ground.
- keyshape-short-axis (y filled 66%): fixed -- saddle and handlebar reach y=10,
  wheels and hoop leg reach y=38; x runs 4 (rear wheel) to 44 (hoop leg).
- stroke-count 7 vs 6: fixed in spirit -- 2 wheels, frame, seat post + saddle,
  stem + handlebar, hoop.
- stroke-width (trace 2.64): redrawn at stroke 4.
Not kept: the hoop fully encircling the wheel at the trace's tight gap --
a concentric hoop needs 2r+16 of width, which with the rear wheel exceeds the
40-unit box; the hoop therefore passes behind the wheel instead.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f7ac223a-3452-4084-8389-29ffab6bfcef"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1705-bicycle-parked-in-rack/bicycle-parked-in-rack_raw.svg"
AUTHOR = "claude-opus-5-5"

R = 5
WHEEL_Y = 33
REAR_X, FRONT_X = 9, 30
REAR_JOINT = (REAR_X + 3, WHEEL_Y - 4)      # (12,29) rear stay
FORK_JOINT = (FRONT_X - 4, WHEEL_Y - 3)     # (26,30) fork
HOOP_JOINT = (FRONT_X + 4, WHEEL_Y - 3)     # (34,30) hoop left leg
BRACKET = (19, 24)
SEAT_CLUSTER = (16, 18)                     # on the seat tube, slope 1:2
HEAD = (23, 18)                             # on the fork line, slope 1:4
STEM_TOP = (21, 10)
SADDLE_POST = (12, 10)                      # seat tube continued to y=10
SADDLE = ((7, 10), (13, 10))                # nose 8 behind the stem top
HOOP_R = 5
HOOP_TOP_Y = 23                             # arc ends / leg tops
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
        import math
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

        # Frame: rear stay -> bracket -> seat tube -> top tube -> fork, one open run.
        self.add_polyline("frame", REAR_JOINT, BRACKET, SEAT_CLUSTER, HEAD, FORK_JOINT)
        self.relate("connect", "frame", "rear-wheel")
        self.relate("connect", "frame", "front-wheel")

        # Seat post and saddle.
        self.add_line("seat-post", SEAT_CLUSTER, SADDLE_POST)
        self.add_line("saddle-rear", SADDLE[0], SADDLE_POST)
        self.add_line("saddle-nose", SADDLE_POST, SADDLE[1])
        self.add_contour("saddle", "saddle-rear", "saddle-nose")
        self.relate("connect", "seat-post", "frame")
        self.relate("connect", "seat-post", "saddle")

        # Stem on the fork line, drop bar hooking forward.
        self.add_line("stem", HEAD, STEM_TOP)
        self.add_line("bar", STEM_TOP, (25, 10))
        self.add_arc("bar-drop", (25, 10), (28, 13), radius_x=3, sweep=True)
        self.add_contour("handlebar", "stem", "bar", "bar-drop")
        self.relate("connect", "handlebar", "frame")

        # Hoop behind the front wheel.
        left = HOOP_JOINT[0]
        self.add_line("hoop-left", HOOP_JOINT, (left, HOOP_TOP_Y))
        self.add_arc("hoop-top", (left, HOOP_TOP_Y), (HOOP_RIGHT, HOOP_TOP_Y), radius_x=HOOP_R, sweep=True)
        self.add_line("hoop-right", (HOOP_RIGHT, HOOP_TOP_Y), (HOOP_RIGHT, WHEEL_Y + R))
        self.add_contour("hoop", "hoop-left", "hoop-top", "hoop-right")
        self.relate("connect", "hoop", "front-wheel")
