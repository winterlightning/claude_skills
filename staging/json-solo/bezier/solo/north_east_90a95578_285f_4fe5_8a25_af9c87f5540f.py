"""North east (weather), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90a95578-285f-4fe5-8a25-af9c87f5540f'
SOURCE_PATH = 'icons-json/weather/north east_90a95578-285f-4fe5-8a25-af9c87f5540f.json'
AUTHOR = 'json_to_solo'

class NorthEastWeather(Solo48):
    icon_id = 'north-east-weather'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('north', 'east', 'weather')

    def build(self):
        self.add_line('e0', (24, 7), (24, 4))
        self.add_line('e1', (41, 24), (44, 24))
        self.add_line('e2', (24, 41), (24, 44))
        self.add_line('e3', (7, 24), (4, 24))
        self.add_line('e4', (32, 15), (23, 33))
        self.add_line('e5', (23, 33), (21, 27))
        self.add_line('e6', (20, 26), (15, 24))
        self.add_line('e7', (15, 24), (32, 15))
        self.add_arc('e8-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e8-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e9', (21, 27), ((20.891, 26.609), (20.282, 26.255), (20, 26)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e5', 'e9', 'e6', 'e7', closed=True)
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.relate('connect', 'c0', 'e8')
        self.relate('connect', 'c1', 'e8')
        self.relate('connect', 'c2', 'e8')
        self.relate('connect', 'c3', 'e8')
