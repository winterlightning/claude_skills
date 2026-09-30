"""horizontal ruler with five top ticks (redraw of the new-pipeline traced SVG).

Plan: a flat horizontal ruler on HRECT_M (centerline box (4,10)-(44,38)).
- body: one closed rounded rectangle, corner radius 3, on all four extremes
  (x=4, x=44, y=10, y=38); its top edge is split at every tick x so each
  graduation shares a node with the body (declared connect).
- graduations: a repeat series hanging from the top edge on an 8-unit pitch,
  x = 12, 20, 28, 36, alternating long (to y=26) / short (to y=19). Long
  ticks stop 12 above the bottom wall; short ticks show 7 units of ink below
  the top wall so they still read at 48 px.
Construction follows Lucide `ruler` (rounded body, ticks from one long edge),
kept horizontal as in the trace.

Metric issues:
- clearance e1/e4, e1/e5, e2/e4, e3/e5 (ticks 7.7 apart): fixed by an exact
  8-unit tick pitch. Cannot keep five ticks: every tick must also sit 8 from
  the side walls, so the 40-unit centerline width holds at most four
  (x = 12..36); five would need 48. Reduced five -> four, keeping the
  long/short alternation (the trace's end ticks at 4.5 from the walls were
  the ones that could not survive).
- keyshape-short-axis (y filled 47%): fixed by drawing the body to the full
  HRECT_M height (y 10..38) instead of stretching the trace; the ruler is
  stockier (40x28 centerlines) than the 3:1 trace, which the keyshape's
  tolerance-0 extremes require.
- stroke-width (trace 2.65 vs 4): redrawn at stroke 4; all gaps measured at 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8e5cf0f4-16ef-55be-9abb-2b6fd8017da3"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1522-horizontal-ruler-with-five-top-ticks/horizontal-ruler-with-five-top-ticks_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT, RIGHT, TOP, BOTTOM = 4, 44, 10, 38   # HRECT_M centerline box
R = 3                                      # corner radius
LONG_END, SHORT_END = 26, 19               # tick bottoms (top edge at y=10)
# (x, bottom) per graduation; 8 apart and 8 in from the side walls.
TICKS = ((12, LONG_END), (20, SHORT_END), (28, LONG_END), (36, SHORT_END))


class HorizontalRulerWithFiveTopTicksRedraw(Solo48):
    icon_id = "horizontal-ruler-with-five-top-ticks-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ("ruler", "straightedge", "measuring ruler")
    keywords = ("ruler", "measure", "measurement", "length", "scale", "ticks", "graduations", "design")

    def build(self) -> None:
        # Top edge split at every tick so each tick shares a node with it.
        xs = [LEFT + R] + [x for x, _ in TICKS] + [RIGHT - R]
        top = []
        for i, (a, b) in enumerate(zip(xs, xs[1:]), 1):
            self.add_line(f"top-{i}", (a, TOP), (b, TOP))
            top.append(f"top-{i}")
        self.add_arc("corner-tr", (RIGHT - R, TOP), (RIGHT, TOP + R), radius_x=R)
        self.add_line("right", (RIGHT, TOP + R), (RIGHT, BOTTOM - R))
        self.add_arc("corner-br", (RIGHT, BOTTOM - R), (RIGHT - R, BOTTOM), radius_x=R)
        self.add_line("bottom", (RIGHT - R, BOTTOM), (LEFT + R, BOTTOM))
        self.add_arc("corner-bl", (LEFT + R, BOTTOM), (LEFT, BOTTOM - R), radius_x=R)
        self.add_line("left", (LEFT, BOTTOM - R), (LEFT, TOP + R))
        self.add_arc("corner-tl", (LEFT, TOP + R), (LEFT + R, TOP), radius_x=R)
        self.add_contour("body", *top, "corner-tr", "right", "corner-br", "bottom",
                         "corner-bl", "left", "corner-tl", closed=True)

        for i, (x, end) in enumerate(TICKS, 1):
            self.add_line(f"tick-{i}", (x, TOP), (x, end))
            self.relate("connect", f"tick-{i}", "body")
