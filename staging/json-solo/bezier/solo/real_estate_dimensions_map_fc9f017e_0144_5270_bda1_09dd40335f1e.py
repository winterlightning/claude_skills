"""Real estate dimensions map (maps), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc9f017e-0144-5270-bda1-09dd40335f1e'
SOURCE_PATH = 'icons-json/maps/real estate dimensions map_fc9f017e-0144-5270-bda1-09dd40335f1e.json'
AUTHOR = 'json_to_solo'

class RealEstateDimensionsMapMaps(Solo48):
    icon_id = 'real-estate-dimensions-map-maps'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('real', 'estate', 'dimensions', 'map', 'maps')

    def build(self):
        self.add_line('e0', (19, 27), (27, 24))
        self.add_line('e1', (27, 24), (27, 37))
        self.add_line('e2', (37, 33), (19, 40))
        self.add_line('e3', (19, 40), (19, 15))
        self.add_line('e4', (19, 15), (4, 10))
        self.add_line('e5', (4, 10), (4, 35))
        self.add_line('e6', (4, 35), (19, 40))
        self.add_line('e7', (37, 33), (37, 8))
        self.add_line('e8', (37, 33), (44, 37))
        self.add_line('e9', (44, 37), (44, 11))
        self.add_line('e10', (44, 11), (37, 8))
        self.add_line('e11', (37, 8), (19, 15))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4', 'e5', 'e6')
        self.add_contour('c2', 'e7')
        self.add_contour('c3', 'e8', 'e9', 'e10')
        self.add_contour('c4', 'e11')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
