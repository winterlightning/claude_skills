"""inward-arrow-with-curved-and-dashed-bounds (redraw of the new-pipeline traced SVG).

Plan: SQUARE, centerline box (6,6)-(42,42); a right-pointing arrow enters a
D-shaped bound through a dashed left side (Lucide `log-in` read, with the
square bracket replaced by a semicircle).
- bound: one open contour, a short top lead (22,6)->(24,6), a
  semicircle r18 about (24,24) through the right extreme (42,24), and the
  mirrored bottom lead. The leads are tangent to the arc, so the D is smooth.
- dashes: two vertical strokes at x=13, y 6..14 and 34..42, mirrored
  about y=24; they are the left side of the bound with a 20-long opening.
- arrow: shaft (6,24)->(30,24) and two 45-degree chevron arms to (22,16) and
  (22,32), all three sharing the tip (declared connect). The tip sits 12
  inside the arc; the head of 8 follows Lucide's arrow proportions.
Extremes: left 6 (arrow tail), right 42 (arc apex), top 6 / bottom 42
(leads and dashes).
Metric issues fixed:
- clearance e0/e1 and e1/e5 (dash 5.16 from the bound): the leads now start
  9 right of the dashes on the same level line (9, not 8: an exact 8 to the
  arc-owning contour comes back as a review warning).
- keyshape-short-axis (x filled 87%): the arrow tail is extended to x=6 and
  the arc apex sits at x=42, so all four extremes lie on the SQUARE box.
- stroke-width (2.4 traced): authored at stroke 4 with every gap budgeted at
  8 on centerlines (dash to shaft 10, chevron to dashes 9.2, tip to arc 12).
Not fixable (metrics-script artifact, not a defect):
- svg_metrics on the redraw flags shaft vs each chevron arm at 6.25 apart.
  It discards samples within 8 of the shared tip and then measures the rest
  of the 45-degree wedge, which is never 8 wide there for any arrowhead; the
  trace escaped only because its arms were shorter than 8. The parts share
  the tip and validate_icon() certifies the joint.
Lucide: `log-in` (arrow with chevron entering an open bound) for the arrow
proportions and the lead-in of the bound.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7e004778-d88c-4db0-9a9c-c9364d42ee86"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1513-inward-arrow-with-curved-and-dashed-bounds/"
    "inward-arrow-with-curved-and-dashed-bounds_raw.svg"
)
AUTHOR = "claude-opus-5-5"

TOP, BOT, CY = 6, 42, 24
# Bound: semicircle about (ARC_CX, CY); its apex is the keyshape right edge.
ARC_CX, ARC_R = 24, 18
# Dashes: the left side of the bound; the leads start 9 to their right
# (an exact 8 across a curve-owning contour is only certified as review).
DASH_X, DASH_LEN = 13, 8
LEAD_X = DASH_X + 9
# Arrow: tail on the keyshape left edge, 45-degree chevron of 8, so each arm end clears the shaft by 8.
TAIL_X, TIP_X, HEAD = 6, 30, 8


class InwardArrowWithCurvedAndDashedBoundsRedraw(Solo48):
    icon_id = "inward-arrow-with-curved-and-dashed-bounds-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    aliases = ("transform inside", "move inside", "enter bounds")
    keywords = ("transform", "inside", "arrow", "inward", "enter", "bounds", "dashed")

    def build(self) -> None:
        # -- bound: top lead, semicircle, bottom lead ------------------------
        self.add_line("lead-top", (LEAD_X, TOP), (ARC_CX, TOP))
        self.add_arc("arc", (ARC_CX, TOP), (ARC_CX, BOT), radius_x=ARC_R)
        self.add_line("lead-bot", (ARC_CX, BOT), (LEAD_X, BOT))
        self.add_contour("bound", "lead-top", "arc", "lead-bot")

        # -- dashed left side, mirrored about CY -----------------------------
        self.add_line("dash-top", (DASH_X, TOP), (DASH_X, TOP + DASH_LEN))
        self.add_line("dash-bot", (DASH_X, BOT - DASH_LEN), (DASH_X, BOT))

        # -- arrow ------------------------------------------------------------
        self.add_line("shaft", (TAIL_X, CY), (TIP_X, CY))
        # Both chevron arms start at the tip the shaft ends on.
        self.add_line("head-top", (TIP_X, CY), (TIP_X - HEAD, CY - HEAD))
        self.add_line("head-bot", (TIP_X, CY), (TIP_X - HEAD, CY + HEAD))
        self.relate("connect", "shaft", "head-top")
        self.relate("connect", "shaft", "head-bot")
        self.relate("connect", "head-top", "head-bot")
