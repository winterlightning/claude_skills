"""Turreted chateau hotel: reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd4c1285a-03ff-4854-95de-453b55fedb44'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/chateau frontenac canada_d4c1285a-03ff-4854-95de-453b55fedb44.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'turreted-chateau-hotel'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('chateau', 'hotel', 'castle', 'turret', 'quebec', 'canada', 'landmark', 'architecture', 'building')

    def build(self):
        # Centerline extremes: (2,5)-(46,43); intentionally stepped massing.
        self.add_polyline("outline", (2,43), (2,29), (7,19), (12,29), (16,29), (16,15), (21,5), (33,5), (38,15), (38,25), (41,25), (46,33), (46,43), (32,43), (20,43), (12,43), closed=True)
        self.add_line("main-eave", (16,15), (38,15))
        self.relate("connect", "main-eave", "outline")
        self.add_polyline("gable", (20,43), (20,29), (26,21), (32,29), (32,33), (32,43))
        self.relate("connect", "gable", "outline")
        self.add_line("wing-eave", (32,33), (46,33))
        self.relate("connect", "wing-eave", "gable")
        self.relate("connect", "wing-eave", "outline")
        self.add_polyline("turret-eave", (2,29), (12,29), (12,43))
        self.relate("connect", "turret-eave", "outline")
