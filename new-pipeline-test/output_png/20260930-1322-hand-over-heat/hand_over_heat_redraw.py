"""hand-over-heat (redraw of the new-pipeline traced SVG).

Plan: a bent arm held palm-down over two rising heat waves, on SQUARE
(centerline box (6,6)-(42,42)), the keyshape the metrics suggested (score
1.12, square hint).
- arm: one contour. Upper arm on a 3:4 diagonal from the top-left corner
  (6,6) to (12,14); a radius-5 elbow arc centred (16,11) turns it tangentially
  into the level forearm on y 16; the forearm runs to x 38, where the hand is
  a radius-4 hook (centre (38,20), apex on x 42) folding back under itself to
  a short palm line on y 24, ending at x 34. Forearm and palm lines are 8
  apart on centerlines (the in-contour parallel minimum).
- heat: one S-wave definition, two cubics point-symmetric about their middle
  knot, top knot y 28, bottom knot y 42, bulging left then right by ~2;
  repeated at x 17 and x 27 (10 apart; the steepened mid tangent (2,3) keeps
  the pair ~8.3 apart perpendicular to the curves).
Extremes: left/top (6,6) arm start, right x 42 hook apex, bottom y 42 wave
feet.
Lucide construction: `heater` (steam wisps as a single S cubic whose ends
share one x); arm and hand have no useful Lucide match.

Metric issues (hand-over-heat_metrics.json) and how they were handled:
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- keyshape-short-axis (y filled 87%): fixed without stretching -- the arm
  starts on the top edge (y 6) and the wave feet sit on the bottom edge
  (y 42), so every SQUARE extreme is met exactly.
- clearance e0/e2 (hand to right wave, 4.61): fixed. The waves now start 12
  below the forearm and the right wave's top knot (27,28) is 8.06 from the
  palm line's end (34,24); the left wave is well clear.
- no-head (warn): not applicable -- the subject is an arm and hand only, not
  a stick figure, so there is no head or torso to draw or flag.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e2391138-4aaf-4587-83d5-f636e7ba5379"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1322-hand-over-heat/hand-over-heat_raw.svg"
AUTHOR = "claude-opus-5-5"

SHOULDER = (6, 6)
ELBOW_IN = (12, 14)        # end of the 3:4 upper arm
ELBOW_RADIUS = 5           # centre (16,11): tangent to both runs
FOREARM_Y = 16
HAND_X = 38                # hook arc centre x; apex at HAND_X + HAND_RADIUS
HAND_RADIUS = 4            # palm line 2*radius = 8 below the forearm
PALM_END_X = 34

WAVE_TOP, WAVE_MID, WAVE_FOOT = 28, 35, 42
WAVE_XS = (17, 27)


def wave_segments(x):
    """One S: bulge left above the middle knot, right below, point-symmetric."""
    return (
        ((x - 3, WAVE_TOP + 2), (x - 2, WAVE_MID - 3), (x, WAVE_MID)),
        ((x + 2, WAVE_MID + 3), (x + 3, WAVE_FOOT - 2), (x, WAVE_FOOT)),
    )


class HandOverHeatRedraw(Solo48):
    icon_id = "hand-over-heat-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/gestures"
    aliases = ("hand over heat", "warming hands", "hand above heat")
    keywords = ("hand", "arm", "heat", "warm", "hot", "temperature", "heater", "stove", "warmth")

    def build(self) -> None:
        elbow_out = (ELBOW_IN[0] + 4, FOREARM_Y)
        hand_top = (HAND_X, FOREARM_Y)
        hand_bottom = (HAND_X, FOREARM_Y + 2 * HAND_RADIUS)
        self.add_line("arm-upper", SHOULDER, ELBOW_IN)
        self.add_arc("arm-elbow", ELBOW_IN, elbow_out, radius_x=ELBOW_RADIUS, sweep=False)
        self.add_line("arm-forearm", elbow_out, hand_top)
        self.add_arc("arm-hand", hand_top, hand_bottom, radius_x=HAND_RADIUS, sweep=True)
        self.add_line("arm-palm", hand_bottom, (PALM_END_X, hand_bottom[1]))
        self.add_contour(
            "arm", "arm-upper", "arm-elbow", "arm-forearm", "arm-hand", "arm-palm"
        )

        for index, x in enumerate(WAVE_XS, start=1):
            self.add_bezier(f"heat-{index}", (x, WAVE_TOP), *wave_segments(x))
