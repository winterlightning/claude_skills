"""clock-with-counterclockwise-arrival-arrow (redraw of the new-pipeline traced SVG).

Plan: a history / rewind clock on CIRCLE (centerline radius 20 about (24,24)),
the keyshape the metrics suggested for this round subject.
- rim: one open contour, a radius-17 circle about (25,25), drawn as four
  quarter-or-less arcs from the left point (8,25) down through the bottom,
  right and top to the arrow apex (10,17), 28 degrees above the left
  horizontal, like the opening in the generated image.
- arrowhead: an open V polyline (8,12) -> (10,17) -> (15,16) whose apex is the
  rim end, so the head is a shared endpoint declared with relate("connect").
  Both arms are ~5.2 long at ~50 degrees either side of the backwards rim
  tangent, so the head points down along the counterclockwise travel.
- hands: one L polyline (25,17) -> (25,25) -> (33,25) at the rim centre,
  both hands 8 long, 9 clear of the rim (a curved pair cannot certify exactly 8).
- extremes: the outer arrow arm tip (8,12) is exactly radius 20 from (24,24);
  the rim reaches 17 + sqrt(2) = 18.4. The rim is shifted one unit right and
  down so the head, which must stick out of the rim, still fits the circle.
  The generated image has the same balance: its head pokes out at the left.
Lucide `history` informed the construction (arc + arrowhead at the upper-left
end + L hands at the centre); its square-corner head at (3,3) does not fit a
CIRCLE keyshape, so the head here is a V on the arc end as in the image.

Metric issues (clock-with-counterclockwise-arrival-arrow_metrics.json):
- stroke-width (info, trace 2.69 after fitting): redrawn at stroke 4. The only
  measured clearance that shrinks, rim/minute hand (8.03 in the trace, an ink
  gap under 4 once the stroke is 4), is now 9 on centerlines (hand tip (25,17)
  to rim top (25,8)); the head to hand clearance is 10.
No errors or warnings were listed. The e0/e1 t-junction of the trace (the head
joined part way along its own V) is rebuilt as a clean shared endpoint at the
apex.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7420a5ad-20b8-4125-a020-7f6c31b74aac"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1930-clock-with-counterclockwise-arrival-arrow/clock-with-counterclockwise-arrival-arrow_raw.svg"
AUTHOR = "claude-opus-5-5"

CX, CY = 25, 25                 # rim centre, one unit right/down of the canvas centre
R = 17                          # rim radius
RIM_START = (CX - R, CY)        # left point, lower end of the opening
APEX = (10, 17)                 # rim end: (CX-15, CY-8), on the rim (15-8-17)
ARM_OUT = (8, 12)               # outer arm tip, exactly radius 20 from (24,24)
ARM_IN = (15, 16)               # inner arm tip
MINUTE = (CX, 17)               # minute hand tip, 9 below the rim top
HOUR = (33, CY)                 # hour hand tip


class ClockWithCounterclockwiseArrivalArrowRedraw(Solo48):
    icon_id = "clock-with-counterclockwise-arrival-arrow-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "time/clock"
    aliases = ("history", "clock rewind", "time back", "arrival time")
    keywords = ("clock", "history", "counterclockwise", "rewind", "undo", "arrival",
                "eta", "time", "past", "recent")

    def build(self) -> None:
        bottom, right, top = (CX, CY + R), (CX + R, CY), (CX, CY - R)
        self.add_arc("rim-0", RIM_START, bottom, radius_x=R, sweep=False)
        self.add_arc("rim-1", bottom, right, radius_x=R, sweep=False)
        self.add_arc("rim-2", right, top, radius_x=R, sweep=False)
        self.add_arc("rim-3", top, APEX, radius_x=R, sweep=False)
        self.add_contour("rim", "rim-0", "rim-1", "rim-2", "rim-3")

        self.add_polyline("head", ARM_OUT, APEX, ARM_IN)
        self.relate("connect", "head", "rim")

        self.add_polyline("hands", MINUTE, (CX, CY), HOUR)
