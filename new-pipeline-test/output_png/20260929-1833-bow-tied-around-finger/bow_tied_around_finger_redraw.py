"""bow-tied-around-finger (redraw of the new-pipeline trace).

Plan: an upright finger with a ribbon bow tied across it, mirrored about
x=24 on VRECT_M (centerline box (10,4)-(38,44)).
- finger: an r6 fingertip arch centred on (24,10), with its top at y=4, and
  straight sides at x=18/30. The sides stop at the bow's upper edge (y=20)
  and resume from its lower edge (y=28) down to y=44, so the finger reads
  as passing behind the ribbon.
- bow: two closed teardrop loops that meet in a point at the knot K=(24,24).
  Each loop is a straight tie edge from K to the finger side (A=(18,20) up,
  B=(18,28) down), then one smooth two-cubic run around the round outer end
  at x=10 (mirror x=38). The cubics leave A and arrive at B along the tie
  edges' direction (3:2), so only the knot point is a corner. The finger
  sides end on the loop nodes A/B and share those endpoints (declared
  connect).
Traced shape: bow-tied-around-finger_raw.svg, read for the subject only;
no coordinates copied.
Lucide: the `gift` bow (two loops meeting at a central point) informed the
loops; no local finger-with-bow match.

Metric issues:
- clearance e0 (fingertip) vs e2/e3/e4 (loops) at 2.6 and vs e1 (knot) at
  6.7: fixed. The finger sides now end on the loop nodes (a declared,
  shared-endpoint contact), not 2.6 short of the loops.
- clearance e1 (knot circle) vs e2/e3/e4/e5/e6/e7/e8: fixed. The r2.6 knot
  circle is dropped; the loops meet in a point at K, which reads as the knot.
  A circle knot would need r>=5 for a 6-wide hole and would swallow the
  12-wide finger.
- clearance e2/e3 vs e4 (loops against the tie stroke) and loop
  crossings: fixed. Each loop is one closed contour; the two loops share
  only K.
- clearance e5/e6 (tails) vs e1/e2/e3/e7/e8: fixed by dropping the tails.
  Cannot keep them: the box is 28 wide, so a tail outside the finger has
  only x=10..18 and must be 8 from the finger side at x=18, and a tail
  between the finger sides would be only 6 from each. See compromise.
- clearance e7/e8 (lower finger sides) vs tails and knot: fixed; they now
  start on the loop nodes B/B'.
- holes at [15.8,21.0] / [32.2,20.9] (loops, 3.5 inscribed) and at
  [23.8,22.6] (knot, 1.1): fixed. The loops are 14 wide and about 12 tall on
  centerline, and the knot hole is gone. The fingertip hole is 8 wide in ink.
- keyshape-short-axis (x only 86%): fixed. The loop ends reach x=10/38, and
  the fingertip and finger base reach y=4/44.
- stroke-count (9 strokes, budget 6): reduced to 6 parts (fingertip, two
  loops, two lower finger sides and the knot join).
- stroke-width (info): drawn at stroke 4 with every gap budgeted for 4.
Compromise: the two ribbon tails are dropped (reason above); the bow reads
from the two loops and the knot alone.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "cb7f5956-8d37-4c5d-be74-835813bcddcd"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1833-bow-tied-around-finger/"
    "bow-tied-around-finger_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AX = 24                     # mirror axis
TOP, BOTTOM = 4, 44         # VRECT_M centerline box (10,4)-(38,44)
TIP_R = 6                   # fingertip arch, sides at x = 18 / 30
KNOT = (AX, 24)             # loops meet here
BOW_UP, BOW_DN = 20, 28     # loop nodes on the finger sides
LOOP_END = 10               # outer loop end, x = 10 / 38
LOOP_MID = 24               # loop end tangent point (vertical tangent)
REACH = 6                   # control reach along the 3:2 tie direction
END_REACH = 5               # vertical control reach at the loop ends


def _m(p):
    return (2 * AX - p[0], p[1])


class BowTiedAroundFingerRedraw(Solo48):
    icon_id = "bow-tied-around-finger-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hands"
    aliases = ("string-on-finger", "reminder-bow", "finger-bow")
    keywords = ("bow", "ribbon", "finger", "reminder", "remember", "memo", "tie")

    def build(self) -> None:
        sl, sr = AX - TIP_R, AX + TIP_R
        tip_y = TOP + TIP_R

        # fingertip: side up, arch over the top, side down
        self.add_line("tip-left", (sl, BOW_UP), (sl, tip_y))
        self.add_arc("tip-arch", (sl, tip_y), (sr, tip_y), radius_x=TIP_R)
        self.add_line("tip-right", (sr, tip_y), (sr, BOW_UP))
        self.add_contour("fingertip", "tip-left", "tip-arch", "tip-right")

        # left loop: tie edge up, round outer end, tie edge back to the knot
        a, b = (sl, BOW_UP), (sl, BOW_DN)
        dx, dy = 3, 2                      # tie direction K -> A is (-3,-2)
        end = (LOOP_END, LOOP_MID)
        self.add_line("loop-left-tie-up", KNOT, a)
        self.add_bezier(
            "loop-left-end", a,
            ((a[0] - REACH, a[1] - REACH * dy // dx), (LOOP_END, LOOP_MID - END_REACH), end),
            ((LOOP_END, LOOP_MID + END_REACH), (b[0] - REACH, b[1] + REACH * dy // dx), b),
        )
        self.add_line("loop-left-tie-down", b, KNOT)
        self.add_contour(
            "loop-left", "loop-left-tie-up", "loop-left-end", "loop-left-tie-down",
            closed=True,
        )

        # right loop: mirror, same winding order from the knot
        self.add_line("loop-right-tie-up", KNOT, _m(a))
        self.add_bezier(
            "loop-right-end", _m(a),
            (_m((a[0] - REACH, a[1] - REACH * dy // dx)), _m((LOOP_END, LOOP_MID - END_REACH)), _m(end)),
            (_m((LOOP_END, LOOP_MID + END_REACH)), _m((b[0] - REACH, b[1] + REACH * dy // dx)), _m(b)),
        )
        self.add_line("loop-right-tie-down", _m(b), KNOT)
        self.add_contour(
            "loop-right", "loop-right-tie-up", "loop-right-end", "loop-right-tie-down",
            closed=True,
        )

        # finger below the bow
        self.add_line("base-left", b, (sl, BOTTOM))
        self.add_line("base-right", _m(b), (sr, BOTTOM))

        self.relate("connect", "fingertip", "loop-left")
        self.relate("connect", "fingertip", "loop-right")
        self.relate("connect", "loop-left", "loop-right")
        self.relate("connect", "base-left", "loop-left")
        self.relate("connect", "base-right", "loop-right")
