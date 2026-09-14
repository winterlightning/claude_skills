"""Astronomy planet uranus (science), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '10fad549-cea5-54a7-bdbb-de22ea172e2a'
SOURCE_PATH = 'icons-json/science/astronomy planet uranus_10fad549-cea5-54a7-bdbb-de22ea172e2a.json'
AUTHOR = 'json_to_solo'

class AstronomyPlanetUranusScience(Solo48):
    icon_id = 'astronomy-planet-uranus-science'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('astronomy', 'planet', 'uranus', 'science')

    def build(self):
        self.add_line('e0', (24, 39), (24, 44))
        self.add_line('e1', (24, 39), (24, 4))
        self.add_arc('e2-top', (8, 24), (40, 24), radius_x=16, radius_y=15)
        self.add_arc('e2-bottom', (40, 24), (8, 24), radius_x=16, radius_y=15)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'e2')
        self.relate('connect', 'c1', 'e2')
