"""Two equal rounded squares offset diagonally by eight grid units.

SQUARE extrema (6,6)-(42,42). The rear outline stops at the front border;
the shared offset preserves equal square sizes. Lucide copy informed the
occluded rear outline and rounded corners.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "caa1869e-ea95-42fc-aab0-8ff68e2c9cf0"
SOURCE_PATH = "pictographic-primitives/_uncategorized_13/crackers_caa1869e-ea95-42fc-aab0-8ff68e2c9cf0.svg"
AUTHOR = "gpt-6"


class TwoOverlappingSquares(Solo48):
    icon_id = "two-overlapping-squares"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("stacked squares", "duplicate squares")
    keywords = ("overlap", "copy", "rounded", "shapes")

    def build(self) -> None:
        self.add_line("front-top",(18,6),(38,6))
        self.add_arc("front-ne",(38,6),(42,10),radius_x=4,radius_y=4,sweep=True)
        self.add_line("front-right",(42,10),(42,30))
        self.add_arc("front-se",(42,30),(38,34),radius_x=4,radius_y=4,sweep=True)
        self.add_line("front-bottom-right",(38,34),(34,34))
        self.add_line("front-bottom-left",(34,34),(18,34))
        self.add_arc("front-sw",(18,34),(14,30),radius_x=4,radius_y=4,sweep=True)
        self.add_line("front-left-lower",(14,30),(14,14))
        self.add_line("front-left-upper",(14,14),(14,10))
        self.add_arc("front-nw",(14,10),(18,6),radius_x=4,radius_y=4,sweep=True)
        self.add_contour("front","front-top","front-ne","front-right","front-se","front-bottom-right","front-bottom-left","front-sw","front-left-lower","front-left-upper","front-nw",closed=True)
        self.add_line("rear-top",(14,14),(10,14))
        self.add_arc("rear-nw",(10,14),(6,18),radius_x=4,radius_y=4,sweep=False)
        self.add_line("rear-left",(6,18),(6,38))
        self.add_arc("rear-sw",(6,38),(10,42),radius_x=4,radius_y=4,sweep=False)
        self.add_line("rear-bottom",(10,42),(30,42))
        self.add_arc("rear-se",(30,42),(34,38),radius_x=4,radius_y=4,sweep=False)
        self.add_line("rear-right",(34,38),(34,34))
        self.add_contour("rear","rear-top","rear-nw","rear-left","rear-sw","rear-bottom","rear-se","rear-right")
        self.relate("connect","front","rear")
