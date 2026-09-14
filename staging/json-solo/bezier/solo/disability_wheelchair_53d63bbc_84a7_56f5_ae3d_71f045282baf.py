"""Disability wheelchair (wayfinding), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53d63bbc-84a7-56f5-ae3d-71f045282baf'
SOURCE_PATH = 'icons-json/wayfinding/disability wheelchair_53d63bbc-84a7-56f5-ae3d-71f045282baf.json'
AUTHOR = 'json_to_solo'

class DisabilityWheelchairWayfinding(Solo48):
    icon_id = 'disability-wheelchair-wayfinding'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('disability', 'wheelchair', 'wayfinding')

    def build(self):
        self.add_line('e0', (16, 13), (19, 32))
        self.add_line('e1', (19, 32), (32, 29))
        self.add_line('e2', (32, 29), (36, 41))
        self.add_line('e3', (36, 41), (40, 40))
        self.add_line('e4', (27, 22), (17, 23))
        self.add_arc('e5-top', (12, 9), (20, 9), radius_x=4, radius_y=5)
        self.add_arc('e5-bottom', (20, 9), (12, 9), radius_x=4, radius_y=5)
        self.add_bezier('e6', (15, 24), ((11.505, 25.5), (8.017, 28.555), (8.017, 32.973)), ((8.017, 33.191), (8, 33.4), (8, 33.618)), ((8, 33.622), (8, 33.625), (8, 33.628)), ((8, 33.843), (8.008, 34.049), (8.008, 34.255)), ((8.008, 39.2), (12.926, 43.991), (17.398, 43.991)), ((17.539, 43.991), (17.68, 44), (17.821, 44)), ((17.823, 44), (17.825, 44), (17.827, 44)), ((18.029, 44), (18.232, 43.991), (18.434, 43.991)), ((19.688, 43.991), (20.994, 43.582), (22.122, 43.018)), ((25.853, 41.155), (27.051, 37.291), (27, 33)))
        self.add_contour('c0', 'e6')
        self.add_contour('c1', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c1', 'e5')
        self.relate('connect', 'c2', 'c1')
