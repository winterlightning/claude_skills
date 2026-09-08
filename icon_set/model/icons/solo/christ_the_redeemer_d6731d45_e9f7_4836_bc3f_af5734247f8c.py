"""Outstretched arms, round head and upright robe; folds and sleeve outlines omitted for clear negative space."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6731d45-e9f7-4836-bc3f-af5734247f8c'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/christ the reedemer_d6731d45-e9f7-4836-bc3f-af5734247f8c.svg'
AUTHOR = 'gpt-6'

class ChristTheRedeemer(Solo48):
    icon_id = 'christ-the-redeemer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('christ the redeemer', 'rio', 'brazil', 'statue', 'monument', 'figure', 'landmark', 'religion')

    def build(self) -> None:
        # Centerline extremes (2, 2, 46, 46).
        self.add_arc("head-top", (18,8), (30,8), radius_x=6)
        self.add_arc("head-bottom", (30,8), (18,8), radius_x=6)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        self.add_polyline("robe", (2,22), (17,22), (17,38), (31,38), (31,22), (46,22))
        self.add_polyline("pedestal", (12,46), (36,46))
