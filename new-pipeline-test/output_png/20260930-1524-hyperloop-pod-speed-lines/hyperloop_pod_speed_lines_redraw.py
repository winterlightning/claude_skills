"""hyperloop-pod-speed-lines (redraw of the new-pipeline traced SVG).

Plan: a bullet pod in side profile flying right over its track, a window
slot, and two speed dashes trailing to the left, on HRECT_M (centerline box
(4,10)-(44,38)). The pod is mirrored about its own axis y=20.
- pod: one closed contour. Flat rear wall at x=16 with square centerline
  corners (round joins paint ink radius 2), straight roof y=10 and floor
  y=30 to x=30, and a two-cubic bullet nose whose apex (44,20) is a drawn
  endpoint and the right extreme.
- window: a slot line on the pod axis, x=25..35, centred in the pod; 9 from
  the rear wall and the nose (curve contours need 9 to certify), 10 from
  roof and floor.
- speed lines: two 4-unit dashes on y=16 / y=24 (8 apart, mirrored about
  the pod axis), x=4..8, ending 8 from the straight rear wall.
- track: one line y=38 across the full width, 8 under the floor. It gives
  the pod its hyperloop / maglev context and carries the bottom and the
  left/right extremes of HRECT_M.
Budget: HRECT_M is 40x28 on centerlines, and 12 of the 40 go to the dashes
and their gap. The trace's pod was a 3:1 capsule holding an enclosed slot
window; an enclosed window needs a pod 26+ tall, which leaves a 28x28
D-shape (tried: it reads as a letter D with a lens, not a vehicle). So the
pod is 28x20, the enclosed window became a slot line, and the track takes
the remaining height.

Traced shape: 20260930-1524-hyperloop-pod-speed-lines/hyperloop-pod-speed-lines_raw.svg
(read for the subject only; no coordinates copied).
Lucide: no hyperloop icon; the flat-rear, round-nosed body with a single
ground line follows lucide/train-front-tunnel and lucide/tram-front in
spirit (one body contour, detail on the axis, a base line).

Metric issues fixed:
- stroke-width (2.63 traced): redrawn at stroke 4 with every gap re-budgeted.
- keyshape-short-axis (y filled 47%): roof on y=10, track on y=38, track
  and dashes start on x=4, track and nose apex end on x=44, so all four
  HRECT_M extremes are exact.
- clearance e0/e1 (pod/window 3.03): window is 9+ from every pod wall.
- clearance e0/e2, e0/e3 (pod/dashes 2.1): dashes end 8 from the rear wall.
- clearance e1/e2, e1/e3 (window/dashes 6.9): now 17+ apart.
- clearance e2/e3 (dashes 5.56 apart): now 8 apart on centerlines.
- holes 1.26 / 3.06 / 2.8 wide: the only enclosed hole is the pod interior,
  9+ wide around the window slot.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0b674991-fc01-44ec-9571-1f5372072662"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1524-hyperloop-pod-speed-lines/"
    "hyperloop-pod-speed-lines_raw.svg"
)
AUTHOR = "claude-opus-5-5"

LEFT, RIGHT = 4, 44
ROOF, FLOOR = 10, 30
POD_AXIS = (ROOF + FLOOR) // 2   # y=20
REAR_X = 16
NOSE_X = 30                      # roof and floor end, nose begins
TRACK_Y = 38
WINDOW_X = (25, 35)
DASH_X1 = 8
DASH_DY = 4                      # dashes on y=16 and y=24


class HyperloopPodSpeedLinesRedraw(Solo48):
    icon_id = "hyperloop-pod-speed-lines-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ("hyperloop", "hyperloop-pod", "maglev-pod")
    keywords = ("hyperloop", "pod", "capsule", "train", "maglev", "track",
                "speed", "fast", "transport", "travel", "motion")

    def build(self) -> None:
        apex = (RIGHT, POD_AXIS)
        self.add_line("rear", (REAR_X, FLOOR), (REAR_X, ROOF))
        self.add_line("roof", (REAR_X, ROOF), (NOSE_X, ROOF))
        self.add_bezier("nose-top", (NOSE_X, ROOF), ((38, ROOF), (RIGHT, 15), apex))
        self.add_bezier("nose-bottom", apex, ((RIGHT, 25), (38, FLOOR), (NOSE_X, FLOOR)))
        self.add_line("floor", (NOSE_X, FLOOR), (REAR_X, FLOOR))
        self.add_contour(
            "pod", "rear", "roof", "nose-top", "nose-bottom", "floor", closed=True,
        )

        self.add_line("window", (WINDOW_X[0], POD_AXIS), (WINDOW_X[1], POD_AXIS))

        for name, y in (("dash-top", POD_AXIS - DASH_DY), ("dash-bottom", POD_AXIS + DASH_DY)):
            self.add_line(name, (LEFT, y), (DASH_X1, y))

        self.add_line("track", (LEFT, TRACK_Y), (RIGHT, TRACK_Y))
