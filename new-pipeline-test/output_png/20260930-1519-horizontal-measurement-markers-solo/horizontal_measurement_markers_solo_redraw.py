"""horizontal-measurement-markers (redraw of the new-pipeline traced SVG).

Plan: a width dimension on HRECT_M (centerline box (4,10)-(44,38)), mirrored
about x=24 and y=24.
- end markers: two vertical lines at x=4 and x=44 running the full box height
  (y 10..38); they are all four keyshape extremes.
- arrow: one repeat definition (open chevron head + half shaft) mirrored
  through x=24. Tips at x=12 and x=36, exactly GAP=8 on centerlines from the
  markers; 45 degree chevron arms 6 on each axis (Lucide proportion) share the tip node with the shaft.
Reference: Lucide `move-horizontal` (shaft + open 45 degree chevrons) and the
generated PNG for the free markers at both ends.

Metric issues:
- clearance e0/e2, e0/e3, e0/e5, e1/e2, e1/e4, e1/e6 (3.92-3.97): fixed, the
  arrow tips now stop 8 from each marker (4 of white between inks).
- keyshape-short-axis (y fill 47%): fixed, the markers span y 10..38 so the
  box is reached exactly; the arrow stays centred at y=24.
- stroke-count (7, budget 6): fixed, the trace's two degenerate tip loops
  (e5, e6) are dropped; 5 strokes: 2 markers, shaft, 2 chevrons.
- stroke-width info: redrawn at stroke 4 with every gap budgeted at 8.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5e331499-062d-4a4a-965e-e100d55ce756"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1519-horizontal-measurement-markers-solo/horizontal-measurement-markers-solo_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS_X, AXIS_Y = 24, 24
LEFT = 4          # left marker; the right one mirrors it at 44
TOP, BOTTOM = 10, 38
GAP = 8           # marker to arrow tip, on centerlines
HEAD = 6          # chevron arm run and rise (45 degrees)


def mirror(p):
    return (2 * AXIS_X - p[0], p[1])


class HorizontalMeasurementMarkersSoloRedraw(Solo48):
    icon_id = "horizontal-measurement-markers-solo-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "editing/measurement"
    aliases = ("horizontal-measurement-markers", "width dimension", "measure width")
    keywords = ("measure", "measurement", "width", "dimension", "distance", "span", "arrow", "ruler")

    def build(self) -> None:
        self.add_line("marker-l", (LEFT, BOTTOM), (LEFT, TOP))
        self.add_line("marker-r", mirror((LEFT, TOP)), mirror((LEFT, BOTTOM)))

        tip = (LEFT + GAP, AXIS_Y)
        self.add_line("shaft", tip, mirror(tip))
        arm_top = (tip[0] + HEAD, AXIS_Y - HEAD)
        arm_bot = (tip[0] + HEAD, AXIS_Y + HEAD)
        self.add_polyline("head-l", arm_top, tip, arm_bot)
        self.add_polyline("head-r", mirror(arm_top), mirror(tip), mirror(arm_bot))
        for side in ("l", "r"):
            for leg in ("1", "2"):
                self.relate("connect", f"head-{side}-{leg}", "shaft")
