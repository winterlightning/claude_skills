"""A ship's anchor with a ring, stock, and mirrored curved arms."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "034b7012-646c-415d-b54b-2efd12d0ccce"
SOURCE_PATH = "pictographic-primitives/landmarks/batch-08/anchor_034b7012-646c-415d-b54b-2efd12d0ccce.svg"
AUTHOR = "gpt-6"


class ShipsAnchor(Solo48):
    icon_id = "ships-anchor"
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/nautical"
    aliases = ("anchor", "ship-anchor")
    keywords = ("ship", "nautical", "marine", "harbour", "port", "sailing", "sea", "maritime")

    def build(self) -> None:
        # VRECT_XL centerline extremes: left 5, top 2, right 43, bottom 46.
        self.add_arc("ring-left", (24, 12), (24, 2), radius_x=5)
        self.add_arc("ring-right", (24, 2), (24, 12), radius_x=5)
        self.add_contour("ring", "ring-left", "ring-right", closed=True)
        self.add_line("shank-upper", (24, 12), (24, 22))
        self.add_line("shank-lower", (24, 22), (24, 46))
        self.add_contour("shank", "shank-upper", "shank-lower")
        self.add_polyline("stock", (16, 22), (24, 22), (32, 22))
        self.add_line("fluke-left", (11, 32), (5, 27))
        self.add_arc("arm-left", (5, 27), (24, 46), radius_x=19, sweep=False)
        self.add_arc("arm-right", (24, 46), (43, 27), radius_x=19, sweep=False)
        self.add_line("fluke-right", (43, 27), (37, 32))
        self.add_contour("arms", "fluke-left", "arm-left", "arm-right", "fluke-right")
        self.relate("connect", "ring", "shank")
        self.relate("connect", "stock", "shank")
        self.relate("connect", "arms", "shank")
