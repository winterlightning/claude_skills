"""counterclockwise-circular-arrow (redraw of the new-pipeline traced SVG).

Plan: a rotate / undo arrow on CIRCLE (centerline radius 20 about (24,24)),
the keyshape the metrics suggested for this round subject.
- ring: one open contour, a radius-17 circle about (24,27), drawn as four
  quarter-or-less arcs from the tail (9,19) (28 degrees above the left
  horizontal, the generated image's upper-left opening) down through the left,
  bottom and right points to the top (24,10), then a short tangent lead
  (24,10) -> (LEAD_X,10) to the arrow apex, as in the image where the head
  sits a little left of the ring top.
- arrowhead: an open V polyline whose apex is the lead end, arms at 45 degrees
  above and below the horizontal travel so the head points left
  (counterclockwise). The apex is a shared endpoint declared with
  relate("connect").
- extremes: the ring bottom (24,44) is exactly radius 20 from (24,24); the
  outer arm tip stays inside radius 20. The ring centre is shifted three units
  down so the head, which must stick out above the ring, still fits the
  circle, the same balance as the generated image.
Lucide `rotate-ccw` informed the idea (a near-full arc with the head at its
upper end); its square-corner head at the left does not match the image, so
the head here is the image's V at the ring top.

Metric issues (counterclockwise-circular-arrow-batch-019-08_metrics.json):
- stroke-width (info, trace 2.67 after fitting): redrawn at stroke 4; the only
  tight spot is the tail-to-head opening, kept well over 8 on centerlines.
- loose-join (info, e0 ends 1.14 short of e1): the ring now ends exactly at
  the arrow apex, a shared endpoint declared with relate("connect").
No errors or warnings were listed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "567f7df5-55ba-4b86-8f69-4c5a4f43e848"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1047-counterclockwise-circular-arrow-batch-019-08/counterclockwise-circular-arrow-batch-019-08_raw.svg"
AUTHOR = "claude-opus-5-5"

CX, CY = 24, 27                 # ring centre, three units below the canvas centre
R = 17                          # ring radius
TAIL = (CX - 15, CY - 8)        # (9,19), on the ring (8-15-17)
TOP = (CX, CY - R)              # (24,10)
LEAD_X = 21                     # arrow apex x, the head sits left of the ring top
ARM = 5                         # arm run and rise (45 degree arms)
APEX = (LEAD_X, TOP[1])
ARM_OUT = (LEAD_X + ARM, TOP[1] - ARM)
ARM_IN = (LEAD_X + ARM, TOP[1] + ARM)


class CounterclockwiseCircularArrowBatch01908Redraw(Solo48):
    icon_id = "counterclockwise-circular-arrow-batch-019-08-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "arrows/rotate"
    aliases = ("rotate counterclockwise", "undo", "rotate left", "refresh")
    keywords = ("arrow", "circular", "counterclockwise", "anticlockwise", "rotate",
                "undo", "reset", "reload", "refresh", "back")

    def build(self) -> None:
        left, bottom, right = (CX - R, CY), (CX, CY + R), (CX + R, CY)
        self.add_arc("ring-0", TAIL, left, radius_x=R, sweep=False)
        self.add_arc("ring-1", left, bottom, radius_x=R, sweep=False)
        self.add_arc("ring-2", bottom, right, radius_x=R, sweep=False)
        self.add_arc("ring-3", right, TOP, radius_x=R, sweep=False)
        members = ["ring-0", "ring-1", "ring-2", "ring-3"]
        if LEAD_X != TOP[0]:
            self.add_line("ring-4", TOP, APEX)
            members.append("ring-4")
        self.add_contour("ring", *members)

        self.add_polyline("head", ARM_OUT, APEX, ARM_IN)
        self.relate("connect", "head", "ring")
