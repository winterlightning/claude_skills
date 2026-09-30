"""car-viewed-from-the-rear (redraw of the new-pipeline traced SVG).

Subject: a car seen straight from behind -- a rounded body box, a
trapezoid cabin with its rear window on top, two taillights and two short
tyre stubs under the body.

Plan (mirrored about x=24): HRECT_L, centerline box (4,8)-(44,40).
Extremes: x=4 / x=44 body walls, y=8 roof, y=40 tyre stubs.
- body: one closed contour, walls x=4 / x=44, beltline y=18, bottom
  y=36, corner radius 4 (Lucide `car-front` rounded body). The beltline is
  split at x=11 / x=37 where the cabin stands on it.
- cabin: open polyline (11,18)-(16,8)-(32,8)-(37,18) on 1:2 slants,
  connected to the beltline at both feet; the enclosed trapezoid is the
  rear window (10 tall on centerlines = the 6-unit ink hole floor).
- taillights: one mirrored definition, a horizontal stroke on y=27,
  x 13-18 / 30-35: 9 from the beltline, the bottom and the walls (the
  body contour has arcs, so an exact 8 comes back `review`).
- tyres: one mirrored definition, stubs x=8 / x=40 from the corner
  tangent points (y=36) down to y=40, connected to the body.
References: generated PNG read for the subject only; Lucide `car-front`
(cabin trapezoid sitting on a rounded body rect, short tyre stubs, lights
inside the body). No trace coordinates copied.

Vertical budget: cabin hole 10 + taillight 9 above and 9 below + tyre 4 =
32. HRECT_M only has 28 (it leaves no tyres, or the lights 8 from a curved
contour, which validates as `review`), so HRECT_L (score 1.17 vs 1.20) was
used.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted at 8.
- stroke-count (7, budget 6): fixed; 6 strokes (body, cabin, 2 lights,
  2 tyres). The trace's two zero-length dots e1/e2 are gone.
- keyshape-short-axis (x fills 95% of HRECT_M): fixed by the keyshape
  change; x runs exactly 4-44 and y exactly 8-40 on HRECT_L.
- clearance e3/e4 (roof vs window, 3.3): fixed; the window is the cabin
  interior itself, no inner window contour.
- clearance e3/e5, e3/e6 (walls vs lights, 3.6): fixed; 9 from the walls.
- clearance e4/e5, e4/e6 (window vs lights, 5.7): fixed; 9 below the
  beltline.
- hole [17.1,16.7] (3.0, the roof/window sliver): fixed; that sliver no
  longer exists and the window hole is 6 tall in ink (the floor).
Not kept as drawn: the PNG's separate inner window ring and its flared
shoulders (no room for two nested rings at 8 spacing plus lights).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2ae26408-156c-43de-9e16-97f3b148035f"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1941-car-viewed-from-the-rear/car-viewed-from-the-rear_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                      # mirror axis
WALL = 4                     # left wall; right mirrors to 44
BELT, BOTTOM = 18, 36        # body top (beltline) / bottom
CR = 4                       # body corner radius
ROOF = 8
CABIN_FOOT, CABIN_TOP = 11, 16   # left foot / left roof corner x
LIGHT_Y, LIGHT_X0, LIGHT_X1 = 27, 13, 18
TYRE_X, TYRE_END = WALL + CR, 40


def mx(x: int) -> int:
    return 2 * AX - x


class CarViewedFromTheRearRedraw(Solo48):
    icon_id = "car-viewed-from-the-rear-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/vehicle"
    aliases = ("car rear", "car back view", "rear view car")
    keywords = ("car", "rear", "back", "vehicle", "automobile", "taillight", "transport")

    def build(self) -> None:
        left, right = WALL, mx(WALL)

        # Body: rounded box, beltline split at the cabin feet.
        self.add_line("left", (left, BOTTOM - CR), (left, BELT + CR))
        self.add_arc("tl", (left, BELT + CR), (left + CR, BELT), radius_x=CR, sweep=True)
        self.add_line("belt-l", (left + CR, BELT), (CABIN_FOOT, BELT))
        self.add_line("belt-m", (CABIN_FOOT, BELT), (mx(CABIN_FOOT), BELT))
        self.add_line("belt-r", (mx(CABIN_FOOT), BELT), (right - CR, BELT))
        self.add_arc("tr", (right - CR, BELT), (right, BELT + CR), radius_x=CR, sweep=True)
        self.add_line("right", (right, BELT + CR), (right, BOTTOM - CR))
        self.add_arc("br", (right, BOTTOM - CR), (right - CR, BOTTOM), radius_x=CR, sweep=True)
        self.add_line("bottom", (right - CR, BOTTOM), (left + CR, BOTTOM))
        self.add_arc("bl", (left + CR, BOTTOM), (left, BOTTOM - CR), radius_x=CR, sweep=True)
        self.add_contour(
            "body", "left", "tl", "belt-l", "belt-m", "belt-r", "tr",
            "right", "br", "bottom", "bl", closed=True,
        )

        # Cabin / rear window: trapezoid standing on the beltline.
        self.add_polyline(
            "cabin", (CABIN_FOOT, BELT), (CABIN_TOP, ROOF),
            (mx(CABIN_TOP), ROOF), (mx(CABIN_FOOT), BELT),
        )
        self.relate("connect", "cabin", "body")

        # Taillights and tyres: one mirrored definition each.
        for side, f in (("l", lambda x: x), ("r", mx)):
            self.add_line(f"light-{side}", (f(LIGHT_X0), LIGHT_Y), (f(LIGHT_X1), LIGHT_Y))
            self.add_line(f"tyre-{side}", (f(TYRE_X), BOTTOM), (f(TYRE_X), TYRE_END))
            self.relate("connect", f"tyre-{side}", "body")
