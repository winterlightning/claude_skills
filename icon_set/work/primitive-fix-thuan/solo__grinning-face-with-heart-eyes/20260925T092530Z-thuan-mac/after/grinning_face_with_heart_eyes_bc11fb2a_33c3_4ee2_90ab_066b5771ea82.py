"""Grinning face with heart eyes: two heart-shaped eyes above a wide open
D-shaped grin.

Symbol plan: both eyes are one heart definition (two cubic lobes whose tops
and outer sides are exact nodes, a V notch at the dip, curved sides into a
bottom point) instanced at x = 12 and 36, mirrored about x = 24. The grin is
a closed D: a straight top and a radius-12 half circle. The reference's
face circle is omitted: inside a radius-20 rim every feature must stay within
radius 12 of the centre, which leaves no room for heart holes of the
required 6-unit inscribed size (attempts/ keeps that ringed attempt).
Keyshape SQUARE, centerline box (6,6)-(42,42).
Lucide construction: laugh (D-shaped open grin) and heart (two lobes into a
point).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "bc11fb2a-33c3-4ee2-90ab-066b5771ea82"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__grinning-face-with-heart-eyes/20260925T092530Z-thuan-mac/reference/face grin hearts_bc11fb2a-33c3-4ee2-90ab-066b5771ea82.svg"
AUTHOR = "claude-opus-5-5"


class GrinningFaceWithHeartEyes(Solo48):
    icon_id = "grinning-face-with-heart-eyes"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "emoji"
    aliases = ("heart eyes", "in love", "smiling face with heart eyes")
    keywords = ("face", "grin", "heart", "love", "eyes", "emoji")

    def build(self) -> None:
        for index, cx in enumerate((12, 36), 1):
            self.heart(f"eye-{index}", cx)
        self.add_line("grin-1", (12, 30), (36, 30))
        self.add_arc("grin-2", (36, 30), (12, 30), radius_x=12)
        self.add_contour("grin", "grin-1", "grin-2", closed=True)

    def heart(self, name, cx, top=6, half=6, side_y=10, dip_y=9, bottom=19):
        lobe = half // 2
        self.add_bezier(name, (cx, bottom),
                        ((cx + 3, bottom - 3), (cx + half, side_y + 4), (cx + half, side_y)),
                        ((cx + half, side_y - 2.5), (cx + lobe + 1.8, top), (cx + lobe, top)),
                        ((cx + lobe - 1.5, top), (cx + 1.2, dip_y - 1.5), (cx, dip_y)),
                        ((cx - 1.2, dip_y - 1.5), (cx - lobe + 1.5, top), (cx - lobe, top)),
                        ((cx - lobe - 1.8, top), (cx - half, side_y - 2.5), (cx - half, side_y)),
                        ((cx - half, side_y + 4), (cx - 3, bottom - 3), (cx, bottom)))
        self.add_contour(f"{name}-outline", name, closed=True)
