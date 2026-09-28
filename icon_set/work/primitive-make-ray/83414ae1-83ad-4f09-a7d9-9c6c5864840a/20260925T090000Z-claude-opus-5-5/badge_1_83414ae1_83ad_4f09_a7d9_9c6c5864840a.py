"""Badge: an eight-point starburst seal made of a square overlaid on a diamond.

Symbol plan: one closed 16-vertex contour, 8-fold symmetric about (24,24).
Diamond tips on the CIRCLE radius 20; square corners at (24+-14, 24+-14)
(radius 19.8); the inner notches are where the square's sides cross the
diamond's sides, so every edge lies on one of the two base squares. Round
joins give the reference's softened points. Lucide: `badge` (scalloped
seal) informed the single-outline construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "83414ae1-83ad-4f09-a7d9-9c6c5864840a"
SOURCE_PATH = "icon_set/work/todo-references/badge 1_83414ae1-83ad-4f09-a7d9-9c6c5864840a.svg"
AUTHOR = "claude-opus-5-5"

C, TIP, SQ = 24, 20, 14
NOTCH = TIP - SQ          # square side meets diamond side at (SQ, TIP - SQ)


class Badge1(Solo48):
    icon_id = "badge-1"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/badge"
    aliases = ("seal", "starburst badge", "rosette seal")
    keywords = ("badge", "seal", "star", "octagram", "certified", "verified")

    def build(self) -> None:
        # One eighth, relative to centre, then rotated by quarter turns.
        eighth = [(0, -TIP), (NOTCH, -SQ), (SQ, -SQ), (SQ, -NOTCH)]
        pts = []
        for k in range(4):
            for x, y in eighth:
                for _ in range(k):
                    x, y = -y, x
                pts.append((C + x, C + y))
        self.add_polyline("outline", *pts, closed=True)
