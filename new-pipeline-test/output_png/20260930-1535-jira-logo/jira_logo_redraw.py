"""jira-logo (redraw of the new-pipeline traced SVG).

Plan: the Jira mark as three bent ribbons staggered diagonally from lower
left to upper right on SQUARE (centerline box (6,6)-(42,42)). Each ribbon is
one open stroke: a horizontal top arm, a shared-radius r6 bend, and a
vertical arm dropping from the right end. Ribbons step 10 up-right, so every
parallel arm pair sits 10 apart on centerlines (6 of ink), and they grow
from the lower-left (16x16) to the upper-right (20x22), as in the trace.
- ribbon-l: top y=26, right x=22, from x=6 down to y=42 (touches left/bottom)
- ribbon-m: top y=16, right x=32, from x=14 down to y=36
- ribbon-u: top y=6,  right x=42, from x=22 down to y=28 (touches top/right)

Metric issues:
- stroke-width (info): redrawn at stroke 4; spacing was budgeted for it.
- clearance e0/e1 (5.55) and e1/e2 (4.96): fixed, the ribbons are now 10
  apart on centerlines.
- holes 3.26 / 2.41 / 1.41 (need 6 inscribed): fixed by dropping the hollow
  ribbon outlines. A hollow ribbon needs an arm 10 wide between centerlines;
  three of them plus two 8 gaps need 46 units on each axis, the SQUARE box has
  36. Each ribbon is therefore drawn as its single centre stroke, which
  leaves no enclosed holes.
Traced shape: 20260930-1535-jira-logo/jira-logo_raw.svg.
No useful Lucide match: Lucide has no Jira mark; the r6 bend follows the
corner-up-right construction (a straight arm, a quarter arc, a straight arm).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "725a957e-63e3-4f03-87bd-d37db9fb9241"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1535-jira-logo/jira-logo_raw.svg"
AUTHOR = "claude-opus-5-5"

BEND_R = 6
# name, left x of the top arm, top y, right x, bottom y of the vertical arm
RIBBONS = (
    ("ribbon-l", 6, 26, 22, 42),
    ("ribbon-m", 14, 16, 32, 36),
    ("ribbon-u", 22, 6, 42, 28),
)


class JiraLogoRedraw(Solo48):
    icon_id = "jira-logo-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ("jira", "jira-software")
    keywords = ("jira", "atlassian", "logo", "brand", "issue", "tracker", "agile")

    def build(self) -> None:
        for name, left, top, right, bottom in RIBBONS:
            self.add_line(f"{name}-top", (left, top), (right - BEND_R, top))
            self.add_arc(
                f"{name}-bend", (right - BEND_R, top), (right, top + BEND_R),
                radius_x=BEND_R, sweep=True,
            )
            self.add_line(f"{name}-drop", (right, top + BEND_R), (right, bottom))
            self.add_contour(name, f"{name}-top", f"{name}-bend", f"{name}-drop")


if __name__ == "__main__":
    from pathlib import Path

    from icon_set.renderers.png import render_png

    here = Path(__file__).resolve().parent
    icon = JiraLogoRedraw()
    print(icon.validate_icon().describe())
    icon.export_icon_to(here / "jira-logo_redraw.svg")
    (here / "jira-logo_redraw.png").write_bytes(render_png(icon, scale=8))
    (here / "jira-logo_redraw-48.png").write_bytes(render_png(icon))
