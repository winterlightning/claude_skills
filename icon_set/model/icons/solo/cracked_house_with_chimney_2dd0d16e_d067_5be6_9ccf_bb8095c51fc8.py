"""A gabled house with right chimney, left doorway and a jagged roof crack. Intentional asymmetric details convey damage."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2dd0d16e-d067-5be6-9ccf-bb8095c51fc8'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/poverty housing_2dd0d16e-d067-5be6-9ccf-bb8095c51fc8.svg'
AUTHOR = 'gpt-6'


class CrackedHouseWithChimney(Solo48):
    icon_id = 'cracked-house-with-chimney'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('house', 'home', 'damage', 'crack', 'poverty', 'housing', 'shelter', 'chimney', 'repair')

    def build(self) -> None:
        # Centerline extremes (2,2)-(46,46).
        self.add_polyline("roof", (2,22), (13,12), (24,2), (32,10), (42,20), (46,24))
        self.add_polyline("chimney", (32,10), (32,2), (42,2), (42,20))
        self.relate("connect", "roof", "chimney")
        self.add_polyline("walls", (2,22), (2,46), (12,46), (26,46), (46,46), (46,24))
        self.relate("connect", "roof", "walls")
        self.add_polyline("door", (12,46), (12,32), (26,32), (26,46))
        self.relate("connect", "door", "walls")
        self.add_polyline("crack", (13,12), (18,19), (25,19), (29,25))
        self.relate("connect", "crack", "roof")
