"""compact car beneath clouds (redraw of the new-pipeline traced SVG).

Subject: a compact car seen from the front -- a wide rounded body, a cabin
with one broad windshield (the belt line is the body's top edge) and two
wheel stubs -- under two small rounded clouds.

Plan: SQUARE, centerline box (6,6)-(42,42), everything mirrored about x=24.
Extremes: x=6/42 the body sides and the clouds' small outer lobes, y=6 the
clouds' big lobes, y=42 the wheel stubs.
Vertical budget (36): clouds 6..16 (10), gap 8, cabin 24..32 (8), body
32..40 (8), stubs 40..42.
- clouds: Lucide "cloud" construction scaled down -- a big r5 lobe about
  (14,11) that meets a small r4 lobe at a cusp on the grid point (10,8), both
  tangent to a short flat base on y=16. The right cloud is the exact mirror,
  so the small lobes face outward and the gap between clouds is 10.
- body: rounded rectangle (6,32)-(42,40), r3 corners, top and bottom edges
  split where the cabin and the stubs attach.
- cabin: 1:2 slopes (11,32)-(15,24) and the roof (15,24)-(33,24), joined
  with round joins. A cubic roof corner was tried and dropped: its nearly
  level part runs 7.6 from the belt line (build-gate internal spacing).
- wheels: stubs (11,40)-(11,42) and (37,40)-(37,42), under the cabin feet.
References: generated PNG read for the subject only. Lucide car-front gave
the body/cabin/stub construction (open cabin standing on the body's top edge,
wheel stubs instead of rings); Lucide cloud gave the big-lobe/small-lobe
cloud with a flat base. No trace coordinates copied.

Keyshape: SQUARE as suggested (score 1.25, exact fill on both axes).

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted for it.
- stroke-count (7 vs 6, warn): fixed; 4 parts now (two clouds, the car
  outline with its cabin, stubs joined to the body).
- clearance e0/e1 (3.87, the clouds nearly touching): fixed; 10 apart.
- clearance e0/e6, e1/e6 (4.64, 3.39, clouds on the roof): fixed; cloud
  bases on y=16, roof on y=24 (8 line-to-line with no horizontal overlap,
  cloud lobes 8.5+ from the roof corners).
- clearance e2/e6, e3/e6 (6.86, 6.97, the cabin feet crowding the body's
  shoulders): fixed; the cabin now stands on the body's top edge at shared
  nodes (11,32)/(37,32), declared connected.
- clearance e3/e4, e3/e5 (4.39, the wheel rings crowding the body): fixed;
  the wheels are stubs joined to the body's bottom edge at shared nodes.
- hole [35.2,14.2] (4.49, right cloud): fixed; both clouds have a big r5
  lobe (6 of ink inside).
- hole [18.6,25.2] (3.0, windshield) and [14.5,33.1] (5.0, body): partly;
  both are 8 tall on centerlines (4 of ink inside, centerline-inscribed
  diameter 8, passes the build hole gate). 10 tall each would need 40 of
  height with the clouds above, over the SQUARE budget of 36; keeping the
  belt line keeps the windshield, which carries the car's identity.
Dropped: the hollow wheel rings (a ring needs 8 of clearance below the body,
no room; stubs as in Lucide car-front), the clouds' third lobe and the
vertical stagger between the two clouds (no height left for it).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ee5bbd28-411f-4a8f-bec4-24171fa57174"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1044-compact-car-beneath-clouds/compact-car-beneath-clouds_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24                       # mirror axis
CLOUD_BASE = 16                 # both clouds' flat base
BIG = (14, 11, 5)               # left cloud's big lobe (cx, cy, r)
CUSP = (10, 8)                  # left cloud: big lobe meets the small r4 lobe
BODY = (6, 32, 42, 40, 3)       # left, top, right, bottom, corner radius
FOOT, ROOF = (11, 32), (15, 24)  # left cabin nodes: foot on the belt, roof corner
STUB_X, STUB_BOTTOM = 11, 42    # left wheel stub


def mirror(point):
    x, y = point
    return (2 * AXIS - x, y)


class CompactCarBeneathCloudsRedraw(Solo48):
    icon_id = "compact-car-beneath-clouds-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/cars"
    aliases = ("car under clouds", "car in cloudy weather")
    keywords = ("car", "compact car", "cloud", "clouds", "weather", "cloudy",
                "drive", "travel", "vehicle")

    def cloud(self, name: str, flip: bool) -> None:
        """Big lobe + small outer lobe + flat base; flip mirrors it right."""
        m = mirror if flip else (lambda p: p)
        cx, cy, r = BIG
        big_bottom = m((cx, CLOUD_BASE))
        cusp = m(CUSP)
        small_bottom = m((CUSP[0], CLOUD_BASE))
        small_r = (CLOUD_BASE - CUSP[1]) // 2
        # Left cloud winds counter-clockwise; the mirror flips both sweeps.
        self.add_arc(f"{name}-big", big_bottom, cusp, radius_x=r,
                     large_arc=True, sweep=flip)
        self.add_arc(f"{name}-small", cusp, small_bottom, radius_x=small_r,
                     sweep=flip)
        self.add_line(f"{name}-base", small_bottom, big_bottom)
        self.add_contour(name, f"{name}-big", f"{name}-small", f"{name}-base",
                         closed=True)

    def build(self) -> None:
        self.cloud("cloud-left", flip=False)
        self.cloud("cloud-right", flip=True)

        # Body: rounded rectangle, edges split at the cabin feet and stubs.
        left, top, right, bottom, r = BODY
        foot_l, foot_r = FOOT, mirror(FOOT)
        stub_l, stub_r = (STUB_X, bottom), mirror((STUB_X, bottom))
        self.add_line("body-top-1", (left + r, top), foot_l)
        self.add_line("body-top-2", foot_l, foot_r)
        self.add_line("body-top-3", foot_r, (right - r, top))
        self.add_arc("body-corner-tr", (right - r, top), (right, top + r), radius_x=r)
        self.add_line("body-right", (right, top + r), (right, bottom - r))
        self.add_arc("body-corner-br", (right, bottom - r), (right - r, bottom), radius_x=r)
        self.add_line("body-bottom-1", (right - r, bottom), stub_r)
        self.add_line("body-bottom-2", stub_r, stub_l)
        self.add_line("body-bottom-3", stub_l, (left + r, bottom))
        self.add_arc("body-corner-bl", (left + r, bottom), (left, bottom - r), radius_x=r)
        self.add_line("body-left", (left, bottom - r), (left, top + r))
        self.add_arc("body-corner-tl", (left, top + r), (left + r, top), radius_x=r)
        self.add_contour(
            "body",
            "body-top-1", "body-top-2", "body-top-3", "body-corner-tr",
            "body-right", "body-corner-br", "body-bottom-1", "body-bottom-2",
            "body-bottom-3", "body-corner-bl", "body-left", "body-corner-tl",
            closed=True,
        )

        # Cabin: 1:2 slopes meeting the roof in round joins. A rounded
        # corner would run nearly level under 8 from the belt line.
        self.add_line("cabin-slope-left", foot_l, ROOF)
        self.add_line("cabin-roof", ROOF, mirror(ROOF))
        self.add_line("cabin-slope-right", mirror(ROOF), foot_r)
        self.add_contour("cabin", "cabin-slope-left", "cabin-roof",
                         "cabin-slope-right")
        for slope, a, b in (("cabin-slope-left", "body-top-1", "body-top-2"),
                            ("cabin-slope-right", "body-top-2", "body-top-3")):
            self.relate("connect", slope, a)
            self.relate("connect", slope, b)

        # Wheels: stubs hanging from the body's bottom edge.
        self.add_line("wheel-left", stub_l, (STUB_X, STUB_BOTTOM))
        self.add_line("wheel-right", stub_r, mirror((STUB_X, STUB_BOTTOM)))
        for wheel, a, b in (("wheel-left", "body-bottom-2", "body-bottom-3"),
                            ("wheel-right", "body-bottom-1", "body-bottom-2")):
            self.relate("connect", wheel, a)
            self.relate("connect", wheel, b)
