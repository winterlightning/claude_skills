"""Chateau frontenac: reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ba45a21-4375-538a-afb6-e6d71151d5e5'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/chateau frontenac canada_8ba45a21-4375-538a-afb6-e6d71151d5e5.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'chateau-frontenac'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('chateau', 'frontenac', 'quebec', 'canada', 'hotel', 'castle', 'landmark', 'architecture', 'turret')

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
