"""Skull (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf5df3c7-d268-41dc-98ce-7353737563c4'
SOURCE_PATH = 'icons-json/interface-essential/skull_cf5df3c7-d268-41dc-98ce-7353737563c4.json'
AUTHOR = 'json_to_solo'

class Skull(Solo48):
    icon_id = 'skull'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')

    def build(self):
        self.add_line('e0', (15, 44), (15, 38))
        self.add_line('e1', (33, 39), (33, 44))
        self.add_line('e2', (24, 38), (24, 44))
        self.add_bezier('e3', (15, 38), ((15, 36.155), (13.903, 35.427), (12.766, 34.173)), ((12.177, 33.527), (11.638, 32.791), (11.133, 32.073)), ((9.314, 29.455), (8.017, 25.809), (8.017, 22.518)), ((8.017, 22.303), (8, 22.089), (8, 21.865)), ((8, 21.862), (8, 21.858), (8, 21.855)), ((8, 21.564), (8.017, 21.273), (8.017, 20.973)), ((8.017, 12.473), (15.048, 4.018), (23.099, 4.018)), ((23.431, 4.018), (23.754, 4), (24.085, 4)), ((24.091, 4), (24.096, 4), (24.101, 4)), ((24.446, 4), (24.783, 4.018), (25.128, 4.018)), ((32.901, 4.018), (39.992, 12.582), (39.992, 20.782)), ((39.992, 21.023), (40, 21.265), (40, 21.507)), ((40, 21.511), (40, 21.514), (40, 21.518)), ((40, 21.891), (39.983, 22.264), (39.983, 22.636)), ((39.983, 26.155), (38.568, 29.482), (36.749, 32.309)), ((36.118, 33.291), (35.427, 34.164), (34.678, 35.027)), ((34.274, 35.482), (33.735, 35.955), (33.44, 36.491)), ((33.112, 37.091), (33, 38.355), (33, 39)))
        self.add_dot('e4', (32, 24))
        self.add_dot('e5', (17, 24))
        self.add_contour('c0', 'e0', 'e3', 'e1')
        self.add_contour('c1', 'e2')
