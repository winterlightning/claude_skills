"""angled-handlebar-road-bicycle (redraw of the new-pipeline traced SVG).

Plan: side-view road bicycle facing right on HRECT_L, centerline box
(4,8)-(44,40): rear rim x=4, front rim and drop x=44, saddle and bar y=8,
both wheels y=40.
- wheels: one r6 circle definition (four quarter arcs) at (10,34) and
  (38,34); 12 apart rim to rim, 8-unit ink holes. Frame joints use the
  cardinal points only, so every node stays on the integer grid.
- main triangle: seat cluster (16,14), head (33,13), bottom bracket (24,30)
  on the axis x=24, which puts the bracket 8.6 clear of both rims. Seat tube
  on the (-1,-2) line, fork on the (1,3) line; the down tube keeps 8.2 from
  the front rim. Centerline inradius 5.2, so the 6-unit hole holds (6.28).
- seat stay: seat cluster down to the rear rim's top (10,28); with the
  triangle it gives the diamond frame read. Fork: head to the front rim top.
- seat post continues the seat tube to (13,8); flat saddle (8,8)-(15,8).
- angled forward stem (33,13)->(36,8), short bar to (40,8), r4 quarter
  curve down to (44,12) and a short drop to (44,15), 9.8 clear of the fork.
- no hubs, no chainstay: at stroke 4 anything reaching a hub splits the
  wheel hole below 6, and a chainstay closed the rear triangle into a
  5.49-unit hole (measured), so the rear triangle is left open at the bottom.
Lucide `bike` informed the equal round wheels without hubs; the generated
PNG gave the diamond frame, angled stem and forward drop bar.

Metric issues (angled-handlebar-road-bicycle_metrics.json):
- clearance errors (wheels, frame quad, stays, fork, handlebar all fused in
  the trace): fixed -- touching parts share an integer endpoint and are
  declared `connect`; everything else keeps >= 8 on centerlines.
- holes 3.4 / 3.22 / 3.4 inscribed: fixed -- main triangle 6.28, wheels 7.87.
- keyshape-short-axis (HRECT_M, y filled 68%): switched to HRECT_L and
  filled all four sides. HRECT_M's 28 height cannot hold a 12-unit wheel plus
  a frame triangle with a 6-unit hole and the saddle above it.
- stroke-width (trace 2.66): redrawn at stroke 4 with gaps budgeted for it.
- stroke-count (trace 6): 2 wheels, frame, seat stay, fork, seat post +
  saddle, handlebar -- 7 parts, all joined into one shape.
Not kept: the curl of the drop bar back toward the stem; any return past the
vertical drop comes within 8 of the fork.
Re-running svg_metrics on the redraw still flags two frame wedges (seat
tube / seat stay 6.84 and down tube / fork 6.39, measured 8 past the apex)
and the saddle nose 6.08 from the seat cluster (joined through the 6.7-long
seat post, which the metric does not follow). These are frame joints;
widening the wedges would push the bracket or head inside 8 of a rim.
validate_icon() is valid with no warnings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7eea5c25-9b41-4dec-ba5e-91b557120a37"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1716-angled-handlebar-road-bicycle/"
    "angled-handlebar-road-bicycle_raw.svg"
)
AUTHOR = "claude-opus-5-5"

R = 6                          # wheel radius (both wheels)
WHEEL_Y = 34
REAR_X, FRONT_X = 10, 38
REAR_TOP = (REAR_X, WHEEL_Y - R)          # (10,28) seat-stay joint
FRONT_TOP = (FRONT_X, WHEEL_Y - R)        # (38,28) fork joint
BRACKET = (24, 30)                        # bottom bracket, on the axis x=24
SEAT = (16, 14)                           # seat cluster, BRACKET + 8*(-1,-2)
HEAD = (33, 13)                           # head, FRONT_TOP - 5*(1,3)
POST_TOP = (13, 8)                        # SEAT + 3*(-1,-2), seat tube line
SADDLE = ((8, 8), (15, 8))
STEM_TOP = (36, 8)                        # angled forward stem
BAR_END = (40, 8)
DROP_R = 4
DROP_KNEE = (BAR_END[0] + DROP_R, BAR_END[1] + DROP_R)   # (44,12)
DROP_END = (44, 15)


class AngledHandlebarRoadBicycleRedraw(Solo48):
    icon_id = "angled-handlebar-road-bicycle-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ("road bike", "racing bicycle", "drop bar bike")
    keywords = ("bicycle", "bike", "road bike", "racing", "cycling", "drop handlebar", "transport")

    def _wheel(self, name: str, cx: int, cy: int) -> None:
        """Circle as four clockwise quarter arcs meeting at the cardinals."""
        top, right, bottom, left = (cx, cy - R), (cx + R, cy), (cx, cy + R), (cx - R, cy)
        self.add_arc(f"{name}-1", top, right, radius_x=R, sweep=True)
        self.add_arc(f"{name}-2", right, bottom, radius_x=R, sweep=True)
        self.add_arc(f"{name}-3", bottom, left, radius_x=R, sweep=True)
        self.add_arc(f"{name}-4", left, top, radius_x=R, sweep=True)
        self.add_contour(name, f"{name}-1", f"{name}-2", f"{name}-3", f"{name}-4", closed=True)

    def build(self) -> None:
        self._wheel("rear-wheel", REAR_X, WHEEL_Y)
        self._wheel("front-wheel", FRONT_X, WHEEL_Y)

        # Main triangle: top tube, down tube, seat tube.
        self.add_polyline("main-triangle", SEAT, HEAD, BRACKET, closed=True)

        # Seat stay lands on the rear rim's top cardinal.
        self.add_line("seat-stay", SEAT, REAR_TOP)
        self.relate("connect", "seat-stay", "main-triangle")
        self.relate("connect", "seat-stay", "rear-wheel")

        # Fork from the head to the front wheel's top.
        self.add_line("fork", HEAD, FRONT_TOP)
        self.relate("connect", "fork", "main-triangle")
        self.relate("connect", "fork", "front-wheel")

        # Seat post on the seat-tube line, saddle on top.
        self.add_line("seat-post", SEAT, POST_TOP)
        self.add_line("saddle-rear", SADDLE[0], POST_TOP)
        self.add_line("saddle-nose", POST_TOP, SADDLE[1])
        self.add_contour("saddle", "saddle-rear", "saddle-nose")
        self.relate("connect", "seat-post", "main-triangle")
        self.relate("connect", "seat-post", "seat-stay")
        self.relate("connect", "seat-post", "saddle")

        # Angled stem, flat bar, drop curving down at the front.
        self.add_line("stem", HEAD, STEM_TOP)
        self.add_line("bar", STEM_TOP, BAR_END)
        self.add_arc("drop-curve", BAR_END, DROP_KNEE, radius_x=DROP_R, sweep=True)
        self.add_line("drop", DROP_KNEE, DROP_END)
        self.add_contour("handlebar", "stem", "bar", "drop-curve", "drop")
        self.relate("connect", "handlebar", "main-triangle")
        self.relate("connect", "handlebar", "fork")
