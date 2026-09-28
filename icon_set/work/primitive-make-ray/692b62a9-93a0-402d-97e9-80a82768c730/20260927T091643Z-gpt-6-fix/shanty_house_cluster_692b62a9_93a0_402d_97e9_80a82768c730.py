"""Three overlapping narrow gabled dwellings with open feet and staggered heights. Asymmetry retains the informal cluster."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '692b62a9-93a0-402d-97e9-80a82768c730'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__shanty-house-cluster/20260927T091435Z-thuan-mac-1/reference/shanty house village_692b62a9-93a0-402d-97e9-80a82768c730.svg'
AUTHOR = "gpt-6"


class ShantyHouseCluster(Solo48):
    icon_id = 'shanty-house-cluster'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    categories = ("landmarks", "primitives")
    aliases = ()
    keywords = ('shanty', 'slum', 'village', 'houses', 'informal', 'settlement', 'shelter', 'housing')

    def build(self) -> None:
        # Centerline extremes (8,4)-(40,44).
        self.add_polyline("front-left", (8,44), (8,29), (14,23), (24,29), (24,44))
        self.add_polyline("front-right", (24,29), (24,22), (34,16), (37,18), (40,22), (40,44))
        self.relate("connect", "front-left", "front-right")
        # Raise and balance the rear gable so three separate rooftops remain legible.
        self.add_polyline("rear", (14,23), (14,12), (26,4), (37,12), (37,18))
        self.relate("connect", "rear", "front-left")
        self.relate("connect", "rear", "front-right")
