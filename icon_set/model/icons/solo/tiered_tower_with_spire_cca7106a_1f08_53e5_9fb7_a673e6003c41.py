"""A three-tier tower with a triangular roof and a round-arched door."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cca7106a-1f08-53e5-9fb7-a673e6003c41'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/tower_cca7106a-1f08-53e5-9fb7-a673e6003c41.svg'
AUTHOR = 'gpt-6'


class TieredTowerWithSpire(Solo48):
    icon_id = 'tiered-tower-with-spire'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('tower', 'castle', 'keep', 'spire', 'tiers', 'building', 'medieval', 'landmark')

    def build(self) -> None:
        # Centerline extremes: (8,2)-(40,46); mirrored around x=24.
        self.add_polyline('roof',(12,14),(24,2),(36,14),(30,14),(18,14),(12,14),closed=True)
        self.add_polyline('upper-tier',(18,14),(18,24),(30,24),(30,14))
        self.relate('connect','upper-tier','roof')
        self.add_polyline('middle-tier',(12,34),(12,24),(18,24),(30,24),(36,24),(36,34))
        self.relate('connect','upper-tier','middle-tier')
        self.add_polyline('lower-left',(18,46),(8,46),(8,34),(12,34),(36,34),(40,34),(40,46),(30,46))
        self.relate('connect','middle-tier','lower-left')
        self.add_arc('door',(18,46),(30,46),radius_x=6,sweep=True)
        self.relate('connect','door','lower-left')
