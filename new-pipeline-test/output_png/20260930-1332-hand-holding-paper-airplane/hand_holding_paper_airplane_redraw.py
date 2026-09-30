"""hand holding paper airplane (redraw of the new-pipeline traced SVG).

Plan: SQUARE (centerline box (6,6)-(42,42)); the subject is diagonal, so it
fills the square from the arm's cap at the lower left to the nose at the
upper right.
- paper airplane: Lucide `send` construction, one closed outline
  nose -> left wing tip -> tail -> right wing tip, plus one fold from the nose
  to the tail that splits it into two triangular wings. The nose is the (42,6)
  corner, the left wing tip is on the x=6 edge.
- arm: one open contour, a 45 deg forearm rising from the (6,42) corner, a
  tangent cubic bend into a flat palm under the plane's tail, ending in a
  short upturned fingertip curve.
Repairs of the metric issues:
- clearance e0/e2 (plane vs hand, 2.98): the right wing tip is raised to
  (38,26) and the palm lowered to y=34, with the fingertip curl kept left of
  the wing tip; nearest plane/arm distance is now >= 8 (validator MIC pass).
- holes 1.79 / 4.12 (need 6): the trace's tail notch (two tiny facets) is
  dropped and the wings are enlarged; the centerline inradii are 5.25 (upper
  wing) and 5.38 (lower wing), i.e. ink openings of about 6.5 and 6.8.
- clearance e0/e1 (fold 2.66 from the upper edge beyond the joint): the fold
  now runs to the tail point, a real shared vertex, so it only meets the
  outline at the nose and the tail.
- narrow-join at the nose (26 deg): the nose wedges are now 27 deg (upper
  edge/fold) and 40 deg (fold/lower edge). Not fully fixed: a paper plane
  nose is an acute point by nature (Lucide `send` has the same ~26 deg
  wedges); widening it further makes a kite, not a dart. Validator is clean.
- no-head: not applicable, the subject is a hand only (choice.json parts).
- stroke-width: redrawn at stroke 4 with every gap budgeted at 8.
Lucide reference: `send` for the plane outline + fold; no Lucide hand used.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b3f6c409-ce6d-47c9-92ed-52d3c36236bc"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1332-hand-holding-paper-airplane/hand-holding-paper-airplane_raw.svg"
AUTHOR = "claude-opus-5-5"

NOSE = (42, 6)
WING_L = (8, 13)
TAIL = (22, 22)
WING_R = (38, 26)

ARM_START = (6, 42)
BEND_IN = (12, 36)          # forearm runs at 45 deg to here
PALM_Y = 34
BEND_OUT = (16, PALM_Y)
PALM_END = (24, PALM_Y)
FINGER_TIP = (27, 32)


class HandHoldingPaperAirplaneRedraw(Solo48):
    icon_id = "hand-holding-paper-airplane-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "communication/send"
    aliases = ("launch paper plane", "send message by hand")
    keywords = ("hand", "paper airplane", "paper plane", "send", "launch", "message", "holding")

    def build(self) -> None:
        self.add_polyline("plane", NOSE, WING_L, TAIL, WING_R, NOSE, closed=True)
        self.add_line("fold", NOSE, TAIL)
        self.relate("connect", "plane", "fold")

        self.add_line("forearm", ARM_START, BEND_IN)
        self.add_bezier("bend", BEND_IN, ((14, PALM_Y), (14, PALM_Y), BEND_OUT))
        self.add_line("palm", BEND_OUT, PALM_END)
        self.add_bezier("finger", PALM_END, ((26, PALM_Y), (27, 33), FINGER_TIP))
        self.add_contour("arm", "forearm", "bend", "palm", "finger")
