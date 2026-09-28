"""A brick trowel: a capsule handle, a straight shank and a triangular blade on a diagonal.

Symbol plan: the tool axis runs along (4,-3) (about 37 degrees), so the perpendicular
(3,4) is a whole grid step of 5. The handle is a capsule of two r5 caps centred (39,13)
and (31,19); the shank leaves the near cap's tip (27,22) along the axis to the blade's
base centre (19,28), 10 clear of the handle. The blade base runs perpendicular to the axis
from (13,20) to (25,36) and its point sits at the lower-left corner (4,40), which lies on
the axis within a unit, so both blade edges are near mirror images about it.
Lucide construction: no trowel glyph; Lucide 'paintbrush'-style capsule handle on a
diagonal tool axis.
Keyshape HRECT_L: centerline x 4..44 (blade point, handle cap), y 8..40 (cap, point).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ab28c662-ca28-5468-96ca-7027884adf42"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__brick-trowel/20260926T030905Z-thuan-mac/reference/tools palette trowel_ab28c662-ca28-5468-96ca-7027884adf42.svg"
AUTHOR = "claude-opus-5-5"


class BrickTrowel(Solo48):
    icon_id = "brick-trowel"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools/construction"
    aliases = ("tools-palette-trowel", "trowel", "mason-trowel")
    keywords = ("trowel", "brick", "mason", "masonry", "mortar", "plaster", "construction", "tool", "diy")

    def build(self) -> None:
        # handle capsule
        self.add_arc("handle-cap-far", (42, 17), (36, 9), radius_x=5, sweep=False)
        self.add_line("handle-side-top", (36, 9), (28, 15))
        self.add_arc("handle-cap-near-1", (28, 15), (27, 22), radius_x=5, sweep=False)
        self.add_arc("handle-cap-near-2", (27, 22), (34, 23), radius_x=5, sweep=False)
        self.add_line("handle-side-bottom", (34, 23), (42, 17))
        self.add_contour("handle", "handle-cap-far", "handle-side-top", "handle-cap-near-1",
                         "handle-cap-near-2", "handle-side-bottom", closed=True)
        # shank and blade
        self.add_line("shank", (27, 22), (19, 28))
        self.add_polyline("blade", (13, 20), (19, 28), (25, 36), (4, 40), closed=True)
        self.relate("connect", "handle", "shank")
        self.relate("connect", "shank", "blade")
