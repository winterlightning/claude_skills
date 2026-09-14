"""Plane 1 (travel), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd64bbae0-775c-45ae-a797-8152cc224a80'
SOURCE_PATH = 'icons-json/travel/plane 1_d64bbae0-775c-45ae-a797-8152cc224a80.json'
AUTHOR = 'json_to_solo'

class Plane1D64bbae0(Solo48):
    icon_id = 'plane-1-d64bbae0'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('plane', 'travel')

    def build(self):
        self.add_line('e0', (30, 20), (27, 16))
        self.add_line('e1', (27, 16), (19, 9))
        self.add_line('e2', (14, 8), (18, 21))
        self.add_line('e3', (7, 18), (4, 18))
        self.add_line('e4', (4, 18), (7, 24))
        self.add_line('e5', (7, 24), (4, 30))
        self.add_line('e6', (4, 30), (7, 30))
        self.add_line('e7', (12, 27), (18, 27))
        self.add_line('e8', (18, 27), (14, 40))
        self.add_line('e9', (14, 40), (18, 40))
        self.add_line('e10', (20, 38), (30, 28))
        self.add_line('e11', (30, 28), (39, 28))
        self.add_line('e12', (39, 20), (30, 20))
        self.add_bezier('e13', (19, 9), ((18.455, 8.495), (17.264, 8.008), (16.491, 8.008)), ((15.918, 8.008), (15.336, 8), (14.764, 8)), ((14.509, 8), (14.255, 8), (14, 8)))
        self.add_bezier('e14', (18, 21), ((16.555, 21.025), (11.527, 21.044), (10.282, 20.564)), ((8.955, 20.051), (8.2, 18.733), (7, 18)))
        self.add_bezier('e15', (7, 30), ((9.127, 29.048), (9.536, 27), (12, 27)))
        self.add_bezier('e16', (18, 40), ((19.791, 39.587), (18.791, 39.221), (20, 38)))
        self.add_bezier('e17', (39, 28), ((41.055, 28), (43.991, 26.509), (43.991, 24.328)), ((44, 24.254), (44, 24.187), (44, 24.113)), ((44, 24.112), (44, 24.111), (44, 24.109)), ((44, 24.034), (44, 23.958), (43.991, 23.882)), ((43.991, 21.701), (41.118, 20), (39, 20)))
        self.add_contour('c0', 'e0', 'e1', 'e13', 'e2', 'e14', 'e3', 'e4', 'e5', 'e6', 'e15', 'e7', 'e8', 'e9', 'e16', 'e10', 'e11', 'e17', 'e12', closed=True)
