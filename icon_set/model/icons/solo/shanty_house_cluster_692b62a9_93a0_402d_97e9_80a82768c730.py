"""Three overlapping narrow gabled dwellings with open feet and staggered heights. Asymmetry retains the informal cluster."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '692b62a9-93a0-402d-97e9-80a82768c730'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/shanty house village_692b62a9-93a0-402d-97e9-80a82768c730.svg'
AUTHOR = 'gpt-6'


class ShantyHouseCluster(Solo48):
    icon_id = 'shanty-house-cluster'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('shanty', 'slum', 'village', 'houses', 'informal', 'settlement', 'shelter', 'housing')

    def build(self) -> None:
        # Centerline extremes (5,2)-(43,46).
        self.add_polyline("front-left", (5,46), (5,29), (14,23), (24,29), (24,46))
        self.add_polyline("front-right", (24,29), (24,22), (34,16), (37,18), (43,22), (43,46))
        self.relate("connect", "front-left", "front-right")
        self.add_polyline("rear", (14,23), (14,10), (26,2), (37,9), (37,18))
        self.relate("connect", "rear", "front-left")
        self.relate("connect", "rear", "front-right")
