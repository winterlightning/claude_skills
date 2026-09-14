"""Ice snowflake (weather), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1ae2009c-069c-5d8b-b45c-7070506d36c5'
SOURCE_PATH = 'icons-json/weather/ice snowflake_1ae2009c-069c-5d8b-b45c-7070506d36c5.json'
AUTHOR = 'json_to_solo'

class IceSnowflakeWeather(Solo48):
    icon_id = 'ice-snowflake-weather'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('ice', 'snowflake', 'weather')

    def build(self):
        self.add_line('sym-e0', (24, 4), (24, 12))
        self.add_line('sym-e1', (24, 12), (24, 24))
        self.add_line('sym-e2', (24, 24), (24, 36))
        self.add_line('sym-e3', (24, 36), (24, 44))
        self.add_line('sym-e4', (24, 36), (30, 40))
        self.add_line('sym-e5', (35, 38), (33, 29))
        self.add_line('sym-e6', (33, 29), (40, 34))
        self.add_line('sym-e7', (40, 28), (33, 29))
        self.add_line('sym-e8', (33, 29), (24, 24))
        self.add_line('sym-e9', (24, 24), (33, 19))
        self.add_line('sym-e10', (33, 19), (40, 21))
        self.add_line('sym-e11', (40, 14), (33, 19))
        self.add_line('sym-e12', (33, 19), (35, 11))
        self.add_line('sym-e13', (30, 8), (24, 12))
        self.add_line('sym-e14', (24, 12), (18, 8))
        self.add_line('sym-e15', (24, 36), (18, 40))
        self.add_line('sym-e16', (13, 38), (15, 29))
        self.add_line('sym-e17', (15, 29), (8, 34))
        self.add_line('sym-e18', (8, 28), (15, 29))
        self.add_line('sym-e19', (15, 29), (24, 24))
        self.add_line('sym-e20', (24, 24), (15, 19))
        self.add_line('sym-e21', (15, 19), (8, 21))
        self.add_line('sym-e22', (8, 14), (15, 19))
        self.add_line('sym-e23', (15, 19), (13, 11))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c4', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c5', 'sym-e13', 'sym-e14')
        self.add_contour('sym-c6', 'sym-e15')
        self.add_contour('sym-c7', 'sym-e16', 'sym-e17')
        self.add_contour('sym-c8', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21')
        self.add_contour('sym-c9', 'sym-e22', 'sym-e23')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c3', 'sym-c8')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c6')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c7', 'sym-c8')
        self.relate('connect', 'sym-c8', 'sym-c9')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c8')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c8')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c7', 'sym-c8')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c7', 'sym-c8')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c8', 'sym-c9')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c8', 'sym-c9')
        self.relate('connect', 'sym-c3', 'sym-c4')
