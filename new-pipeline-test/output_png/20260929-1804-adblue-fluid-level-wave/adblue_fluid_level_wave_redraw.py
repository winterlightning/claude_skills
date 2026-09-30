"""adblue-fluid-level-wave (redraw of the new-pipeline traced SVG).

Plan: a hollow droplet centred above two stacked fluid-level waves, on
SQUARE (centerline box (6,6)-(42,42), ink (4,4)-(44,44)).
- droplet: one closed contour, mirrored about x=24.
  - bowl: an r6 arc about (24,17) from its right apex (30,17) under the
    bottom (24,23) to its left apex (18,17); the hole stays 8 across.
  - flanks: one cubic per side from the bowl apex up to the tip (24,6); the
    control at the bowl leaves vertically, so flank-to-bowl joins are
    tangent-continuous. The tip is the one deliberate corner and sits on the
    top edge y=6.
- waves: one repeat definition, drawn twice 10 apart (troughs y=32, y=42).
  Each is four S-cubics with horizontal tangents at every knot (so joins are
  tangent-continuous): troughs at x=6, 24, 42 and crests at x=15, 33,
  amplitude 3, controls 3 in from each knot (max slope 0.5, so the two
  rows stay ~8.9 apart on centerlines). The lower wave's troughs sit on y=42 and its ends on x=6 and
  x=42, so the envelope touches all four sides of the SQUARE box.
  The upper wave's centre trough lies under the droplet bottom, as in the
  generated image, which keeps the droplet >= 8 from both crests.
Traced shape: adblue-fluid-level-wave_raw.svg (read for the subject only;
nothing copied from its coordinates).
Lucide: droplet (round bowl + two curved flanks to a tip) and waves
(repeated S-curve rows) inform the construction, redrawn on this grid.

Metric issues:
- clearance e0/e1 (droplet 5.99 from the upper wave): fixed, the droplet
  bowl ends at y=23 over the upper wave's centre trough (y=32) and is
  >= 8 from both crests at (15,29) and (33,29).
- clearance e1/e2 (waves 5.06 apart): fixed, the waves are one shape
  repeated 10 apart with a gentler slope, >= 8 apart everywhere.
- keyshape-short-axis (y fills 87%): fixed, tip on y=6 and the lower
  wave's troughs on y=42; waves span x=6..42.
- stroke-width (info): drawn at stroke 4; every gap budgeted for 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ddba64a9-7a33-401d-9571-bce55808907f"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1804-adblue-fluid-level-wave/"
    "adblue-fluid-level-wave_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AX = 24            # mirror axis
TIP = (AX, 6)
BOWL_Y = 17        # bowl centre y
BR = 6             # bowl radius
LEFT = (AX - BR, BOWL_Y)
RIGHT = (AX + BR, BOWL_Y)

WAVE_TROUGH = 42   # lower wave trough y
WAVE_AMP = 3       # trough-to-crest height
WAVE_GAP = 10      # vertical repeat distance
HALF = 9           # trough-to-crest run
K = 3              # horizontal control reach at each knot


def mirror(p):
    return (2 * AX - p[0], p[1])


class AdblueFluidLevelWaveRedraw(Solo48):
    icon_id = "adblue-fluid-level-wave-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/vehicle-fluids"
    aliases = ("adblue", "def-fluid", "diesel-exhaust-fluid")
    keywords = ("adblue", "def", "diesel exhaust fluid", "fluid level",
                "droplet", "liquid", "wave", "urea")

    def _wave(self, element_id: str, trough_y: int) -> None:
        crest_y = trough_y - WAVE_AMP
        x0 = 6
        segments = []
        y = trough_y
        for i in range(4):
            xa, xb = x0 + i * HALF, x0 + (i + 1) * HALF
            y_next = crest_y if y == trough_y else trough_y
            segments.append(((xa + K, y), (xb - K, y_next), (xb, y_next)))
            y = y_next
        self.add_bezier(element_id, (x0, trough_y), *segments)

    def build(self) -> None:
        # Droplet: right flank tip -> bowl apex (arriving vertically), bowl, left flank.
        c1, c2 = (26, 9), (30, 12)
        self.add_bezier("flank-right", TIP, (c1, c2, RIGHT))
        self.add_arc("bowl", RIGHT, LEFT, radius_x=BR, sweep=True)
        self.add_bezier("flank-left", LEFT, (mirror(c2), mirror(c1), TIP))
        self.add_contour("droplet", "flank-right", "bowl", "flank-left", closed=True)

        self._wave("wave-upper", WAVE_TROUGH - WAVE_GAP)
        self._wave("wave-lower", WAVE_TROUGH)
