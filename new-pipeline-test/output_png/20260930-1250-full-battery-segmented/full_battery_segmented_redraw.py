"""full-battery-segmented (redraw of the new-pipeline traced SVG).

Plan: a wide full battery on HRECT_M (centerline box (4,10)-(44,38)),
mirrored across y=24.
- case: closed rectangle (4,10)-(36,38), one straight polyline contour; the
  round stroke joins give the ink corners a radius of 2, so it still reads as
  the rounded case of the generated image.
- terminal: Lucide battery construction, a detached vertical stroke at x=44
  (y 20..28), 8 right of the case wall; it sets the right extreme.
- charge: a full three-slot series at x = 12, 20, 28 (8 apart), y 18..30, so
  every bar is exactly 8 from each case wall and from its neighbour: the case
  interior is split into even bands.
Extremes: x 4 (case) / 44 (terminal), y 10 / 38 (case).

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4; every gap re-budgeted for it.
- keyshape-short-axis: the case spans the full 28 on y (10..38) instead of
  the trace's 66%, so every HRECT_M extreme lies on its box.
- clearance e0/e1, e0/e2, e0/e3 (bars 3.1-4.6 from the bottom wall): bars now
  end 8 from the top and bottom walls and sit 8 from the side walls.
- hole at (7.7, 18.4), 3.6 wide: the traced left bar ran into the bottom wall
  (ink gap -0.9), sealing a thin pocket beside the left wall. The bars are now
  detached with an ink gap of 4 all round, so no pocket is sealed; the only
  enclosed space is the case interior. The traced hollow terminal nub (a 2-wide
  hole at stroke 4) is replaced by Lucide's single detached terminal stroke.
Deliberate change: the case corners are straight round joins rather than
radius-4 arcs. SOLO48 returns review for an arc contour at exactly 8 from a
bar (tried: 3 warnings), and three bars with a 9 margin need a 34-wide
interior, which pushes the detached terminal past x=44. Straight walls at 8
are certified, and the round joins keep the corners soft at 48 px.
Lucide: battery / battery-full informed the case, detached terminal and the
evenly spaced charge bars.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "33faddf4-6c93-4508-bf49-bd5a27dd53af"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1250-full-battery-segmented/full-battery-segmented_raw.svg"
AUTHOR = "claude-opus-5-5"

X0, X1, Y0, Y1 = 4, 36, 10, 38   # case centerline box
GAP = 8                          # SOLO48 centerline minimum
TERM_X, TERM_H = X1 + GAP, 4     # terminal x (44), half height about y=24
CY = (Y0 + Y1) // 2              # 24, mirror axis
BAR_X = tuple(range(X0 + GAP, X1, GAP))  # 12, 20, 28
BAR_Y0, BAR_Y1 = Y0 + GAP, Y1 - GAP      # 18..30


class FullBatterySegmentedRedraw(Solo48):
    icon_id = "full-battery-segmented-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "devices"
    aliases = ("battery-full", "full-battery")
    keywords = ("battery", "full", "charge", "charged", "power", "energy", "level")

    def build(self) -> None:
        self.add_polyline("case", (X0, Y0), (X1, Y0), (X1, Y1), (X0, Y1), closed=True)
        self.add_line("terminal", (TERM_X, CY - TERM_H), (TERM_X, CY + TERM_H))
        for x in BAR_X:
            self.add_line(f"charge-{x}", (x, BAR_Y0), (x, BAR_Y1))
