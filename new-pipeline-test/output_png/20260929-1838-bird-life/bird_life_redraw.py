"""bird-life (redraw of the new-pipeline trace).

PLAN
- Subject: one songbird in side profile facing right: an upturned tail at the
  left, a back that dips and rises into a round head, a V beak, a plump breast
  and belly, and one curved wing line inside the body.
- Keyshape HRECT_M (the metrics suggestion, fit score 1.21), centerline box
  (4,10)-(44,38): tail tip on x=4, head crown on y=10, beak tip on x=44, belly
  on y=38.
- Body is one closed contour: back cubic (tail tip -> neck), r5 head arc about
  (33,15) from the 3-4-5 neck point (29,12) over the crown to (38,15), beak
  lines (38,15)->(44,18)->(38,21) at 1:2, breast cubic down to the belly
  (23,38), tail-under cubic back up to the tail tip. The belly join is
  tangent-continuous (both controls on y=38); the tail tip and beak are
  deliberate corners.
- Wing: one free cubic (17,28)->(30,24), a shallow smile rising to the right
  like the reference, kept 8+ from every body wall.
- Rebuilt on the grid from the image, not from trace coordinates.

METRIC ISSUES
- error clearance (e0/e1 2.8 apart, need 8): fixed. The wing is shortened
  and moved inward (it starts at x=17, not ~12), the tail-under and breast
  curves bulge outward a little to widen the interior; min wing-body
  centerline distance is now >= 8.3.
- warn keyshape-short-axis (x fill 96%): fixed. The tail tip sits on x=4 and
  the beak tip on x=44, so all four HRECT_M extremes are exact.
- info stroke-width (trace 2.55 vs 4): handled by redrawing at stroke 4 with
  every gap budgeted at 8 on centerlines.
- validate_icon(): valid, 0 warnings; build_gate.py: PASS, 0 warnings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "dee6f213-07ab-4305-8dd4-d656ac7937ec"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1838-bird-life/bird-life_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT, RIGHT, TOP, BOTTOM = 4, 44, 10, 38   # HRECT_M centerline box
TAIL = (LEFT, 14)
HEAD_C, HEAD_R = (33, 15), 5
NECK = (29, 12)                # 3-4-5 point on the head circle
BEAK_TOP, BEAK_TIP, BEAK_LOW = (38, 15), (RIGHT, 18), (38, 21)
BELLY = (23, BOTTOM)
WING = ((17, 28), (24, 29), (29, 27), (30, 24))


class BirdLifeRedraw(Solo48):
    icon_id = "bird-life-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ("bird", "songbird", "sparrow")
    keywords = ("bird", "wildlife", "nature", "animal", "birdwatching", "songbird")

    def build(self) -> None:
        self.add_bezier("back", TAIL, ((9, 22), (22, 22), NECK))
        self.add_arc("head", NECK, BEAK_TOP, radius_x=HEAD_R)
        self.add_line("beak-top", BEAK_TOP, BEAK_TIP)
        self.add_line("beak-low", BEAK_TIP, BEAK_LOW)
        self.add_bezier("breast", BEAK_LOW, ((40, 30), (34, BOTTOM), BELLY))
        self.add_bezier("tail-under", BELLY, ((11, BOTTOM), (LEFT, 30), TAIL))
        self.add_contour("body", "back", "head", "beak-top", "beak-low", "breast",
                         "tail-under", closed=True)
        self.add_bezier("wing", WING[0], WING[1:])
