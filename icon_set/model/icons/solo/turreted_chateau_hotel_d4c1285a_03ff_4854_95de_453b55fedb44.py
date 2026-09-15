"""Square envelope; narrowed and centered the main gable to leave eight units beside the turret divider.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd4c1285a-03ff-4854-95de-453b55fedb44'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/chateau frontenac canada_d4c1285a-03ff-4854-95de-453b55fedb44.svg'
AUTHOR = 'gpt-6'

class Landmark(Solo48):
    icon_id = 'turreted-chateau-hotel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('chateau', 'hotel', 'castle', 'turret', 'quebec', 'canada', 'landmark', 'architecture', 'building')

    def build(self):
        self.add_polyline('outline', (6, 42), (6, 32), (6, 27), (8, 17), (14, 27), (16, 27), (16, 15), (22, 6), (32, 6), (38, 15), (38, 27), (42, 27), (42, 37), (42, 42), (34, 42), (22, 42), (14, 42), closed=True)
        self.add_line('main-eave', (16, 15), (38, 15))
        self.relate('connect', 'main-eave', 'outline')
        self.add_polyline('gable', (22, 42), (22, 33), (28, 23), (34, 33), (34, 42))
        self.relate('connect', 'gable', 'outline')
        self.add_polyline('turret-eave', (6, 32), (14, 32), (14, 42))
        self.relate('connect', 'turret-eave', 'outline')
