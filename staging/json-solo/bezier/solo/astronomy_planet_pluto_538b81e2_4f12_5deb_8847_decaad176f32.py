"""Astronomy planet pluto (science), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '538b81e2-4f12-5deb-8847-decaad176f32'
SOURCE_PATH = 'icons-json/science/astronomy planet pluto_538b81e2-4f12-5deb-8847-decaad176f32.json'
AUTHOR = 'json_to_solo'

class AstronomyPlanetPlutoScience(Solo48):
    icon_id = 'astronomy-planet-pluto-science'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('astronomy', 'planet', 'pluto', 'science')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e1', (44, 24), ((41.782, 23.4), (39.473, 23.2), (37.718, 21.564)), ((37.291, 21.164), (36.955, 20.591), (36.609, 20.118)), ((35.673, 18.818), (34.782, 17.718), (33.345, 16.936)), ((26.555, 13.236), (18.873, 21.091), (22, 27.909)), ((23.473, 31.118), (28.327, 31.827), (28.336, 35.855)), ((28.345, 38.255), (25.309, 42.2), (24, 44)))
        self.add_contour('c0', 'e1')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        self.relate('connect', 'c0', 'e0')
        self.relate('connect', 'c0', 'e0')
