"""jira-software-logo (redraw of the new-pipeline traced SVG).

Plan: the Jira Software emblem, three bent ribbons stepped diagonally from
the lower left to the upper right, on SQUARE (centerline box (6,6)-(42,42)).
- One repeat definition, a chevron: a horizontal top arm of length ARM
  that turns down through an r CORNER_R arc into a vertical arm of the
  same length, both ends round-capped.
- Three copies, each STEP further down-left along the diagonal, so they
  nest like the trace: chevron 0 turns at (42,6), chevron 1 at (33,15), and
  chevron 2 at (24,24), the canvas centre. ARM = 2 * STEP, the same
  ribbon-to-step ratio as the generated image.
- Each ribbon is drawn as a single stroke instead of a hollow outline. A
  hollow ribbon needs an arm 10 wide on centerlines (6 hole + 4 stroke), so
  each step would have to be at least 18 (10 + 8 clearance). Three steps
  would then need more than 36, the whole box.

Metric issues fixed:
- clearance e0/e1 (3.21) and e1/e2 (3.34): neighbouring chevrons are now
  STEP = 9 apart on parallel centerlines (need 8).
- holes at [38.3,9.7], [33.8,14.8], [29.0,19.1], [19.4,28.6] (1.2-3.4
  wide): there are no enclosed holes now, because every ribbon is an open
  stroke.
- stroke-width info: drawn at the profile stroke 4, and the clearance is
  budgeted at that stroke.
Not kept: the diagonal cut at each ribbon end. A 45-degree hook at the end
comes within 7 of the next chevron.
No useful Lucide match: Lucide has no Jira or Atlassian mark.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0697abc9-3868-4637-8bea-f5804a5c6af5"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1538-jira-software-logo/jira-software-logo_raw.svg"
)
AUTHOR = "claude-opus-5-5"

TOP_CORNER = (42, 6)   # outer corner of the upper-right chevron
STEP = 9               # diagonal offset between chevrons (>= 8 clearance)
ARM = 2 * STEP         # arm length from corner to cap
CORNER_R = 6
COUNT = 3


class JiraSoftwareLogoRedraw(Solo48):
    icon_id = "jira-software-logo-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ("jira", "jira-software")
    keywords = ("jira", "atlassian", "software", "logo", "brand", "chevrons", "agile")

    def build(self) -> None:
        for i in range(COUNT):
            cx, cy = TOP_CORNER[0] - i * STEP, TOP_CORNER[1] + i * STEP
            name = f"ribbon-{i + 1}"
            self.add_line(f"{name}-top", (cx - ARM, cy), (cx - CORNER_R, cy))
            self.add_arc(
                f"{name}-turn", (cx - CORNER_R, cy), (cx, cy + CORNER_R),
                radius_x=CORNER_R, sweep=True,
            )
            self.add_line(f"{name}-side", (cx, cy + CORNER_R), (cx, cy + ARM))
            self.add_contour(name, f"{name}-top", f"{name}-turn", f"{name}-side")
