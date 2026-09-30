"""exposure compensation (redraw of the new-pipeline traced SVG).

Plan: the camera "+/-" exposure-compensation mark on SQUARE (centerline box
(6,6)-(42,42)), point-symmetric about the canvas centre (24,24).
- divider: one straight 45-degree stroke from (6,42) to (42,6), touching the
  bottom-left and top-right keyshape extremes exactly.
- plus: two crossing strokes centred on (14,14) with arm ARM=8, so it spans
  x 6..22 and y 6..22 (reaching the left and top extremes); the crossing is
  declared with relate("connect").
- minus: the plus's horizontal bar rotated 180 degrees about (24,24):
  centred on (34,34), x 26..42, reaching the right and bottom extremes.
Clearances: the nearest plus/minus endpoints ((22,14), (14,22), (26,34)) sit
12/sqrt(2) = 8.49 from the divider centerline x+y=48, above the 8 minimum.

Metric issues fixed:
- clearance e0-e1 (0.0 apart): the plus bars are meant to cross; they are
  now one intentional crossing declared as a connection, not two unrelated
  parts overlapping.
- stroke-width: drawn at stroke 4 on the 48 grid; the plus arm and minus
  were sized so every gap to the divider stays >= 8 on centerlines.
Change from the trace: the minus is moved up from y=37 to y=34 so it mirrors
the plus through the centre, balancing the negative space in both corners.
Lucide construction: `plus` / `minus` (straight round-capped bars) with the
`slash` diagonal, as in Lucide's `diff` / `plus-minus` family.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a0943d1c-4cfd-4ede-af66-e71962ed04ec"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1155-exposure-compensation/exposure-compensation_raw.svg"
AUTHOR = "claude-opus-5-5"

CENTER = 24
LO, HI = 6, 42                  # SQUARE centerline extremes
ARM = 8                         # plus arm length and minus half-width
PLUS_C = LO + ARM               # plus centre (14,14)
MINUS_C = 2 * CENTER - PLUS_C   # minus centre (34,34), point mirror of the plus


class ExposureCompensationRedraw(Solo48):
    icon_id = "exposure-compensation-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography/camera-settings"
    aliases = ("exposure value", "ev compensation", "plus minus exposure")
    keywords = ("exposure", "compensation", "ev", "camera", "brightness", "plus", "minus", "photo")

    def build(self) -> None:
        self.add_line("divider", (LO, HI), (HI, LO))

        c = PLUS_C
        self.add_line("plus-horizontal", (c - ARM, c), (c + ARM, c))
        self.add_line("plus-vertical", (c, c - ARM), (c, c + ARM))
        self.relate("connect", "plus-horizontal", "plus-vertical")

        m = MINUS_C
        self.add_line("minus", (m - ARM, m), (m + ARM, m))
