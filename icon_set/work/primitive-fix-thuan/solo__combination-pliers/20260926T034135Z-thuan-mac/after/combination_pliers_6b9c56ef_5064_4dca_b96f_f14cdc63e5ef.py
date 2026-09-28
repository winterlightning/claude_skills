"""Combination pliers: a diagonal pair of pliers - curved handles at the bottom left, a pivot rivet, and closing jaws at the top right.

Symbol plan: mirror-symmetric about the diagonal x+y=48 ((x, y) -> (48-y, 48-x)). The
pivot is a small rivet ring (r3, the approved 6-diameter circle) at (24,24); four strokes
leave it at its cardinal points (shared endpoints): two handles bowing outward down to the
bottom-left edges, and two jaws that swell outward and turn back in so their tips close
to a narrow gap at the top right.
An outlined single-silhouette version (the reference's drawing style) was built first; at
48 with 8-unit clearances its jaws and handles collapsed into a star-shaped blob with no
pivot, so the tool is drawn with strokes around a visible rivet instead.
Lucide construction: none for pliers; 'scissors'-style strokes crossing at a pivot.
Keyshape SQUARE: centerline x 6..42 (handle end, lower jaw), y 6..42 (upper jaw, handle end).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6b9c56ef-5064-4dca-b96f-f14cdc63e5ef"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__combination-pliers/20260926T034135Z-thuan-mac/reference/tools pliers_6b9c56ef-5064-4dca-b96f-f14cdc63e5ef.svg"
AUTHOR = "claude-opus-5-5"


def _m(p):
    """Mirror across the diagonal x+y=48."""
    return (48 - p[1], 48 - p[0])


class CombinationPliers(Solo48):
    icon_id = "combination-pliers"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tool"
    aliases = ("pliers", "tools pliers", "lineman pliers")
    keywords = ("pliers", "tool", "grip", "repair", "hardware", "electrician", "diy", "workshop")

    def build(self) -> None:
        cx, cy, r = 24, 24, 3
        left, top, right, bottom = (cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)
        names = ("rivet-nw", "rivet-ne", "rivet-se", "rivet-sw")
        pts = (left, top, right, bottom)
        for i, name in enumerate(names):
            self.add_arc(name, pts[i], pts[(i + 1) % 4], radius_x=r)
        self.add_contour("rivet", *names, closed=True)
        # handles: left point -> bottom-left edge, bottom point -> bottom edge (mirrors)
        self.add_bezier("handle-1", left, ((16, 24), (9, 27), (6, 34)))
        self.add_bezier("handle-2", bottom, (_m((16, 24)), _m((9, 27)), _m((6, 34))))
        # jaws: top point and right point -> tips near the top-right corner (mirrors)
        self.add_bezier("jaw-1", top, ((24, 14), (28, 6), (34, 6)))
        self.add_bezier("jaw-2", right, (_m((24, 14)), _m((28, 6)), _m((34, 6))))
        for part in ("handle-1", "handle-2", "jaw-1", "jaw-2"):
            self.relate("connect", "rivet", part)
