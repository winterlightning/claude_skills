'Outstretched statue with long robe and pedestal. Sleeve outlines and diagonal cloth fold omitted for native-size clarity.'
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
        # SQUARE centerline extremes (6,6)-(42,42).
        axis, radius = 24, 3
        self.add_arc("head-top", (axis-radius,9), (axis+radius,9), radius_x=radius)
        self.add_arc("head-bottom", (axis+radius,9), (axis-radius,9), radius_x=radius)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        self.add_polyline("robe", (6,21), (17,21), (17,34), (31,34), (31,21), (42,21))
        self.add_line("pedestal", (12,42), (36,42))
