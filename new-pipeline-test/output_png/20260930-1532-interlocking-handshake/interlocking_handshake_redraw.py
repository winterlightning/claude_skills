"""interlocking-handshake (redraw of the new-pipeline traced SVG).

Plan: two hands clasped side-on, sleeves as four level wrist lines, on
HRECT_M (centerline box (4,10)-(44,38)), the metrics' suggestion and the
closest fit to the wide 1.68 trace.
- wrists: upper pair on y=17 (x 4..7 and 41..44), lower pair on y=31
  (x 4..8 and 36..44); x=4 and x=44 are the side extremes.
- backs of the hands: two mirrored S-rises (peaks (13,10) and (35,10), the
  top extreme) that slope into a V notch at J=(22,13). The right back runs on
  into the thumb with tangent (-1,1); the left back ends on J at 90 degrees,
  so no rise runs parallel to the thumb.
- right thumb: a 45-degree tube, edges x+y=35 and x+y=49 (9.9 apart), r5 tip
  about (21,21) with 3-4-5 ends (18,17)/(25,24).
- right palm and index finger: line x-y=7 from the thumb notch (28,21) to an
  r5 fingertip about (31,31); the lower-right wrist ends on its east point.
- left fingers: the lower-left wrist drops at 45 degrees into one rounded
  finger bump whose bottom is the y=38 extreme, ending on the right
  fingertip at (28,35).
Construction from Lucide `handshake` (a thumb hook over the other palm,
round fingertip loops, straight sleeve strokes); no human_ref applies since
there are no heads or figures.

Metric issues:
- clearance e0/e1 (7.95), e0/e4 (4.6), e1/e3 (4.22), e3/e5 (7.75) and
  e4/e5 (3.33): fixed. The trace's four wrapped finger lines, 3-5 units
  apart, cannot keep 8 at 48, so they reduce to one finger tube and one
  finger bump. The thumb tip keeps 8 from the left hand's back and fingers,
  and validate_icon plus build_gate pass with no warnings.
- keyshape-short-axis (HRECT_M y fill 85%): fixed. The arches reach y=10
  and the finger bump reaches y=38, so all four extremes land exactly on the box.
- stroke-width (trace 2.65): redrawn at stroke 4 with every gap re-measured.
- junctions (t-junctions e1/e2, e0/e3, e3/e4, e1/e4, e1/e5): kept as shared
  lattice endpoints with declared connects (left back on J, lower-right
  wrist on the fingertip, left finger on the fingertip end).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e18ed81a-df3e-442f-9876-54ac0d744866"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1532-interlocking-handshake/"
    "interlocking-handshake_raw.svg"
)
AUTHOR = "claude-opus-5-5"


class InterlockingHandshakeRedraw(Solo48):
    icon_id = "interlocking-handshake-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/gestures"
    aliases = ("handshake", "clasped hands")
    keywords = ("handshake", "deal", "agreement", "partnership", "greeting", "hands")

    def build(self) -> None:
        # left hand back
        self.add_line("a-wrist", (4, 17), (7, 17))
        self.add_bezier("a-rise", (7, 17), ((9, 17), (10, 10), (13, 10)))
        self.add_bezier("a-slope", (13, 10), ((17, 10), (20, 11), (22, 13)))
        self.add_contour("a-top", "a-wrist", "a-rise", "a-slope")
        # right hand
        self.add_line("b-wrist", (44, 17), (41, 17))
        self.add_bezier("b-rise", (41, 17), ((39, 17), (38, 10), (35, 10)))
        self.add_bezier("b-slope", (35, 10), ((29, 10), (24, 11), (22, 13)))
        self.add_line("b-thumb-top", (22, 13), (18, 17))
        self.add_arc("b-thumb-tip", (18, 17), (25, 24), radius_x=5, large_arc=True, sweep=False)
        self.add_line("b-thumb-low", (25, 24), (28, 21))
        self.add_line("b-palm", (28, 21), (35, 28))
        self.add_arc("b-tip-1", (35, 28), (36, 31), radius_x=5, sweep=True)
        self.add_arc("b-tip-2", (36, 31), (28, 35), radius_x=5, sweep=True)
        self.add_line("b-finger", (28, 35), (26, 33))
        self.add_contour("b-hand", "b-wrist", "b-rise", "b-slope", "b-thumb-top", "b-thumb-tip",
                         "b-thumb-low", "b-palm", "b-tip-1", "b-tip-2", "b-finger")
        self.relate("connect", "a-top", "b-hand")
        # lower wrists
        self.add_line("b-cuff", (44, 31), (36, 31))
        self.relate("connect", "b-cuff", "b-hand")
        self.add_line("a-cuff", (4, 31), (8, 31))
        self.add_line("a-heel", (8, 31), (14, 37))
        self.add_bezier("a-low", (14, 37), ((15, 37.67), (16, 38), (18, 38)), ((22, 38), (26, 36), (26, 33)))
        self.add_contour("a-lower", "a-cuff", "a-heel", "a-low")
        self.relate("connect", "a-lower", "b-hand")
