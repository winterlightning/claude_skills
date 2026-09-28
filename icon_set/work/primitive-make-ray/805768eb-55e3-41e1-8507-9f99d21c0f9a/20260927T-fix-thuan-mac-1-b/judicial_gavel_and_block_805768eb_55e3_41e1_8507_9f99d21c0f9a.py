"""Judge's gavel above its sound block.

Symbol plan: the gavel lies on the 45-degree diagonal. Head = rectangle
10 along the handle axis by 14 across it (corners (20,6) (30,16) (16,30)
(6,20)), so it reads as a mallet head, not a diamond. The handle leaves the
middle of the head's lower-right face (23,23) and runs to (42,42). Sound
block = low trapezoid 8 below the head, open at the base like the reference.
Revision: the rejected drawing used a square diamond head and a bracket
block; the reference has an oblong mallet head and a splayed block.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "805768eb-55e3-41e1-8507-9f99d21c0f9a"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__judicial-gavel-and-block/20260927T153253Z-thuan-mac-1/reference/judge_805768eb-55e3-41e1-8507-9f99d21c0f9a.svg"
AUTHOR = "claude-opus-5-5"


class JudicialGavelAndBlock(Solo48):
    icon_id = "judicial-gavel-and-block"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "law"
    categories = ("primitives", "law")
    aliases = ("judge", "gavel", "court")
    keywords = ("gavel", "judge", "court", "law", "justice", "auction", "verdict")

    def build(self) -> None:
        self.add_line("head-top", (20, 6), (30, 16))
        self.add_line("head-face-upper", (30, 16), (23, 23))
        self.add_line("head-face-lower", (23, 23), (16, 30))
        self.add_line("head-bottom", (16, 30), (6, 20))
        self.add_line("head-back", (6, 20), (20, 6))
        self.add_contour("head", "head-top", "head-face-upper", "head-face-lower",
                         "head-bottom", "head-back", closed=True)
        self.add_line("handle", (23, 23), (42, 42))
        self.relate("connect", "head", "handle")
        self.add_polyline("block", (6, 42), (8, 38), (22, 38), (24, 42))
