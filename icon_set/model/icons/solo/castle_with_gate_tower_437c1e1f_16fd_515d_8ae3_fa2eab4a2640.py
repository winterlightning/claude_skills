"""Castle with gate tower: reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '437c1e1f-16fd-515d-8ae3-fa2eab4a2640'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/historical building castle_437c1e1f-16fd-515d-8ae3-fa2eab4a2640.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'castle-with-gate-tower'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('castle', 'fortress', 'gate', 'tower', 'battlement', 'spire', 'medieval', 'flag')

    def build(self):
        # SQUARE centerline extremes (6,6)-(42,42).
        # Building owns silhouette and attached architecture; repeat pairs share axes.
        # Tall right turret and attached flag retain the source's asymmetry.
        self.add_polyline("outline", (6,42), (6,26), (14,26), (14,30), (22,30), (22,26), (30,26), (30,18), (36,6), (42,18), (42,42), (30,42), (22,42), (14,42), closed=True)
        self.add_line("tower-eave", (30,18), (42,18))
        self.add_line("tower-wall", (30,26), (30,42))
        self.relate("connect", "tower-eave", "outline")
        self.relate("connect", "tower-wall", "outline")
        self.add_polyline("flag", (6,26), (6,16), (6,8), (18,8), (18,16), (6,16))
        self.relate("connect", "flag", "outline")
        self.add_line("door-left", (14,42), (14,38))
        self.add_arc("door-top", (14,38), (22,38), radius_x=4)
        self.add_line("door-right", (22,38), (22,42))
        self.add_contour("door", "door-left", "door-top", "door-right")
        self.relate("connect", "door", "outline")
