"""A plain magnifying glass (explore / search): a large round lens with a straight handle.

Symbol plan: the lens is a circle of radius 14 about (20,20), drawn as r14 quarter arcs
through its cardinal points, with the lower-right quarter split at the handle joint
(30,30) on the diagonal (14.1 from the centre, a hair outside the true circle), as large as the reference lens.
The handle runs straight from the joint to the bottom-right corner (42,42), in line with
the lens centre.
Lucide construction: 'search' - circle lens with a straight diagonal handle.
Keyshape SQUARE: centerline x 6..42, y 6..42 (lens extremes, handle end).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "aaa50182-047b-43ed-8260-9042ec663a23"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__plain-magnifying-glass/20260926T035939Z-thuan-mac/reference/explore_aaa50182-047b-43ed-8260-9042ec663a23.svg"
AUTHOR = "claude-opus-5-5"


class PlainMagnifyingGlass(Solo48):
    icon_id = "plain-magnifying-glass"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface/search"
    aliases = ("explore", "magnifier", "search")
    keywords = ("search", "magnifying", "glass", "explore", "find", "zoom", "lens", "look")

    def build(self) -> None:
        L, T, J = (6, 20), (20, 6), (30, 30)
        Rt, B = (34, 20), (20, 34)
        self.add_arc("lens-top-left", L, T, radius_x=14, sweep=True)
        self.add_arc("lens-top-right", T, Rt, radius_x=14, sweep=True)
        self.add_arc("lens-right-lower", Rt, J, radius_x=14, sweep=True)
        self.add_arc("lens-bottom-right", J, B, radius_x=14, sweep=True)
        self.add_arc("lens-bottom-left", B, L, radius_x=14, sweep=True)
        self.add_contour("lens", "lens-top-left", "lens-top-right", "lens-right-lower", "lens-bottom-right",
                         "lens-bottom-left", closed=True)
        self.add_line("handle", J, (42, 42))
        self.relate("connect", "lens", "handle")
