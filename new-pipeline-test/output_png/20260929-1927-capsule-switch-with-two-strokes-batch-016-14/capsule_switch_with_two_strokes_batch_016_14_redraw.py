"""capsule-switch-with-two-strokes (redraw of the new-pipeline traced SVG).

Plan: a horizontal pill-shaped switch housing with two short parallel vertical
strokes in its middle, mirrored about x = 24 and y = 24, on HRECT_M
(centerline box (4,10)-(44,38)).
- housing: one closed stadium contour. Both end caps are radius 14 half
  circles (two quarter arcs each) centred on (18,24) and (30,24), joined by
  tangent top/bottom lines at y = 10 and y = 38. The cap apexes are the x = 4
  and x = 44 extremes, the lines the y = 10 and y = 38 extremes.
- strokes: two vertical lines at x = 20 and x = 28 (8 apart on centerlines),
  from y = 19 to y = 29, 9 below the top line and above the bottom line
  (exactly 8 against the arc-bearing contour is only sampled and comes back
  `review`, so 9 is given); nearest cap points (18,10)/(30,10) are 9.2 away.
No useful Lucide match (Lucide `toggle-left`/`pill` carry a knob or split,
not two strokes); construction follows Lucide's stadium: tangent line + arc.

Metric issues (capsule-switch-with-two-strokes-batch-016-14_metrics.json):
- stroke-width (info, trace 2.67): redrawn at stroke 4, every gap budgeted.
- keyshape-short-axis (y filled 67%): the housing is 28 tall on centerlines,
  so its extremes sit exactly on the HRECT_M box; the pill becomes rounder
  (40x28 centerline) than the trace's 2.1:1, the only way to fill the box.
- clearance e0/e1 and e0/e2 (5.1 on centerlines): the strokes now end 9 from
  the housing lines.
- clearance e1/e2 (7.43): the strokes are exactly 8 apart.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5aacf220-3104-5628-83e3-8dddf6e85cbc"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1927-capsule-switch-with-two-strokes-batch-016-14/capsule-switch-with-two-strokes-batch-016-14_raw.svg"
AUTHOR = "claude-opus-5-5"

CY = 24
CAP_R = 14                      # end-cap radius; half the housing height
LEFT_CX, RIGHT_CX = 18, 30      # cap centres; apexes at x = 4 and x = 44
STROKE_DX = 4                   # strokes at 24 -/+ 4
STROKE_HALF = 5                 # strokes run CY -/+ 5; 9 from the housing


class CapsuleSwitchWithTwoStrokesRedraw(Solo48):
    icon_id = "capsule-switch-with-two-strokes-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("capsule switch", "pill switch", "rocker switch")
    keywords = ("switch", "toggle", "capsule", "pill", "button", "control", "pause")

    def build(self) -> None:
        top, bottom = CY - CAP_R, CY + CAP_R

        # Housing: clockwise stadium, lines tangent to the caps.
        self.add_line("top", (LEFT_CX, top), (RIGHT_CX, top))
        self.add_arc("cap-r-top", (RIGHT_CX, top), (RIGHT_CX + CAP_R, CY), radius_x=CAP_R, sweep=True)
        self.add_arc("cap-r-bottom", (RIGHT_CX + CAP_R, CY), (RIGHT_CX, bottom), radius_x=CAP_R, sweep=True)
        self.add_line("bottom", (RIGHT_CX, bottom), (LEFT_CX, bottom))
        self.add_arc("cap-l-bottom", (LEFT_CX, bottom), (LEFT_CX - CAP_R, CY), radius_x=CAP_R, sweep=True)
        self.add_arc("cap-l-top", (LEFT_CX - CAP_R, CY), (LEFT_CX, top), radius_x=CAP_R, sweep=True)
        self.add_contour(
            "housing", "top", "cap-r-top", "cap-r-bottom", "bottom", "cap-l-bottom", "cap-l-top",
            closed=True,
        )

        # Two mirrored strokes about x = 24.
        for name, x in (("stroke-l", 24 - STROKE_DX), ("stroke-r", 24 + STROKE_DX)):
            self.add_line(name, (x, CY - STROKE_HALF), (x, CY + STROKE_HALF))
