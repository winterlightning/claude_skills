"""codefactor-logo (redraw of the new-pipeline traced SVG).

Plan: three rings in a column on the left with two list bars to their
right (top bar long, middle bar short), on SQUARE (centerline box
(6,6)-(42,42)).
- rings: r6 about x=12, centres y=12/24/36, so the column spans the full
  36 of the box height; each ring is split at its top and bottom points
  and neighbouring rings share the tangency point (y=18, y=30), declared
  as connect.
- bars: start at x=26 (8 clear of the ring edge at x=18); top bar runs to
  x=42 (the right extreme), the middle bar to x=36 (long:short ~ 1.6, as
  in the generated image).

Metric issues fixed:
- stroke-width: redrawn at stroke 4; every gap re-budgeted at stroke 4.
- keyshape-short-axis: the ring column now fills the SQUARE's y axis
  exactly (6..42) instead of 87%.
- clearance e0/e1, e2/e3: bars start 8 from the ring centerlines.
- hole x3: rings grow from r~3.8 to r6, hole 8 inscribed (need 6).
- clearance e0/e2, e2/e4: three r>=5 rings with 8-unit gaps need 46 of
  height and the box has 36, so the rings touch instead: a declared
  tangent contact, not a gap.
Traced shape: new-pipeline-test/output_png/20260929-1927-codefactor-logo/
codefactor-logo_raw.svg. Lucide construction: list-todo / list (bullet
column + bars); the rings are larger here to keep a readable hole.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "de32221d-3ae3-4517-b767-d8728cf1083f"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1927-codefactor-logo/codefactor-logo_raw.svg"
)
AUTHOR = "claude-opus-5-5"

RING_X = 12
RING_R = 6
RING_YS = (12, 24, 36)
BAR_X0 = RING_X + RING_R + 8   # 26
BAR_ENDS = (42, 36)            # top (long), middle (short)


class CodefactorLogoRedraw(Solo48):
    icon_id = "codefactor-logo-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ("codefactor",)
    keywords = ("codefactor", "logo", "brand", "code", "quality", "list", "review")

    def build(self) -> None:
        for i, cy in enumerate(RING_YS):
            top, bottom = (RING_X, cy - RING_R), (RING_X, cy + RING_R)
            self.add_arc(f"ring{i}-r", top, bottom, radius_x=RING_R, sweep=True)
            self.add_arc(f"ring{i}-l", bottom, top, radius_x=RING_R, sweep=True)
            self.add_contour(f"ring{i}", f"ring{i}-r", f"ring{i}-l", closed=True)
        self.relate("connect", "ring0", "ring1")
        self.relate("connect", "ring1", "ring2")

        for i, x1 in enumerate(BAR_ENDS):
            cy = RING_YS[i]
            self.add_line(f"bar{i}", (BAR_X0, cy), (x1, cy))
