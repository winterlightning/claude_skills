"""intellij-idea-logo (redraw of the new-pipeline traced SVG).

Plan: the IntelliJ IDEA "IJ" monogram with its signature underline, three
separate strokes on SQUARE (centerline box (6,6)-(42,42)).
- I: a straight upright at x=10 from the top y=6 down to y=34.
- J: an upright at x=38 from y=6 down to y=26, a radius-8 quarter arc about
  (30,26) that turns it tangent-continuously into a horizontal foot at y=34,
  and the foot running left to x=20. Both letters share top (y=6) and
  baseline (y=34) and sit mirrored about x=24 (10 / 38).
- underline: one horizontal stroke at y=42 from x=6 to x=42. It carries the
  left, right and bottom keyshape extremes; the letter tops carry the top.
Traced shape: 20260930-1522-intellij-idea-logo/intellij-idea-logo_raw.svg
and intellij-idea-logo.png (read for the subject only; nothing copied from
its coordinates).
Lucide: no useful match (lucide has no JetBrains/IntelliJ mark); the J hook
follows the usual Lucide straight-line + quarter-arc construction.
Letters: a logo monogram, drawn as the logo's own strokes rather than the
typeface glyphs, which would not read as the IntelliJ mark.

Metric issues:
- stroke-width (info): drawn at stroke 4; every gap is budgeted for 4.
- keyshape-short-axis (x filled 73%): fixed. The underline spans the full
  box width (6..42) and the letters widen to x=10 / x=38, so all four
  SQUARE extremes sit exactly on the box.
- clearance e0/e2 (7.75, need 8): fixed. The I ends at y=34, exactly 8
  above the underline at y=42.
- clearance e1/e2 (7.63, need 8): fixed. The J foot runs on y=34, exactly 8
  above the underline; the J foot tip (20,34) is also 10 clear of the I.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f4752828-8f41-472e-a48e-c509754917dd"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1522-intellij-idea-logo/"
    "intellij-idea-logo_raw.svg"
)
AUTHOR = "claude-opus-5-5"

TOP = 6          # shared letter top
BASE = 34        # shared letter baseline
LINE_Y = 42      # underline, 8 below the baseline
I_X = 10         # I stem; the J stem is its mirror about x=24
J_X = 38
HOOK_R = 8       # J quarter arc radius
FOOT_END = 20    # J foot tip, 10 clear of the I


class IntellijIdeaLogoRedraw(Solo48):
    icon_id = "intellij-idea-logo-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ("intellij", "jetbrains-idea")
    keywords = ("intellij", "idea", "jetbrains", "ide", "java", "logo", "brand", "developer", "code")

    def build(self) -> None:
        self.add_line("i-stem", (I_X, TOP), (I_X, BASE))

        self.add_line("j-stem", (J_X, TOP), (J_X, BASE - HOOK_R))
        self.add_arc("j-hook", (J_X, BASE - HOOK_R), (J_X - HOOK_R, BASE), radius_x=HOOK_R, sweep=True)
        self.add_line("j-foot", (J_X - HOOK_R, BASE), (FOOT_END, BASE))
        self.add_contour("j", "j-stem", "j-hook", "j-foot")

        self.add_line("underline", (6, LINE_Y), (42, LINE_Y))
