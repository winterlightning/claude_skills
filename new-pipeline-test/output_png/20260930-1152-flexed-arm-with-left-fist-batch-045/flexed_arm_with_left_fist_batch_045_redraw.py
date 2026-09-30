"""flexed arm with left fist (redraw of the new-pipeline traced SVG).

Plan: one isolated arm on SQUARE (centerline box (6,6)-(42,42)), drawn as a
single open outline like the trace: it starts at the cut end of the upper arm
on the right, runs over the bicep, dips into the elbow crease, climbs the inner
forearm to the fist, wraps round the fist, and returns down the outer forearm,
round the elbow and along the underside of the upper arm to the second cut end.
- fist: a rounded block (x 6..24, y 6..18) with radius-5 corners on the right
  and a radius-6 shoulder where it meets the outer forearm; its top is the
  y=6 extreme, no finger detail (as briefed).
- forearm: the outer edge is the x=6 extreme (vertical); the inner edge leans
  out from the fist (15,18) to the elbow crease (19,33), so the forearm widens
  toward the elbow.
- elbow: one radius-12 arc from the outer forearm into the y=42 underside,
  tangent at both ends.
- bicep: two tangent cubics, crease -> peak (28,24) -> the horizontal top edge
  y=32, which ends at the x=42 extreme. The underside ends at x=40, a slight
  stagger of the two cut ends as in the generated image.
Metric issues fixed:
- keyshape-short-axis (x filled 87%, SQUARE needs a 1.16 stretch): the arm was
  rebuilt wider, extremes exactly on x 6 and 42, y 6 and 42.
- stroke-width (trace 2.4): drawn at the profile stroke 4; the forearm is at
  least 9 wide between centerlines and the upper arm 10, so no gap shrinks
  below 8.
- no-head: not applicable. The subject is an isolated arm with no head or
  torso (the brief says so), so there is no head gap to measure and no human
  figure to mark.
Lucide biceps-flexed was considered; its construction (fist and bicep as one
continuous outline) informs the drawing, but the pose follows the generated
image (vertical forearm, fist on top, upper arm going right).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ee5bfb94-7340-47f3-893b-14b8899829f6"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1152-flexed-arm-with-left-fist-batch-045/flexed-arm-with-left-fist-batch-045_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT, TOP, RIGHT, BOTTOM = 6, 6, 42, 42
FIST_RIGHT, FIST_BOTTOM = 24, 18
FIST_R = 5                      # right-hand fist corners
SHOULDER_R = 6                  # fist top into the outer forearm
INNER_TOP_X = 15                # inner forearm leaves the fist here
CREASE = (19, 33)               # elbow crease, inner forearm meets bicep
ELBOW_R = 12
PEAK = (28, 24)                 # bicep peak
ARM_TOP_Y = 32                  # upper arm top edge
BICEP_END_X = 38
UNDER_END_X = 40


class FlexedArmWithLeftFistBatch045Redraw(Solo48):
    icon_id = "flexed-arm-with-left-fist-batch-045-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "body"
    aliases = ("flexed arm", "flexed bicep", "strong arm")
    keywords = ("arm", "bicep", "muscle", "flex", "fist", "strength", "fitness", "body")

    def build(self) -> None:
        elbow_y = BOTTOM - ELBOW_R
        self.add_line("arm-top", (RIGHT, ARM_TOP_Y), (BICEP_END_X, ARM_TOP_Y))
        self.add_bezier("bicep", (BICEP_END_X, ARM_TOP_Y),
                        ((34, ARM_TOP_Y), (33, PEAK[1]), PEAK),
                        ((24, PEAK[1]), (21, 28), CREASE))
        self.add_line("inner-forearm", CREASE, (INNER_TOP_X, FIST_BOTTOM))
        self.add_line("fist-bottom", (INNER_TOP_X, FIST_BOTTOM),
                      (FIST_RIGHT - FIST_R, FIST_BOTTOM))
        self.add_arc("fist-lower", (FIST_RIGHT - FIST_R, FIST_BOTTOM),
                     (FIST_RIGHT, FIST_BOTTOM - FIST_R), radius_x=FIST_R, sweep=False)
        self.add_line("fist-front", (FIST_RIGHT, FIST_BOTTOM - FIST_R),
                      (FIST_RIGHT, TOP + FIST_R))
        self.add_arc("fist-upper", (FIST_RIGHT, TOP + FIST_R),
                     (FIST_RIGHT - FIST_R, TOP), radius_x=FIST_R, sweep=False)
        self.add_line("fist-top", (FIST_RIGHT - FIST_R, TOP), (LEFT + SHOULDER_R, TOP))
        self.add_arc("fist-shoulder", (LEFT + SHOULDER_R, TOP),
                     (LEFT, TOP + SHOULDER_R), radius_x=SHOULDER_R, sweep=False)
        self.add_line("outer-forearm", (LEFT, TOP + SHOULDER_R), (LEFT, elbow_y))
        self.add_arc("elbow", (LEFT, elbow_y), (LEFT + ELBOW_R, BOTTOM),
                     radius_x=ELBOW_R, sweep=False)
        self.add_line("arm-under", (LEFT + ELBOW_R, BOTTOM), (UNDER_END_X, BOTTOM))
        self.add_contour("arm", "arm-top", "bicep", "inner-forearm", "fist-bottom",
                         "fist-lower", "fist-front", "fist-upper", "fist-top",
                         "fist-shoulder", "outer-forearm", "elbow", "arm-under")
