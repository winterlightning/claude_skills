"""Chateau frontenac: reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ba45a21-4375-538a-afb6-e6d71151d5e5'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/chateau frontenac canada_8ba45a21-4375-538a-afb6-e6d71151d5e5.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'chateau-frontenac'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('chateau', 'frontenac', 'quebec', 'canada', 'hotel', 'castle', 'landmark', 'architecture', 'turret')

    def build(self):
        # HRECT_L centerline extremes (6,8)-(42,40).
        # Building owns silhouette and attached architecture; repeat pairs share axes.
        # Deliberate asymmetry: rear hipped block, front turrets, lower right wing.
        self.add_polyline("outline", (6,40), (6,26), (10,16), (16,26), (16,16), (21,8), (31,8), (36,16), (36,26), (38,26), (42,32), (42,40), (32,40), (20,40), (16,40), closed=True)
        self.add_line("main-eave", (16,16), (36,16))
        self.relate("connect", "main-eave", "outline")
        self.add_polyline("front-turret", (20,40), (20,32), (26,24), (32,32), (32,40))
        self.relate("connect", "front-turret", "outline")
        self.add_line("wing-eave", (32,32), (42,32))
        self.relate("connect", "wing-eave", "front-turret")
        self.relate("connect", "wing-eave", "outline")
