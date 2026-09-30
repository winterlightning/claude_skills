"""breakfast-pancake-stack (redraw of the new-pipeline traced SVG).

Plan: HRECT_L (centerline box (4,8)-(44,40)), the suggested keyshape (source
aspect 1.15, fit score 1.17).
- stack: the closed outline of the three pancakes. Top rim (8,16)-(40,16) and
  bottom rim (40,40)-(8,40) are loose lines connected at their shared
  endpoints to two scallop contours; each side is three r4 semicircles about
  x=8 / x=40 (centres y=20, 28, 36), so the stack reaches x=4 and x=44 and
  every pancake shows its own rounded rim. The scallops meet in cusps at
  y=24 and y=32 that mark the pancake boundaries.
- layers: two short dividers (17,24)-(31,24) and (17,32)-(31,32) continue the
  cusps inward. Each stops 9 short of its cusps (a curved pair exactly on 8
  comes back `review`) and sits exactly 8 from its neighbour and from the
  straight rims, so the stack has one open interior instead of three thin
  sealed bands.
- butter: a pat on top, the line (18,8)-(30,8) on the top extreme, centred on
  the stack axis x=24 and 8 above the top edge.
Mirrored about x=24 throughout.

Metric issues:
- clearance e0/e1, e1/e2, e2/e3 (3.25, 2.46, 2.37 on centerlines): fixed. The
  butter is 8 above the stack and the pancakes no longer sit as separate
  outlines 2-3 apart; their boundaries are drawn as cusps and dividers with
  8-unit spacing.
- holes at (19.2,10.5), (9,19.5), (9,28.2), (9.1,36.8), 1.2-2.4 wide: fixed.
  The butter is an open stroke (no hole) and the pancakes share one interior
  hole of 24x24 centerline, well over 6 inscribed.
- keyshape-short-axis (x filled 92%): fixed, scallops reach x=4 and x=44 and
  the butter and bottom edge reach y=8 and y=40.
- stroke-width (trace 2.46 vs 4): handled by laying out at stroke 4.
Not kept: three separately closed capsules plus a hollow butter pat need at
least 10+8+10+8+10 of height (6 inscribed holes, 8 gaps) for the pancakes
alone, plus 18 for a hollow pat; the HRECT_L height is 32.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "799ea4de-0531-534a-9c5e-9d0bf37abe6f"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1943-breakfast-pancake-stack/"
    "breakfast-pancake-stack_raw.svg"
)
AUTHOR = "claude-opus-5-5"

LEFT, RIGHT = 8, 40          # scallop centres
TOP, BOTTOM = 16, 40         # stack top and bottom edges
BOUNDS = (24, 32)            # pancake boundaries (cusps + dividers)
R = 4                        # scallop radius
DIVIDER = (17, 31)           # divider x span, 9 inside each cusp
BUTTER_Y, BUTTER = 8, (18, 30)


class BreakfastPancakeStackRedraw(Solo48):
    icon_id = "breakfast-pancake-stack-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("pancake stack", "pancakes", "hotcakes", "flapjacks")
    keywords = ("pancake", "breakfast", "butter", "food", "brunch", "stack")

    def build(self) -> None:
        ys = (TOP, *BOUNDS, BOTTOM)
        # The straight rims stay loose lines so the dividers 8 below/above
        # them are measured line to line; each scallop side is one contour.
        self.add_line("stack-top", (LEFT, TOP), (RIGHT, TOP))
        self.add_line("stack-bottom", (RIGHT, BOTTOM), (LEFT, BOTTOM))
        for side, x, sweep in (("right", RIGHT, True), ("left", LEFT, False)):
            members = []
            for i in range(3):
                self.add_arc(f"stack-{side}-{i + 1}", (x, ys[i]), (x, ys[i + 1]),
                             radius_x=R, sweep=sweep)
                members.append(f"stack-{side}-{i + 1}")
            self.add_contour(f"stack-{side}", *members)
            self.relate("connect", "stack-top", f"stack-{side}")
            self.relate("connect", "stack-bottom", f"stack-{side}")

        for i, y in enumerate(BOUNDS):
            self.add_line(f"layer-{i + 1}", (DIVIDER[0], y), (DIVIDER[1], y))

        self.add_line("butter", (BUTTER[0], BUTTER_Y), (BUTTER[1], BUTTER_Y))


if __name__ == "__main__":
    import sys
    from pathlib import Path

    here = Path(__file__).resolve().parent
    icon = BreakfastPancakeStackRedraw()
    print(icon.validate_icon().describe())
    if "--export" in sys.argv:
        icon.export_icon_to(here / "breakfast-pancake-stack_redraw.svg")
