"""capped-glue-stick (redraw of the new-pipeline traced SVG).

Plan: an upright glue stick on VRECT_M (centerline box (10,4)-(38,44)),
mirrored about x=24.
- cap: a closed shape (10,4)-(38,18) with radius-4 top corners and a square
  rim, owning the x=10 / x=38 / y=4 extremes. Its rim is split at x=14 and
  x=34 where the tube hangs from it.
- tube: an open U, walls x=14 / x=34 (20 wide, 4 inside the cap so the cap
  reads as a separate, broader part) with radius-4 bottom corners on y=44.
- twist-base band: one line across the tube at y=34, leaving a 10-unit band.
A first try with cap and tube the same width (full 28) read as a phone or
cabinet at 48 px; the stepped cap keeps it a glue stick.
Metric issues:
- hole at [20.3,41.4] (base band 1.2 wide): the band is now 10 between
  centerlines (6 inscribed at stroke 4). Fixed.
- keyshape-short-axis (VRECT_M x fill 46%): the cap is widened to the full
  28-unit short axis so x=10 and x=38 are exact. Fixed by widening; the
  narrowest SOLO48 keyshape cannot keep the trace's 0.32 aspect, so the
  stick is stubbier than the trace.
- stroke-width (trace 2.61): drawn at stroke 4; every gap is at least 8 on
  centerlines. Fixed.
Lucide construction: no glue-stick original; the rounded-cap-over-tube build
follows Lucide's `pill-bottle` (broad cap, narrower body, straight band).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6640054a-f461-4b24-bad8-f2a7fd52f7fb"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1924-capped-glue-stick/capped-glue-stick_raw.svg"
AUTHOR = "claude-opus-5-5"

L, R, T, B = 10, 38, 4, 44   # centerline box; the cap owns x=10/38 and y=4
TL, TR = 14, 34              # tube walls, 4 inside the cap
RAD = 4                      # cap and tube corner radius
CAP_Y = 18                   # cap rim
BASE_Y = 34                  # twist-base band


class CappedGlueStickRedraw(Solo48):
    icon_id = "capped-glue-stick-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/stationery"
    aliases = ("glue stick", "glue", "adhesive stick")
    keywords = ("glue", "stick", "adhesive", "paste", "craft", "school", "office", "stationery")

    def build(self) -> None:
        # Cap: rounded top, square rim, clockwise from the top edge. The rim
        # is split where the tube walls hang from it.
        self.add_line("cap-top", (L + RAD, T), (R - RAD, T))
        self.add_arc("cap-tr", (R - RAD, T), (R, T + RAD), radius_x=RAD, sweep=True)
        self.add_line("cap-right", (R, T + RAD), (R, CAP_Y))
        self.add_line("rim-r", (R, CAP_Y), (TR, CAP_Y))
        self.add_line("rim-mid", (TR, CAP_Y), (TL, CAP_Y))
        self.add_line("rim-l", (TL, CAP_Y), (L, CAP_Y))
        self.add_line("cap-left", (L, CAP_Y), (L, T + RAD))
        self.add_arc("cap-tl", (L, T + RAD), (L + RAD, T), radius_x=RAD, sweep=True)
        self.add_contour("cap", "cap-top", "cap-tr", "cap-right", "rim-r", "rim-mid",
                         "rim-l", "cap-left", "cap-tl", closed=True)

        # Tube: open U from the right rim knot down, round bottom, back up.
        self.add_line("tube-right", (TR, CAP_Y), (TR, BASE_Y))
        self.add_line("base-right", (TR, BASE_Y), (TR, B - RAD))
        self.add_arc("tube-br", (TR, B - RAD), (TR - RAD, B), radius_x=RAD, sweep=True)
        self.add_line("tube-bottom", (TR - RAD, B), (TL + RAD, B))
        self.add_arc("tube-bl", (TL + RAD, B), (TL, B - RAD), radius_x=RAD, sweep=True)
        self.add_line("base-left", (TL, B - RAD), (TL, BASE_Y))
        self.add_line("tube-left", (TL, BASE_Y), (TL, CAP_Y))
        self.add_contour("tube", "tube-right", "base-right", "tube-br", "tube-bottom",
                         "tube-bl", "base-left", "tube-left")
        self.relate("connect", "tube", "cap")

        self.add_line("base-band", (TL, BASE_Y), (TR, BASE_Y))
        self.relate("connect", "base-band", "tube")
