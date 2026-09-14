"""Buildings (building), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '72baa0f0-a708-4c35-a415-a2c377a1f8af'
SOURCE_PATH = 'icons-json/building/buildings_72baa0f0-a708-4c35-a415-a2c377a1f8af.json'
AUTHOR = 'json_to_solo'

class BuildingsBuilding(Solo48):
    icon_id = 'buildings-building'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('buildings', 'building')

    def build(self):
        self.add_line('e0', (18, 37), (18, 44))
        self.add_line('e1', (28, 16), (40, 16))
        self.add_line('e2', (40, 18), (40, 44))
        self.add_line('e3', (40, 44), (8, 44))
        self.add_line('e4', (8, 44), (8, 4))
        self.add_line('e5', (8, 4), (28, 14))
        self.add_line('e6', (28, 14), (28, 44))
        self.add_bezier('e7', (40, 16), ((40, 16.609), (40, 17.391), (40, 18)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7', 'e2', 'e3', 'e4', 'e5', 'e6')
        self.relate('connect', 'c0', 'c1')
