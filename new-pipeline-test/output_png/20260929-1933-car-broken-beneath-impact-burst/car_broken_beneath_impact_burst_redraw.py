"""car-broken-beneath-impact-burst (redraw of the new-pipeline traced SVG).

Plan: a front-facing car with a dented roof under an open three-point impact
burst, on SQUARE (centerline box (6,6)-(42,42)), the keyshape the metrics
suggested (fill 1.0 x 1.0, matches the square shape hint). Everything is
mirrored about x = 24.
- burst: one open polyline end -> tip -> valley -> apex -> valley -> tip -> end.
  Apex (24,6) is the top extreme; tips (6,7)/(42,7) touch the side extremes
  as ~40 degree spikes; valleys (20,12)/(28,12) give the apex a ~67 degree
  spike; the ends (10,14)/(38,14) hang down 45-60 degrees inward outside the
  roof (8.5 from the roof corner) so they can sit lower than the valleys.
- cabin: one open polyline from pillar foot (12,31) up to the roof corner
  (16,20), a short shoulder to (18,20), the dent V down to (24,24) and back
  up to (30,20), shoulder to (32,20) and the right pillar down to (36,31).
  The pillar feet are shared endpoints on the body top (the beltline), which
  is split there, and declared with relate("connect").
- body: one closed contour, beltline y = 31, bottom y = 39 (8 on centerlines),
  flared top corners (chamfer (9,31)->(6,34)), r = 2 bottom corners and two
  wheel tabs folded into the outline (walls x = 9..17 and 31..39, 8 apart,
  r = 2 corners) hanging to y = 42, the bottom extreme. Side extremes are the
  body walls x = 6 / 42.
Vertical budget: burst 6..13, >= 8 gap, roof 20, dent 4 deep, 7 above the
beltline, body 8, wheels 3 = 36.
No useful Lucide match for a crash scene; Lucide `car-front` informed the
body-with-flared-shoulders + short wheels below the body construction.

Metric issues (car-broken-beneath-impact-burst_metrics.json):
- stroke-width (info, 2.77 fitted): redrawn at stroke 4 with every gap
  re-budgeted for 4.
- clearance e0/e3 3.13 (burst end over the roof): fixed; the burst ends now
  hang outside the roof, 8.5 from the roof corner, and the valleys are 8.25
  from the dent corner, their nearest roof point.
- clearance e2/e3 4.42 (dent apex over the beltline): fixed; dent apex is 7
  above the beltline and its arms are 34 degrees off parallel to it, so no
  parallel-run crowding; the separate cabin-bottom line is merged into the
  body top.
- hole at [14.1,24.0] 3.8 wide (sliver between cabin corner and body flare):
  fixed; the cabin pillars stand directly on the beltline, no sliver remains.
- hole at [10.7,32.5] 5.4 wide (body interior): fixed; body is 8 tall on
  centerlines with the wheels folded into its outline.
- holes at [11.4,39.6] / [35.4,39.6] 0.8 wide (wheel-body slivers): fixed;
  the wheels are open tabs of the body contour, not closed U shapes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "757187c1-fd16-4577-8bb6-b25ad4df2330"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1933-car-broken-beneath-impact-burst/car-broken-beneath-impact-burst_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24


def mx(x: int) -> int:
    return 2 * AXIS - x


# burst (left half; mirrored)
BURST_END = (10, 14)
BURST_TIP = (6, 7)
BURST_VALLEY = (20, 12)
BURST_APEX = (AXIS, 6)

# cabin
PILLAR_FOOT = (12, 31)
ROOF_CORNER = (16, 20)
DENT_START = (18, 20)
DENT_APEX = (AXIS, 24)

# body
BELT_Y, BOTTOM_Y = 31, 39
FLARE = (9, BELT_Y)                 # beltline end, top of the chamfer
SIDE_X, SIDE_TOP = 6, 34            # wall and chamfer foot
CORNER_R = 2
WHEEL_X0, WHEEL_X1 = 9, 17          # left wheel walls (8 apart)
WHEEL_Y = 42                        # wheel bottom
WHEEL_R = 2                         # wheel corner radius


class CarBrokenBeneathImpactBurstRedraw(Solo48):
    icon_id = "car-broken-beneath-impact-burst-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/car"
    aliases = ("car crash", "car accident", "vehicle collision", "dented car")
    keywords = ("car", "crash", "accident", "collision", "impact", "dent",
                "broken", "damage", "insurance", "vehicle")

    def build(self) -> None:
        m = lambda p: (mx(p[0]), p[1])

        self.add_polyline(
            "burst", BURST_END, BURST_TIP, BURST_VALLEY, BURST_APEX,
            m(BURST_VALLEY), m(BURST_TIP), m(BURST_END),
        )

        self.add_polyline(
            "cabin", PILLAR_FOOT, ROOF_CORNER, DENT_START, DENT_APEX,
            m(DENT_START), m(ROOF_CORNER), m(PILLAR_FOOT),
        )

        r, wr = CORNER_R, WHEEL_R
        corner_top = BOTTOM_Y - r
        w0, w1, wy = WHEEL_X0, WHEEL_X1, WHEEL_Y
        members = []

        def line(a, b):
            name = f"body-{len(members) + 1}"
            self.add_line(name, a, b)
            members.append(name)

        def arc(a, b, radius):
            name = f"body-{len(members) + 1}"
            self.add_arc(name, a, b, radius_x=radius, sweep=True)
            members.append(name)

        def wheel(x_start, x_end):
            # clockwise: down the first wall, along the bottom, up the second
            step = 1 if x_end > x_start else -1
            line((x_start, BOTTOM_Y), (x_start, wy - wr))
            arc((x_start, wy - wr), (x_start + step * wr, wy), wr)
            line((x_start + step * wr, wy), (x_end - step * wr, wy))
            arc((x_end - step * wr, wy), (x_end, wy - wr), wr)
            line((x_end, wy - wr), (x_end, BOTTOM_Y))

        line(FLARE, PILLAR_FOOT)
        line(PILLAR_FOOT, m(PILLAR_FOOT))
        line(m(PILLAR_FOOT), m(FLARE))
        line(m(FLARE), (mx(SIDE_X), SIDE_TOP))
        line((mx(SIDE_X), SIDE_TOP), (mx(SIDE_X), corner_top))
        arc((mx(SIDE_X), corner_top), (mx(SIDE_X + r), BOTTOM_Y), r)
        line((mx(SIDE_X + r), BOTTOM_Y), (mx(w0), BOTTOM_Y))
        wheel(mx(w0), mx(w1))
        line((mx(w1), BOTTOM_Y), (w1, BOTTOM_Y))
        wheel(w1, w0)
        line((w0, BOTTOM_Y), (SIDE_X + r, BOTTOM_Y))
        arc((SIDE_X + r, BOTTOM_Y), (SIDE_X, corner_top), r)
        line((SIDE_X, corner_top), (SIDE_X, SIDE_TOP))
        line((SIDE_X, SIDE_TOP), FLARE)
        self.add_contour("body", *members, closed=True)

        self.relate("connect", "cabin", "body")
