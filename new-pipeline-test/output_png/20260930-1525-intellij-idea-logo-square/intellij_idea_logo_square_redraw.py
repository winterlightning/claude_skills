"""intellij-idea-logo-square (redraw of the new-pipeline traced SVG).

Plan: the IntelliJ IDEA mark reduced to its tile and underscore bar, on
SQUARE (centerline box (6,6)-(42,42)).
- tile: one closed rounded square filling the centerline box, four r4
  quarter-circle corners on integer centres, so each arc apex is the
  keyshape edge.
- bar: a horizontal underscore in the lower-left of the tile, 12 long
  (a third of the tile), 9 from the left wall and 9 above the bottom wall.
The IJ lettering is omitted, as in the generated image (no-lettering brief).

Metric issues:
- clearance e0/e1 (5.26 apart on centerlines, need 8): fixed. The bar now
  starts at x=15 (9 from the wall at x=6) and sits at y=33 (9 from the wall
  at y=42). Exactly 8 came back as a mic review because the tile contour has
  curves, so both gaps are 9.
- stroke-width (trace 2.77 after fitting, target 4): handled by authoring at
  stroke 4 with the 8-unit gaps above.
Traced shape: 20260930-1525-intellij-idea-logo-square/intellij-idea-logo-square_raw.svg.
Lucide construction: lucide/square (rect with rx) for the rounded tile.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "66cf9f40-4254-4619-ba1e-7b78e0914552"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1525-intellij-idea-logo-square/"
    "intellij-idea-logo-square_raw.svg"
)
AUTHOR = "claude-opus-5-5"

LO, HI = 6, 42   # tile centerline box
R = 4            # corner radius
BAR_Y = 33       # 9 above the bottom wall
BAR_X0 = 15      # 9 right of the left wall (exact 8 is not certified next to a curved contour)
BAR_LEN = 12     # a third of the tile


class IntellijIdeaLogoSquareRedraw(Solo48):
    icon_id = "intellij-idea-logo-square-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ("intellij-idea", "intellij")
    keywords = ("intellij", "idea", "jetbrains", "ide", "logo", "brand", "developer", "code")

    def build(self) -> None:
        self.add_line("top", (LO + R, LO), (HI - R, LO))
        self.add_arc("corner-tr", (HI - R, LO), (HI, LO + R), radius_x=R, sweep=True)
        self.add_line("right", (HI, LO + R), (HI, HI - R))
        self.add_arc("corner-br", (HI, HI - R), (HI - R, HI), radius_x=R, sweep=True)
        self.add_line("bottom", (HI - R, HI), (LO + R, HI))
        self.add_arc("corner-bl", (LO + R, HI), (LO, HI - R), radius_x=R, sweep=True)
        self.add_line("left", (LO, HI - R), (LO, LO + R))
        self.add_arc("corner-tl", (LO, LO + R), (LO + R, LO), radius_x=R, sweep=True)
        self.add_contour(
            "tile",
            "top", "corner-tr", "right", "corner-br",
            "bottom", "corner-bl", "left", "corner-tl",
            closed=True,
        )

        self.add_line("bar", (BAR_X0, BAR_Y), (BAR_X0 + BAR_LEN, BAR_Y))
