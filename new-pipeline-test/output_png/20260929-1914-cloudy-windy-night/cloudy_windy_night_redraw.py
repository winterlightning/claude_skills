"""cloudy-windy-night (redraw of the new-pipeline traced SVG).

Plan: a three-lobe cloud at the left, a crescent moon alone in the top-right
corner and two wind strokes under the cloud, the upper one curling up at its
right end. SQUARE, centerline box (6,6)-(42,42).
- cloud: one closed contour, mirrored about x=15. Left and right lobes are
  r4 semicircles (centres (10,21) and (20,21)) and the crown is an r5
  semicircle (centre (15,17)). Each lobe starts where the one before it
  ends, so the two notches are exact cusps at (10,17) and (20,17). The base
  runs flat along y=25, tangent to both side lobes. Left edge x=6.
- moon: two r6 arcs between the horns (35,6) and (42,13). The outer arc is
  the long way round (left and bottom), so the horns themselves are the top
  and right extremes. The inner arc bows towards the centre. The horns are
  more than a quarter-turn apart, which gives a visible bite at 48 px; with
  the horns on the axis points (36,6)/(42,12) it read as a notched disc.
- wind: the upper stroke runs (10,34)->(32,34) and ends in an r4 half-turn
  up to (32,26). The lower stroke runs (10,42)->(26,42) along the bottom
  edge. Both start at x=10, set in from the cloud as in the PNG.
Lucide `cloud-moon` and `wind`: the notched cloud lobes, the two-arc crescent
and the half-turn curl at the end of a wind line. The cloud is not tucked
under the moon as in Lucide, because the PNG keeps them apart.

Metric issues (cloudy-windy-night_metrics.json):
- clearance e0/e1 (moon on the cloud's shoulder, 3.7 apart): fixed. The
  cloud is kept within x<=24 and the moon is pushed into the corner. The
  nearest cloud lobe is more than 8 from the moon's outer arc.
- clearance e1/e2 (cloud base on the curled wind, 4.55): fixed. The cloud
  base is at y=25 and the wind at y=34, and the curl's top is at (32,26),
  which is right of the cloud's right lobe. With the base at y=26 (exactly
  8) the lobe ends came back `review`.
- clearance e2/e3 (the two winds, 4.05): fixed. They are now 8 apart, at
  y=34 and y=42.
- hole 1.22 at the moon's inner horn: fixed. The crescent is two clean r6
  arcs meeting at two horns, about 7 wide on centerlines at the middle; the
  build gate's hole check passes.
- keyshape-short-axis (y 86%): fixed. The moon reaches y=6 and x=42, the
  cloud reaches x=6 and the lower wind is at y=42.
- stroke-width (trace 2.4): redrawn at stroke 4.
Not kept: the PNG's cloud is larger relative to the moon. With stroke 4 and
8 between the cloud, the moon and the curl, a cloud any wider than 18 hits
the moon or the curl.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f236e29a-8ef1-4244-a485-206757ee3b57"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1914-cloudy-windy-night/cloudy-windy-night_raw.svg"
AUTHOR = "claude-opus-5-5"

CLOUD_AXIS, CLOUD_BASE = 15, 25
SIDE_R, SIDE_DX = 4, 5            # side lobes: r4, centres 5 either side of the axis
CROWN_R = 5                       # crown: r5, centre on the axis
MOON_TOP_HORN, MOON_RIGHT_HORN, MOON_R = (35, 6), (42, 13), 6
WIND_LEFT, WIND_UPPER_Y, WIND_LOWER_Y = 10, 34, 42
CURL_X, CURL_R = 32, 4
WIND_LOWER_END = 26


class CloudyWindyNightRedraw(Solo48):
    icon_id = "cloudy-windy-night-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ("windy night", "night wind")
    keywords = ("cloud", "moon", "crescent", "wind", "night", "windy", "cloudy", "weather", "breeze")

    def build(self) -> None:
        # Cloud, clockwise from the bottom of the left lobe.
        lx, rx = CLOUD_AXIS - SIDE_DX, CLOUD_AXIS + SIDE_DX
        side_top = CLOUD_BASE - 2 * SIDE_R
        self.add_arc("cloud-left", (lx, CLOUD_BASE), (lx, side_top), radius_x=SIDE_R)
        self.add_arc("cloud-crown", (lx, side_top), (rx, side_top), radius_x=CROWN_R)
        self.add_arc("cloud-right", (rx, side_top), (rx, CLOUD_BASE), radius_x=SIDE_R)
        self.add_line("cloud-base", (rx, CLOUD_BASE), (lx, CLOUD_BASE))
        self.add_contour("cloud", "cloud-left", "cloud-crown", "cloud-right", "cloud-base", closed=True)

        # Crescent: outer arc the long way round from the top horn to the right horn.
        self.add_arc("moon-outer", MOON_TOP_HORN, MOON_RIGHT_HORN, radius_x=MOON_R, large_arc=True, sweep=False)
        self.add_arc("moon-inner", MOON_RIGHT_HORN, MOON_TOP_HORN, radius_x=MOON_R, sweep=True)
        self.add_contour("moon", "moon-outer", "moon-inner", closed=True)

        # Wind: the upper stroke ends in a half-turn up; the lower is plain.
        self.add_line("wind-upper-run", (WIND_LEFT, WIND_UPPER_Y), (CURL_X, WIND_UPPER_Y))
        self.add_arc("wind-upper-curl", (CURL_X, WIND_UPPER_Y), (CURL_X, WIND_UPPER_Y - 2 * CURL_R),
                     radius_x=CURL_R, sweep=False)
        self.add_contour("wind-upper", "wind-upper-run", "wind-upper-curl")
        self.add_line("wind-lower", (WIND_LEFT, WIND_LOWER_Y), (WIND_LOWER_END, WIND_LOWER_Y))
