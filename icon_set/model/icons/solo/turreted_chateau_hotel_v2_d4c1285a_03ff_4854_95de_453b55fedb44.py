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
        """Opening repair: Lowered the turret crossbeam to open the small spire counter."""
        self.add_polyline('outline', (6, 42), (6, 32), (6, 27), (8, 17), (14, 27), (16, 27), (16, 15), (22, 6), (32, 6), (38, 15), (38, 27), (40, 27), (42, 37), (42, 42), (34, 42), (20, 42), (14, 42), closed=True)
        self.add_line('main-eave', (16, 15), (38, 15))
        self.relate('connect', 'main-eave', 'outline')
        self.add_polyline('gable', (20, 42), (20, 33), (27, 23), (34, 33), (34, 42))
        self.relate('connect', 'gable', 'outline')
        self.add_polyline('turret-eave', (6, 32), (14, 32), (14, 42))
        self.relate('connect', 'turret-eave', 'outline')
