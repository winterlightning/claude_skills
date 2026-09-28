"""West compass marker: a left-pointing notched dart arrowhead beside the letter W.

Plan: HRECT_L centerline box (4,8)-(44,40). Arrowhead: closed dart mirrored about y=24,
tip (4,24) on the left extreme, back corners (20,10)/(20,38) and a back notch at (17,24);
notch depth 3 is the deepest that keeps the notch 8 clear of the opposite edges.
Letter W: 16 wide with upright outer legs (28 and 44, full height 8-40) and a middle apex
at (36,22), exactly 8 from each outer leg; the arrow back sits 8 clear of the W's left leg.
Attempt 1 (slanted-leg W + plain triangle, kept in attempt-1-triangle/) validated but made
the arrow too small against the reference; this version keeps the reference's large notched
dart. Reduction: the reference's circle around the W is dropped (a legible W at stroke 4
needs a ring of r>=18, which leaves no width for the arrow). Lucide `navigation-2`
informed the notched dart; no Lucide W.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "68aa7319-a9e3-4030-8fbb-2d42e243d96f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__west-direction-marker/20260927T101553Z-thuan-mac-1/reference/compass west_68aa7319-a9e3-4030-8fbb-2d42e243d96f.svg"
AUTHOR = "claude-opus-5-5"


class WestDirectionMarker(Solo48):
    icon_id = "west-direction-marker"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "navigation"
    categories = ("navigation", "primitives")
    aliases = ()
    keywords = ("west", "direction", "compass", "navigation", "arrow", "orientation", "marker")

    def build(self) -> None:
        cy, half = 24, 14
        self.add_polyline("arrow", (20, cy - half), (4, cy), (20, cy + half), (17, cy), closed=True)
        self.add_polyline("letter-w", (28, 8), (28, 40), (36, 22), (44, 40), (44, 8))
