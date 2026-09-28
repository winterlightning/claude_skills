"""A long coat with broad sleeves, paired lapels, and a central opening.

The silhouette follows the source coat. Lucide shirt informed the continuous
garment boundary; paired sleeve and lapel coordinates share the x=24 axis.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d94018b9-07e2-45ee-8c77-48c33f5b5d6b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__collared-long-sleeve-coat/20260927T164357Z-thuan-mac-1/reference/coat_d94018b9-07e2-45ee-8c77-48c33f5b5d6b.svg"
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = "collared-long-sleeve-coat"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "clothing"
    aliases = ("coat",)
    keywords = ("long", "collar", "sleeves")

    def build(self):
        self.add_polyline(
            "coat-outline",
            (20, 6), (28, 6), (32, 8), (38, 12), (42, 34),
            (34, 36), (34, 42), (14, 42), (14, 36),
            (6, 34), (10, 12), (16, 8),
            closed=True,
        )
        self.add_polyline("collar", (16, 8), (24, 17), (32, 8))
        self.add_line("opening", (24, 17), (24, 42))
        self.add_line("left-sleeve-seam", (14, 36), (16, 26))
        self.add_line("right-sleeve-seam", (34, 36), (32, 26))
        for detail in ("collar", "opening", "left-sleeve-seam", "right-sleeve-seam"):
            self.relate("connect", "coat-outline", detail)
        self.relate("connect", "collar", "opening")
