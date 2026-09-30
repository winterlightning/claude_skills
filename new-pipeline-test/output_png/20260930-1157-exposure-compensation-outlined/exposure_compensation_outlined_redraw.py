"""exposure-compensation-outlined (redraw of the new-pipeline traced SVG).

Plan: the camera +/- exposure-compensation sign on SQUARE (centerline box
(6,6)-(42,42)), built point-symmetric about the canvas centre (24,24).
- divider: one 45-degree stroke (6,42)-(42,6), the box diagonal; it alone
  reaches all four keyshape extremes, so the fit is exact.
- plus: two arms of length 2*ARM crossing at P=(13,13), pushed into the
  top-left corner (left arm end and top arm end on the box edges).
- minus: the plus rotated 180 degrees about (24,24): centre M=(35,35), the
  same 14-unit width, touching the right edge.
Clearance to the divider (x+y=48): nearest plus ends (20,13)/(13,20) and
minus end (28,35) are 15/sqrt(2)=10.6 on centerlines (need 8).

Metric issues:
- clearance e0/e1 (0.0 apart, error): fixed. The two plus strokes are one
  sign that genuinely crosses, so they are built as two polylines through a
  shared centre vertex and declared with relate("connect"), not as two
  unrelated parts.
- stroke-width (info): redrawn at stroke 4; every gap was re-budgeted at 8 on
  centerlines instead of scaling the trace.
Lucide construction: `diff` / `plus` / `minus` (straight operator strokes,
equal arm lengths) and the diagonal of `slash`.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7e0c4b3a-5601-40b2-8ea5-02186da2356f"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1157-exposure-compensation-outlined/"
    "exposure-compensation-outlined_raw.svg"
)
AUTHOR = "claude-opus-5-5"

LO, HI = 6, 42          # SQUARE centerline box
ARM = 7                 # half-length of the plus arms and of the minus
P = (LO + ARM, LO + ARM)            # plus centre (13,13)
M = (48 - P[0], 48 - P[1])          # minus centre (35,35), P mirrored about (24,24)


class ExposureCompensationOutlinedRedraw(Solo48):
    icon_id = "exposure-compensation-outlined-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography"
    aliases = ("exposure value", "ev compensation", "plus minus")
    keywords = ("exposure", "compensation", "ev", "plus", "minus", "camera",
                "brightness", "photography", "setting")

    def build(self) -> None:
        self.add_line("divider", (LO, HI), (HI, LO))

        px, py = P
        self.add_polyline("plus-h", (px - ARM, py), P, (px + ARM, py))
        self.add_polyline("plus-v", (px, py - ARM), P, (px, py + ARM))
        self.relate("connect", "plus-h", "plus-v")

        mx, my = M
        self.add_line("minus", (mx - ARM, my), (mx + ARM, my))
