"""flying blimp airship (redraw of the new-pipeline traced SVG).

Plan: side view of a blimp flying right on HRECT_M (centerline box
(4,10)-(44,38)), mirrored top/bottom about the envelope axis y=AXIS_Y except
for the gondola. The envelope fills y 10..28 so the fins stay inside its
height and the gondola takes the remaining 10 units down to y=38.
- envelope + tail: ONE closed silhouette. Nose = two quarter arcs r=NOSE_R
  about (NOSE_CX, AXIS_Y), apex on the x=44 extreme; flat top/bottom runs;
  a short cubic taper at the rear flows into the leading edge of each fin.
- fins: leading edge up/down-left from the taper, flat tip edge on the
  y=10 extreme reaching the x=4 extreme, trailing edge back into the tail
  point T, so the fins are part of the outline rather than separate shapes.
- gondola: rounded U (corner r=3) whose walls hang from the two ends of the
  flat bottom run (taper join and nose join); its bottom is the y=38
  extreme; it shares both endpoints with the envelope.

Metric issues:
- clearance e1/e2 3.67 apart at the tail (fixed): the trace drew each fin as
  its own loop touching the envelope tail; merging fins into the envelope
  outline removes the fin/tail pair entirely.
- hole 0.63 wide at [7.3, 17.5] (fixed): the sliver between fin and tail no
  longer exists; the only holes are the envelope interior and the gondola
  (11x10 on centerlines = 6 inscribed ink).
- keyshape short axis at 66% (fixed): envelope top and fin tips on y=10 and the gondola
  dropped to y=38, so every HRECT_M extreme is touched exactly.
- stroke width 2.63 vs 4 (fixed by construction): redrawn at stroke 4 with
  gaps budgeted at 8 on centerlines.
No useful Lucide match (Lucide has no blimp/airship).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "94ee19fa-6c64-4340-9c2b-4d23bc7e3842"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1201-flying-blimp-airship-batch-033/flying-blimp-airship-batch-033_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS_Y = 19
HALF_H = 9                       # envelope runs y 10..28
TOP, BOTTOM = AXIS_Y - HALF_H, AXIS_Y + HALF_H
NOSE_RX, NOSE_RY = 12, HALF_H    # elliptical nose
NOSE_CX = 44 - NOSE_RX           # nose apex on x=44
REAR_X = 21                      # where the flat runs start to taper
ROOT = (15, 14)                  # upper fin root on the taper
FIN_TIP_IN = (10, 10)            # fin tip edge on y=10
FIN_TIP_OUT = (4, 10)            # ... reaching x=4
TAIL = (6, AXIS_Y)               # shallow notch: fins, not a fish tail
GONDOLA_X = (REAR_X, NOSE_CX)    # walls at the taper and nose joins
GONDOLA_BOTTOM = 38
GONDOLA_R = 3


def my(p):
    return (p[0], 2 * AXIS_Y - p[1])


def my_seg(seg):
    return tuple(my(p) for p in seg)


# Upper taper from the fin root to the flat top run, horizontal at the run.
TAPER_UP = ((17, 12), (18.5, TOP), (REAR_X, TOP))


class FlyingBlimpAirshipRedraw(Solo48):
    icon_id = "flying-blimp-airship-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/aircraft"
    aliases = ("blimp", "airship", "dirigible", "zeppelin")
    keywords = ("blimp", "airship", "dirigible", "zeppelin", "flying", "aircraft", "balloon", "flight")

    def build(self) -> None:
        g0, g1 = GONDOLA_X
        nose_apex = (44, AXIS_Y)
        self.add_arc("nose-top", (NOSE_CX, TOP), nose_apex, radius_x=NOSE_RX, radius_y=NOSE_RY)
        self.add_arc("nose-bottom", nose_apex, (NOSE_CX, BOTTOM), radius_x=NOSE_RX, radius_y=NOSE_RY)
        self.add_line("bottom-mid", (g1, BOTTOM), (g0, BOTTOM))
        # Lower taper: the mirror of TAPER_UP, run backwards.
        c1, c2, _ = my_seg(TAPER_UP)
        self.add_bezier("taper-low", (REAR_X, BOTTOM), (c2, c1, my(ROOT)))
        self.add_polyline("fin-low", my(ROOT), my(FIN_TIP_IN), my(FIN_TIP_OUT), TAIL)
        self.add_polyline("fin-up", TAIL, FIN_TIP_OUT, FIN_TIP_IN, ROOT)
        self.add_bezier("taper-up", ROOT, TAPER_UP)
        self.add_line("top", (REAR_X, TOP), (NOSE_CX, TOP))
        members = ["nose-top", "nose-bottom", "bottom-mid",
                   "taper-low", "fin-low-1", "fin-low-2", "fin-low-3",
                   "fin-up-1", "fin-up-2", "fin-up-3", "taper-up", "top"]
        # add_polyline registered its own open contours; replace them with
        # one closed silhouette.
        self.contours = [c for c in self.contours if c.contour_id not in ("fin-low", "fin-up")]
        self.add_contour("envelope", *members, closed=True)

        r = GONDOLA_R
        self.add_line("gondola-rear", (g0, BOTTOM), (g0, GONDOLA_BOTTOM - r))
        self.add_arc("gondola-c1", (g0, GONDOLA_BOTTOM - r), (g0 + r, GONDOLA_BOTTOM),
                     radius_x=r, sweep=False)
        self.add_line("gondola-floor", (g0 + r, GONDOLA_BOTTOM), (g1 - r, GONDOLA_BOTTOM))
        self.add_arc("gondola-c2", (g1 - r, GONDOLA_BOTTOM), (g1, GONDOLA_BOTTOM - r),
                     radius_x=r, sweep=False)
        self.add_line("gondola-front", (g1, GONDOLA_BOTTOM - r), (g1, BOTTOM))
        self.add_contour("gondola", "gondola-rear", "gondola-c1", "gondola-floor",
                         "gondola-c2", "gondola-front")
        self.relate("connect", "gondola", "envelope")
