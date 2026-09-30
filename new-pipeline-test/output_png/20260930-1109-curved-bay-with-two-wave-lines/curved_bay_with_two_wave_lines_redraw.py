"""Curved bay with two wave lines (redraw of the new-pipeline traced SVG).

Plan: SQUARE keyshape, centerline box (6,6)-(42,42). Three parts, as in the
trace: one C-shaped coastline and two identical wave lines.

- Coastline: one smooth cubic run mirrored about y = 24. The headland tips
  are (COAST_END, 6) and (COAST_END, 42) (top / bottom extremes); each half
  bends to a vertical tangent at the leftmost point (6, 24) (left extreme),
  so the shore is one tangent-continuous curve opening to the right.
- Waves: one wave definition (start, trough, crest, trough, end) translated
  to two rows WAVE_GAP apart and centred on y = 24. Each row runs from
  x = WAVE_X0 inside the bay to x = 42 (right extreme), past the headland
  tips, like the trace. Trough / crest joins have horizontal tangents.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4; every gap budgeted for it.
- keyshape-short-axis (warn): the metrics' SQUARE candidate needs no stretch
  (fill 1.0 x 1.0, the trace is square, aspect 1.0), whereas HRECT_L would
  stretch x by 1.25 and cut the height to 32, which leaves no room for two
  waves 8+ clear of each other and of the shore. SQUARE is used and all four
  extremes sit exactly on its box.
- clearance e1/e2 (waves 6.0 apart): the rows are now WAVE_GAP apart with a
  gentle 4-unit swing, so their closest approach is above 8.
- clearance e0/e2 (shore to lower wave 7.97): the shore's shoulders are
  pulled outward (handles along y = 6 / 42), so both waves clear it by
  more than 8 where the lower wave's first trough comes nearest.
Dropped: the small kinks on the traced shoreline (vectorizer wobble that
reads as noise at 48 px).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "95af3736-8137-457c-a403-3663a17cb3af"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1109-curved-bay-with-two-wave-lines/curved-bay-with-two-wave-lines_raw.svg"
AUTHOR = "claude-opus-5-5"

MID = 24                # horizontal mirror axis of the bay
LEFT, TOP, RIGHT, BOTTOM = 6, 6, 42, 42
COAST_END = 30          # x of both headland tips
WAVE_X0 = 20            # where each wave starts inside the bay
WAVE_GAP = 14           # centerline spacing of the two wave rows
SWING = 2               # wave half-amplitude
HANDLE = 3              # horizontal handle on the trough/crest joins


class CurvedBayWithTwoWaveLinesRedraw(Solo48):
    icon_id = "curved-bay-with-two-wave-lines-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/geography"
    aliases = ("bay", "cove", "harbor", "lagoon")
    keywords = ("bay", "coast", "shore", "sea", "water", "waves", "beach", "harbor")

    def build(self) -> None:
        half = MID - TOP
        self.add_bezier(
            "coast", (COAST_END, TOP),
            ((18, TOP), (LEFT, MID - half / 1.5), (LEFT, MID)),
            ((LEFT, MID + half / 1.5), (18, BOTTOM), (COAST_END, BOTTOM)),
        )
        for name, y in (("wave-top", MID - WAVE_GAP // 2), ("wave-bottom", MID + WAVE_GAP // 2)):
            self._wave(name, y)

    def _wave(self, name: str, y: int) -> None:
        lo, hi = y + SWING, y - SWING
        x0, x1, x2, x3, x4 = WAVE_X0, WAVE_X0 + 5, WAVE_X0 + 11, WAVE_X0 + 17, RIGHT
        self.add_bezier(
            name, (x0, y),
            ((x0 + 1.2, y + 1), (x1 - HANDLE + 1, lo), (x1, lo)),
            ((x1 + HANDLE, lo), (x2 - HANDLE, hi), (x2, hi)),
            ((x2 + HANDLE, hi), (x3 - HANDLE, lo), (x3, lo)),
            ((x3 + HANDLE - 1, lo), (x4 - 1.2, y + 1), (x4, y)),
        )
