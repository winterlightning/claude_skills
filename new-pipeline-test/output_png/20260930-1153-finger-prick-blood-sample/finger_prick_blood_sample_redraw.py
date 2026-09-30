"""finger prick blood sample (redraw of the new-pipeline traced SVG).

Plan: SQUARE (centerline box (6,6)-(42,42)), two separate parts laid on the
diagonal like the generated image: fingertip top-left, blood drop bottom-right.
- fingertip: one open contour, a horizontal U open at the left. Straight
  sides on y=6 (top extreme) and y=18 start at x=6 (left extreme) and meet a
  radius-6 half circle centred on the integer point (FINGER_CX, 12), so both
  joins are tangent. The 12-unit channel leaves an 8-unit white band.
- drop: the repo `blood-drop` construction at half size -- pointed crown at
  (34,22), straight flanks into radius-10 shoulder arcs, and a 16x12 elliptic
  bowl split at the bottom point (34,42) with vertical tangents at x=26/42,
  so the right (42) and bottom (42) extremes land exactly on the box.

Metric issues fixed:
- clearance e0-e1 (5.35 apart on centerlines): the fingertip was shortened to
  end at x=29 and the drop crown sits at (34,22); the nearest pair (crown to
  the fingertip arc) is ~8.9 on centerlines, over the 8 minimum (not exactly
  8, which the curved-pair check returns as review).
- stroke-width (trace 2.77 after fitting): drawn at stroke 4 on the 48 grid,
  every gap budgeted for stroke 4.
The trace's stray 1-unit kink at the drop's right flank and its skewed
off-grid arcs are dropped; the drop is mirror-symmetric about x=34.
Lucide construction: `droplet` (pointed crown, round bowl) for the drop; the
fingertip is a plain U like the rounded end of Lucide `pill` halves.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e3dc0da0-bd87-41fd-95b9-89f6eee043aa"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1153-finger-prick-blood-sample/finger-prick-blood-sample_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT, TOP, RIGHT, BOTTOM = 6, 6, 42, 42
FINGER_R = 6
FINGER_CX = 23                 # fingertip arc centre x; rightmost ink at 29
FINGER_BOTTOM = TOP + 2 * FINGER_R
DROP_AXIS = 34                 # drop mirrored about x=34
DROP_TIP_Y = 22


class FingerPrickBloodSampleRedraw(Solo48):
    icon_id = "finger-prick-blood-sample-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "medical/testing"
    aliases = ("finger prick", "blood sample", "glucose test", "lancet test")
    keywords = ("finger", "prick", "blood", "drop", "sample", "glucose", "diabetes", "test")

    def build(self) -> None:
        r, cx = FINGER_R, FINGER_CX
        self.add_line("finger-top", (LEFT, TOP), (cx, TOP))
        self.add_arc("finger-tip", (cx, TOP), (cx, FINGER_BOTTOM), radius_x=r)
        self.add_line("finger-bottom", (cx, FINGER_BOTTOM), (LEFT, FINGER_BOTTOM))
        self.add_contour("finger", "finger-top", "finger-tip", "finger-bottom", closed=False)

        a = DROP_AXIS
        tip = (a, DROP_TIP_Y)
        left, right = (a - 8, BOTTOM - 6), (a + 8, BOTTOM - 6)
        self.add_line("drop-upper-left", tip, (a - 6, DROP_TIP_Y + 8))
        self.add_arc("drop-shoulder-left", (a - 6, DROP_TIP_Y + 8), left, radius_x=10, sweep=False)
        self.add_arc("drop-base-left", left, (a, BOTTOM), radius_x=8, radius_y=6, sweep=False)
        self.add_arc("drop-base-right", (a, BOTTOM), right, radius_x=8, radius_y=6, sweep=False)
        self.add_arc("drop-shoulder-right", right, (a + 6, DROP_TIP_Y + 8), radius_x=10, sweep=False)
        self.add_line("drop-upper-right", (a + 6, DROP_TIP_Y + 8), tip)
        self.add_contour(
            "drop", "drop-upper-left", "drop-shoulder-left", "drop-base-left",
            "drop-base-right", "drop-shoulder-right", "drop-upper-right", closed=True,
        )
