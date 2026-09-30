"""circle-colon (redraw of the new-pipeline traced SVG).

Plan: a colon (two stacked marks on the vertical axis x=24) inside a round
outline, on CIRCLE (centerline radius 20 about (24,24)).
- ring: two semicircles r20 split at the top and bottom apexes (24,4)/(24,44),
  so the outline touches the CIRCLE extremes exactly and is proved as a circle.
- colon: two solid discs mirrored about y=24 at (24, 24 -/+ 7), each a closed
  r2 circle (two semicircles), which at stroke 4 paints an 8-wide disc with
  no hole; a plain stroke dot (4 wide) looked too light against the ring.
No useful Lucide match beyond the plain `circle` construction, which the ring
follows. Symmetric about both axes.

Metric issues (circle-colon_metrics.json) and how they were handled:
- stroke-width (info): redrawn at stroke 4; the budget below uses it.
- clearance e1/e2 (the two marks 5.99 apart): the discs are 10 apart on
  centerlines (14 - 2*2 >= 8) and 11 from the ring (20 - 7 - 2 >= 8).
- holes at (23.9,17.5) and (23.9,30.1) (2.4 wide, need 6): the hollow marks
  are drawn as solid discs, so no hole remains. Hollow marks cannot pass inside
  the ring: a ring of radius r needs r >= 5 for a 6-wide hole, and then its
  centre offset d must satisfy d >= r + 4 (8 between the two rings) and
  d + r + 8 <= 20 (8 to the outline), i.e. 2r + 12 <= 20, r <= 4. The hollow
  look of the generated image is therefore dropped; a colon reads as dots.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6a0ef6b0-613d-4883-ad08-e75fd510a4f6"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1916-circle-colon/circle-colon_raw.svg"
AUTHOR = "claude-opus-5-5"

C = 24          # centre and shared axis
R = 20          # CIRCLE centerline radius
DOT_OFFSET = 7  # disc centres 14 apart
DOT_R = 2       # r2 ring at stroke 4 paints a solid disc 8 wide


class CircleColonRedraw(Solo48):
    icon_id = "circle-colon-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/punctuation"
    aliases = ("colon in circle", "circled colon")
    keywords = ("colon", "punctuation", "ratio", "time separator", "circle", "divider")

    def build(self) -> None:
        top, bottom = (C, C - R), (C, C + R)
        self.add_arc("ring-right", top, bottom, radius_x=R, sweep=True)
        self.add_arc("ring-left", bottom, top, radius_x=R, sweep=True)
        self.add_contour("ring", "ring-right", "ring-left", closed=True)

        for name, cy in (("dot-top", C - DOT_OFFSET), ("dot-bottom", C + DOT_OFFSET)):
            self.add_arc(f"{name}-r", (C, cy - DOT_R), (C, cy + DOT_R), radius_x=DOT_R, sweep=True)
            self.add_arc(f"{name}-l", (C, cy + DOT_R), (C, cy - DOT_R), radius_x=DOT_R, sweep=True)
            self.add_contour(name, f"{name}-r", f"{name}-l", closed=True)
