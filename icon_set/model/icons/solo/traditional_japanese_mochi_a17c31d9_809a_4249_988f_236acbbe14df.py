"""A rounded mochi outline surrounding a smaller bottom-open filling arc.

Symbol plan: paired open contours share the vertical axis x=24; their
upper lobes use mirrored cubic controls and the lower ends stay separate.
Lucide circle informed the symmetric four-extreme silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "a17c31d9-809a-4249-988f-236acbbe14df"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/mochi_a17c31d9-809a-4249-988f-236acbbe14df.svg"
AUTHOR = "gpt-6"


class TraditionalJapaneseMochi(Solo48):
    icon_id = "traditional-japanese-mochi"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/desserts"
    aliases = ("mochi", "rounded rice cake")
    keywords = ("rice", "cake", "filling", "japanese")

    def build(self) -> None:
        self.add_bezier(
            "mochi-outer", (21, 42),
            ((12, 40), (6, 32), (6, 24)),
            ((6, 14), (14, 6), (24, 6)),
            ((34, 6), (42, 14), (42, 24)),
            ((42, 32), (36, 40), (27, 42)),
        )
        self.add_bezier(
            "mochi-filling", (19, 31),
            ((17, 31), (16, 30), (16, 28)),
            ((16, 24), (20, 22), (24, 22)),
            ((28, 22), (32, 24), (32, 28)),
            ((32, 30), (31, 31), (29, 31)),
        )
