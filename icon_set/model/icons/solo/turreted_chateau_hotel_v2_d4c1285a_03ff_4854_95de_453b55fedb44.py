# Variant of turreted-chateau-hotel; parent file remains unchanged.
"""Turreted chateau with consistent roof rises, aligned wing eaves and a simple central gable. HRECT_XL retains deliberate asymmetric architectural massing. Lucide castle informs clear roof and wall hierarchy."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd4c1285a-03ff-4854-95de-453b55fedb44'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/chateau frontenac canada_d4c1285a-03ff-4854-95de-453b55fedb44.svg'
AUTHOR = 'gpt-6'

class LandmarkVariant2(Solo48):
    icon_id = 'turreted-chateau-hotel-v2'
    variant_of = 'turreted-chateau-hotel'
    variant_label = 'Consistent roof geometry'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('chateau', 'hotel', 'castle', 'turret', 'quebec', 'canada', 'landmark', 'architecture', 'building')

    def build(self):
        # HRECT_XL: centerline extremes (2,5)-(46,43).
        self.add_polyline('outline', (2,43), (2,27), (8,17), (14,27), (16,27), (16,15), (22,5), (32,5), (38,15), (38,27), (40,27), (46,37), (46,43), (34,43), (20,43), (14,43), closed=True)
        self.add_line('main-eave', (16,15), (38,15))
        self.relate('connect', 'main-eave', 'outline')
        self.add_polyline('gable', (20,43), (20,33), (27,23), (34,33), (34,43))
        self.relate('connect', 'gable', 'outline')
        self.add_polyline('turret-eave', (2,27), (14,27), (14,43))
        self.relate('connect', 'turret-eave', 'outline')
