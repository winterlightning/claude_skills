"""One plain clove-like bud, broad at its head and tapered to a curved stalk.

VRECT_L extrema (8,4)-(40,44). The silhouette is one continuous symbol;
the original's ambiguity is preserved without adding invented bud seams.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "f6f8dff7-4bbf-4a12-a864-fabb05b563d8"
SOURCE_PATH = "pictographic-primitives/_uncategorized_11/clove_f6f8dff7-4bbf-4a12-a864-fabb05b563d8.svg"
AUTHOR = "gpt-6"


class SingleSpiceCloveBud(Solo48):
    icon_id = "single-spice-clove-bud"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/spices"
    aliases = ("clove", "clove silhouette")
    keywords = ("spice", "bud", "stalk")

    def build(self) -> None:
        self.add_bezier("outline", (30, 4),
            ((35, 4), (40, 10), (40, 16)),
            ((40, 22), (35, 24), (30, 27)),
            ((26, 30), (23, 39), (18, 42)),
            ((14, 44), (11, 44), (8, 44)),
            ((8, 39), (16, 34), (18, 25)),
            ((20, 21), (16, 19), (16, 16)),
            ((16, 10), (23, 4), (30, 4)))
        self.add_contour("bud", "outline", closed=True)
