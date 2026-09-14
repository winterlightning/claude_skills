"""Rocky mountain (outdoors), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84a801ec-9a72-520e-9d5e-e141e4bfa565'
SOURCE_PATH = 'icons-json/outdoors/rocky mountain_84a801ec-9a72-520e-9d5e-e141e4bfa565.json'
AUTHOR = 'json_to_solo'

class RockyMountainOutdoors(Solo48):
    icon_id = 'rocky-mountain-outdoors'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('rocky', 'mountain', 'outdoors')

    def build(self):
        self.add_line('e0', (24, 30), (17, 18))
        self.add_line('e1', (15, 18), (4, 37))
        self.add_line('e2', (6, 40), (40, 40))
        self.add_line('e3', (43, 35), (29, 10))
        self.add_line('e4', (29, 10), (27, 8))
        self.add_line('e5', (27, 8), (19, 21))
        self.add_bezier('e6', (17, 18), ((16.391, 18), (15.609, 18), (15, 18)))
        self.add_bezier('e7', (4, 37), ((4, 37.27), (4.009, 37.53), (4.009, 37.8)), ((4.009, 38), (4.009, 38.21), (4.009, 38.41)), ((4.009, 39.61), (4.464, 39.99), (5.582, 39.99)), ((5.655, 39.99), (5.918, 40), (6, 40)))
        self.add_bezier('e8', (40, 40), ((40.209, 40), (40.782, 39.99), (40.991, 39.99)), ((41.4, 39.99), (42.018, 39.99), (42.4, 39.8)), ((43.027, 39.5), (43.991, 38.54), (43.991, 37.7)), ((43.991, 37.621), (44, 37.533), (44, 37.444)), ((44, 37.443), (44, 37.441), (44, 37.44)), ((43.991, 37.35), (43.991, 37.27), (43.982, 37.18)), ((43.982, 36.42), (43.355, 35.61), (43, 35)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7', 'e2', 'e8', 'e3', 'e4', 'e5')
