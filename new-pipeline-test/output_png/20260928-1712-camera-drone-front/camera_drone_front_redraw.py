"""camera drone, front view (redraw of the new-pipeline traced SVG).

Plan: front view of a quadcopter on HRECT_M (centerline box (4,10)-(44,38)),
mirrored about x=24.
- rotors: seen edge-on from the front, each spinning rotor is a flat blade
  line on the y=10 extreme; left blade x 4..12 reaches the x=4 extreme, the
  right one mirrors to x=44. Each blade is split at its hub (x=8 / x=40).
- arms: one polyline per side, down from the hub (motor post) to y=BODY_Y and
  straight in to the body's side apex; connected to blade and body.
- body: stadium, half-height R=5 (6-unit hole), straight top/bottom runs
  x 22..26, end arcs about (22,19) / (26,19); bottom split at x=24.
- camera: circle r=5 about (24,33), bottom apex on the y=38 extreme, hung
  from the body on a 4-unit stem so the neck stays visible at 48 px.

Metric issues fixed by the rebuild:
- clearance errors (e0/e2, e0/e3, e0/e4, e0/e5, e0/e7, e1/e5, e2/e4, e3/e4,
  e4/e5, e4/e7, e5/e6, e5/e7, ...): every distinct part is now >= 8 apart on
  centerlines; touching parts share an endpoint and are declared `connect`.
- body hole (0.4 inscribed): the body is a stadium with a 6-unit inner height.
- keyshape-short-axis (y filled 47%): the parts are re-spaced so blades sit
  on y=10 and the camera bottom on y=38, exact HRECT_M fit.
- stroke-width (2.61): redrawn at the profile stroke 4 with gaps budgeted for it.
- stroke-count (8 > 6): the trace's stray lens specks (e4, e7) are gone;
  7 parts remain (2 blades, 2 arms, body, stem, camera).
Not kept, with reason:
- hollow oval rotors: an oval needs ry >= 5 for a 6-unit hole, so rotors
  (10 tall) + 8-unit gap + body (10) + stem + camera (10) exceed the 28-unit
  HRECT_M height (and HRECT_L's 32); the body also sits within 8 of an oval's
  lower-inner quadrant. Edge-on blade lines are the true front view.
- the camera lens dot: a dot inside an r=5 ring is only 5 from it (needs 8),
  and a ring large enough for it does not fit the height.
No useful Lucide match (Lucide has no drone; its icons are top-down aircraft).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d66af9da-0871-557c-abb0-a240e310287a"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1712-camera-drone-front/camera-drone-front_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
BLADE_Y = 10
BLADE_L = (4, 12)          # left blade x span; hub at its middle
HUB_X = sum(BLADE_L) // 2
BODY_Y = 19                # body centre line and arm level
BODY_R = 5                 # stadium half-height
BODY_HALF = 2              # half the straight top/bottom run
CAM_C = (AXIS, 33)
CAM_R = 5


def mx(p):
    return (2 * AXIS - p[0], p[1])


class CameraDroneFrontRedraw(Solo48):
    icon_id = "camera-drone-front-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("camera drone", "quadcopter", "drone front")
    keywords = ("drone", "quadcopter", "camera", "aerial", "uav", "rotor", "flying")

    def build(self) -> None:
        left, right = AXIS - BODY_HALF, AXIS + BODY_HALF
        top, bottom = BODY_Y - BODY_R, BODY_Y + BODY_R
        self.add_line("body-top", (left, top), (right, top))
        self.add_arc("body-right", (right, top), (right, bottom), radius_x=BODY_R)
        self.add_line("body-bottom-r", (right, bottom), (AXIS, bottom))
        self.add_line("body-bottom-l", (AXIS, bottom), (left, bottom))
        self.add_arc("body-left", (left, bottom), (left, top), radius_x=BODY_R)
        self.add_contour(
            "body", "body-top", "body-right", "body-bottom-r", "body-bottom-l",
            "body-left", closed=True,
        )

        hub = (HUB_X, BLADE_Y)
        body_side = (left - BODY_R, BODY_Y)
        for side, f in (("l", lambda p: p), ("r", mx)):
            self.add_line(f"blade-{side}-out", f((BLADE_L[0], BLADE_Y)), f(hub))
            self.add_line(f"blade-{side}-in", f(hub), f((BLADE_L[1], BLADE_Y)))
            self.add_contour(f"blade-{side}", f"blade-{side}-out", f"blade-{side}-in")
            self.add_polyline(f"arm-{side}", f(hub), f((HUB_X, BODY_Y)), f(body_side))
            self.relate("connect", f"arm-{side}", f"blade-{side}")
            self.relate("connect", f"arm-{side}", "body")

        cx, cy = CAM_C
        cam_top, cam_bottom = (cx, cy - CAM_R), (cx, cy + CAM_R)
        self.add_line("stem", (AXIS, bottom), cam_top)
        self.add_arc("camera-r", cam_top, cam_bottom, radius_x=CAM_R)
        self.add_arc("camera-l", cam_bottom, cam_top, radius_x=CAM_R)
        self.add_contour("camera", "camera-r", "camera-l", closed=True)
        self.relate("connect", "stem", "body")
        self.relate("connect", "stem", "camera")
